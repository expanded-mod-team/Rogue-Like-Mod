# Start Chat menus / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Chat(Girl=0):
        if Current_Time == "Evening" and "yesdate" in Player.DailyActions:
                #checks to see if you want to go on a date
                call Readytogo
        if not Girl:
                menu:
                    "Chat with [RogueX.Name]" if RogueX.Loc == bg_current: 
                            $ Girl = RogueX        
                    "Text [RogueX.Name]" if RogueX.Loc != bg_current: 
                            $ Girl = RogueX        
                                
                    "Chat with [KittyX.Name]" if KittyX.Loc == bg_current: 
                            $ Girl = KittyX        
                    "Text [KittyX.Name]" if KittyX.Loc != bg_current and "met" in KittyX.History: 
                            $ Girl = KittyX        
                                
                    "Chat with [EmmaX.Name]" if EmmaX.Loc == bg_current: 
                            $ Girl = EmmaX        
                    "Text [EmmaX.Name]" if EmmaX.Loc != bg_current and "met" in EmmaX.History: 
                            $ Girl = EmmaX        
                    
                    "Chat with [LauraX.Name]" if LauraX.Loc == bg_current:   
                            $ Girl = LauraX        
                    "Text [LauraX.Name]" if LauraX.Loc != bg_current and "met" in LauraX.History: 
                            $ Girl = LauraX   
                            
                    "Never Mind":
                        pass
        if Girl:
                if Girl.Loc == bg_current:  
                        if Girl == EmmaX and "classcaught" not in EmmaX.History:
                                        jump Emma_Chat_Minimal
                        if "caught" in Girl.DailyActions:
                                if Girl == RogueX:
                                        ch_r "We should probably keep our distance for now."
                                elif Girl == KittyX:
                                        ch_k "I'm[Girl.like]going to keep my distance 'til this blows over."
                                elif Girl == EmmaX:                                    
                                        ch_e "I don't think we should be seen together, if you don't mind."
                                elif Girl == LauraX:
                                        ch_l "I think we should lie low for a bit."
                                return
                        if Girl == LauraX and Girl.Loc == bg_current and "scent" in Player.DailyActions:
                                #if you've fucked another girl, and not showered, Laura will know.     
                                if not ApprovalCheck(Girl, 1700) and not ApprovalCheck(Girl, 600,"O"): 
                                        $ Options = TotalGirls[:]
                                        while Options:
                                                if Options[0] in Player.DailyActions and "saw with " + Options[0].Tag not in Girl.Traits and Girl.GirlLikeCheck(Options[0]) <= 700:
                                                        $ Girl.Traits.append("saw with " + Options[0].Tag)
                                                $ Options.remove(Options[0])
                                $ Player.DailyActions.remove("scent") 
                
                        if "les" in Girl.RecentActions:
                                #if she's with a girl. . .
                                if Girl == RogueX:
                                        ch_r "Ooof. . . gimme a minute. . ."
                                        "You hear some shifting around. . ."
                                        ch_r "Ok, just um, never mind. . ."
                                        "You hear some muffled giggles in the background."
                                elif Girl == KittyX:
                                        ch_k "Ah! One minute. . ."
                                        "You hear some shifting around. . ."
                                        ch_k "Ok, (\"quit it!\") what did you. . .)"
                                        "You hear some muffled giggles in the background."
                                        ch_k "So. . ."
                                elif Girl == EmmaX:
                                        ch_e "One moment, [Girl.Petname]. . ."
                                        "You hear some shifting around. . ."
                                        ch_e "Ok, so. . ."
                                        "You hear some muffled giggles in the background."
                                elif Girl == LauraX:
                                        ch_l "Just a minute. . ."
                                        "You hear some shifting around. . ."
                                        ch_l "Yeah, um. . . what was it you wanted?"
                                        "You hear some muffled giggles in the background."
                                        ch_l "So. . ."  
                                        
                        if "angry" not in Girl.RecentActions:
                                if Girl == RogueX:
                                        ch_r "So what did you want to talk about, [Girl.Petname]?"
                                elif Girl == KittyX:
                                        ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
                                elif Girl == EmmaX:
                                        ch_e "What was it you wanted to discuss, [Girl.Petname]?"
                                elif Girl == LauraX:            
                                        ch_l "Yeah?"
                        call Chat_Menu
                        #call expression Girl.Tag + "_Chat_Set" pass ("chat")    
                elif Girl in Digits:
                    if Girl.Loc == "hold":
                        "She doesn't seem to be picking up."
                    else:
                        if Girl == EmmaX:
                                    if EmmaX.Loc == "bg teacher" and bg_current == "bg classroom":
                                            "She texts back, \"We can speak after class, [EmmaX.Petname].\"" 
                                            return
                                    elif "classcaught" not in EmmaX.History:
                                            call Emma_Chat_Minimal
                                            return                                           
                        if Girl.Loc != bg_current:
                                    show Cellphone at SpriteLoc(StageLeft)
                        else:
                                    hide Cellphone 
                        "You send [Girl.Name] a text."
                        #intro dialog
                        if "angry" not in Girl.RecentActions:
                                if Girl == RogueX:
                                        ch_r "So what did you want to talk about, [Girl.Petname]?"
                                elif Girl == KittyX:
                                        ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
                                elif Girl == EmmaX:
                                        ch_e "What was it you wanted to discuss, [Girl.Petname]?"
                                elif Girl == LauraX:            
                                        ch_l "Yeah?"
                        call Chat_Menu  
                else:
                        "You don't know her number, you'll have to go to her." 
        return
            
# Start Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
           
label Chat_Menu:
        #Primary chat menu, called by "Chat", carries over "Girl"   
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        $ Girl.FaceChange()      
        call Shift_Focus(Girl)
        if Girl.Loc != bg_current:
                    show Cellphone at SpriteLoc(StageLeft)
        else:
                    hide Cellphone
        
        if "angry" in Girl.RecentActions:
                    if Girl == RogueX:
                            ch_r "I really don't want to talk to you right now."
                    elif Girl == KittyX:
                            ch_k "I'm[Girl.like]so mad at you right now!"
                    elif Girl == EmmaX:
                            ch_e "I would not press my luck if I were you."
                    elif Girl == LauraX:
                            ch_l "You don't want to be around me right now."
                    return
                    
        #intro dialog
#        if Girl == RogueX:
#                ch_r "So what did you want to talk about, [Girl.Petname]?"
#        elif Girl == KittyX:
#                ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
#        elif Girl == EmmaX:
#                ch_e "What was it you wanted to discuss, [Girl.Petname]?"
#        elif Girl == LauraX:            
#                ch_l "Yeah?"
        menu:
            "Come on over." if Girl.Loc != bg_current:
                        if Girl in Nearby and bg_current != "bg showerrroom":
                                call Swap_Nearby(Girl)
                        elif Room_Full():
                                "It's already pretty crowded here."
                                call Dismissed
                        else:
                                call expression Girl.Tag + "_Summon" #call Rogue_Summon
            "Ask [Girl.Name] to leave" if Girl.Loc == bg_current:
                                call Girl_Dismissed(Girl)
                                return
                        
            "Romance her":      
                    menu:
                        "Flirt with her (locked)" if Girl.Chat[5]:  
                                    pass
                        "Flirt with her" if not Girl.Chat[5]:
                                    call Flirt(Girl)    
                            
                        "Sex Menu (locked)" if Girl.Loc != bg_current:
                                    pass
                        "Sex Menu" if Girl.Loc == bg_current:
                                    if Girl.Love >= Girl.Obed:
                                            ch_p "Did you want to fool around?"
                                    else:
                                            ch_p "I'd like to get naughty."
                                    if "angry" in Girl.RecentActions:  
                                            if Girl == RogueX:
                                                    ch_r "I don't want to deal with you right now."
                                            elif Girl == KittyX:
                                                    ch_k "Not even!"
                                            elif Girl == EmmaX:
                                                    ch_e "You should know better than that."
                                            elif Girl == LauraX: 
                                                    ch_l "Bad idea right now."
                                    elif ApprovalCheck(Girl, 600, "LI"):
                                            $ Girl.FaceChange("sexy")
                                            if Girl == RogueX:
                                                    ch_r "Heh, all right, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "Mmmm, ok, [Girl.Petname]."
                                            elif Girl == EmmaX:
                                                    ch_e "Perhaps. . ."
                                            elif Girl == LauraX: 
                                                    ch_l "Cool."
                                            call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
                                            return
                                    elif ApprovalCheck(Girl, 400, "OI"):
                                            if Girl == RogueX:
                                                    ch_r "If that's what you want, [Girl.Petname]."
                                            elif Girl == KittyX:
                                                    ch_k "Yes, [Girl.Petname]."
                                            elif Girl == EmmaX:
                                                    ch_e "If that's what you want, [Girl.Petname]."
                                            elif Girl == LauraX: 
                                                    ch_l "Yes, [Girl.Petname]."
                                            call expression Girl.Tag + "_SexMenu" #call Rogue_SexMenu
                                            return
                                    else:
                                            if Girl == RogueX:
                                                    ch_r "I'm not really interested, [Girl.Petname]." 
                                            elif Girl == KittyX:
                                                    ch_k "No thanks, [Girl.Petname]."   
                                            elif Girl == EmmaX:
                                                    ch_e "No thank you, [Girl.Petname]."
                                            elif Girl == LauraX: 
                                                    ch_l "No thanks, [Girl.Petname]."  
                                   
                        "Dirty Talk (locked)" if Girl.SEXP < 10:
                                        pass
                        "Dirty Talk" if Girl.SEXP >= 10:
                                        ch_p "About when we get together. . ."
                                        call expression Girl.Tag + "_SexChat" #call Rogu_SexChat
                                        
                        "Date":
                                        ch_p "Do you want to go on a date tonight?"
                                        call Date_Ask(Girl)
                                        
                        "Gifts (locked)" if Girl.Loc != bg_current:
                                        pass
                        "Gifts" if Girl.Loc == bg_current:
                                        ch_p "I'd like to give you something."
                                        call Gifts #(Girl)  
                        "Back":
                                        pass        
                                              
            "Talk with her": 
                    menu:
                        "I just wanted to talk. . .":
                                    call expression Girl.Tag + "_Chitchat" #call Rogue_Chitchat
                        "Relationship status":
                                    ch_p "Could we talk about us?"
                                    if Girl.Loc == bg_current:
                                        call expression Girl.Tag + "_Relationship" #call Rogue_Relationship
                                    else:
                                        if Girl == RogueX:
                                                ch_r "That sounds like it might be a little heavy to do over the phone."
                                                ch_r "Maybe later?"
                                        elif Girl == KittyX:
                                                ch_k "That seems like something we'd want to do face to face."
                                                ch_k "Maybe later?" 
                                        elif Girl == EmmaX:
                                                ch_e "This seems a bit serious to discuss over the phone."
                                                ch_e "Later, perhaps."
                                        elif Girl == LauraX: 
                                                ch_l "Sounds heavy."
                                                ch_l "Maybe later when we're face to face?"
                              
                        "Other girls":
                                    menu:
                                        "How do you feel about [RogueX.Name]?" if Girl != RogueX:
                                                call expression Girl.Tag + "_About" pass (RogueX)
                                        "How do you feel about [KittyX.Name]?" if Girl != KittyX and "met" in KittyX.History:
                                                call expression Girl.Tag + "_About" pass (KittyX)
                                        "How do you feel about [EmmaX.Name]?" if Girl != EmmaX and "met" in EmmaX.History:
                                                call expression Girl.Tag + "_About" pass (EmmaX)
                                        "How do you feel about [LauraX.Name]?" if Girl != LauraX and "met" in LauraX.History:
                                                call expression Girl.Tag + "_About" pass (LauraX)
                                        "About hooking up with other girls. . .":
                                                call expression Girl.Tag + "_Monogamy" #call Rogue_Monogamy
                                        "Never mind.":
                                                pass
                                                
                        "Could I get your number?" if Girl not in Digits:     
                                    if Girl == EmmaX and ApprovalCheck(Girl, 800, "LI"):
                                            ch_e "I don't see why not."
                                            $ Digits.append(Girl) 
                                    elif Girl != EmmaX and (ApprovalCheck(Girl, 400, "L") or ApprovalCheck(Girl, 200, "I")):
                                            if Girl == RogueX:
                                                    ch_r "Sure, I suppose."
                                            elif Girl == KittyX:
                                                    ch_k "OMG[Girl.like]sure."
                                            elif Girl == LauraX: 
                                                    ch_l "Oh, sure."
                                            $ Digits.append(Girl) 
                                    elif ApprovalCheck(Girl, 200, "O",Alt=[[EmmaX],500-EmmaX.Inbt]):
                                            if Girl == RogueX:
                                                    ch_r "If you want it, I guess."  
                                            elif Girl == KittyX:
                                                    ch_k "[Girl.Like]fine."             
                                            elif Girl == EmmaX:
                                                    ch_e "Hmm. . . fine, hand me your phone."    
                                            elif Girl == LauraX:    
                                                    ch_l "I guess."                     
                                            $ Digits.append(Girl)
                                    else:
                                            if Girl == RogueX:
                                                    ch_r "I don't really want you calling me."  
                                            elif Girl == KittyX:
                                                    ch_k "[Girl.Like]I'd rather not?"  
                                            elif Girl == EmmaX:
                                                    ch_e "I don't think it's appropriate to give my number out to a student like that."     
                                            elif Girl == LauraX:  
                                                    ch_l "Um, probably not."  
                        "Back":
                                    pass
                        
            "Change her":
                        call Girl_Settings
             
            "Add her to party" if Girl not in Party and Girl.Loc == bg_current:
                        ch_p "Could you follow me for a bit?"
                        if Girl == EmmaX and ApprovalCheck(Girl, 1250):
                                $ Party.append(Girl)
                                ch_e "Lead away."
                                return
                        if ApprovalCheck(Girl, 600,Alt=[[EmmaX],900]):
                                $ Party.append(Girl)
                                if Girl == RogueX: 
                                        ch_r "Ok, Where did you want to go?"
                                elif Girl == KittyX:
                                        ch_k "[Girl.Like]where to?"
                                elif Girl == EmmaX: 
                                        ch_e "You'd better not bore me."
                                elif Girl == LauraX: 
                                        ch_l "Where to?"
                                        return
                        elif not ApprovalCheck(Girl, 400):
                                if Girl == RogueX: 
                                        ch_r "Um, no thanks."
                                elif Girl == KittyX:
                                        ch_k "Ew, no."
                                elif Girl == EmmaX: 
                                        ch_e "I can't imagine why I would."
                                elif Girl == LauraX: 
                                        ch_l "No."
                        else:
                                if Girl == RogueX: 
                                        ch_r "I'm fine here, thanks."
                                elif Girl == KittyX:
                                        ch_k "I think I'll stay here."
                                elif Girl == EmmaX: 
                                        ch_e "I'd rather not."
                                elif Girl == LauraX: 
                                        ch_l "I'd rather not."
                                                                  
            "Disband party" if Girl in Party: 
                        ch_p "Ok, you can leave if you prefer."
                        $ Options = Party[:]
                        while Options:
                                $ Party.remove(Options[0])       
                                call Girls_Schedule([Options[0]],0)         
                                if "leaving" in Options[0].RecentActions:
                                        $ Options[0].DrainWord("leaving")
                                if Options[0] == RogueX: 
                                        if Options[0].Loc == bg_current:
                                                ch_r "Ok, I'll probably stick around for a bit anyway."
                                        else:
                                                ch_r "Ok, see you later then."               
                                elif Options[0] == KittyX:
                                        if Options[0].Loc == bg_current:
                                                ch_k "Good to know, but I'm[Girl.like] fine here."
                                        else:
                                                ch_k "Cool, later."
                                elif Options[0] == EmmaX: 
                                        if Options[0].Loc == bg_current:
                                                ch_e "I'm glad I have your \"permission\" to leave, but I'd rather be here."
                                        elif Options[0].Loc == "bg teacher" and bg_current == "bg classroom":
                                                ch_e "I'm glad I have your \"permission\" to leave, but I {i}do{/i} have a class to teach."
                                        else:
                                                ch_e "If that's all then, I'll see you later."
                                elif Options[0] == LauraX: 
                                        if Options[0].Loc == bg_current:
                                                ch_l "I think i'm fine here."
                                        else:
                                                ch_l "Ok, see ya then." 
                                if Options[0].Loc != bg_current:
                                        call Set_The_Scene   
                                $ Options.remove(Options[0])
                        return
                    
            "Switch to. . .":
                    call Switch_Chat
                            
            "Never mind.":
                        if Girl == RogueX: 
                                ch_r "Ok, later then."
                        elif Girl == KittyX:
                                ch_k "Ok, bye."
                        elif Girl == EmmaX: 
                                ch_e "We'll talk later then."
                        elif Girl == LauraX: 
                                ch_l "Ok."
                        return     
        jump Chat_Menu
# End Main Chat menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Switch_Chat:
    #called from Main Chat, Settings, or Wardrobe
    $ Line = Girl
    menu:
        "[RogueX.Name]" if Girl != RogueX:
                $ Girl = RogueX    
        "[KittyX.Name]" if Girl != KittyX and "met" in KittyX.History:
                $ Girl = KittyX      
        "[EmmaX.Name]" if Girl != EmmaX and "met" in EmmaX.History:
                $ Girl = EmmaX       
        "[LauraX.Name]" if Girl != LauraX and "met" in LauraX.History:
                $ Girl = LauraX  
        "Never mind":
                $ Line = 0
                return
                
    if Girl.Loc != bg_current:
        if Girl in Digits:
                "You give [Girl.Name] a call."                                
                if "classcaught" not in EmmaX.History:
                    ch_e "I don't have time to talk to students right now."
                    $ Girl = Line                                    
        else:
                    "You don't have her number."
                    $ Girl = Line
    call Shift_Focus(Girl)
    if "angry" not in Girl.RecentActions and Girl != Line:
            if Girl == RogueX:
                    ch_r "So what did you want to talk about, [Girl.Petname]?"
            elif Girl == KittyX:
                    ch_k "So[Girl.like]what did you want to talk about, [Girl.Petname]?"
            elif Girl == EmmaX:
                    ch_e "What was it you wanted to discuss, [Girl.Petname]?"
            elif Girl == LauraX:            
                    ch_l "Yeah?"
    $ Line = 0
    return
    
# Start Girl_Dismissed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Dismissed(Girl=0,Leaving = 0):
    if Girl not in TotalGirls:
            $ Girl = Ch_Focus
    if Girl in Party:        
            $ Party.remove(Girl)
    call Girls_Schedule([Girl],0) 
    #if Girl.Loc == bg_current then it means she wants to stay here
    if "leaving" in Girl.RecentActions:
                $ Girl.DrainWord("leaving")
    menu:
        "You can leave if you like.":
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 700, "O"):
                        if Girl == RogueX:
                                ch_r "Thanks, but I think I'll stick around."
                        elif Girl == KittyX:  
                                ch_k "Well, I think I'll stay."
                        elif Girl == EmmaX:
                                ch_e "Be that as it may, I'll stick around for a bit."
                        elif Girl == LauraX: 
                                ch_l "Ok. [[she does not seem to be moving. . .]"
                else:
                        if Girl == RogueX:
                                ch_r "Sure, ok. See you later."
                        elif Girl == KittyX:  
                                ch_k "Ok, later!"
                        elif Girl == EmmaX:
                                ch_e "Very well, [Girl.Petname]"
                        elif Girl == LauraX: 
                                ch_l "Ok."
                        $ Leaving = 1     
                # End "You can leave if you like."
        "Could you give me the room please?":                            
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 800, "LO"):
                        if Girl == RogueX:
                                ch_r "I'd rather stick around."
                        elif Girl == KittyX: 
                                ch_k "I've got nowhere better to be."
                        elif Girl == EmmaX:
                                ch_e "As it happens, I don't have any other plans."
                        elif Girl == LauraX: 
                                ch_l "Nobody's kicking you out [[She doesn't move]."
                elif not ApprovalCheck(Girl, 500, "LO"):
                        if Girl == RogueX:
                                ch_r "I think I should probably stick around."
                        elif Girl == KittyX:  
                                ch_k "Yeah, no."     
                        elif Girl == EmmaX:     
                                ch_e "I don't think that I can."          
                        elif Girl == LauraX: 
                                ch_l "Nope."               
                else:
                        if "dismissed" not in Girl.DailyActions:
                                $ Girl.Statup("Obed", 30, 5)
                                $ Girl.Statup("Obed", 50, 5)
                        if Girl == RogueX:
                                ch_r "Not a problem, see you later then." 
                        elif Girl == KittyX:            
                                ch_k "Sure, ok."  
                        elif Girl == EmmaX:
                                ch_e "Very well. . ." 
                        elif Girl == LauraX:   
                                ch_l "Sure, ok." 
                        $ Leaving = 1
                #end "Could you give me the room please?"
        "You can go now.":                         
                if Girl.Loc == bg_current and not ApprovalCheck(Girl, 500, "O"):
                        if Girl == RogueX:
                                ch_r "I think I'll stay."    
                        elif Girl == KittyX: 
                                ch_k "Um, no."
                        elif Girl == EmmaX:
                                ch_e "No, I don't believe that I can."
                        elif Girl == LauraX:     
                                ch_l "But I won't."
                elif not ApprovalCheck(Girl, 300, "O"):
                        $ Girl.FaceChange("confused") 
                        if Girl == RogueX:
                                ch_r "Well if you want me to go, then maybe I should stick around."
                        elif Girl == KittyX:  
                                ch_k "Not when you've got me curious."
                        elif Girl == EmmaX:
                                ch_e "Now I am intrigued."
                        elif Girl == LauraX: 
                                ch_l "Why?"
                else:
                        if "dismissed" not in Girl.DailyActions:
                                $ Girl.Statup("Obed", 40, 10)
                                $ Girl.Statup("Obed", 60, 5)
                        if Girl == RogueX:
                                ch_r "If you wish." 
                        elif Girl == KittyX:  
                                ch_k "Um, ok." 
                        elif Girl == EmmaX:
                                ch_e "Very well. . ."
                        elif Girl == LauraX:    
                                ch_l "Ok."  
                        $ Leaving = 1 
                #end "You can go now."
        "Nevermind.":
                        return                             
    
    if not Leaving and bg_current in ("bg campus","bg classroom","bg dangerroom"):
            #if there is space nearby. . .
            call Remove_Girl(Girl,1,1)
    elif not Leaving:     
            #if she's refused to leave yet. . .
            menu:
                extend ""
                "I insist, get going.":  
                        if Girl.Loc != bg_current and (ApprovalCheck(Girl, 1200, "LO") or ApprovalCheck(Girl, 500, "O")):
                                #If she has someplace to be and is obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 70, -5, 1)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Obed", 80, 5)
                                if Girl == RogueX:
                                        ch_r "Ok, if you insist." 
                                elif Girl == KittyX:  
                                        ch_k "Um, ok."  
                                elif Girl == EmmaX:
                                        ch_e "Very well. . ."  
                                elif Girl == LauraX: 
                                        ch_l "Ok, fine."  
                                $ Leaving = 1           
                        elif Girl.Loc != bg_current and (ApprovalCheck(Girl, 1000, "LO") or ApprovalCheck(Girl, 300, "O")):
                                #If she has someplace to be and is less obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 70, -5, 1)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Obed", 80, 5)
                                $ Girl.FaceChange("angry") 
                                if Girl == RogueX:
                                        ch_r "Fine, if you're going to be a dick about it."
                                elif Girl == KittyX:  
                                        ch_k "Fine, jerk!"    
                                elif Girl == EmmaX:
                                        ch_e "I'll leave, but do not test me, [Girl.Petname]" 
                                elif Girl == LauraX: 
                                        ch_l "I've got stuff to do anyway."      
                                $ Leaving = 1           
                        elif Girl.Loc != bg_current:
                                #If she has someplace to be but is not obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 70, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 50, 5)
                                        $ Girl.Statup("Inbt", 80, 3)
                                $ Girl.FaceChange("angry") 
                                if Girl == RogueX:
                                        ch_r "Like hell I will."   
                                elif Girl == KittyX:  
                                        ch_k "Noooope."          
                                elif Girl == EmmaX:
                                        ch_e "Well now I'm definitely not."    
                                elif Girl == LauraX: 
                                        ch_l "Not until I see what you have planned here."  
                        elif ApprovalCheck(Girl, 1400, "LO") or ApprovalCheck(Girl, 400, "O"):
                                #If she has nowhere to be to be but is obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Obed", 50, 10)
                                        $ Girl.Statup("Obed", 80, 5)
                                $ Girl.FaceChange("sad") 
                                if Girl == RogueX:
                                        ch_r "Ok, if that's what you want."
                                elif Girl == KittyX: 
                                        ch_k "Um, sure, fine." 
                                elif Girl == EmmaX:
                                        ch_e "I suppose I could get out of your way."
                                elif Girl == LauraX: 
                                        ch_l "Ok."
                                $ Leaving = 1           
                        else:
                                #If she has nowhere to be to be and is not obedient
                                if "dismissed" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 50, -5, 1)
                                        $ Girl.Statup("Love", 70, -10, 1)
                                        $ Girl.Statup("Obed", 50, -5)
                                        $ Girl.Statup("Inbt", 50, 3)
                                        $ Girl.Statup("Inbt", 80, 2)
                                $ Girl.FaceChange("sad") 
                                if Girl == RogueX:
                                        ch_r "You wish."  
                                elif Girl == KittyX:  
                                        ch_k "Yeah right."      
                                elif Girl == EmmaX:
                                        ch_e "That doesn't look like it'll be happening."   
                                elif Girl == LauraX:  
                                        ch_l "Nope."  
                        #end "I insist, get going."
                "Ok, nevermind.":
                                pass               
                    
    if "dismissed" not in Girl.DailyActions:
            $ Girl.DailyActions.append("dismissed")  
    if Girl in Nearby:
            "You shift a bit away from [Girl.Name]"
    elif Leaving == 0:
            # Stay
            $ Girl.Loc = bg_current
    else:
            # Go
            if Girl.Loc != bg_current: #it stays the same
                pass
            elif bg_current == Girl.Home:
                $ Girl.Loc = "bg campus"
            else:
                $ Girl.Loc = Girl.Home
            call AllReset(Girl)
            "[Girl.Name] heads out." 
    return
    #end "you can leave"
# End Girl_Dismissed / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Flirt menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Flirt(Girl =0):
    # call Flirt(RogueX)   
    $ Girl = Ch_Focus if Girl not in TotalGirls else Girl
    call Shift_Focus(Girl)
    
    if Girl.Loc != bg_current: 
            #menu for if over the phone
            menu:            
                "Compliment her":
                        $ Girl.Chat[5] = 1 #can only flirt once per cycle. 
                        call Compliment(Girl)
                "Never mind [[exit]":
                        pass
    else:
            #Menu for if local.
            $ Girl.Chat[5] = 1 #can only flirt once per cycle. 
            menu:        
                "Compliment her":
                            call Compliment(Girl)
                        
                "Say you love her":
                            call Love_You(Girl)
                    
                "Touch her cheek":                                                                              
                            call TouchCheek(Girl)
                
                "Hold hands":
                            call Hold_Hands(Girl)        
                        
                "Pat her head":
                            call Girl_Headpat(Girl)
                    
                "Kiss her cheek":                                                                          
                            "You lean over, brush her hair aside and kiss her on the cheek."                
                            if ApprovalCheck(Girl, 650, "L", TabM=1):
                                        $ Girl.FaceChange("sexy", 1) 
                                        $ Girl.Statup("Love", 90, 1)          
                                        $ Girl.Statup("Obed", 40, 2) 
                                        if Girl == RogueX: 
                                                ch_r "That was real sweet, [Girl.Petname]."
                                        elif Girl == KittyX: 
                                                ch_k ". . ."
                                                ch_k "Wow. Hey."  
                                        elif Girl == EmmaX: 
                                                ch_e ". . ."
                                                ch_e "Hello. . ."    
                                        elif Girl == LauraX:     
                                                ch_l ". . ."
                                                $ Girl.FaceChange("sexy", 1, Eyes="side") 
                                                ch_l "Huh."
                            elif ApprovalCheck(Girl, 500, "L", TabM=1):
                                        $ Girl.FaceChange("surprised", 1)
                                        $ Girl.Statup("Love", 70, 2)         
                                        $ Girl.Statup("Obed", 40, 2)            
                                        $ Girl.Statup("Inbt", 20, 1) 
                                        if Girl == RogueX: 
                                                ch_r "What was that for, [Girl.Petname]?"
                                        elif Girl == KittyX:   
                                                ch_k ". . . hey! What's the deal?"
                                        elif Girl == EmmaX: 
                                                ch_e ". . . to what do I owe the pleasure?"    
                                        elif Girl == LauraX:     
                                                ch_l ". . . hey!"
                                                ch_l "What's that about?"
                            elif ApprovalCheck(Girl, 300, "L", TabM=1):                    
                                        $ Girl.FaceChange("angry", 1)
                                        $ Girl.Statup("Love", 90, -1)          
                                        $ Girl.Statup("Obed", 60, 2)            
                                        $ Girl.Statup("Inbt", 40, 1) 
                                        if Girl == RogueX: 
                                                ch_r "Hey, keep your distance, [Girl.Petname]!"
                                        elif Girl == KittyX:   
                                                ch_k "I don't[Girl.like]like you like that?"
                                        elif Girl == EmmaX:     
                                                ch_e "That's highly inappropriate, [Girl.Petname]"
                                                ch_e "[[mumbles] -in public, at least. . ."
                                        elif Girl == LauraX:     
                                                ch_l "That's a bit forward."
                            else: 
                                        $ Girl.FaceChange("angry", 1)
                                        $ Girl.Statup("Love", 90, -5)          
                                        $ Girl.Statup("Obed", 90, 5)            
                                        $ Girl.Statup("Inbt", 40, 3) 
                                        if Girl == RogueX: 
                                                ch_r "Hey, back off!" 
                                        elif Girl == KittyX:   
                                                ch_k "Keep off me!"
                                        elif Girl == EmmaX:     
                                                ch_e "Stop that at once."
                                        elif Girl == LauraX:    
                                                ch_l "Keep back!"
                            $ Girl.Addict -= 1
                            $ Girl.Addictionrate += 1
                            $ Girl.Addictionrate = 3 if Girl.Addictionrate < 3 else Girl.Addictionrate 
                       
                "Kiss her lips":
                            if ApprovalCheck(Girl, 1000, TabM=2,Alt=[[RogueX],800]) or ApprovalCheck(Girl, 600, "L", TabM=2): 
                                    $ Line = renpy.random.choice(["You lean over, put your hand against her cheek, and plant a kiss on her lips.",      
                                                                    "You lean down, tilt her head back, and plant a kiss on her lips.",
                                                                    "You turn "+Girl.Name+" around and plant a deep kiss on her."]) 
                                    "[Line]"
                            elif ApprovalCheck(Girl, 1000,Alt=[[RogueX],800]) or ApprovalCheck(Girl, 600, "L"): 
                                    $ Girl.FaceChange("bemused", 1)
                                    $ Girl.Eyes = "side"                  
                                    $ Girl.Statup("Obed", 50, -1)            
                                    $ Girl.Statup("Inbt", 40, 2)
                                    if Girl == RogueX: 
                                            "You lean close for a kiss, but [Girl.Name] plants a hand on your face and pushes you back."
                                            ch_r "Isn't this a bit public, [Girl.Petname]?" 
                                    elif Girl == KittyX:   
                                            "You lean close for a kiss, but [Girl.Name] gently elbows your ribs."
                                            ch_k "Not in public, [Girl.Petname]." 
                                    elif Girl == EmmaX:     
                                            "You lean close for a kiss, but [Girl.Name] plants a hand on your face and pushes you back."
                                            ch_e "Not in public, [Girl.Petname]." 
                                    elif Girl == LauraX:     
                                            "You lean close for a kiss, but [Girl.Name] gently elbows your ribs."
                                            ch_l "Not here, [Girl.Petname]."                             
                                    return
                            else:                
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.Statup("Love", 90, -5)          
                                    $ Girl.Statup("Obed", 50, -1)            
                                    $ Girl.Statup("Inbt", 40, 5) 
                                    if Girl == RogueX: 
                                            "You lean close for a kiss, but [Girl.Name] plants a hand on your face and pushes you back."
                                            ch_r "What the hell, [Girl.Petname]?" 
                                    elif Girl == KittyX:   
                                            "You lean close for a kiss, but [Girl.Name] gently elbows your ribs."
                                            ch_k "Keep your distance, [Girl.Petname]." 
                                    elif Girl == EmmaX:     
                                            "You lean close for a kiss, but [Girl.Name] plants a hand on your face and pushes you back."
                                            ch_e "No." 
                                    elif Girl == LauraX:     
                                            "You lean close for a kiss, but [Girl.Name] gently elbows your ribs."
                                            ch_l "Keep to yourself, [Girl.Petname]." 
                                    return
                            if Girl.Kissed:
                                    #if this wasn't the first kiss. . .
                                    if ApprovalCheck(Girl, 750, "L", TabM=1):
                                            $ Girl.FaceChange("sexy", 1)
                                            $ Girl.Statup("Love", 90, 2)          
                                            $ Girl.Statup("Obed", 50, 2) 
                                            if Girl == RogueX: 
                                                    ch_r "Hmm we should do that again, [Girl.Petname]."
                                            else:                               
                                                    call AnyLine(Girl,"Mmmmmmm. . .")
                                    elif ApprovalCheck(Girl, 650, "L", TabM=1):
                                            $ Girl.FaceChange("sexy", 1)
                                            $ Girl.Statup("Love", 90, 2)          
                                            $ Girl.Statup("Obed", 50, 2) 
                                            if Girl == RogueX: 
                                                    ch_r "Hmm, that was a nice surprise, [Girl.Petname]?"
                                            elif Girl == KittyX:   
                                                    ch_k "Hmm, \"hello\" to you too, [Girl.Petname]?"
                                            elif Girl == EmmaX:     
                                                    ch_e "Hmm, hello [Girl.Petname]. . ."
                                            elif Girl == LauraX:     
                                                    ch_l "Hmm, that's nice. . ."
                                    elif ApprovalCheck(Girl, 500, "L", TabM=1):
                                            $ Girl.FaceChange("surprised", 1)
                                            $ Girl.Statup("Love", 70, 3)          
                                            $ Girl.Statup("Obed", 50, 2) 
                                            if Girl == RogueX: 
                                                    ch_r "Hey, what do you think you're doing, [Girl.Petname]?"
                                            elif Girl == KittyX: 
                                                    ch_k "That's[Girl.like]a bit forward?"  
                                            elif Girl == EmmaX:   
                                                    ch_e "You're incorrigible."  
                                            elif Girl == LauraX:     
                                                    ch_l "I don't know about that."
                                    elif ApprovalCheck(Girl, 300, "L", TabM=1):
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -3)          
                                            $ Girl.Statup("Obed", 60, 3)            
                                            $ Girl.Statup("Inbt", 40, 2) 
                                            if Girl == RogueX: 
                                                    ch_r "That really wasn't appropriate, [Girl.Petname]!"
                                            elif Girl == KittyX:     
                                                    ch_k "Dude!"
                                            elif Girl == EmmaX: 
                                                    ch_e "Highly inappropriate!"
                                                    $ Girl.FaceChange("bemused", Eyes="side")
                                                    ch_e "-at least while in public. . ."    
                                            elif Girl == LauraX:   
                                                    ch_l "Back it off, [Girl.Petname]."
                                    else: 
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -8)          
                                            $ Girl.Statup("Obed", 90, 6)            
                                            $ Girl.Statup("Inbt", 40, 3)                         
                                            if Girl == RogueX: 
                                                    ch_r "Not cool, [Girl.Petname]."
                                            elif Girl == KittyX:  
                                                    ch_k "Back off, [Girl.Petname]." 
                                            elif Girl == EmmaX:    
                                                    ch_e "Down boy." 
                                            elif Girl == LauraX:     
                                                    ch_l "Fuck off."
                            else:                   
                                    #If this is the first kiss
                                    if ApprovalCheck(Girl, 750, "L", TabM=1):
                                            $ Girl.FaceChange("surprised", 1)
                                            $ Girl.Statup("Love", 70, 45)           
                                            $ Girl.Statup("Obed", 50, 20)
                                            $ Girl.Statup("Inbt", 50, 35)
                                            if Girl == RogueX: 
                                                    ch_r "Hmmm, that was a pleasant suprise. . ."
                                                    $ Girl.FaceChange("sexy")
                                                    ch_r "Maybe we should do that again, [Girl.Petname]."
                                            elif Girl == KittyX:   
                                                    ch_k ". . ."
                                                    ch_k "Hmmm, that was nice. . ."
                                                    $ Girl.FaceChange("sexy")
                                                    ch_k "Let me know if you want to do that again, [Girl.Petname]."
                                            elif Girl == EmmaX:     
                                                    ch_e ". . ."
                                                    ch_e "Hmmm, that was a pleasant surprise. . ."
                                                    $ Girl.FaceChange("sexy")
                                                    ch_e "I could always use some more, [Girl.Petname]."
                                            elif Girl == LauraX:     
                                                    $ Girl.FaceChange("normal",Eyes="side")
                                                    ch_l ". . ."
                                                    $ Girl.FaceChange("sexy",Eyes="side")
                                                    ch_l "Hmmm, that was nice. . ."
                                                    $ Girl.FaceChange("sexy")
                                    elif ApprovalCheck(Girl, 650, "L", TabM=1):
                                            $ Girl.FaceChange("surprised", 1)
                                            $ Girl.Statup("Love", 80, 30)           
                                            $ Girl.Statup("Obed", 50, 25)
                                            $ Girl.Statup("Inbt", 50, 35)
                                            if Girl == RogueX: 
                                                    ch_r "Wha, what was that, [Girl.Petname]?"
                                                    ch_r "Hmm, not that it was entirely unpleasant. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "Huh?"
                                                    ch_k "I, um[Girl.like]don't know what to do with that. . ."
                                            elif Girl == EmmaX:  
                                                    ch_e "Hmm?"
                                                    ch_e "So we're there now, are we? . ."   
                                            elif Girl == LauraX:     
                                                    ch_l " ! "
                                                    ch_l "I'm not sure what to do with that. . ."
                                    elif ApprovalCheck(Girl, 500, "L", TabM=1):
                                            $ Girl.FaceChange("surprised", 1)            
                                            $ Girl.Statup("Obed", 70, 30)
                                            $ Girl.Statup("Inbt", 70, 35)
                                            if Girl == RogueX: 
                                                    ch_r "Hey, what do you think you're doing, [Girl.Petname]?"
                                            elif Girl == KittyX:   
                                                    ch_k "What's the deal, [Girl.Petname]?!"
                                            elif Girl == EmmaX: 
                                                    ch_e "I don't think that's really appropriate, [Girl.Petname]."    
                                            elif Girl == LauraX:     
                                                    ch_l "What are you thinking, [Girl.Petname]?!"
                                    elif ApprovalCheck(Girl, 700, TabM=1):
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 60, -5) 
                                            $ Girl.Statup("Obed", 70, 40)
                                            $ Girl.Statup("Inbt", 70, 40)
                                            if Girl == RogueX: 
                                                    ch_r "Wha, what the hell was that about?!"
                                            elif Girl == KittyX:   
                                                    ch_k "the hell, [Girl.Petname]?!"
                                            elif Girl == EmmaX:     
                                                    ch_e "We can't be seen doing that, [Girl.Petname]."
                                            elif Girl == LauraX:     
                                                    ch_l "What the hell, [Girl.Petname]?!"
                                    else: 
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 60, -15) 
                                            $ Girl.Statup("Obed", 70, 50)
                                            $ Girl.Statup("Inbt", 70, 40)
                                            if Girl == RogueX: 
                                                    ch_r "Not cool, [Girl.Petname]."
                                            elif Girl == KittyX:   
                                                    ch_k "[Girl.Like]WTF?!"
                                            elif Girl == EmmaX: 
                                                    ch_e "How dare you?"    
                                            elif Girl == LauraX:     
                                                    ch_l "Fuck off."
                                    
                            $ Girl.Kissed += 1            
                            $ Girl.Addict -= 1
                            $ Girl.Addictionrate += 1
                            $ Girl.Addictionrate = 3 if Girl.Addictionrate < 3 else Girl.Addictionrate 
                                
                            if ApprovalCheck(Girl, 650, TabM=1) and (Girl != EmmaX or Taboo < 40):
                                if Girl == EmmaX and "three" not in EmmaX.History:
                                        if not AloneCheck(EmmaX):
                                                # if there are other girls in the room. . .
                                                call Emma_ThreeCheck
                                if Girl.Love > Girl.Obed and Girl.Love > Girl.Inbt:
                                        if Girl == RogueX: 
                                                ch_r "Gimme some more sugar, [Girl.Petname]."
                                        elif Girl == KittyX:   
                                                ch_k "More smooches, [Girl.Petname]!"
                                        elif Girl == EmmaX:     
                                                ch_e "I hope there's more where that came from. . ."
                                        elif Girl == LauraX:     
                                                ch_l "I think I'd like some more."
                                elif Girl.Obed > Girl.Inbt:
                                        if Girl == RogueX: 
                                                ch_r "Did you want to follow up on that?"
                                        elif Girl == KittyX:   
                                                ch_k "I'd be open to more if you are."
                                        elif Girl == EmmaX:     
                                                ch_e "I wouldn't mind some more of that. . ."
                                        elif Girl == LauraX:     
                                                ch_l "Did you want to continue?"
                                else:
                                        if Girl == RogueX: 
                                                ch_r "You'd best have a follow-up to that, [Girl.Petname]."
                                        elif Girl == KittyX:   
                                                ch_k "We could keep going, [Girl.Petname]."
                                        elif Girl == EmmaX:     
                                                ch_e "Get over here. . ."
                                        elif Girl == LauraX:     
                                                ch_l "We could keep going, [Girl.Petname]."
                                menu:
                                    "Keep kissing?"
                                    "You know it.":
                                            $ Girl.Statup("Lust", 60, 3)  
                                            $ Girl.Statup("Love", 90, 1)
                                            $ Girl.Statup("Love", 60, 3) 
                                            $ Girl.Statup("Inbt", 50, 2)
                                            call expression Girl.Tag + "_SexAct" pass ("kissing")
                                            call Trig_Reset(1)
                                            return
                                    "Just a taste [[no].":
                                            $ Girl.FaceChange("bemused", 1) 
                                            $ Girl.Statup("Lust", 40, 1) 
                                            $ Girl.Statup("Lust", 60, 4) 
                                            $ Girl.Statup("Obed", 70, 2)
                                            $ Girl.Statup("Inbt", 50, 2)
                                            if Girl == RogueX: 
                                                    ch_r "At some point I'm gonna need the whole mouthful, [Girl.Petname]."
                                            elif Girl == KittyX:   
                                                    ch_k "Oh, way to[Girl.like]tease a girl!"
                                            elif Girl == EmmaX:  
                                                    ch_e "Tease. . ."   
                                            elif Girl == LauraX:     
                                                    ch_l "Ah, you were kidding."
                                    "Nope.":
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 80, -2) 
                                            $ Girl.Statup("Obed", 70, 3)
                                            $ Girl.Statup("Inbt", 50, 1)
                                            if Girl == RogueX: 
                                                    ch_r "You're writing checks you can't cash, [Girl.Petname]."
                                            elif Girl == KittyX:   
                                                    ch_k "Don't string me along here, [Girl.Petname]."
                                            elif Girl == EmmaX:   
                                                    ch_e "I don't appreciate games, [Girl.Petname]."  
                                            elif Girl == LauraX:                                 
                                                    ch_l "Ah, you were kidding."
                            elif Taboo and Girl == EmmaX:
                                        $ Girl.FaceChange("sad")
                                        ch_e "But we just can't."
                                        ch_e "Not here."
                            else:
                                if Girl == RogueX: 
                                        ch_r "Don't just plant one on a girl without ask'in first."
                                elif Girl == KittyX: 
                                        ch_k "Well[Girl.like]don't do it again."  
                                elif Girl == EmmaX:  
                                        ch_e "Don't try that again."   
                                elif Girl == LauraX:     
                                        ch_l "Don't push me."
                #end Kiss
                            
                "Hug her":          
                            if ApprovalCheck(Girl, 200, TabM=1):        
                                    "You lean over and wrap [Girl.Name] in a warm hug."
                            else:                
                                    $ Girl.FaceChange("angry", 1)
                                    "You lean in with your arms wide, but [Girl.Name] grabs your shoulders and shoves you back."
                                    if Girl == RogueX: 
                                            ch_r "Hey, what're you doing, [Girl.Petname]?" 
                                    elif Girl == KittyX:   
                                            ch_k "What's the deal, [Girl.Petname]?" 
                                    elif Girl == EmmaX:     
                                            ch_e "What exactly is that about, [Girl.Petname]?" 
                                    elif Girl == LauraX:     
                                            ch_l "What's was that, [Girl.Petname]?" 
                                    return
                            if Girl.SEXP >= 30: 
                                    $ Girl.Statup("Lust", 60, 3) 
                                    $ Girl.Statup("Love", 90, 1)          
                                    $ Girl.Statup("Obed", 90, 3)            
                                    $ Girl.Statup("Inbt", 90, 3) 
                                    $ Girl.FaceChange("sexy")
                                    if Girl == RogueX: 
                                            ch_r "Hmm, are you hinting at something there, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "You're warming me up, [Girl.Petname]."
                                    elif Girl == EmmaX:     
                                            ch_e "Hmmm, what did you have in mind, [Girl.Petname]."
                                    elif Girl == LauraX:     
                                            ch_l "I think you're flipping my switch, [Girl.Petname]."
                            elif ApprovalCheck(Girl, 600, "L", TabM=1):
                                    $ Girl.FaceChange("sexy")
                                    $ Girl.Statup("Love", 90, 1)          
                                    $ Girl.Statup("Obed", 40, 2)            
                                    $ Girl.Statup("Inbt", 30, 1) 
                                    if Girl == RogueX: 
                                            ch_r "Hmm, nice to see you too, [Girl.Petname]?"
                                    elif Girl == KittyX: 
                                            ch_k "Hmm, warm huggies."  
                                    elif Girl == EmmaX:     
                                            ch_e "Hmm, I do enjoy this. . ."
                                    elif Girl == LauraX:     
                                            ch_l "Hmmmmm. . ."
                            elif ApprovalCheck(Girl, 450, TabM=1):
                                    $ Girl.FaceChange("surprised", 1)
                                    $ Girl.Statup("Love", 90, 1)  
                                    $ Girl.Statup("Love", 70, 1)        
                                    $ Girl.Statup("Obed", 40, 2)            
                                    $ Girl.Statup("Inbt", 30, 1) 
                                    if Girl == RogueX: 
                                            ch_r "Hey, [Girl.Petname]. What's up?"
                                    elif Girl == KittyX:   
                                            ch_k "Hey[Girl.like]what is this about?"
                                    elif Girl == EmmaX:   
                                            ch_e "Hm? What was it you wanted?"  
                                    elif Girl == LauraX: 
                                            ch_l "Um, [Girl.Petname]? What is this?"
                            elif ApprovalCheck(Girl, 350, TabM=1):
                                    $ Girl.FaceChange("angry", 1)  
                                    $ Girl.Statup("Love", 70, 1)        
                                    $ Girl.Statup("Obed", 50, 3)            
                                    $ Girl.Statup("Inbt", 30, 2) 
                                    if Girl == RogueX: 
                                            ch_r "I don't really know you that well."
                                    elif Girl == KittyX:   
                                            ch_k "I'm not comfortable with this. . ."
                                    elif Girl == EmmaX:     
                                            ch_e "We can't be seen like this. . ."
                                    elif Girl == LauraX:     
                                            ch_l "This is making me uncomfortable. . ."
                            else: 
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.Statup("Love", 10, -1)  
                                    $ Girl.Statup("Love", 40, -1)         
                                    $ Girl.Statup("Obed", 20, 2)        
                                    $ Girl.Statup("Obed", 50, 2)            
                                    $ Girl.Statup("Inbt", 30, 2)
                                    if Girl == RogueX: 
                                            ch_r "Had enough, [Girl.Petname]?"   
                                    elif Girl == KittyX:   
                                            ch_k "What was that about, [Girl.Petname]?"  
                                    elif Girl == EmmaX:   
                                            ch_e "What was that about, [Girl.Petname]?"
                                    elif Girl == LauraX:     
                                            ch_l "Hey, back off."      
                # end hug
                
                "Slap her ass" if Girl.Loc == bg_current:
                            call Slap_Ass(Girl)
                    
                "Pinch her ass":
                            $ Girl.FaceChange("surprised", 1)
                            if Girl.SEXP < 5 or not ApprovalCheck(Girl, 600, TabM=1):        
                                    "You come up to [Girl.Name] from behind and quickly pinch her butt."
                                    $ Girl.FaceChange("angry")
                                    "She slaps your hand away and rounds on you."
                                    if Girl == RogueX: 
                                            ch_r "Hey, what're you doing, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "Hey! Bad touch!"  
                                    elif Girl == EmmaX:    
                                            ch_e "Down boy!"  
                                    elif Girl == LauraX:     
                                            ch_l "What are you thinking?" 
                                    return
                            if Girl.SEXP >= 30: 
                                    $ Girl.Statup("Lust", 60, 3) 
                                    $ Girl.Statup("Love", 90, 1)           
                                    $ Girl.Statup("Obed", 60, 2)          
                                    $ Girl.Statup("Obed", 90, 1)            
                                    $ Girl.Statup("Inbt", 50, 3) 
                                    $ Girl.FaceChange("sexy")
                                    if Girl == RogueX: 
                                            ch_r "Ooh! Are you hinting at something there, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "Purrrr, Kitty like."
                                    elif Girl == EmmaX:     
                                            ch_e "Mmm, what was that for?"
                                    elif Girl == LauraX:     
                                            ch_l "Oooh! Getting rough?"
                            elif ApprovalCheck(Girl, 800, "L", TabM=1):
                                    $ Girl.FaceChange("sexy")
                                    $ Girl.Statup("Love", 90, 1)           
                                    $ Girl.Statup("Obed", 60, 2)          
                                    $ Girl.Statup("Obed", 90, 1)            
                                    $ Girl.Statup("Inbt", 50, 2) 
                                    if Girl == RogueX: 
                                            ch_r "Hmm, nice to see you too, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "Hmm, you know it, [Girl.Petname]."
                                    elif Girl == EmmaX:   
                                            ch_e "Oooh!"  
                                    elif Girl == LauraX:     
                                            ch_l "You like the way that feels, [Girl.Petname]?"
                            elif ApprovalCheck(Girl, 900, TabM=1):
                                    $ Girl.FaceChange("surprised")
                                    $ Girl.Statup("Love", 90, 1)           
                                    $ Girl.Statup("Obed", 60, 3)          
                                    $ Girl.Statup("Obed", 90, 2)            
                                    $ Girl.Statup("Inbt", 50, 2) 
                                    if Girl == RogueX: 
                                            ch_r "Ooh! What's up?"
                                    elif Girl == KittyX:   
                                            ch_k "Ooh! Hey!"
                                    elif Girl == EmmaX:    
                                            ch_e "Mmm, watch it." 
                                    elif Girl == LauraX:     
                                            ch_l "Wha?!"
                            elif ApprovalCheck(Girl, 800, TabM=1):
                                    $ Girl.FaceChange("angry")
                                    $ Girl.Statup("Love", 60, -3) 
                                    $ Girl.Statup("Love", 90, -1)           
                                    $ Girl.Statup("Obed", 60, 4)          
                                    $ Girl.Statup("Obed", 90, 3)            
                                    $ Girl.Statup("Inbt", 50, 2) 
                                    if Girl == RogueX: 
                                            ch_r "Hey, not cool."
                                    elif Girl == KittyX:   
                                            ch_k "Dude!"
                                    elif Girl == EmmaX:     
                                            ch_e "That is not something you can do in public."
                                    elif Girl == LauraX:     
                                            ch_l "Hey!"
                            else: 
                                    $ Girl.FaceChange("angry")
                                    $ Girl.Statup("Love", 60, -3) 
                                    $ Girl.Statup("Love", 90, -3)           
                                    $ Girl.Statup("Obed", 60, 5)          
                                    $ Girl.Statup("Obed", 90, 4)            
                                    $ Girl.Statup("Inbt", 50, 3)
                                    if Girl == RogueX: 
                                            ch_r "Ow! Lay off."  
                                    elif Girl == KittyX:   
                                            ch_k "Ow! That hurt!"  
                                    elif Girl == EmmaX: 
                                            ch_e "Would you like me to break those fingers?"    
                                    elif Girl == LauraX:       
                                            ch_l "Ouch! What the fuck?!"  
                #End pinch her ass
                            
                "Flip her skirt up" if Girl.PantsNum() == 5 and not Girl.Upskirt:      
                            $ Girl.FaceChange("surprised", 1)
                            $ Girl.Upskirt = 1
                            pause 0.5            
                            $ Girl.Upskirt = 0
                            "You sneak up on [Girl.Name] from behind and flip her skirt up quickly!"
                            $ Girl.Upskirt = 0
                            if Girl.Panties and not Taboo:
                                    #if this is in private and she's wearing panties
                                    if ApprovalCheck(Girl, 750, "L", TabM=2):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "Oh, naughty, [Girl.Petname]!"
                                                    ch_r "You could have just asked, you know. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "Cute!"
                                                    ch_e "You couldn't[Girl.like]ask? . ."
                                            elif Girl == EmmaX:    
                                                    ch_e "Cheeky. . ."
                                                    ch_e "You could have asked for a look."
                                            elif Girl == LauraX:   
                                                    ch_l "Hey!"  
                                                    ch_l "You wanted to see my underwear?"
                                            $ Girl.Statup("Love", 90, 3) 
                                    elif ApprovalCheck(Girl, 650, "L", TabM=2):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "Naughty naughty, [Girl.Petname]!"
                                            elif Girl == KittyX:  
                                                    ch_k "real cute, [Girl.Petname]." 
                                            elif Girl == EmmaX:   
                                                    ch_e "Cheeky."  
                                            elif Girl == LauraX:    
                                                    ch_l "What's the deal, [Girl.Petname]?"                                          
                                    elif ApprovalCheck(Girl, 300, "I", TabM=1):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == KittyX: 
                                                    ch_k "What's the deal?"  
                                            else: 
                                                    call AnyLine(Girl,"Hey, what do you think you're doing, "+Girl.Petname+"?")
                                    elif ApprovalCheck(Girl, 300, TabM=1) or Girl == LauraX:
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -3)           
                                            $ Girl.Statup("Obed", 80, 1)  
                                            if Girl == EmmaX:  
                                                    ch_e "Totally inappropriate, [Girl.Petname]."   
                                            elif Girl == LauraX:     
                                                    ch_l "Huh?"
                                            else:
                                                    call AnyLine(Girl,"Not cool, "+Girl.Petname+".") 
                                    else: 
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -5)          
                                            $ Girl.Statup("Obed", 80, 2) 
                                            if Girl == RogueX: 
                                                    ch_r "What the fuck, [Girl.Petname]!"
                                                    ch_r "That is not how you treat a lady!"
                                            elif Girl == KittyX:  
                                                    ch_k "What the fuck?" 
                                            elif Girl == EmmaX:   
                                                    ch_e "Completely inappropriate!"  
                                                    ch_e "I may have to consider your future at this school."
                                    $ Girl.Statup("Obed", 80, 5)             
                                    $ Girl.Statup("Inbt", 30, 2)           
                                    $ Girl.Statup("Inbt", 80, 3) 
                                    $ Girl.SeenPanties = 1
                            #end in private and she's wearing panties
                            
                            elif Girl.Panties: 
                                    #panties on, but in public
                                    if ApprovalCheck(Girl, 750, "L") and ApprovalCheck(Girl, 1300, TabM=2):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "Oh, naughty, [Girl.Petname]!"
                                                    ch_r "You could have just asked, you know. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "Cute!"
                                                    ch_e "You couldn't[Girl.like]ask? . ."
                                            elif Girl == EmmaX:    
                                                    ch_e "Cheeky. . ."
                                                    ch_e "You could have asked for a look."
                                            elif Girl == LauraX:   
                                                    ch_l "Hey!"  
                                                    ch_l "You wanted to see my underwear?"
                                            $ Girl.Statup("Love", 90, 3) 
                                    elif ApprovalCheck(Girl, 600, "L") and ApprovalCheck(Girl, 1200, TabM=2):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "[Girl.Petname]! A little warning!"
                                            elif Girl == KittyX:  
                                                    ch_k "[Girl.Petname]! A head's up wouldn't hurt." 
                                            elif Girl == EmmaX:   
                                                    ch_e "[Girl.Petname]!"
                                                    ch_e "Oh don't give me that look."  
                                            elif Girl == LauraX:  
                                                    ch_l "Hey, it's kinda public for that."
                                    elif ApprovalCheck(Girl, 600, "L"):
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -3)           
                                            $ Girl.Statup("Obed", 80, 3)  
                                            if Girl == RogueX: 
                                                    ch_r "[Girl.Petname]! This isn't the time or place for this!"
                                            elif Girl == KittyX: 
                                                    ch_k "[Girl.Petname]! Not in public!"  
                                            elif Girl == EmmaX:     
                                                    ch_e "[Girl.Petname]! I do have a reputation to maintain."
                                            elif Girl == LauraX:
                                                    ch_l "Hey, chill it."
                                    elif ApprovalCheck(Girl, 800, TabM=2):
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -5)           
                                            $ Girl.Statup("Obed", 80, 2)
                                            if Girl == EmmaX:   
                                                    ch_e "Are you out of your mind, [Girl.Petname]?" 
                                            elif Girl == LauraX:
                                                    ch_l "Hey!"
                                            else:
                                                    call AnyLine(Girl,"Wha! "+Girl.Petname+"!")
                                    else: 
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -10)          
                                            $ Girl.Statup("Obed", 80, 2)           
                                            $ Girl.Statup("Inbt", 80, 1) 
                                            if Girl == EmmaX:    
                                                    ch_e "Are you out of your mind, [Girl.Petname]?" 
                                            elif Girl == LauraX:
                                                    ch_l "Dude!" 
                                            else:
                                                    call AnyLine(Girl,"What the fuck, "+Girl.Petname+"!")
                                            call AnyLine(Girl,"Why would you even do that in public?")
                                    $ Girl.Statup("Obed", 80, 7)             
                                    $ Girl.Statup("Inbt", 30, 3)           
                                    $ Girl.Statup("Inbt", 80, 3)
                                    $ Girl.SeenPanties = 1                                
                            #end panties on, but in public
                            
                            elif not Taboo: 
                                    #no panties, in private
                                    if ApprovalCheck(Girl, 850, "L"):
                                            if Girl == RogueX: 
                                                    ch_r "Oh, naughty, [Girl.Petname]!"
                                                    ch_r "You could have just asked, you know. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "Cute!"
                                                    ch_e "You couldn't[Girl.like]ask? . ."
                                            elif Girl == EmmaX:    
                                                    ch_e "Cheeky. . ."
                                                    ch_e "You could have asked for a look."
                                            elif Girl == LauraX:   
                                                    ch_l "Hey!"  
                                                    ch_l "Like what you see?"
                                    elif ApprovalCheck(Girl, 700, "L"):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "[Girl.Petname]! A little warning!"
                                            elif Girl == KittyX:  
                                                    ch_k "[Girl.Petname]! A head's up wouldn't hurt." 
                                            elif Girl == EmmaX:   
                                                    ch_e "[Girl.Petname]!"
                                                    ch_e "Oh don't give me that look."  
                                            elif Girl == LauraX:  
                                                    ch_l "Hey, what's up?"
                                    elif ApprovalCheck(Girl, 600, "L"):
                                            $ Girl.FaceChange("bemused", 1)
                                            $ Girl.Statup("Love", 90, -3)           
                                            $ Girl.Statup("Obed", 80, 3) 
                                            if Girl == RogueX: 
                                                    ch_r "Wha?! [Girl.Petname]? . . I don't usually. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "Wha?! [Girl.Petname]? . ."
                                                    ch_k "It's not like I usually. . ."
                                            elif Girl == EmmaX:   
                                                    ch_e "Wha?! [Girl.Petname]?"
                                                    ch_e "You were expecting something else?"  
                                            elif Girl == LauraX:   
                                                    ch_l "Wha?! [Girl.Petname]?"  
                                    elif ApprovalCheck(Girl, 500):
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -5)           
                                            $ Girl.Statup("Obed", 80, 2)  
                                            if Girl == EmmaX:   
                                                    ch_e "Are you out of your mind, [Girl.Petname]?" 
                                            elif Girl == LauraX:
                                                    ch_l "Hey!"
                                            else:
                                                    call AnyLine(Girl,"Wha! "+Girl.Petname+"!")
                                    else: 
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -10)          
                                            $ Girl.Statup("Obed", 80, 2)           
                                            $ Girl.Statup("Inbt", 80, 1) 
                                            if Girl == EmmaX:    
                                                    ch_e "Are you out of your mind, [Girl.Petname]?" 
                                                    ch_e "Even if I had been wearing panties. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Dude!" 
                                            else:
                                                    call AnyLine(Girl,"What the fuck, "+Girl.Petname+"!")
                                                    call AnyLine(Girl,"I- I don't usually, you know. . .") 
                                    $ Girl.Statup("Obed", 80, 7)             
                                    $ Girl.Statup("Inbt", 30, 3)           
                                    $ Girl.Statup("Inbt", 80, 4) 
                                    call expression Girl.Tag + "_First_Bottomless" 
                             
                            #end no panties, in private   
                            else: 
                                    #no panties, in public
                                    if ApprovalCheck(Girl, 850, "L") and ApprovalCheck(Girl, 1500):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "Oh, naughty, [Girl.Petname]!"
                                                    ch_r "You could have just asked, you know. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "Cute!"
                                                    ch_e "You couldn't[Girl.like]ask? . ."
                                            elif Girl == EmmaX:    
                                                    ch_e "Cheeky. . ."
                                                    ch_e "You could have asked for a look."
                                            elif Girl == LauraX:   
                                                    ch_l "Hey!"  
                                                    ch_l "Like what you see?"
                                    elif ApprovalCheck(Girl, 700, "L") and ApprovalCheck(Girl, 1500):
                                            $ Girl.FaceChange("sexy", 1)
                                            if Girl == RogueX: 
                                                    ch_r "[Girl.Petname]! A little warning!"
                                            elif Girl == KittyX:  
                                                    ch_k "[Girl.Petname]! A head's up wouldn't hurt." 
                                            elif Girl == EmmaX:   
                                                    ch_e "[Girl.Petname]!"
                                                    ch_e "Oh don't give me that look."  
                                            elif Girl == LauraX:  
                                                    ch_l "Hey, what's up?"
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("bemused", 1)
                                            $ Girl.Statup("Love", 90, -3)           
                                            $ Girl.Statup("Obed", 80, 3)  
                                            if Girl == RogueX: 
                                                    ch_r "[Girl.Petname]! This isn't the time or place for this!"
                                            elif Girl == KittyX: 
                                                    ch_k "[Girl.Petname]! Not in public!"  
                                            elif Girl == EmmaX:     
                                                    ch_e "[Girl.Petname]! I do have a reputation to maintain."
                                            elif Girl == LauraX:
                                                    ch_l "Hey, chill it."
                                    elif ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -5)           
                                            $ Girl.Statup("Obed", 80, 2)  
                                            if Girl == EmmaX:   
                                                    ch_e "Are you out of your mind, [Girl.Petname]?" 
                                            elif Girl == LauraX:
                                                    ch_l "Hey!"
                                            else:
                                                    call AnyLine(Girl,"Wha! "+Girl.Petname+"!")
                                    else: 
                                            $ Girl.FaceChange("angry", 1)
                                            $ Girl.Statup("Love", 90, -10)          
                                            $ Girl.Statup("Obed", 80, 2)           
                                            $ Girl.Statup("Inbt", 80, 1) 
                                            if Girl == EmmaX:    
                                                    ch_e "Are you out of your mind, [Girl.Petname]?" 
                                                    ch_e "Even if I had been wearing panties. . ."
                                            elif Girl == LauraX:
                                                    ch_l "Dude!" 
                                            else:
                                                    call AnyLine(Girl,"What the fuck, "+Girl.Petname+"!")                                              
                                                    call AnyLine(Girl,"I- I don't usually, you know. . .")
                                    $ Girl.Statup("Obed", 80, 7)             
                                    $ Girl.Statup("Inbt", 30, 4)           
                                    $ Girl.Statup("Inbt", 80, 4)  
                                    call expression Girl.Tag + "_First_Bottomless" 
                            #end no panties, in public                
                            $ Girl.Statup("Lust", 60, 1) 
                            if "exhibitionist" in Girl.Traits:
                                $ Girl.Statup("Lust", 200, 4) 
                #End Flip her Skirt
                            
                "Grab her tit":
                            $ Girl.FaceChange("surprised", 1)
                            "You come up to [Girl.Name] and quickly honk her boob."
                            if Girl.SEXP < 5 or not ApprovalCheck(Girl, 600, TabM=2):  
                                    "You come up to [Girl.Name] and quickly honk her boob."
                                    $ Girl.FaceChange("angry")                                
                                    if Girl == RogueX: 
                                            show Rogue_Sprite
                                            with vpunch
                                            "She slaps your hand away and smacks your face."
                                            ch_r "What the fuck, [Girl.Petname]?" 
                                    elif Girl == KittyX: 
                                            show Kitty_Sprite
                                            with vpunch
                                            "She slaps your hand away and elbows you in the ribs."
                                            ch_k "[Girl.Like]WTF, [Girl.Petname]?"   
                                    elif Girl == EmmaX:  
                                            show Emma_Sprite
                                            with vpunch  
                                            "She slaps your hand away and elbows you in the ribs."
                                            ch_e "You must learn to resist temptations, [Girl.Petname]." 
                                    elif Girl == LauraX: 
                                            show Laura_Sprite
                                            with vpunch  
                                            "She flips you onto your back."
                                            ch_l "What the fuck?!" 
                                    return
                            if Girl.SEXP >= 40: 
                                    $ Girl.Statup("Lust", 60, 5) 
                                    $ Girl.Statup("Love", 90, 2) 
                                    $ Girl.FaceChange("sexy")
                                    if Girl == RogueX: 
                                            ch_r "Ooh! Are you hinting at something there, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "Hmm, I'm glad I can't phase right now, [Girl.Petname]."
                                    elif Girl == EmmaX:     
                                            ch_e "I do enjoy this, [Girl.Petname]. . ."
                                    elif Girl == LauraX:     
                                            ch_l "Hmm, that's pleasant."
                                    $ Count = 10
                            elif ApprovalCheck(Girl, 800, "L", TabM=1):
                                    $ Girl.FaceChange("sexy")
                                    $ Girl.Statup("Lust", 60, 2) 
                                    $ Girl.Statup("Love", 90, 1) 
                                    if Girl == RogueX: 
                                            ch_r "Hmm, hand to my heart, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "Hmm, keep it there, [Girl.Petname]."
                                    elif Girl == EmmaX:     
                                            ch_e "Mmmmmm. . ."
                                    elif Girl == LauraX:     
                                            ch_l "Hmm, are you enjoying that as much as I am?"
                                    $ Count = 7
                            elif ApprovalCheck(Girl, 1000, TabM=1):
                                    $ Girl.FaceChange("perplexed")  
                                    $ Girl.Statup("Lust", 60, 1)  
                                    if Girl == RogueX: 
                                            ch_r "Oh! A little handsy, eh [Girl.Petname]?"  
                                    elif Girl == KittyX:       
                                            ch_k "Kinda forward, [Girl.Petname]." 
                                    elif Girl == EmmaX:     
                                            ch_e "Rather forward of you, [Girl.Petname]."  
                                    elif Girl == LauraX:     
                                            ch_l "That's a bit inappropriate, [Girl.Petname]."              
                                    $ Count = 5
                            elif ApprovalCheck(Girl, 800, TabM=1):
                                    $ Girl.FaceChange("angry")
                                    $ Girl.Statup("Love", 90, -3)          
                                    $ Girl.Statup("Obed", 90, 4)            
                                    $ Girl.Statup("Inbt", 90, 3) 
                                    if Girl == RogueX: 
                                            ch_r "You seem to have misplaced something. . ."
                                    elif Girl == KittyX:   
                                            ch_k "You might want to move that?"
                                    elif Girl == EmmaX:  
                                            ch_e "You should move that, immediately."   
                                    elif Girl == LauraX:     
                                            ch_l "Are you going to move that hand or will I have to?"
                                    $ Count = 3
                            else: 
                                    $ Girl.FaceChange("angry")
                                    $ Girl.Statup("Love", 90, -5)          
                                    $ Girl.Statup("Obed", 90, 5)            
                                    $ Girl.Statup("Inbt", 90, 3) 
                                    if Girl == RogueX: 
                                            ch_r "Move it or lose it, [Girl.Petname]." 
                                    elif Girl == KittyX:   
                                            ch_k "You wanna lose that hand?" 
                                    elif Girl == EmmaX: 
                                            ch_e "Do you want to lose that hand?"     
                                    elif Girl == LauraX:                                          
                                            $ Girl.ArmPose = 2
                                            $ LauraX.Claws = 1
                                            ch_l "You wanna lose that hand?" 
                                    $ Count = 2
                            $ Girl.Statup("Obed", 70, 3)            
                            $ Girl.Statup("Inbt", 70, 2) 
                            if Girl == RogueX: 
                                    ch_r "Um, are you going to let go?"
                            elif Girl == KittyX:   
                                    ch_k "Um, are you done yet?"
                            elif Girl == EmmaX:   
                                    ch_e "Had enough?"  
                            elif Girl == LauraX:     
                                    ch_l "Are you satisfied?"
                            while Count > 0:
                                if Count == 6:
                                        $ Girl.FaceChange("sexy", 1)
                                        if Girl == RogueX: 
                                                ch_r "Hmmm, maybe do keep at it. . ."  
                                        elif Girl == KittyX:   
                                                ch_k "Mmmmm, I do kinda like it. . ."  
                                        elif Girl == EmmaX:  
                                                ch_e "Mmmmm, I do enjoy that. . ."     
                                        elif Girl == LauraX:     
                                                ch_l "That's pretty comforting. . ."  
                                        $ Girl.Statup("Lust", 90, 2)       
                                        $ Girl.Statup("Inbt", 70, 1)
                                elif Count == 3:
                                        $ Girl.FaceChange("perplexed")
                                        $ Girl.Statup("Lust", 90, 1) 
                                        if Girl == RogueX: 
                                                ch_r "That's nice [Girl.Petname], but maybe cut it out?"
                                        elif Girl == KittyX:  
                                                ch_k "Not that it's not nice, [Girl.Petname], but maybe stop?" 
                                        elif Girl == EmmaX:     
                                                ch_e "Not that I don't enjoy that, [Girl.Petname]. . ."
                                        elif Girl == LauraX:     
                                                ch_l "I like it, but maybe stop for now?"
                                elif Count == 2:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 90, -1) 
                                        if Girl == RogueX: 
                                                ch_r "Ok, stop it right now."
                                        elif Girl == KittyX:   
                                                ch_k "Ok, give it a rest."
                                        elif Girl == EmmaX:   
                                                ch_e "Ok, enough of that. . ."  
                                        elif Girl == LauraX:     
                                                ch_l "Ok, that's enough now."
                                elif Count == 1:
                                        $ Girl.FaceChange("angry")                                
                                        $ Girl.Statup("Love", 90, -5) 
                                        if Girl == RogueX: 
                                                ch_r "Back the hell off, [Girl.Petname]!"
                                                show Rogue_Sprite
                                                with vpunch
                                                "She slaps your hand away and smacks your face."
                                                ch_r "What the fuck, [Girl.Petname]?" 
                                        elif Girl == KittyX:   
                                                ch_k "Back it up, [Girl.Petname]!"
                                                show Kitty_Sprite
                                                with vpunch
                                                "She elbows you in the ribs."
                                                ch_k "WTF, [Girl.Petname]?" 
                                        elif Girl == EmmaX:     
                                                ch_e "Time to stop, [Girl.Petname]."
                                                show Emma_Sprite
                                                with vpunch
                                                "She elbows you in the ribs."
                                                ch_e "You should learn from social cues. . ." 
                                        elif Girl == LauraX:     
                                                ch_l "Take a step back, [Girl.Petname]!"
                                                show Laura_Sprite
                                                with vpunch
                                                "She gives you a quick shove."
                                        $ Count = 1                     
                                $ Count -= 1 if Count >= 0 else 0
                                    
                                if Count > 0:
                                    menu:
                                        "Your hand is still on her chest."
                                        "Let go immediately":
                                            if Count >= 7:
                                                    if Girl == RogueX: 
                                                            ch_r "Aw, can't say I'm not a {i}little{/i} disappointed. . ."  
                                                    elif Girl == KittyX:   
                                                            ch_k "That wasn't[Girl.like]{i}so{/i} bad. . ."  
                                                    elif Girl == EmmaX:     
                                                            ch_e "It's not that I really minded. . ."  
                                                    elif Girl == LauraX:     
                                                            ch_l "I didn't really mind it. . ."  
                                                    $ Girl.Statup("Lust", 60, 2)         
                                                    $ Girl.Statup("Inbt", 70, 1) 
                                            elif Count <= 4:
                                                    if Girl == RogueX: 
                                                            ch_r "Smart move."
                                                    elif Girl == KittyX:   
                                                            ch_k "Probably for the best."
                                                    elif Girl == EmmaX:   
                                                            ch_e "I suppose it's for the best."  
                                                    elif Girl == LauraX:     
                                                            ch_l "Probably for the best."
                                            $ Count = 0
                                            
                                        "Honk it again and let go":
                                            if Count >= 7:
                                                    if Girl == RogueX: 
                                                            ch_r "Heh, can't say I'm not a {i}little{/i} disappointed. . ."  
                                                    elif Girl == KittyX:  
                                                            ch_k "That wasn't[Girl.like]{i}so{/i} bad. . ."   
                                                    elif Girl == EmmaX:   
                                                            ch_e "Hmm, so amusing."      
                                                    elif Girl == LauraX:               
                                                            ch_l "I didn't mind it so much. . ."     
                                                    $ Girl.Statup("Lust", 60, 4) 
                                                    $ Girl.Statup("Inbt", 70, 1)
                                            elif Count >= 4:                                
                                                    if Girl == RogueX: 
                                                            ch_r "Classy, [Girl.Petname]."
                                                    elif Girl == KittyX:   
                                                            ch_k "A real joker, [Girl.Petname]."
                                                    elif Girl == EmmaX:  
                                                            ch_e "How droll."   
                                                    elif Girl == LauraX:    
                                                            ch_l "Heh."
                                            else:
                                                    $ Girl.FaceChange("angry")                                
                                                    if Girl == RogueX: 
                                                            ch_r "Dick move."
                                                    elif Girl == KittyX:   
                                                            ch_k "Douche."
                                                    elif Girl == EmmaX:     
                                                            ch_e "You'd better take more care."
                                                    elif Girl == LauraX:    
                                                            ch_l "Asshole."
                                            $ Girl.Statup("Obed", 70, 3)            
                                            $ Girl.Statup("Inbt", 70, 2)
                                            $ Count = 0 
                                                
                                        "Fondle it a little":                            
                                                if Girl.FondleB and ApprovalCheck(Girl, 1000, TabM=2):                                
                                                        $ Girl.FaceChange("sexy",1)
                                                        $ Girl.Eyes = "closed"
                                                        $ Girl.Statup("Lust", 90, 5) 
                                                else:
                                                        $ Girl.FaceChange("perplexed")
                                                        $ Girl.Statup("Lust", 90, 2) 
                                                        $ Count -= 1
                                                $ Girl.Statup("Obed", 70, 4)            
                                                $ Girl.Statup("Inbt", 70, 2)
                                                if Girl == EmmaX:   
                                                        ch_e "Mmm. . ."  
                                                elif Girl == LauraX:  
                                                        ch_l "Hmm. . ."
                                                else:
                                                        call AnyLine(Girl,"Umm. . .")
                                            
                                        "Just leave it there.":
                                            if Count == 5:
                                                    $ Girl.FaceChange("perplexed")
                                                    $ Girl.Statup("Lust", 90, 3) 
                                                    if Girl == RogueX: 
                                                            ch_r "This is a bit odd."  
                                                    else:      
                                                            call AnyLine(Girl,"Huh.")
                                            elif Count == 2:
                                                    $ Girl.FaceChange("perplexed")
                                                    $ Girl.Statup("Lust", 90, 1) 
                                                    if Girl == EmmaX:    
                                                            ch_e "Um, [EmmaX.Petname]."                  
                                                    elif Girl == LauraX:     
                                                            ch_l "This is getting uncomfortable."
                                                    else:
                                                            call AnyLine(Girl,"This is getting a bit uncomfortable.")
                                            $ Girl.Statup("Obed", 70, 2)            
                                            $ Girl.Statup("Inbt", 70, 1)
                                           
                            $ LauraX.ArmPose = 1
                            $ LauraX.Claws = 0 
                            if Girl == EmmaX and Taboo and "taboo" not in EmmaX.History:
                                    ch_e "Show some respect when in public, [EmmaX.Petname]."
                            elif Girl.FondleB and ApprovalCheck(Girl, 1100, TabM = 3): 
                                    $ Girl.FaceChange("sexy", 1)
                                    if Girl == RogueX: 
                                            ch_r "You know, maybe we could keep this party roll'in. . ."
                                    elif Girl == KittyX:                                        
                                            ch_k "I wouldn't mind if we kept. . . you know. . ."
                                    elif Girl == EmmaX:                                               
                                            if "three" not in EmmaX.History and not AloneCheck(EmmaX):
                                                        # if there are other girls in the room. . .
                                                        call Emma_ThreeCheck
                                            ch_e "Were you just sampling, or did you want to continue?"  
                                    elif Girl == LauraX:    
                                            ch_l "We could keep going. . ."
                                    menu:
                                        extend ""
                                        "Yeah!":
                                                $ Girl.Statup("Lust", 60, 5) 
                                                $ Girl.Statup("Love", 90, 2)          
                                                $ Girl.Statup("Obed", 60, 3)            
                                                $ Girl.Statup("Inbt", 60, 3) 
                                                call expression Girl.Tag + "_SexAct" pass ("breasts")
                                                call Trig_Reset(1)
                                                return
                                        "Nah, that was enough.":
                                                $ Girl.FaceChange("sad", 1)
                                                $ Girl.Statup("Lust", 60, 2) 
                                                $ Girl.Statup("Love", 90, -1)          
                                                $ Girl.Statup("Obed", 60, 4)            
                                                $ Girl.Statup("Inbt", 60, 3)                                 
                                                if Girl == RogueX: 
                                                        ch_r "Whatever."
                                                elif Girl == KittyX:  
                                                        ch_k "Whatevs." 
                                                elif Girl == EmmaX:  
                                                        ch_e "Oh. Pity."   
                                                elif Girl == LauraX:   
                                                        ch_l "Fine."
                            elif ApprovalCheck(Girl, 800, TabM = 3):  
                                    $ Girl.Brows = "confused"
                                    $ Girl.Eyes = "sexy"
                                    $ Girl.Mouth = "smile"
                                    if Girl == RogueX: 
                                            ch_r "Was that fun for you?"
                                    elif Girl == KittyX:   
                                            ch_k "You enjoy that?"
                                    elif Girl == EmmaX:   
                                            ch_e "Did you enjoy that?"  
                                    elif Girl == LauraX:                                          
                                            ch_l "You enjoyed that?"
                            elif ApprovalCheck(Girl, 800): 
                                    $ Girl.FaceChange("angry", 1)                                
                                    if Girl == RogueX: 
                                            ch_r "I can't believe you'd do that in public!"
                                    elif Girl == KittyX:   
                                            ch_k "How could you do that in public?"
                                    elif Girl == EmmaX:   
                                            ch_e "I can't believe you would do that in public."  
                                    elif Girl == LauraX:     
                                            ch_l "You do that in public?"
                            else:
                                    $ Girl.FaceChange("angry", 1)
                                    if Girl == RogueX: 
                                            ch_r "Just, don't do that sort of thing again!"
                                    elif Girl == KittyX:   
                                            ch_k "[Girl.like]keep your hands to yourself!"
                                    elif Girl == EmmaX:    
                                            ch_e "Just keep your hands to yourself." 
                                    elif Girl == LauraX:     
                                            ch_l "Keep your hands to yourself!"
                #End Grab her tit
                        
                "Rub her shoulders":
                            "You come up to [Girl.Name] from behind and gently rub her shoulders."
                            if Girl.SEXP >= 30:
                                    $ Girl.FaceChange("sexy") 
                                    $ Girl.Statup("Lust", 60, 3) 
                                    $ Girl.Statup("Love", 90, 2)
                                    "She leans back into your hands"
                                    if Girl == RogueX: 
                                            ch_r "Hmm, are you hinting at something there, [Girl.Petname]?"
                                    elif Girl == KittyX:   
                                            ch_k "Hmm, getting frisky, [Girl.Petname]?"
                                    elif Girl == EmmaX:     
                                            ch_e "Hmm, to what do I owe the pleasure, [Girl.Petname]?"
                                    elif Girl == LauraX:     
                                            ch_l "Hmm, are you thinking what I'm thinking, [Girl.Petname]?"
                            elif ApprovalCheck(Girl, 650, "L",Alt=[[RogueX],600]):
                                    $ Girl.FaceChange("sexy")
                                    $ Girl.Statup("Lust", 60, 1) 
                                    $ Girl.Statup("Love", 90, 2)
                                    if Girl == RogueX: 
                                            ch_r "Hmm, that feels nice, [Girl.Petname]."
                                    elif Girl == KittyX:   
                                            ch_k "Purr, that's nice, [Girl.Petname]."
                                    elif Girl == EmmaX:     
                                            ch_e "Well that's lovely, [Girl.Petname]."
                                    elif Girl == LauraX:     
                                            ch_l "Hmmm, that's nice, [Girl.Petname]."
                            elif ApprovalCheck(Girl, 500,Alt=[[RogueX],450]):
                                    $ Girl.FaceChange("surprised", 1)
                                    $ Girl.Statup("Love", 90, 1) 
                                    if Girl == EmmaX:   
                                            ch_e "Well hello, [Girl.Petname]."  
                                    elif Girl == LauraX:     
                                            ch_l "Oh, hey there, [Girl.Petname]."
                                    else:
                                            call AnyLine(Girl,"Oh, hey, "+Girl.Petname+". What's up?")
                            elif ApprovalCheck(Girl, 350):
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.Statup("Love", 90, -1)
                                    if Girl == RogueX: 
                                            if Taboo:  
                                                ch_r "Hey, um, ease up on the PDAs there, [Girl.Petname]."
                                            else:
                                                ch_r "Whoa, um, give me some space here."
                                    elif Girl == KittyX:   
                                            if Taboo:
                                                ch_k "Hey[Girl.like]maybe chill out, [Girl.Petname]?"
                                            else:
                                                ch_k "Whoa, back it up."
                                    elif Girl == EmmaX:   
                                            if Taboo:
                                                ch_e "Do I have to explain boundaries to you, [Girl.Petname]?"
                                            else:
                                                ch_e "I'd rather you didn't. . ."  
                                    elif Girl == LauraX:     
                                            if Taboo:
                                                ch_l "Maybe take a step back, [Girl.Petname]?"
                                            else:
                                                ch_l "Whoa, back it up."
                            else: 
                                        $ Girl.FaceChange("angry", 1)
                                        "She slaps your hands away."
                                        if Girl == RogueX: 
                                                ch_r "Not really the time or place, [Girl.Petname]?"   
                                        elif Girl == KittyX:   
                                                ch_k "No touchy!"  
                                        elif Girl == EmmaX:     
                                                ch_e "That will be enough of that."  
                                        elif Girl == LauraX:    
                                                ch_l "No hands or you lose them."      
                            $ Girl.Statup("Obed", 30, 3)            
                            $ Girl.Statup("Inbt", 30, 2) 
                #End "Rub shoulders"
                
                "Ask for her panties":
                            call AskPanties(Girl)
                 
                "Ask her to yoink some clothes" if Girl == KittyX:
                            call Kitty_Yoink
                    
                "Never mind [[exit]":
                            $ Girl.Chat[5] = 0 
    return
    
#End flirt core menu. / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Compliments / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
label Compliment(Girl=0,Line0=0,Line1=0,Line2=0,Options=[],CountList=[],Line=0,D20=0):
    #called from the flirt menu, picked three random options from the Options list
    #player picks one, then that outcome is evaluated to determine stat outcomes. 
    #call Compliment(Girl)
    
    $ Options = ["You really nailed that Danger Room exercise", #0
                "Great job in class the other day",             #1
                "You're looking extra beautiful today",         #2
                "Hey there, gorgeous",                          #3
                "I'm sorry, I got lost in your eyes",           #4
                "You're looking really toned lately",           #5
                "You have some really nice tits",               #6
                "Your ass looks really great",                  #7
                "Oh, what's that fragrance? It suits you",      #8
                "I'm so into you"]                              #9
    
    $ CountList = [0,1,2,3,4,5,6,7,8,9]    
    $ renpy.random.shuffle(CountList)
    
    $ Line0 = Options[CountList[0]] #let's say, this is 7
    $ Line1 = Options[CountList[1]]
    $ Line2 = Options[CountList[2]]
    menu:
            "[Line0]":
                $ Line = CountList[0] # Line would now = 7, corresponding to the 7th entry in Options
            "[Line1]":
                $ Line = CountList[1]
            "[Line2]":
                $ Line = CountList[2]
            "Never mind":                 
                $ Girl.Chat[5] = 0 #can only flirt once per cycle. 
                return
                    
    $ D20 = renpy.random.randint(5, 20)
    
    #responses based on compliment <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <>
    if Line == 0:       
            #"You really nailed that Danger Room exercise",  #0
            if ApprovalCheck(Girl, 1000):
                    $ D20 += 5                      
                    
            $ Girl.Statup("Love", 60, 3) 
            if Girl == LauraX:  
                    $ Girl.Statup("Love", 40, 3)
                    if D20 >= 10:
                            $ Girl.FaceChange("smile") 
                            $ Girl.Statup("Love", 80, 2) 
                            $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.Statup("Lust", 50, 2)
                            ch_l "I know right? I think I nailed that one."
                            ch_l "Those tin cans never stood a chance!"
                    else:
                            $ Girl.FaceChange("angry",1,Eyes="side") 
                            $ Girl.Statup("Inbt", 50, 1)
                            ch_l "Thanks. . ."
                            ch_l "I don't know, I think I missed one of the Sentinels."
                            ch_l "I have to be better than this."
                            $ Girl.FaceChange("normal",0) 
            else:
                    $ Girl.Statup("Obed", 60, 2)
                    if D20 >= 15:
                            $ Girl.FaceChange("smile") 
                            $ Girl.Statup("Love", 60, 1) 
                            $ Girl.Statup("Obed", 60, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            call AnyLine(Girl,"Yeah, I think I really nailed that one.")
                    elif D20 >= 10:
                            $ Girl.FaceChange("bemused",2) 
                            $ Girl.Statup("Love", 60, 1) 
                            $ Girl.Statup("Obed", 60, 1)
                            call AnyLine(Girl,"I think there's room for improvement though.")
                    else:
                            $ Girl.FaceChange("bemused",1,Eyes="side") 
                            $ Girl.Statup("Love", 80, 1) 
                            call AnyLine(Girl,"I appreciate the support, but we both know I could have done better.")
                            $ Girl.FaceChange("smile") 
            #"You really nailed that Danger Room exercise",  #0
    elif Line == 1:    
            #"Great job in class the other day",             #1
            if not ApprovalCheck(Girl, 700):
                    $ D20 -= 5    
                    
            if D20 >= 10:
                    $ Girl.Statup("Love", 70, 2) 
                    $ Girl.Statup("Obed", 60, 1)
                    if Girl == KittyX:
                            $ Girl.FaceChange("smile") 
                            $ Girl.Statup("Love", 80, 2) 
                            $ Girl.Statup("Inbt", 50, 1) 
                            ch_k "Thanks, [KittyX.Petname]!"
                            ch_k "The numbers really spoke to me."                         
                    elif Girl == EmmaX:
                            $ Girl.FaceChange("bemused") 
                            $ Girl.Statup("Love", 80, 2) 
                            ch_e "I'm glad you were paying attention, [EmmaX.Petname]."                      
                    else:           
                            $ Girl.FaceChange("confused") 
                            call AnyLine(Girl,"Thanks?")                         
            else:             
                    $ Girl.FaceChange("bemused") 
                    $ Girl.Statup("Love", 60, 1) 
                    $ Girl.Statup("Inbt",50, 1)   
                    if Girl == KittyX:
                            ch_k "Yeah, I definitely gave it my all there."
                            $ D20 += 5  
                    elif Girl == EmmaX:
                            ch_e "I'm surprised you were paying attention."
                    else:           
                            call AnyLine(Girl,"Yeah, it was ok. Got a little dull though.")
            #"Great job in class the other day",             #1
    elif Line == 2:   
            #"You're looking extra beautiful today",         #2
            if not ApprovalCheck(Girl, 900):
                    $ D20 -= 10
            if Girl == KittyX or Girl == RogueX: 
                    $ D20 += 5    
                    
            $ Girl.Statup("Inbt", 50, 2) 
            if Girl == LauraX: 
                    $ Girl.FaceChange("confused",1) 
                    $ Girl.Statup("Love", 80, 1, 1) 
                    $ Girl.Statup("Obed", 60, 2)             
                    ch_l ". . ."
                    ch_l "Ok?"
            elif D20 >= 10:
                    $ Girl.FaceChange("bemused",2) 
                    $ Girl.Statup("Love", 70, 2) 
                    $ Girl.Statup("Love", 90, 2) 
                    if Girl == RogueX:
                            ch_r "Well aren't you full'a sugar."
                    elif Girl == KittyX:
                            ch_k "Aw, that's sweet of you to say."
                    elif Girl == EmmaX:
                            ch_e "I do make an effort. . ."
                    $ Girl.FaceChange("bemused",1) 
            else:
                    $ Girl.FaceChange("bemused",1) 
                    $ Girl.Statup("Love", 50, -1)
                    $ Girl.Statup("Love", 70, -1) 
                    $ Girl.Statup("Obed", 50, 2)
                    if Girl == RogueX:
                            ch_r "Well aren't you full'a crap. . ."
                    elif Girl == KittyX:
                            ch_k "Um, ok. . ."
                    elif Girl == EmmaX:
                            ch_e "So -just- today? . ."
            #"You're looking extra beautiful today",         #2
    elif Line == 3:    
            #"Hey there, gorgeous",                          #3
            if not ApprovalCheck(Girl, 900):
                    $ D20 -= 10           
            if Girl == KittyX or Girl == EmmaX: 
                    $ D20 += 5 
                    
            if Girl == LauraX:  
                    $ Girl.FaceChange("confused",1) 
                    $ Girl.Statup("Love", 70, 2, 1) 
                    $ Girl.Statup("Inbt", 50, 1)            
                    ch_l "Um. . . hi?"
            elif D20 >= 10:
                    $ Girl.FaceChange("smile",2) 
                    $ Girl.Statup("Love", 60, 2) 
                    if D20 >= 15:
                            $ Girl.Statup("Love", 200, 1) 
                            $ Girl.Statup("Obed", 60, 1)
                            $ Girl.Statup("Inbt", 80, 1)
                    if Girl == RogueX:
                            ch_r "\"Hey there\" yourself."
                    elif Girl == KittyX:
                            ch_k "Oh, hehe, that's sweet of you. . ."
                    elif Girl == EmmaX:
                            ch_e "Yes. . . hello to you as well."
                    $ Girl.FaceChange("smile",1) 
            else:
                    $ Girl.FaceChange("bemused",1) 
                    $ Girl.Statup("Love", 60, -1) 
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl == RogueX:
                            ch_r "\"Gorgeous\" yourself."
                    elif Girl == KittyX:
                            ch_k "Riight. . ."
                    elif Girl == EmmaX:
                            ch_e "Children these days. . ."
            #"Hey there, gorgeous",                          #3
    elif Line == 4:     
            #"I'm sorry, I got lost in your eyes",           #4       
            if ApprovalCheck(Girl, 900, "L") and Girl != EmmaX:
                    pass
            elif not ApprovalCheck(Girl, 1000):
                    $ D20 -= 10
            if Girl == KittyX or Girl == RogueX: 
                    $ D20 += 10 
                    
            if Girl == LauraX:    
                            $ Girl.FaceChange("confused")           
                            ch_l "What?"     
            elif D20 >= 10:
                    $ Girl.FaceChange("bemused",2) 
                    $ Girl.Statup("Love", 90, 2) 
                    $ Girl.Statup("Obed", 50, 2)
                    $ Girl.Statup("Inbt", 30, 1)
                    if Girl == RogueX:
                            ch_r "What a charmer."
                    elif Girl == KittyX:
                            $ Girl.FaceChange("bemused",2,Mouth="smile") 
                            $ Girl.Statup("Love", 200, 1) 
                            $ Girl.Statup("Lust", 50, 2)
                            ch_k "Heh. . . you don't say. . ."
                    elif Girl == EmmaX:
                            $ Girl.FaceChange("bemused",1) 
                            ch_e "A valiant effort. . ."
                    $ Girl.FaceChange("bemused",1) 
            else:
                    $ Girl.FaceChange("angry",1,Eyes="up") 
                    $ Girl.Statup("Love", 60, 1) 
                    $ Girl.Statup("Obed", 50, 1)
                    if Girl == RogueX:
                            ch_r "Maybe stay lost."
                    elif Girl == KittyX:
                            ch_k "Uh-huh. . ."
                    elif Girl == EmmaX:
                            ch_e "Perhaps you're laying it on a bit thick there. . ."
                    $ Girl.FaceChange("normal") 
            #"I'm sorry, I got lost in your eyes",           #4   
    elif Line == 5:     
            #"You're looking really toned lately",           #5
            if not ApprovalCheck(Girl, 1200):
                if not ApprovalCheck(Girl, 600):
                    $ D20 -= 12
                else:
                    $ D20 -= 8
            if Girl == LauraX: 
                    $ D20 += 8 
                    
            if Girl == LauraX:  
                            $ Girl.FaceChange("bemused") 
                            $ Girl.Statup("Love", 80, 2) 
                            $ Girl.Statup("Love", 90, 1) 
                            $ Girl.Statup("Inbt", 50, 2)              
                            ch_l "Thanks? I've been trying something new."
            elif D20 >= 10:
                    $ Girl.FaceChange("bemused",1) 
                    $ Girl.Statup("Love", 60, 2) 
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 60, 2)
                    if Girl == RogueX:
                            ch_r "Well. . . that's sweet of ya. . ."
                    elif Girl == KittyX:
                            ch_k "Oh. . . ok, um, thank you?"
                    elif Girl == EmmaX:
                            ch_e "Hmm, maybe a bit too lean? Perhaps I should take a break."
            else:
                    $ Girl.FaceChange("angry",2) 
                    $ Girl.Statup("Love", 50, -1) 
                    $ Girl.Statup("Love", 70, -1) 
                    $ Girl.Statup("Obed", 50, 2)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl == RogueX:
                            ch_r "Maybe don't concern yourself with my \"tone.\""
                    elif Girl == KittyX:
                            ch_k "Are you being sarcastic?"
                    elif Girl == EmmaX:
                            ch_e "I don't think we should be discussing my body."
                    $ Girl.FaceChange("angry",1,Mouth="normal") 
            #"You're looking really toned lately",           #5
    elif Line == 6:     
            #"You have some really nice tits",               #6
            if ApprovalCheck(Girl, 700, "I"):
                    pass
            elif not ApprovalCheck(Girl, 1400): #at least -5, -10 if under 900
                if not ApprovalCheck(Girl, 900):
                    $ D20 -= 15
                else:
                    $ D20 -= 10
            if Girl == EmmaX or Girl == KittyX: 
                    $ D20 += 5 
            else:     
                if D20 >= 10:    
                    $ Girl.FaceChange("bemused",2) #for Rogue and Laura's
                else:
                    $ Girl.FaceChange("angry",2) #for Rogue and Laura's
            if D20 >= 10:
                    $ Girl.Statup("Love", 90, 2) 
                    $ Girl.Statup("Love", 200, 1) 
                    $ Girl.Statup("Obed", 80, 4)
                    $ Girl.Statup("Inbt", 80, 3)
                    $ Girl.Statup("Inbt", 200, 1)
                    $ Girl.Statup("Lust", 50, 3)
                    if Girl == KittyX:
                            $ Girl.FaceChange("bemused",2,Mouth="smile") 
                            ch_k "Really? Thanks, I appreciate that. . ."                           
                    elif Girl == EmmaX:
                            $ Girl.FaceChange("bemused",1,Mouth="smile") 
                            ch_e "Marvelous, aren't they?"
            else:        
                    $ Girl.Statup("Love", 70, -1) 
                    $ Girl.Statup("Obed", 60, 3)
                    $ Girl.Statup("Obed", 80, 2)
                    $ Girl.Statup("Inbt", 80, 3)
                    if Girl == KittyX:
                        if D20 <= 5:
                            $ Girl.FaceChange("angry",2) 
                            $ Girl.Statup("Love", 60, -3) 
                            $ Girl.Statup("Love", 90, -1) 
                            ch_k "Asshole!"
                        else:    
                            $ Girl.FaceChange("sadside",2,Mouth="smile")                             
                            ch_k "I get where you're going with that, but. . ."
                        $ Girl.FaceChange(5,1) 
                    elif Girl == EmmaX:
                            $ Girl.FaceChange("bemused",1) 
                            ch_e "Perhaps keep your eyes up here?"
                            if D20 >= 5:
                                    $ Girl.FaceChange("angry",1) 
                                    ch_e ". . ."
                                    $ Girl.FaceChange("bemused",1) 
                                    $ Girl.Statup("Love", 90, 2) 
                                    $ Girl.Statup("Lust", 70, 5)
                                    ch_e "Higher!"            
            if Girl == RogueX:
                    ch_r "Well bless your heart. I appreciate the effort."
            elif Girl == LauraX:                
                    ch_l "I guess so?"          
            if Girl != KittyX:
                    $ Girl.FaceChange("bemused",1)
            #"You have some really nice tits",               #6
    elif Line == 7:   
            #"Your ass looks really great",                  #7            
            if ApprovalCheck(Girl, 700, "I"):
                    pass
            elif not ApprovalCheck(Girl, 1300):
                if not ApprovalCheck(Girl, 900):
                    $ D20 -= 15
                else:
                    $ D20 -= 10
            if Girl == EmmaX or Girl == RogueX: 
                    $ D20 += 5 
                    
            if D20 >= 10:
                    $ Girl.FaceChange("bemused",2) 
                    $ Girl.Statup("Love", 80, 2) 
                    $ Girl.Statup("Love", 90, 1) 
                    $ Girl.Statup("Obed", 60, 1)
                    $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.Statup("Lust", 30, 2)
                    if Girl == RogueX:
                            ch_r "I don't know, my jeans have been getting a bit tight. . ."
                    elif Girl == KittyX:
                            ch_k "I guess so? I mean. . ."
                    elif Girl == EmmaX:
                            ch_e "My, you do have good taste. . ."
                            $ Girl.FaceChange("confused",1)  
                            ch_e "If perhaps poor manners. . ."
                    elif Girl == LauraX:      
                            $ Girl.FaceChange("smile",1)           
                            ch_l "Good to know."
                    $ Girl.FaceChange("bemused",1) 
            else:        
                    $ Girl.FaceChange("angry",1) 
                    $ Girl.Statup("Love", 60, -1) 
                    $ Girl.Statup("Love", 70, -2) 
                    $ Girl.Statup("Obed", 60, 3)
                    $ Girl.Statup("Inbt", 50, 2)
                    if Girl == EmmaX:
                            ch_e "You shouldn't comment on a lady's figure."
                    elif Girl == LauraX:    
                            $ Girl.FaceChange("confused",1)            
                            ch_l "Right. . ."
                    else:
                            call AnyLine(Girl,"Rude.")
                    $ Girl.FaceChange("normal",1) 
            #"Your ass looks really great",                  #7  
    elif Line == 8:    
            #"Oh, what's that fragrance? It suits you",      #8            
            if ApprovalCheck(Girl, 800, "L"):
                    pass
            elif not ApprovalCheck(Girl, 1300):
                    $ D20 -= 10
            if Girl == EmmaX or Girl == LauraX: 
                    $ D20 += 15 
                    
            if D20 >= 10:
                    $ Girl.FaceChange("bemused",1,Mouth="smile") 
                    $ Girl.Statup("Love", 90, 2) 
                    $ Girl.Statup("Love", 200, 1) 
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 80, 3)
                    $ Girl.Statup("Lust", 50, 2)
                    if Girl == RogueX:
                            ch_r "Oh? Thank you, I guess?"
                    elif Girl == KittyX:
                            ch_k "Huh? . . I don't know, my usual shampoo, I guess. . ."
                    elif Girl == EmmaX:
                            ch_e "Thank you, I picked it up last time I was in Grasse."
                    elif Girl == LauraX:                
                            ch_l "Probably blood, mostly. Ninjas."                    
            else:        
                    $ Girl.FaceChange("angry",2,Mouth="grimace") 
                    $ Girl.Statup("Love", 60, -1) 
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl == RogueX:
                            ch_r "Probably best not to talk about a woman's scent."
                    elif Girl == KittyX:
                            ch_k "Gross. . ."
                    elif Girl == EmmaX:
                            ch_e "You might want to back up a bit. . ."
                    elif Girl == LauraX:           
                            $ Girl.FaceChange("confused",1) 
                            $ Girl.Statup("Lust", 50, 2)     
                            ch_l "I don't know, I'm kinda sweaty, I guess. . ."
                    $ Girl.FaceChange("bemused",1) 
            #"Oh, what's that fragrance? It suits you",      #8 
    elif Line == 9:   
            #"I'm so into you"                               #9            
            if ApprovalCheck(Girl, 900, "L"):
                    pass
            elif not ApprovalCheck(Girl, 1100):
                    $ D20 -= 10
            if Girl == LauraX or Girl == RogueX: 
                    $ D20 += 5 
                    
            if D20 >= 10:
                    $ Girl.FaceChange("sly",1) 
                    $ Girl.Statup("Love", 80, 1) 
                    $ Girl.Statup("Love", 90, 1) 
                    $ Girl.Statup("Obed", 70, 2)
                    $ Girl.Statup("Inbt", 80, 3)
                    $ Girl.Statup("Lust", 30, 5)
                    $ Girl.Statup("Lust", 60, 5)
                    if Girl == RogueX:
                            ch_r "I'm glad for that. . ."
                    elif Girl == KittyX:
                            ch_k "You aren't yet. . ."
                            ch_k "but you could be. . ."
                    elif Girl == EmmaX:
                            ch_e "Hmm, yes. . . I can see that."
                    elif Girl == LauraX:                
                            ch_l "Not yet, you aren't."
            else:                 
                    $ Girl.Statup("Love", 60, -2) 
                    $ Girl.Statup("Obed", 60, 1)
                    $ Girl.Statup("Inbt", 50, 1)
                    if Girl == EmmaX:
                            $ Girl.FaceChange("angry",1,Mouth="smirk") 
                            ch_e "That's not really appropriate."
                    else:              
                            $ Girl.FaceChange("bemused",1)   
                            call AnyLine(Girl,"Ok. . .")
            #"I'm so into you"                               #9   
    
    if D20 < 10:
        menu:
            "Sorry":
                    if Girl != LauraX:      
                            $ Girl.Statup("Love", 60, 1) 
                            $ Girl.Statup("Love", 90, 1) 
                            $ Girl.Statup("Obed", 40, -2)
                            $ Girl.Statup("Obed", 70, -1)
                            $ Girl.FaceChange("sadside") 
                    if Girl == RogueX:
                            ch_r "Well, thanks for that. . ."
                    elif Girl == KittyX:
                            ch_k "I guess I won't hold it against you. . ."
                    elif Girl == EmmaX:
                            ch_e "Fine, I can accept that."
                    elif Girl == LauraX:    
                            $ Girl.FaceChange("normal")             
                            ch_l "Whatever."
                    $ Girl.FaceChange("normal") 
            ". . .":
                pass
    return
# End Compliments / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  

# Start Love You Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
label Love_You(Girl=0):
        # Called whenever you say "I love you" in the flirt menu
        # Rejects attempts before the girl confesses
                 
        ch_p "[Girl.Name], I love you."
        if "lover" not in Girl.Petnames:
            #if you didn't clear the love scene with her. . .
            if "love" in Girl.History:
                    #you've tried this before. . .   
                    if ApprovalCheck(Girl, 800,"L"):
                            #she kind of likes you
                            $ Girl.Statup("Love", 90, 2)
                            $ Girl.Statup("Obed", 80, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.Statup("Lust", 30, 5)
                            $ Girl.FaceChange("bemused",2,Brows="confused")   
                            
                            if Girl == RogueX:
                                    ch_r "Don't push it. . ."
                            elif Girl == KittyX:
                                    ch_k "I can't even . ."
                            elif Girl == EmmaX:
                                    ch_e "Just don't. . ."    
                            elif Girl == LauraX:
                                    ch_l "I don't want to. . ."
                            
                    elif ApprovalCheck(Girl, 600,"L"):
                            #she is friendly enough. . .
                            $ Girl.Statup("Love", 95, 2)
                            $ Girl.Statup("Obed", 80, 3)
                            $ Girl.Statup("Inbt", 60, 1)
                            $ Girl.FaceChange("bemused",2)   
                            
                            if Girl == RogueX:
                                    ch_r "I don't know, love? . ."
                            elif Girl == KittyX:
                                    ch_k "I don't know if I think of you like that . ." 
                            elif Girl == EmmaX:
                                    ch_e "This is incredibly inappropriate. . ."
                            elif Girl == LauraX:
                                    ch_l "I don't. . ."
                    else:
                            #she doesn't like you. . .
                            $ Girl.Statup("Love", 95, -5)
                            $ Girl.Statup("Obed", 90, 5)
                            $ Girl.Statup("Inbt", 60, 2)
                            $ Girl.FaceChange("angry",1)   
                            
                            if Girl == RogueX:
                                    ch_r "Bull."
                            elif Girl == KittyX:
                                    ch_k "Stop trolling me!"
                            elif Girl == EmmaX:
                                    ch_e "Oh forget this nonsense already. . ."  
                            elif Girl == LauraX:
                                    ch_l "Fuck off with this. . ."   
                            
            #if this is the first time you've tried this but you haven't agreed to love her yet. . .
            $ Girl.AddWord(1,"love","love",0,"love") #adds the "love" trait to recent and daily actions, and history
            
            if Girl == RogueX:
                    if not RogueX.Event[6]:
                            # if you've never had the "love" talk. . .
                            $ Line = "never"                    
                    elif RogueX.Event[6] >= 20: 
                            # if she's asked you, but you refused before. . .
                            ch_r "You're just giving me whiplash here, [RogueX.Petname]."
#                            call Rogue_Love_Redux #she doesn't have one of these, skip it.
            elif Girl == KittyX:
                    if not KittyX.Event[6]:
                            $ Line = "never"                    
                    elif KittyX.Event[6] >= 20: 
                            call Kitty_Love_Redux
            elif Girl == EmmaX:
                    if not EmmaX.Event[6]:
                            # if you've never had the "love" talk. . .
                            $ Line = "never"                    
                    elif EmmaX.Event[6] >= 20: 
                            call Emma_Love_Redux
            elif Girl == LauraX:
                    if not LauraX.Event[6]:
                            $ Line = "never"                    
                    elif LauraX.Event[6] >= 20: 
                            call Laura_Love_Redux
                    
            if Line == "never":
                    if ApprovalCheck(Girl, 800,"L"):
                            $ Girl.Statup("Love", 90, 10)
                            $ Girl.Statup("Lust", 50, 5)
                            $ Girl.FaceChange("smile",2,Eyes="surprised")   
                    elif ApprovalCheck(Girl, 600,"L"):
                            $ Girl.Statup("Love", 90, 5)
                            $ Girl.FaceChange("confused",2,Eyes="surprised")   
                    else:
                            $ Girl.FaceChange("angry",1,Brows="confused")   
                            $ Girl.Statup("Love", 90, -5)
                            $ Girl.Statup("Obed", 90, 5)
                    $ Girl.Statup("Obed", 70, 5)
                    $ Girl.Statup("Inbt", 60, 5)
                    if Girl == RogueX:
                            ch_r "Whaaa? . ."
                            ch_r "Is this some kind of joke?"   
                    elif Girl == KittyX:
                            ch_k "What was that? . ."
                            ch_k ". . . Um, I gotta go!"   
                    elif Girl == EmmaX:
                            ch_e "What? I. . . I don't know what to say about that."
                            ch_e "I. . . I'll get back to you."     
                    elif Girl == LauraX:
                            ch_l "Huh? You-"
                            ch_l "Um. . ."   
                            ch_l "Bye."
                    
                    "[Girl.Name] leaves the room."
                    call Remove_Girl(Girl)
                    $ renpy.pop_call() #This removes the callback to the previous chat session
                    $ renpy.pop_call() #this removes the callback to the previous chat selector
            return
        # End if you never cleared the love scene stuff        
                
        if "love" in Girl.DailyActions:
                #if you've said it today
                $ Girl.Statup("Love", 95, 5)
                $ Girl.Statup("Obed", 70, 2)
                $ Girl.Statup("Inbt", 60, 1)
                $ Girl.Statup("Lust", 50, 5)                
                $ Girl.FaceChange("smile",1)   
                if Girl == RogueX:
                        ch_r "I think you told me that earlier. . ."
                        ch_r "but don't stop on my account, [RogueX.Petname]."   
                elif Girl == KittyX:
                        ch_k "Didn't you already say that? . ."
                        ch_k ". . . say it again."   
                elif Girl == EmmaX:
                        ch_e "So you've told me. . ."
                        ch_e "but I don't tire of it, [EmmaX.Petname]."   
                elif Girl == LauraX:
                        ch_l "Yeah, I know. . ."
                        ch_l "but you can keep saying it, [LauraX.Petname]."   
                
        elif ApprovalCheck(Girl, 800,"L"):
                #if she still loves you
                $ Girl.Statup("Love", 90, 5)
                $ Girl.Statup("Love", 200, 5)
                $ Girl.Statup("Obed", 70, 1)
                $ Girl.Statup("Inbt", 60, 1)
                $ Girl.Statup("Lust", 30, 5)     
                $ Girl.FaceChange("smile",1)              
                if Girl == RogueX:
                        ch_r "I love you too, [RogueX.Petname]."
                elif Girl == KittyX:
                        ch_k "Awwww! I love you too, [KittyX.Petname]."
                elif Girl == EmmaX:
                        ch_e "And I love you too, [EmmaX.Petname]."
                elif Girl == LauraX:
                        ch_l "Yeah, love you too."
        else:
                #if she doesn't love you anymore
                $ Girl.Statup("Love", 90, 5)
                $ Girl.Statup("Love", 50, -10, 1)
                $ Girl.Statup("Obed", 70, 3)        
                $ Girl.FaceChange("sadside",1)        
                if Girl == RogueX:
                        ch_r "It's too late for that."
                elif Girl == KittyX:
                        ch_k "As if. Jerk."
                elif Girl == EmmaX:
                        ch_e "I dearly wish that I could believe that."
                elif Girl == LauraX:
                        ch_l "You blew it."
        
        $ Girl.AddWord(1,"love","love",0,"love") #adds the "love" trait to recent and daily actions, and history
        return
    
 
# End Love You Girl / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   

# Start Touch Cheek / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label TouchCheek(Girl=0): 
        if Girl not in TotalGirls:
                return
        call Shift_Focus(Girl) 
        $ Girl.FaceChange("surprised", 1) 
        if "no cheek" in Girl.DailyActions:
                "You reach out to brush [Girl.Name]'s face with your hand, but she slaps it away."
                $ Girl.FaceChange("angry")
                if Girl == RogueX:
                        ch_r "Back off, asshole."
                elif Girl == EmmaX: 
                        ch_e "What are you doing, [Girl.Petname]?"         
                else:     
                        call AnyLine(Girl,"Hands off, dickbag.")
                $ Girl.Statup("Love", 50, -2)
                return
        else:
                "You reach out and brush [Girl.Name]'s face with your hand, a shiver runs through her."
        $ Girl.Statup("Obed", 50, 1)
        
        if Girl == RogueX or "addict " + Girl.Tag in Player.Traits:        
                $ Girl.Addict -= 2            
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0 
                $ Girl.Addictionrate = 3 if Girl.Addictionrate < 3 else Girl.Addictionrate 
                $ Girl.Statup("Lust", 70, 5)
        else:
                $ Girl.Statup("Lust", 40, 5)
            
        if ApprovalCheck(Girl, 1000):
                $ Girl.FaceChange("sexy", 1)            
                if Girl == RogueX:
                        ch_r "A promise of things to come, [Girl.Petname]?"
                elif Girl == EmmaX:          
                        ch_e "That's sweet, what was it for, [Girl.Petname]?"
                else:                
                        call AnyLine(Girl,"Hmmm, what were you thinking, " + Girl.Petname + "?")
                $ Girl.Statup("Love", 80, 1)
        elif ApprovalCheck(Girl, 800,Alt=[[RogueX],500]) or ApprovalCheck(Girl, 700,"L"):
                $ Girl.FaceChange("smile", 1)            
                if Girl == RogueX:
                        ch_r "That was. . . nice."  
                elif Girl == EmmaX:         
                        ch_e "Mmmmm. . ."         
                else:                
                        call AnyLine(Girl,"Sweet. . .")      
        elif "cheek" in Girl.DailyActions:        
                $ Girl.FaceChange("angry", 1)            
                if Girl == RogueX:
                        ch_r "Hey, I told you to cut that out already."
                elif Girl == EmmaX:   
                        ch_e "I won't warn you again, [Girl.Petname]."       
                else:                
                        call AnyLine(Girl,"Hey, I warned you, "+Girl.Petname+".")
                $ Girl.Statup("Love", 50, -2)
                $ Girl.DailyActions.append("no cheek")
        elif ApprovalCheck(Girl, 250): #400
                $ Girl.Mouth = "smile"
                $ Girl.Brows = "normal"            
                if Girl == RogueX:
                        ch_r "A. . . little warning maybe next time?"
                elif Girl == EmmaX:    
                        ch_e "Hmm, perhaps we need to discuss \"boundaries.\""      
                else:
                        call AnyLine(Girl,"Um, that was weird.")
        else:
                $ Girl.FaceChange("angry", 1)            
                if Girl == RogueX:
                        ch_r "Don't. . . don't do that."   
                elif Girl == EmmaX:   
                        ch_e "That's inappropriate behavior, [Girl.Petname]."         
                else:
                        call AnyLine(Girl,"Back off, weirdo.")   
                $ Girl.Statup("Love", 50, -3)
                $ Girl.Statup("Obed", 50, 1)
                $ Girl.Statup("Inbt", 30, 1)
        
        if "no cheek" in Girl.DailyActions: 
            menu:
                "Sorry, sorry, won't happen again.":
                        if ApprovalCheck(Girl, 300):
                                $ Girl.FaceChange("sexy", 1) 
                                if Girl == RogueX:
                                        ch_r "Well, ok, just cut it out though."
                                elif Girl == EmmaX:      
                                        ch_e "See that it doesn't."    
                                else:
                                        call AnyLine(Girl,"I don't know that I did. . .")
                                $ Girl.Statup("Love", 80, 2)
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Eyes = "side"
                                if Girl == RogueX:
                                        ch_r "A likely story. . ."              
                                elif Girl == EmmaX:     
                                        ch_e "I'm sure."   
                                else:
                                        call AnyLine(Girl,"Uh-huh.")
                                $ Girl.Statup("Obed", 20, 1)   
                # end "Sorry, sorry, won't happen again.":
                
                "You know you wanted it.":
                        if ApprovalCheck(Girl, 400, "OI",Alt=[[RogueX],300]) or ApprovalCheck(Girl, 800,Alt=[[RogueX,LauraX],1500]): 
                                $ Girl.FaceChange("normal", 1)
                                $ Girl.Eyes = "squint"
                                if Girl == RogueX:
                                        ch_r "Well. . . I guess, maybe. . ."
                                else:
                                        call AnyLine(Girl,"Don't make promises you can't keep.")
                                $ Girl.Statup("Love", 60, -1) 
                                $ Girl.Statup("Obed", 30, 2)                        
                                $ Girl.Statup("Inbt", 40, 2)
                        else:
                                $ Girl.FaceChange("angry", 2)
                                $ Girl.Eyes = "squint"
                                if Girl == RogueX:
                                        ch_r "Like hell I did." 
                                elif Girl == EmmaX:  
                                        ch_e "You {i}must{/i} be daydreaming."          
                                else:
                                        call AnyLine(Girl,"You wish.")  
                                $ Girl.Blush = 1
                                $ Girl.Statup("Love", 60, -3) 
                                $ Girl.Statup("Obed", 30, 3)                        
                                $ Girl.Statup("Inbt", 40, 2) 
                #end "You know you wanted it."
        else:
            menu:
                "Sorry, you looked so cute there.":
                        if ApprovalCheck(Girl, 850, "LI"):
                                $ Girl.FaceChange("sexy", 1)
                                if Girl == RogueX:
                                        ch_r "I'll make sure to collect on that later."
                                elif Girl == KittyX:
                                        ch_k "Yeah,[KittyX.like]stop being weird."
                                elif Girl == EmmaX:         
                                        ch_e "Don't make promises you can't keep." 
                                elif Girl == LauraX:
                                        ch_l "There better be more where that came from."
                                $ Girl.Statup("Love", 80, 2)
                        elif ApprovalCheck(Girl, 500, "LI"):
                                $ Girl.FaceChange("smile", 1)
                                if Girl == RogueX:
                                        ch_r "Aw, you're sweet."
                                elif Girl == KittyX:
                                        ch_k "I'm not the only one looking cute, [LauraX.Petname]."
                                elif Girl == EmmaX:        
                                        ch_e "You don't look so bad yourself, [EmmaX.Petname]."  
                                elif Girl == LauraX:
                                        ch_l "Uh, yeah. . . you too?"
                                $ Girl.Statup("Love", 80, 2)
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Eyes = "side"
                                if Girl == RogueX:
                                        ch_r "Don't you \"cute\" me, just cut it out. . ."   
                                elif Girl == KittyX:
                                        ch_k "Too cute for you."                    
                                elif Girl == EmmaX:         
                                        ch_e "Obviously."               
                                elif Girl == LauraX:
                                        ch_l "I don't do \"cute.\""   
                                $ Girl.Statup("Obed", 20, 1)   
                # end "Sorry, you looked so cute there."   
                
                "You had a fly on you.":
                        if ApprovalCheck(Girl, 850, "LI"):
                                $ Girl.FaceChange("sexy", 1)
                                if Girl == RogueX:
                                        ch_r "Oh? Was that all. . ."
                                elif Girl == EmmaX:    
                                        ch_e "Oh? I'm {i}sure{/i} that was it. . ."      
                                else:                                
                                        call AnyLine(Girl,"Oh? Sorry. . .")
                                $ Girl.Statup("Love", 60, 1)                        
                                $ Girl.Statup("Inbt", 40, 1)
                        elif ApprovalCheck(Girl, 600):
                                $ Girl.FaceChange("normal")
                                call AnyLine(Girl,"A fly, right. . .")
                        else:
                                $ Girl.FaceChange("angry", 1)
                                if Girl == RogueX:
                                        ch_r "A likely story, look, just don't touch me." 
                                elif Girl == EmmaX:      
                                        ch_e "That's no excuse."     
                                else:
                                        call AnyLine(Girl,"Riiiight, just don't touch me.") 
                                $ Girl.Statup("Obed", 50, 2)    
                #end "fly on you"
                        
                "Are you sure you didn't enjoy that?":
                        if ApprovalCheck(Girl, 650, "LI") or ApprovalCheck(Girl, 1000):
                                    $ Girl.FaceChange("sexy", 1)
                                    $ Girl.Eyes = "side"                    
                                    if Girl == RogueX:
                                            ch_r "I suppose I did, at that."
                                    elif Girl == EmmaX:    
                                            ch_e "I'd need to try again to be sure. . ."      
                                    else:                        
                                            call AnyLine(Girl,"Maybe if there were more to it. . .")
                                    $ Girl.Statup("Obed", 50, 2)  
                                    $ Girl.Statup("Obed", 30, 1)                        
                                    $ Girl.Statup("Inbt", 40, 1)
                        elif ApprovalCheck(Girl, 500, "OI"):
                                    $ Girl.FaceChange("normal", 1)
                                    if Girl == EmmaX:  
                                            ch_e "Don't push it. . . too far."        
                                    else:
                                            call AnyLine(Girl,"Well. . . I guess, maybe. . . no, quit it.")
                                    $ Girl.Statup("Love", 60, -1)
                                    $ Girl.Statup("Obed", 50, 2)  
                                    $ Girl.Statup("Obed", 30, 2)                        
                                    $ Girl.Statup("Inbt", 40, 2)
                        else:
                                    $ Girl.FaceChange("angry", 1)
                                    $ Girl.Eyes = "side"
                                    if Girl == KittyX:
                                            ch_k "Not interested." 
                                    elif Girl == EmmaX:    
                                            ch_e "Positive."   
                                    else:
                                            call AnyLine(Girl,"Grrrr. . .")
                                    $ Girl.Statup("Love", 60, -3)
                                    $ Girl.Statup("Obed", 50, 2)  
                                    $ Girl.Statup("Obed", 30, 3)                        
                                    $ Girl.Statup("Inbt", 40, 2)
                #end "Are you sure you didn't enjoy that?"
                
        $ Girl.RecentActions.append("cheek")
        $ Girl.DailyActions.append("cheek")
        return
# End touch cheek/ / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Hold Hands / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
label Hold_Hands(Girl=0,Gloves=0):
        # Called whenever you say "Hold Hands" in the flirt menu
        if Girl.Arms == "gloves":
            menu:
                "Gloves or no Gloves?"
                "Gloves":
                    pass
                "No Gloves":
                    ch_p "Hey, could you lose the gloves for a second?"
                    if Girl == RogueX:
                            ch_r "Ok, [Girl.Petname]. . ."
                    elif Girl == EmmaX:
                            ch_e "Oh, fine, [Girl.Petname]. . ."
                    $ Line = "gloves"
                    $ Girl.Arms = 0
        "You reach down and grab [Girl.Name]'s hand in yours."        
        if ApprovalCheck(Girl, 800,"L"):
                $ Girl.FaceChange("smile",1,Eyes="closed")  
                "She squeezes your hand back and leans her shoulder against yours."  
                $ Count = 10
        elif ApprovalCheck(Girl, 1200):
                $ Girl.FaceChange("bemused",1,Brows="confused")   
                "She gives your hand a light squeeze in return."    
                $ Count = 4
        elif ApprovalCheck(Girl, 800):
                $ Girl.FaceChange("bemused",2,Brows="confused")  
                "She stiffens a bit, but leaves her hand in yours." 
                $ Girl.FaceChange("bemused",1,Eyes="down")   
                $ Count = 2   
        else:
                #not cool with it
                $ Girl.FaceChange("angry",1)   
                $ Girl.Statup("Love", 40, -1)
                $ Girl.Statup("Love", 60, -1)
                $ Girl.Statup("Obed", 60, 2)
                $ Girl.Statup("Obed", 80, 1)
                $ Girl.Statup("Inbt", 50, 1)   
                if Girl == RogueX and not RogueX.Arms:
                    $ Girl.Statup("Obed", 60, 2)
                    $ Girl.Statup("Lust", 30, 5)                    
                    $ RogueX.Addict -= 2            
                    $ RogueX.Addictionrate += 1 if RogueX.Addictionrate < 5 else 0 
                    $ RogueX.Arms = "gloves"
                    "She slaps your hand away, putting her gloves back on."
                else:
                    "She slaps your hand away."
                call AnyLine(Girl,"Don't get too familiar.")
                return
                
        if Girl.Arms != "gloves":
                $ Girl.Addictionrate += 1 if Girl.Addictionrate < 5 else 0 
                
        while Count:
            $ Round -= 5
            if ApprovalCheck(Girl, 800,"L"):
                if Count >= 8:
                    $ Girl.Statup("Love", 90, 2)
                    $ Girl.Statup("Obed", 70, 2)
                    $ Girl.Statup("Lust", 30, 2)
            elif ApprovalCheck(Girl, 1200):
                if Count >= 3:
                    $ Girl.Statup("Love", 80, 3)
                    $ Girl.Statup("Obed", 70, 2)
                    $ Girl.Statup("Lust", 30, 1)
            elif ApprovalCheck(Girl, 800):
                    $ Girl.Statup("Love", 70, 2)
                    $ Girl.Statup("Obed", 50, 2)
            if Girl.Arms != "gloves" and Girl.Addictionrate >= 3 and Girl.Addict >= 5:
                    $ Girl.Statup("Lust", 50, 3)
                    $ Girl.Addict -= 2    
                    $ Count += 1 if Count <= 1 else 0 #she keeps it up
                    if Girl.Lust >= 30:                        
                        $ Girl.FaceChange("sly",2)   
                            
            menu:
                "Keep holding hands.":
                        pass                        
                "Stop holding hands.":
                        $ Count = 0
                        $ Girl.FaceChange("bemused",1)   
                        return
            $ Count -= 1            
            $ Count = 0 if Round <= 10 else Count
            
        #loop breaks. . .
        
        $ Girl.AddWord(1,"holdhands","holdhands") #adds the "holdhands" trait to recent and daily actions
        
        if not ApprovalCheck(Girl, 800,"L") and not ApprovalCheck(Girl, 1200):
                # she's a little creeped out
                $ Girl.FaceChange("sadside",1,Brows="confused")   
                $ Girl.Statup("Love", 60, -2)
                $ Girl.Statup("Obed", 60, -2)
                $ Girl.Statup("Inbt", 50, 3)
                $ Girl.Statup("Lust", 60, -5)   
        else:
                $ Girl.FaceChange("smile",1)  
        if Line == "gloves":
                $ Girl.Arms = "gloves"
        call AnyLine(Girl,"Ok, that's enough of that. . .")
        return
  
# End Hold Hands / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /       

# Start Head Pat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Girl_Headpat(Girl=0):  
    if Girl not in TotalGirls:
            $ Girl = Ch_Focus
    call Shift_Focus(Girl)
    $ Girl.FaceChange("surprised", 1) 
    if "no headpat" in Girl.DailyActions:
            "You reach out to pat [Girl.Name] on the head, but she slaps it away."
            $ Girl.FaceChange("angry")     
            if Girl == RogueX:
                    ch_r "Hands ta yourself, [Girl.Petname]."
            elif Girl == KittyX:
                    ch_k "I told you, weird."
                    ch_k "Weirdo."
            elif Girl == EmmaX:    
                    ch_e "What have we said about this \"head pats\" obsession?"     
            elif Girl == LauraX:                                    
                    ch_l "Seriously, hands off."
            $ Girl.Statup("Love", 50, -2)
            return
    else:
            "You reach out and pat [Girl.Name] on the head."
    $ Girl.Statup("Obed", 50, 2)    
        
    if ApprovalCheck(Girl, 1200,Alt=[[LauraX],1000]):
            $ Girl.FaceChange("sexy", 1)
            if Girl == EmmaX:    
                    ch_e "Hmmmm?"     
            else:
                    call AnyLine(Girl,"Mmmmm. . .")
            $ Girl.Statup("Love", 85, 1)
    elif ApprovalCheck(Girl, 800,Alt=[[EmmaX],1200]) or ApprovalCheck(Girl, 750, "L",Alt=[[LauraX],600]):
            $ Girl.FaceChange("smile", 1) 
            call AnyLine(Girl,"Mmmmm. . .")    
    elif "headpat" in Girl.DailyActions:        
            $ Girl.FaceChange("angry", 1)
            if Girl == RogueX:
                        ch_r "Hands ta yourself, [Girl.Petname]."                
            elif Girl == KittyX: 
                    ch_k "Hey, cut it out."
            elif Girl == EmmaX:        
                    ch_e "Do I look like a child or pet to you?"    
            elif Girl == LauraX:
                    ch_l "I warned you not to do that."
            $ Girl.Statup("Love", 50, -2)
            $ Girl.DailyActions.append("no headpat")
    elif ApprovalCheck(Girl, 400,Alt=[[EmmaX],600]):
            $ Girl.Mouth = "smile"
            $ Girl.Brows = "normal"
            if Girl == RogueX:
                    ch_r "This is. . . weird."
            elif Girl == KittyX:
                    ch_k "Um, okay..."
            elif Girl == EmmaX:  
                    ch_e "Hmph. You have some odd interests."       
            elif Girl == LauraX:
                    ch_l "Um, that was weird."
    else:
            $ Girl.FaceChange("angry", 1)
            if Girl == RogueX:
                    "She slaps your hand aside and glares at you."
                    ch_r "Quit it!" 
            elif Girl == KittyX:
                    "She slaps your hand aside and glares at you."
                    ch_k "Knock it off!" 
            elif Girl == EmmaX:  
                    "She grabs your wrist and pulls it away from her hair."
                    ch_e "I will warn you once. Stop that."         
            elif Girl == LauraX:
                    "She flails her arms around, knocking your hand away." 
                    ch_l "Get away from me."   
            $ Girl.Statup("Love", 50, -3)
            $ Girl.Statup("Obed", 50, 1)
            $ Girl.Statup("Inbt", 30, 1)
    
    if "no headpat" in Girl.DailyActions: 
        menu:
            "Sorry, sorry, won't happen again.":
                if ApprovalCheck(Girl, 300):
                        $ Girl.FaceChange("sexy", 1)
                        if Girl == RogueX:
                                ch_r "Heard that before. . ."
                        elif Girl == KittyX:
                                ch_k "Uh-huh."  
                        elif Girl == EmmaX:  
                                ch_e "I should hope not."       
                        elif Girl == LauraX:
                                ch_l "Yeah, stop being weird."
                        $ Girl.Statup("Love", 80, 2)
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "side"
                        if Girl == RogueX:
                                ch_r "Damned right. . ."
                        elif Girl == KittyX:    
                                ch_k "It'd better not."    
                        elif Girl == EmmaX:  
                                "[EmmaX.Name] silently glares at you."           
                        elif Girl == LauraX:
                                ch_l "Uh-huh."                 
                        $ Girl.Statup("Obed", 20, 1)   
                    
            "You know you wanted it.":
                if ApprovalCheck(Girl, 400, "OI",Alt=[[EmmaX],600]) or ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                        $ Girl.FaceChange("normal", 1)
                        $ Girl.Eyes = "squint"
                        if Girl == RogueX:
                                ch_r "I. . . maybe?"
                        elif Girl == KittyX:
                                ch_k "Maaaaybe..." 
                        elif Girl == EmmaX:  
                                ch_e "Hmph. . ."       
                        elif Girl == LauraX:
                                ch_l "Um. . ."
                        $ Girl.Statup("Love", 60, -1) 
                        $ Girl.Statup("Obed", 30, 2)                        
                        $ Girl.Statup("Inbt", 40, 2)
                else:
                        $ Girl.FaceChange("angry", 2)
                        $ Girl.Eyes = "squint"
                        if Girl == RogueX:
                                ch_r "Wouldn't count on it."
                        elif Girl == KittyX:
                                ch_k "Um. . ."
                        elif Girl == EmmaX:   
                                ch_e "What nonsense. . ."        
                        elif Girl == LauraX:
                                ch_l "Did not!"  
                        $ Girl.Blush = 1
                        $ Girl.Statup("Love", 60, -3) 
                        $ Girl.Statup("Obed", 30, 3)                        
                        $ Girl.Statup("Inbt", 40, 2) 
        
    else:
        #if she hasn't refused this today. . . 
        menu:
            "Sorry, you looked so cute there.":
                if ApprovalCheck(Girl, 850, "LI",Alt=[[EmmaX],1050]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Count = 7
                        if Girl == RogueX:
                                "She tilts her head a bit."
                                ch_r "Mmmmm. . ."
                        elif Girl == KittyX:
                                "She leans into it."
                                ch_k "Purrrrr. . ."
                        elif Girl == EmmaX:  
                                "She hesitates, but then slowly closes her eyes."
                                ch_e "Be grateful. I wouldn't let just anyone do this."
                                $ Count -= 2
                        elif Girl == LauraX:
                                "She leans into it."
                                ch_l "Mmmmm. . ."
                        $ Girl.Statup("Love", 80, 2)  
                elif ApprovalCheck(Girl, 500, "LI",Alt=[[EmmaX],700]):
                        $ Girl.FaceChange("smile", 1)
                        $ Count = 5
                        if Girl == RogueX:
                                ch_r "Well, do go on. . ."
                        elif Girl == KittyX:
                                ch_k "Tell me something I don't know."
                        elif Girl == EmmaX:  
                                ch_e "Just cute? I must be slipping."     
                                $ Count -= 1  
                        elif Girl == LauraX:
                                ch_l "I'm not cute."
                                ch_l "But continue." 
                        $ Girl.Statup("Love", 80, 2)
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "side"
                        if Girl == RogueX:
                                ch_r "You're up ta somethin. . ."
                        elif Girl == KittyX:
                                ch_k "Yeah, right. Pull the other one." 
                        elif Girl == EmmaX:    
                                ch_e "You'll have to do better than that, [Girl.Petname]. Much better."          
                        elif Girl == LauraX:
                                ch_l "This cutie might bite your hand off."                 
                        $ Girl.Statup("Obed", 20, 1) 
                        $ Count = 1  
                    
            "You had a loose hair going on.":
                if ApprovalCheck(Girl, 700, "LI",Alt=[[EmmaX],850]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Count = 4
                        if Girl == RogueX:
                                ch_r "Oh? You'd best put it back then. . ."
                        elif Girl == KittyX:
                                ch_k "Loose hair? Me?"
                        elif Girl == EmmaX:       
                                ch_e "A loose hair, you say? Perhaps you can help get it back under control."  
                                $ Count += 1
                        elif Girl == LauraX:
                                ch_l "Oh? Whatever. . ."
                        $ Girl.Statup("Love", 60, 1)                        
                        $ Girl.Statup("Inbt", 40, 1)
                elif ApprovalCheck(Girl, 700):
                        $ Girl.FaceChange("normal")
                        $ Count = 3
                        if Girl == RogueX:
                                ch_r "Something's loose here. . ."
                        elif Girl == KittyX:
                                ch_k "A hair, right. . ."
                        elif Girl == EmmaX:     
                                ch_e "A loose hair? Oh, [Girl.Petname]. I would hope you'd be more original than that."    
                        elif Girl == LauraX:
                                ch_l "A hair, right. . ."
                else:
                        $ Girl.FaceChange("angry", 1)
                        if Girl == RogueX:
                                ch_r "Ain't no reason to go messin with it."
                        elif Girl == KittyX:
                                ch_k "Uhuh, just... just watch it, okay?"
                        elif Girl == EmmaX:     
                                ch_e "I can handle something like that easily enough on my own."    
                        elif Girl == LauraX:
                                ch_l "Uhuh, just don't touch me." 
                        $ Girl.Statup("Obed", 50, 2)  
                        $ Count = 1  
                    
            "Are you sure you didn't enjoy that?":
                if ApprovalCheck(Girl, 850,Alt=[[EmmaX],1000]):
                        $ Girl.FaceChange("sexy", 1)
                        $ Girl.Eyes = "side"
                        if Girl == RogueX:
                                ch_r "Well, I suppose. . ."
                        elif Girl == KittyX:
                                ch_k "Hmmm... maybe, maybe not."
                        elif Girl == EmmaX:   
                                ch_e "I'll admit that much, at least."     
                        elif Girl == LauraX:
                                ch_l "Well. . . yeah. . ."
                        $ Girl.Statup("Obed", 50, 2)  
                        $ Girl.Statup("Obed", 30, 1)                        
                        $ Girl.Statup("Inbt", 40, 1)
                        $ Count = 4
                elif ApprovalCheck(Girl, 500, "OI"):
                        $ Girl.FaceChange("normal", 1)
                        $ Count = 2
                        if Girl == RogueX:
                                ch_r "Not. . . really?"
                        elif Girl == KittyX:
                                ch_k "Well. . . I guess, maybe. . . nah, nope."
                        elif Girl == EmmaX:  
                                ch_e "Ah. . . no, no. A lady must have some secrets."   
                                $ Count += 1     
                        elif Girl == LauraX:
                                ch_l "Well. . . I guess, maybe. . . no, quit it."
                        $ Girl.Statup("Love", 60, -1)
                        $ Girl.Statup("Obed", 50, 2)  
                        $ Girl.Statup("Obed", 30, 2)                        
                        $ Girl.Statup("Inbt", 40, 2)
                else:
                        $ Girl.FaceChange("angry", 1)
                        $ Girl.Eyes = "side"
                        if Girl == RogueX:
                                ch_r "Oh, I'm sure."
                        elif Girl == KittyX:
                                ch_k "Grrrr. . ."  
                        elif Girl == EmmaX:  
                                ch_e "If you'd tried that a few years ago..."         
                        elif Girl == LauraX:
                                ch_l "Grrrr. . ."   
                        $ Girl.Statup("Love", 60, -3)
                        $ Girl.Statup("Obed", 50, 2)  
                        $ Girl.Statup("Obed", 30, 3)                        
                        $ Girl.Statup("Inbt", 40, 2)
                        $ Count = 1
        while Count > 0 and Round >= 10:
            $ Count -= 1 if Count != 4 else 0
            $ Round -= 1
            menu:
                "Continue?"
                "Yes":
                    "You continue to hold your hand on top of [Girl.Name]'s head, rubbing it softly."                    
                    if not Count:
                        #timed out
                        if ApprovalCheck(Girl, 800):
                                $ Girl.FaceChange("bemused", 2)
                                $ Girl.Statup("Love", 80, 2)                       
                                $ Girl.Statup("Inbt", 40, 2)
                                if Girl == RogueX:
                                        ch_r "Hey, ok, that'll be fine. . ."
                                elif Girl == KittyX:
                                        ch_k "Hey, okay, I think that's enough. . ."
                                elif Girl == EmmaX: 
                                        ch_e "I think. . . that will do."     
                                elif Girl == LauraX:
                                        ch_l "Ok, that's enough of that for now. . ."
                                "She ducks out from under your hand."
                                $ Girl.FaceChange("bemused", 1)
                        else:
                                $ Girl.FaceChange("angry", 2)
                                $ Girl.Statup("Love", 60, -5)                       
                                $ Girl.Statup("Inbt", 40, 3)
                                if Girl == RogueX:
                                        ch_r "Enough's enough there."
                                elif Girl == KittyX:
                                        ch_k "Ok, I think that's enough now. . ."
                                elif Girl == EmmaX:    
                                        ch_e "I think you've had your fun. . ."
                                elif Girl == LauraX:
                                        ch_l "Ok, enough, enough. . ."
                                "She knocks your hand away."
                                $ Girl.FaceChange("angry", 1)
                    elif Count == 1:
                        #nearly timed out
                        if ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                                $ Girl.FaceChange("bemused", 1)
                                $ Girl.Statup("Love", 80, 1)
                                $ Girl.Statup("Obed", 50, 2)                        
                                $ Girl.Statup("Inbt", 40, 2)
                                if Girl == RogueX:
                                        ch_r "Um, you might wanna. . ."
                                elif Girl == KittyX:
                                        ch_k "We should probably do something else. . ."
                                elif Girl == EmmaX:  
                                        if Taboo > 20:
                                                # Taboo ratings over 20 are considered public areas, over 0 means people might be around
                                                ch_e "We really shouldn't do this in public. . . I do have an image."
                                        else:
                                                ch_e "Just be careful not to do that in public. . . I do have an image."       
                                elif Girl == LauraX:
                                        ch_l "We should probably do something else. . ."
                        else:
                                $ Girl.FaceChange("angry", 2)
                                $ Girl.Statup("Love", 60, -2)
                                $ Girl.Statup("Obed", 60, 2)  
                                $ Girl.Statup("Obed", 30, 2)  
                                if Girl == RogueX:
                                        ch_r "You'd best cut that out. . ."
                                elif Girl == KittyX:
                                        ch_k "This [Girl.Name] has claws, you know."
                                elif Girl == EmmaX:         
                                        ch_e "Don't push your luck too far."
                                elif Girl == LauraX:
                                        ch_l "You aiming to lose that hand?"
                    else:
                        #she's ok with it. . .
                        if ApprovalCheck(Girl, 800,Alt=[[EmmaX],900]):
                                $ Girl.FaceChange("bemused", 2,Eyes="closed")
                                if Count > 5:
                                        $ Girl.Statup("Love", 90, 1)
                                        $ Girl.Statup("Love", 70, 1)
                                        $ Girl.Statup("Obed", 50, 1) 
                                if Girl == RogueX:
                                        ch_r "Uhuhh. . ."
                                elif Girl == KittyX:
                                        ch_k "Mmmmm. . ."
                                        "She's practically purring."
                                elif Girl == EmmaX:  
                                        ch_e "Mmmmm. . . you really shouldn't. . ."
                                        "She does seem to be leaning into it. . ."       
                                elif Girl == LauraX:
                                        ch_l "Mmmmm. . ."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                $ Girl.Statup("Love", 60, -1)
                                $ Girl.Statup("Obed", 50, 2)  
                                $ Girl.Statup("Obed", 30, 2)                        
                                $ Girl.Statup("Inbt", 40, 2)
                                if Girl == EmmaX:    
                                        ch_e "Er. . ."     
                                else:
                                        call AnyLine(Girl,"Um. . .")
                                $ Count -= 1 if Count > 2 else 0
                "No":
                    $ Count = 0
    $ Count = 0                
    $ Girl.RecentActions.append("headpat")
    $ Girl.DailyActions.append("headpat")
    return
# End Head Pat / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   
    
    
# Start Ask for panties / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label AskPanties(Girl=0,Store = 0):
    #called from Chat menu flirting options
    if Girl not in TotalGirls:
            return
    $ Store = Tempmod  
    $ Line = 0
    if not Girl.Panties or Girl.Panties == "shorts":
            if ApprovalCheck(Girl, 900):
                $ Girl.FaceChange("sexy", 1)
                $ Girl.Statup("Lust", 80, 5) 
                $ Girl.Statup("Lust", 60, 5) 
                $ Girl.Statup("Lust", 40, 10)            
                $ Girl.Statup("Inbt", 60, 5)            
                $ Girl.Statup("Inbt", 30, 10) 
                if Girl == RogueX:
                        ch_r "I'm not wearing any."
                elif Girl == KittyX:
                        ch_k "I might. . . if I had any. . ."
                elif Girl == EmmaX:
                        ch_e "That. . . isn't exactly an option."
                elif Girl == LauraX:
                        ch_l "I'm not wearing any."
            elif Girl.Over == "towel" or not Girl.Legs:
                $ Girl.FaceChange("bemused", 2)
                if Girl == RogueX:
                        ch_r "I think you can see I can't."            
                elif Girl == KittyX:
                        ch_k "How do you expect I could do that?"  
                elif Girl == EmmaX:
                        ch_e "I think you can see that I don't have any. . ."  
                elif Girl == LauraX:
                        ch_l "Did you think I was wearing any?"  
            else:
                $ Girl.FaceChange("bemused", 2, Eyes="side")
                $ Girl.Statup("Lust", 80, 5) 
                $ Girl.Statup("Lust", 60, 5) 
                $ Girl.Statup("Lust", 40, 10)            
                $ Girl.Statup("Inbt", 60, 5)                  
                if Girl == RogueX:
                        ch_r "I definitely have some on, but you can't have them."  
                elif Girl == KittyX:      
                        ch_k "Um, no. Not right now. For. . . reasons."  
                elif Girl == EmmaX:
                        ch_e "Hrm, I'm afraid not."  
                elif Girl == LauraX:
                        ch_l "I'm not wearing any at the moment."  
    else:
        #if she is wearing some panties
        if Girl.SeenPussy and ApprovalCheck(Girl, 500): 
                    #You've seen her Pussy.
                    $ Tempmod += 15
        elif Girl.SeenPanties and ApprovalCheck(Girl, 500): 
                    #You've seen her panties.
                    $ Tempmod += 5 
        if "exhibitionist" in Girl.Traits:
                    $ Tempmod += (Taboo * 5)
        if "dating" in Girl.Traits or ("sex friend" in Girl.Petnames and not Taboo):
                    $ Tempmod += 10
        if "no bottomless" in Girl.RecentActions: 
                    $ Tempmod -= 20
        
        $ Line = 0                    
        if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10: 
                #pants or something similar
                if ApprovalCheck(Girl, 1000, "OI", TabM = 5) or "exhibitionist" in Girl.Traits:   
                    $ Line = "here"
                elif ApprovalCheck(Girl, 900, TabM = 5):
                    $ Line = "change"
        elif Girl.PantsNum() == 5:
                #skirt
                if ApprovalCheck(Girl, 600, "OI", TabM = 5) or "exhibitionist" in Girl.Traits:   
                    $ Line = "here"
                elif ApprovalCheck(Girl, 1100, TabM = 5):
                    $ Line = "change"
        else:
                if ApprovalCheck(Girl, 1200, TabM = 5) or "exhibitionist" in Girl.Traits:
                    $ Line = "here"
        
        if Girl == KittyX and Line:
                #since Kitty has a trick, she's separate
                $ Girl.Statup("Lust", 60, 2)         
                $ Girl.Statup("Obed", 60, 4)            
                $ Girl.Statup("Inbt", 60, 4)
                call Remove_Panties(Girl)                
                if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:   
                            $ Girl.Statup("Lust", 60, 5)         
                            $ Girl.Statup("Obed", 60, 5)            
                            $ Girl.Statup("Inbt", 60, 5)   
                elif Girl.PantsNum() == 5:
                            $ Girl.Statup("Lust", 60, 5)         
                            $ Girl.Statup("Obed", 60, 4)            
                            $ Girl.Statup("Inbt", 60, 4) 
                else:
                            $ Girl.Statup("Lust", 60, 7)         
                            $ Girl.Statup("Obed", 60, 6)            
                            $ Girl.Statup("Inbt", 60, 8)  
                $ Tempmod = Store       
                $ Line = 0
                return
                    
        if Line == "here":                             
                #She's agreed to change and will do it here
                $ Girl.FaceChange("sly")                          
                if Girl.PantsNum() == 5:    
                    #skirt
                    $ Girl.Statup("Obed", 60, 4)            
                    $ Girl.Statup("Inbt", 60, 4)
                else: #no pants or skirt         
                    $ Girl.Statup("Obed", 60, 6)            
                    $ Girl.Statup("Inbt", 60, 6) 
                
                $ Girl.Statup("Lust", 60, 5)    
                call Remove_Panties(Girl)
                    
                if Taboo:
                    $ Girl.Statup("Lust", 60, 5) 
                    if "exhibitionist" in Girl.Traits: 
                        $ Girl.Statup("Lust", 80, 5)
                        $ Girl.Statup("Lust", 200, 5)    
                    $ Girl.Statup("Obed", 80, 10)            
                    $ Girl.Statup("Inbt", 80, 10)        
            
        elif Line:                                      
                #She's agreed to change, but leaves the room to do it.
                if not Taboo:                           
                    #If it's in one of your rooms                                    
                    $ Girl.FaceChange("bemused", 1)                     
                    if Girl == RogueX:
                            ch_r "Could you head out for a 'sec while I change?"
                    elif Girl == KittyX:
                            ch_k "Could you turn around?"
                    elif Girl == EmmaX:
                            ch_e "I would appreciate some privacy while I change."
                    elif Girl == LauraX:                        
                            ch_l "Could you turn around?"
                    menu:
                        extend ""
                        "OK.": 
                                $ Girl.Statup("Love", 90, 5) 
                                $ Girl.FaceChange("smile", 1)   
                                if Girl == RogueX:
                                        ch_r "I 'preciate it, [Girl.Petname]."
                                elif Girl == KittyX:                                            
                                        ch_k "Thanks, [Girl.Petname]." 
                                elif Girl == EmmaX:                                        
                                        ch_e "Thank you, [Girl.Petname]."  
                                elif Girl == LauraX:         
                                        ch_l "Thanks."
                                $ Girl.FaceChange("sly", 1) 
                                $ Girl.Statup("Lust", 60, 2)         
                                $ Girl.Statup("Obed", 60, 4)            
                                $ Girl.Statup("Inbt", 60, 4)
                                show blackscreen onlayer black 
                                "You exit the room for a minute"                                
                                hide blackscreen onlayer black 
                                $ Girl.DailyActions.append("pantyless")
                                $ Girl.OutfitChange()
                                call OutfitShame(Girl,20)
                                "When you return, she quietly hands you her balled up panties."
                                $ Line = 0
                            
                        "And miss the show?":
                            if ApprovalCheck(Girl, 1000, "LI"): 
                                    $ Girl.Statup("Lust", 70, 5)          
                                    $ Girl.Statup("Obed", 60, 5)            
                                    $ Girl.Statup("Inbt", 60, 5) 
                                    $ Girl.FaceChange("sly", 1) 
                                    if Girl == RogueX:
                                            ch_r "Ok, fine."
                                    elif Girl == KittyX:
                                            ch_k "Oh, you think there's a show?"
                                    elif Girl == EmmaX:
                                            ch_e "How precious."
                                    elif Girl == LauraX:
                                            ch_l "Oh, you'd like to watch?"
                            else:                 
                                    $ Girl.FaceChange("angry", 1) 
                                    $ Girl.Statup("Love", 90, -5)          
                                    $ Girl.Statup("Obed", 60, -3)            
                                    $ Girl.Statup("Inbt", 60, 5)                                     
                                    if Girl == RogueX:
                                            ch_r "Then I guess there'll be no show to see, [Girl.Petname]."
                                    elif Girl == KittyX:
                                            ch_k "Apparently so."
                                    elif Girl == EmmaX:
                                            ch_e "What show would that be, [Player.Name]?"
                                    elif Girl == LauraX:
                                            ch_l "Yes."
                                    $ Line = 0
                                
                        "Nope, I'm staying.":
                            if ApprovalCheck(Girl, 600, "OI"): 
                                    $ Girl.FaceChange("perplexed", 1) 
                                    $ Girl.Statup("Lust", 70, 5)          
                                    $ Girl.Statup("Obed", 60, 10)            
                                    $ Girl.Statup("Inbt", 60, 5)                                 
                                    if Girl == RogueX:
                                            ch_r "If you insist."
                                    elif Girl == KittyX:                                        
                                            ch_k "Ok."
                                    elif Girl == EmmaX:
                                            ch_e "If you must."
                                    elif Girl == LauraX:                                
                                            ch_l "Ok."                                
                                    $ Girl.FaceChange("normal") 
                            else:        
                                    $ Girl.FaceChange("angry", 1) 
                                    $ Girl.Statup("Love", 90, -10)          
                                    $ Girl.Statup("Obed", 60, -5)            
                                    $ Girl.Statup("Inbt", 60, 5)     
                                    if Girl == RogueX:
                                            ch_r "Then I guess I'm not doing anything."
                                    elif Girl == KittyX:
                                            ch_k "Huh, maybe[Girl.like]have a little respect?"
                                    elif Girl == EmmaX:
                                            ch_e "Then I suppose we're done here."
                                    elif Girl == LauraX:                                        
                                            ch_l "I think that's rude under the circumstances."                                
                                    $ Line = 0
                                
                    if Line:                                            
                                    #She agreed to stay  
                                    $ Girl.FaceChange("sly", 1) 
                                    if Girl.PantsNum() >= 6 or Girl.HoseNum() >= 10:   
                                            $ Girl.Statup("Lust", 60, 5)         
                                            $ Girl.Statup("Obed", 60, 5)            
                                            $ Girl.Statup("Inbt", 60, 5)   
                                    elif Girl.PantsNum() == 5:
                                            $ Girl.Statup("Lust", 60, 5)         
                                            $ Girl.Statup("Obed", 60, 4)            
                                            $ Girl.Statup("Inbt", 60, 4)                                         
                                    call Remove_Panties(Girl) 
                                

                else:                                  
                    #if she's in public
                    $ Girl.FaceChange("sly", 1) 
                    $ Girl.Statup("Lust", 60, 2)         
                    $ Girl.Statup("Obed", 60, 4)            
                    $ Girl.Statup("Inbt", 60, 4)
                    $ Girl.Loc = "hold"
                    call Set_The_Scene
                    "[Girl.Name] nods and leaves for a minute." 
                    $ Girl.DailyActions.append("pantyless")
                    $ Girl.OutfitChange()
                    call OutfitShame(Girl,20)
                    $ Girl.Loc = bg_current
                    call Set_The_Scene
                    "She returns and quietly hands you her balled up panties."                               
        else:                                          
            #She refuses.    
            $ Girl.FaceChange("angry", 2)                        
            if not ApprovalCheck(Girl, 500):
                    $ Girl.Statup("Lust", 60, 5) 
                    $ Girl.Statup("Love", 90, -10)          
                    $ Girl.Statup("Obed", 60, 3)            
                    $ Girl.Statup("Inbt", 60, 3) 
                    if Girl == RogueX:
                            ch_r "I can't believe you would even ask me something like that!"
                    elif Girl == KittyX:
                            ch_k "You think I'd do that?"
                    elif Girl == EmmaX:
                            ch_e "Out of the question."
                    elif Girl == LauraX:
                            ch_l "Why do you think I would?"
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")  
            elif not ApprovalCheck(Girl, 500, TabM = 5):
                    $ Girl.Statup("Lust", 60, 5) 
                    $ Girl.Statup("Love", 90, -5)          
                    $ Girl.Statup("Obed", 60, 5)            
                    $ Girl.Statup("Inbt", 60, 5)
                    if Girl == RogueX:
                            ch_r "I can't believe you would even ask me that here!"   
                    elif Girl == KittyX:
                            ch_k "I mean, here?"         
                    elif Girl == EmmaX:      
                            ch_e "Look around you and have some sense."  
                    elif Girl == LauraX:
                            ch_l "In public?"                  
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")  
            else:
                    $ Girl.FaceChange("bemused", 2)
                    $ Girl.Statup("Lust", 60, 3)            
                    $ Girl.Statup("Inbt", 60, 1)
                    if Taboo:            
                            $ Girl.Statup("Inbt", 60, 2)
                            if Girl == RogueX:
                                    ch_r "I'm sorry, [Girl.Petname], I'm not ready yet."
                            elif Girl == KittyX:                                    
                                    ch_k "Maybe you'll earn that, [Girl.Petname]."
                            elif Girl == EmmaX:
                                    ch_e "You know I would, [Girl.Petname], but not here."
                            elif Girl == LauraX:
                                    ch_l "Maybe someday, [Girl.Petname]."
                    else:
                            $ Girl.FaceChange("perplexed")       
                            $ Girl.Statup("Obed", 60, -2)  
                            if Girl == RogueX:
                                    ch_r "Nah, not around you, at least."  
                            elif Girl == KittyX:
                                    ch_k "You're nasty, [Girl.Petname]."                            
                            elif Girl == EmmaX:
                                    ch_e "You'll have to work up to that, [Girl.Petname]."                                  
                            elif Girl == LauraX:
                                    ch_l "Why would you want that?"
            $ Girl.Blush = 1
    $ Tempmod = Store       
    $ Line = 0
    return
    
label Remove_Panties(Girl = 0, Type=0,Store = 0, Store2 = 0):    
    if Girl not in TotalGirls:
            return
    if Girl == KittyX:        
            $ Girl.Panties = 0  
            $ Girl.FaceChange("bemused") 
            if Girl.PantsNum() >= 6:
                "[Girl.Name] looks around, reaches into her pocket, and tugs her panties out."
            elif Girl.PantsNum() == 5:               
                "[Girl.Name] looks around, reaches into her skirt, and pulls her panties out."
            elif Girl.HoseNum() >= 5:  
                "[Girl.Name] looks around, reaches through her [Girl.Hose], and pulls her panties out." 
            else:
                "[Girl.Name] looks around and pulls her panties off."
                
            $ Girl.FaceChange("sexy") 
            "She hands them to you with a smirk." 
            
            if not Girl.Legs and Girl.HoseNum() <= 10:
                    call expression Girl.Tag + "_First_Bottomless"
                    
            $ Girl.DailyActions.append("pantyless")
            $ Girl.OutfitChange()
            call OutfitShame(Girl,20)
            return
    $ Store = Girl.Legs
    $ Store2 = Girl.Hose                   
    if Girl.PantsNum() >= 6:
        #pants or shorts  
        $ Girl.Legs = 0     
        $ Type = 1
    elif Girl.PantsNum() == 5:
        #skirt
        $ Girl.Upskirt = 1 
        $ Type = 2
    if Girl.HoseNum() >= 5:
        $ Girl.Hose = 0   
        $ Type = 3 if Type == 2 else 4
        # 3 if skirt/hose, 4 if just hose
    $ Girl.Panties = 0  
    
    if Taboo:
            if Type == 1:
                "[Girl.Name] looks around, but pulls her pants clean off and her panties with them."
            elif Type == 3:
                "[Girl.Name] looks around, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
            elif Type == 2:               
                "[Girl.Name] looks around, reaches under her skirt, and pulls her panties down."
            elif Type == 4:  
                "[Girl.Name] looks around, but pulls her [Store2] clean off and her panties with them." 
            else:
                "[Girl.Name] looks around, and pulls her panties down."                             
    else: #Not Taboo
            if Type == 1:
                "[Girl.Name] glances at you and pulls her pants clean off and her panties with them."
            elif Type == 3:
                "[Girl.Name] glances at you, hikes up her skirt, pulls her [Store2] clean off and her panties with them."
            elif Type == 2:
                "[Girl.Name] glances at you, reaches under her skirt, and pulls her panties down."
            elif Type == 4:
                "[Girl.Name] glances at you and pulls her [Store2] clean off and her panties with them."
            else:                            
                "[Girl.Name] glances at you and pulls her panties off."
            
    $ Girl.Legs = Store  
    $ Girl.Hose = Store2      
    if Girl.PantsNum() > 6:
        #pants
        "She hands you the panties and then pulls her pants back on."    
    elif Girl.PantsNum() == 6 or Girl.Panties == "shorts":  
        #shorts
        "She hands you the panties and then pulls her shorts back up."  
        $ Girl.Upskirt = 0    
    elif Girl.PantsNum() == 5 and Girl.HoseNum() >= 5:
        #skirt and hose
        "She hands you the panties and then pulls her [Girl.Hose] back on and her skirt back down."  
        $ Girl.Upskirt = 0
    elif Girl.PantsNum() == 5:  
        #skirt
        "She hands you the panties and then pulls her skirt back down."  
        $ Girl.Upskirt = 0    
    elif Girl.HoseNum() >= 5:
        #hose
        "She hands you the panties and then pulls her [Girl.Hose] back on."  
    else:
        "[Girl.Name] hands them to you in a ball." 
    call expression Girl.Tag + "_First_Bottomless" pass (1) 
    
    $ Girl.DailyActions.append("pantyless")
    $ Girl.OutfitChange()
    call OutfitShame(Girl,20)
    return
# End Ask for panties / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    

# Favorite sex acts / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Favorite_Actions(Chr=0, Quick=0, Temp=0, ATemp=0, PTemp=0, BTemp=0, TTemp=0, HTemp=0, FTemp=0, D20F=0, BOptions=0):
    # Character is the selected girl    
    # if there's no selected character, it does it for all girls
    # if Quick is True, it just returns a string of the action as a value, otherwise it sets it as a lasting variable. 
    
    if Chr:
            $ BOptions = [Chr]  
    else:
            $ BOptions = ActiveGirls[:]  
            #cycles through each girl possible
            
    while BOptions:        
            $ Chr = BOptions[0]
            #ass, pussy, blow, tits, hand, fondling, kiss
            $ ATemp = Chr.Anal + Chr.DildoA + Chr.FondleA + Chr.InsertA + Chr.LickA        
            $ PTemp = Chr.Sex + Chr.DildoP + Chr.FondleP + Chr.InsertP + Chr.LickP
            $ BTemp = Chr.Blow
            $ TTemp = Chr.Tit
            $ XTemp = Chr.Foot
            $ HTemp = Chr.Hand
            $ FTemp = Chr.FondleB + Chr.FondleT + Chr.SuckB + Chr.Hotdog
                            
            #This portion sets a bonus based on the player's favorite activity with her.
            if Chr.PlayerFav and ApprovalCheck(Chr, 1500): 
                    if Chr.PlayerFav == "anal":
                        $ ATemp += 20
                    elif Chr.PlayerFav == "sex":
                        $ PTemp += 20
                    elif Chr.PlayerFav == "blow":
                        $ BTemp += 20
                    elif Chr.PlayerFav == "tit":
                        $ TTemp += 20
                    elif Chr.PlayerFav == "foot":
                        $ XTemp += 20
                    elif Chr.PlayerFav == "hand":
                        $ HTemp += 20
                    else:
                        $ FTemp += 20
            elif Chr.PlayerFav and ApprovalCheck(Chr, 800):
                    if Chr.PlayerFav == "anal":
                        $ ATemp += 5
                    elif Chr.PlayerFav == "sex":
                        $ PTemp += 5
                    elif Chr.PlayerFav == "blow":
                        $ BTemp += 5
                    elif Chr.PlayerFav == "tit":
                        $ TTemp += 5
                    elif Chr.PlayerFav == "foot":
                        $ XTemp += 5
                    elif Chr.PlayerFav == "hand":
                        $ HTemp += 5
                    else:
                        $ FTemp += 5
            
            #This adds the numbers together to make a large number, then generates a random number between 1 and that total
            $ Total = ATemp + PTemp + BTemp + TTemp + HTemp + XTemp + FTemp + Chr.Kissed 
            if Total <= 0:
                $ D20F = 999
            else:
                $ D20F = renpy.random.randint(1, Total)
            
            # This selects a favorite activity based on which number is picked.
            if D20F <= ATemp:
                        #if the result is someplace under the "anal" category. . .
                        if Chr.Anal >= 5:
                            $ Temp = "anal"
                        elif Chr.LickA >= 5:
                            $ Temp = "lick ass"
                        else:
                            $ Temp = "insert ass"
            elif D20F <= ATemp + PTemp:
                        #if the result is someplace under the "sex" category. . .            
                        if Chr.Sex >= 5:
                            $ Temp = "sex"
                        elif Chr.LickP >= 5:
                            $ Temp = "lick pussy"
                        else:
                            $ Temp = "fondle pussy"
            elif D20F <= ATemp + PTemp + BTemp:
                            $ Temp = "blow"
            elif D20F <= ATemp + PTemp + BTemp + TTemp:
                            $ Temp = "tit"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
                            $ Temp = "foot"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp:
                            $ Temp = "hand"
            elif D20F <= ATemp + PTemp + BTemp + TTemp + XTemp + HTemp + FTemp:
                        #if the result failed the higher tier categories. . .
                        $ D20F = renpy.random.randint(1, 20)
                        if D20F >= 15 and Chr.Hotdog:
                            $ Temp = "hotdog"
                        elif D20F >= 10 and Chr.SuckB:
                            $ Temp = "suck breasts"
                        elif D20F >= 5 and Chr.FondleB:
                            $ Temp = "fondle breasts"
                        else:
                            $ Temp = "fondle thighs"
            else:
                            $ Temp = "kiss you"
            
            if not Quick:
                $ Chr.Favorite = Temp
            else:
                return Temp            
            $ BOptions.remove(BOptions[0])
    return

# End favorite sex acts / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



#Start Gifts menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Gifts: 
    # call Gifts(RogueX)   
    $ Girl = Ch_Focus if not Girl else Girl
    call Shift_Focus(Girl)
    while True:
            if not Player.Inventory:
                "You don't have anything to give her."
                return
            menu:
                "What would you like to give her?"
                "Toys and Books":
                    menu:
                        "Give her a dildo." if "dildo" in Player.Inventory: 
                            #If you have a Dildo, you'll give it.
                            if "dildo" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the dildo."
                                    $ Girl.Blush = 1
                                    $ Girl.ArmPose = 2
                                    $ Girl.Held = "dildo"
                                    if ApprovalCheck(Girl, 800):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl == RogueX: 
                                                    ch_r "Well, I've got some ideas in mind for this. . ."
                                            elif Girl == LauraX:  
                                                    ch_l "Oh, cool, I've wanted one of these. . ."
                                            else:
                                                    ch_k "I'm sure I can find some place to store it. . ."
                                                    ch_e "I'm sure I can find some place to store it. . ."
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 500):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove("dildo")
                                            $ Girl.Inventory.append("dildo")
                                            if Girl != EmmaX: 
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                            if Girl == RogueX: 
                                                    ch_r "Huh, well I guess I can find a place for it. . ."  
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_r "I- I mean. . . I'll just put it away."
                                            elif Girl == KittyX: 
                                                    ch_k "I don't know what. . ."  
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("surprised")
                                                    ch_k "Oh!"
                                                    ch_k "Oh. . . I'll just[Girl.like]put it away."  
                                            elif Girl == EmmaX:   
                                                    ch_e "This is not an appropriate gift from a student. . ."  
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("sadside",1)
                                                    ch_e "Hm. . ."
                                                    $ Girl.Statup("Love", 200, 10)
                                                    $ Girl.Statup("Obed", 200, 10)
                                                    $ Girl.Statup("Inbt", 200, 10)
                                                    $ Girl.FaceChange("sly")
                                                    ch_e "I suppose I can find {i}some{/i} use for it. . ."
                                            elif Girl == LauraX:     
                                                    ch_l "Huh, you're a weird gift giver." 
                                                    $ Girl.Statup("Lust", 89, 5)
                                                    $ Girl.Statup("Lust", 89, 10)
                                                    $ Girl.FaceChange("smile")
                                                    ch_l "It's very thoughtful though."
                                            $ Girl.FaceChange("bemused")
                                    elif "offered gift" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry")                                    
                                            "She hands it back to you."
                                            if Girl == RogueX: 
                                                    ch_r "Look, maybe you should just rethink your gift-giving choices?" 
                                            elif Girl == KittyX:   
                                                    ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"   
                                            elif Girl == EmmaX:   
                                                    ch_e "I think I have made myself clear about inappropriate gifts?"
                                            elif Girl == LauraX:                    
                                                    ch_l "I said I can't take something like this."            
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)   
                                            if Girl == RogueX: 
                                                    ch_r "That's a pretty forward gift to be giving a lady. . ."  
                                            elif Girl == KittyX:   
                                                    ch_k "I- you shouldn't be giving girls stuff like this!"  
                                            elif Girl == EmmaX:   
                                                    ch_e "[Girl.Petname], I don't believe this is an appropriate gift from a student."  
                                            elif Girl == LauraX:                 
                                                    ch_l "I don't think you should just be handing these out to random chicks."                     
                                            $ Girl.Statup("Lust", 89, 5)
                                            "She hands it back to you."
                                            $ Girl.DailyActions.append("offered gift") 
                            elif Girl.Inventory.count("dildo") == 1:
                                    $ Player.Inventory.remove("dildo")
                                    $ Girl.Inventory.append("dildo")
                                    if Girl == RogueX: 
                                            ch_r "Well, I suppose I could always use another. . ."
                                    elif Girl == KittyX:  
                                            ch_k "Why stop with one. . ." 
                                    elif Girl == EmmaX:   
                                            ch_e "I suppose I always have room for one more. . ."
                                    elif Girl == LauraX:     
                                            ch_l "I don't know if I need another. . ."
                            else: 
                                    if Girl == RogueX: 
                                            ch_r "Honestly, [Girl.Petname], I already have enough of those."
                                    elif Girl == KittyX:   
                                            ch_k "I only have so many places to store these."
                                    elif Girl == EmmaX:   
                                            ch_e "How many places do you think I could put these?"
                                    elif Girl == LauraX:   
                                            ch_l "I'm running out of space at this point."  
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2
                            
                        "Give her the vibrator." if "vibrator" in Player.Inventory: 
                            #If you have a vibrator, you'll give it.
                            if "vibrator" not in Girl.Inventory:                            
                                "You give [Girl.Name] the Shocker Vibrator."
                                $ Girl.Blush = 1
                                $ Girl.ArmPose = 2
                                $ Girl.Held = "vibrator"
                                if ApprovalCheck(Girl, 700):                    
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.Statup("Love", 200, 30)
                                        $ Girl.Statup("Obed", 200, 30)
                                        $ Girl.Statup("Inbt", 200, 30)
                                        if Girl == RogueX: 
                                                ch_r "Well, I've got some ideas in mind for this. . ."
                                        elif Girl == KittyX:   
                                                ch_k "Well this is. . . [[bzzzt]- "
                                                ch_k "-interesting. . ."
                                        elif Girl == EmmaX:   
                                                ch_e "How very thoughtful of you. . ."  
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_e "I'm sure I can put this to good use. . ."
                                        elif Girl == LauraX:   
                                                ch_l "This is. . . [[bzzzt]- "    
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_l "-some kind of sex thing, huh. . ."
                                        $ Girl.Statup("Lust", 89, 10)
                                elif ApprovalCheck(Girl, 400):
                                        $ Girl.FaceChange("confused")
                                        $ Player.Inventory.remove("vibrator")
                                        $ Girl.Inventory.append("vibrator")
                                        $ Girl.Statup("Love", 200, 10)
                                        $ Girl.Statup("Obed", 200, 10)
                                        $ Girl.Statup("Inbt", 200, 10)
                                        if Girl == RogueX: 
                                                ch_r "I guess I can use this to work the kinks out. . ."  
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("surprised")
                                                ch_r "Muscle knots, I mean!"
                                        elif Girl == KittyX: 
                                                ch_k "I've heard these are very relaxing. . ."  
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("surprised")
                                                ch_k "-for my back!"
                                        elif Girl == EmmaX:   
                                                ch_e "How very thoughtful of you. . ."  
                                                $ Girl.Statup("Lust", 89, 10)
                                                $ Girl.FaceChange("sly")
                                                ch_e "a back massager, I assume. . ."
                                        elif Girl == LauraX:                                              
                                                ch_l "This is. . . [[bzzzt]- "                  
                                                $ Girl.FaceChange("sly")
                                                $ Girl.Statup("Lust", 89, 10)
                                                ch_l "-oooh. . ."
                                        $ Girl.FaceChange("bemused", 1)
                                elif "offered gift" in Girl.DailyActions:
                                        $ Girl.FaceChange("angry")
                                        "She hands it back to you."
                                        if Girl == RogueX: 
                                                ch_r "Look, maybe you should just rethink your gift-giving choices?"  
                                        elif Girl == KittyX:    
                                                ch_k "I think I[Girl.like]made myself clear about inappropriate gifts?"   
                                        elif Girl == EmmaX:   
                                                ch_e "I think I have made myself clear about inappropriate gifts?"   
                                        elif Girl == LauraX:   
                                                ch_l "I don't want it."   
                                else:
                                        $ Girl.FaceChange("angry")
                                        $ Girl.Statup("Love", 50, -20)
                                        $ Girl.Statup("Obed", 20, 10)
                                        $ Girl.Statup("Inbt", 20, 20)   
                                        if Girl == RogueX: 
                                                ch_r "I don't think I have much use for that." 
                                        elif Girl == KittyX:               
                                                ch_k "I can't really see the point."  
                                        elif Girl == EmmaX:   
                                                ch_e "[Girl.Petname], I don't believe this is an appropriate gift from a student."     
                                        elif Girl == LauraX:                                            
                                                ch_l "I don't need it."                                 
                                        $ Girl.Statup("Lust", 89, 5)
                                        "She hands it back to you."
                                        $ Girl.DailyActions.append("offered gift") 
                            else: 
                                        if Girl == RogueX: 
                                            ch_r "[Girl.Petname], I only need the one."
                                        elif Girl == EmmaX:   
                                            ch_e "I already have plenty."
                                        else:
                                            call AnyLine(Girl,"I already have one of these.")
                            $ Girl.Held = 0
                            $ Girl.ArmPose = 2
                            
                        "Give her a butt plug." if "buttplug" in Player.Inventory:
                            if "buttplug" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the butt plug."
                                    $ Player.Inventory.remove("buttplug")
                                    $ Girl.Inventory.append("buttplug")
                            else: 
                                    "She already has enough of those."
        
                        "Give her the \"Dazzler and Longshot\" book." if "Dazzler and Longshot" in Player.Inventory: 
                            #If you have a the book, you'll give it.
                            if "Dazzler and Longshot" not in Girl.Inventory:                            
                                "You give [Girl.Name] the book."
                                $ Girl.Blush = 1
                                if ApprovalCheck(Girl, 600, "L"):                    
                                        $ Girl.FaceChange("smile")
                                        if Girl == RogueX: 
                                                ch_r "Oh, I've heard of this one, very romantic!"   
                                        elif Girl == KittyX:        
                                                ch_k "Oh, this one's so sweet!"        
                                        elif Girl == EmmaX:            
                                                $ Girl.FaceChange("angry")
                                                ch_e "Is this the type of thing you expect from me. . ."
                                                $ Girl.FaceChange("sadside", Mouth="lipbite")
                                                ch_e "we'll have to see. . ."  
                                        elif Girl == LauraX:      
                                                ch_l "A love story?"
                                        $ Girl.Statup("Lust", 89, 10)
                                else:
                                        $ Girl.FaceChange("confused")
                                        if Girl == RogueX: 
                                                ch_r "Hmph, well I guess i've heard good things about it, I'll give it a shot."
                                        elif Girl == KittyX:    
                                                ch_k "Hm, worth the read I guess."               
                                        elif Girl == EmmaX:  
                                                $ Girl.FaceChange("angry")
                                                ch_e "I don't exactly read this dime store trash. . ."
                                                $ Girl.FaceChange("sadside", Mouth="lipbite")
                                                ch_e "but I will take it. . ."    
                                        elif Girl == LauraX: 
                                                ch_l "Huh. Is there a movie?"  
                                        $ Girl.FaceChange("bemused")       
                                $ Player.Inventory.remove("Dazzler and Longshot")
                                $ Girl.Inventory.append("Dazzler and Longshot") 
                                $ Girl.Statup("Love", 200, 50) 
                                if Girl.Love >= 1000:
                                    $ Girl.Love = 1000
                            else:               
                                if Girl == EmmaX:   
                                        ch_e "You're repeating yourself."      
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")
                            
                        "Give her the \"256 Shades of Grey\" book." if "256 Shades of Grey" in Player.Inventory: 
                            #If you have a book, you'll give it.
                            if "256 Shades of Grey" not in Girl.Inventory:                            
                                "You give [Girl.Name] the book."
                                $ Girl.Blush = 1
                                if ApprovalCheck(Girl, 500, "O"):                    
                                        $ Girl.FaceChange("bemused")
                                        if Girl == RogueX: 
                                                ch_r "I'll research it thoroughly."
                                        elif Girl == KittyX:    
                                                ch_k "I'll give it a good look."           
                                        elif Girl == EmmaX:    
                                                ch_e "I expect it might be somewhat entertaining."  
                                        elif Girl == LauraX: 
                                                ch_l "Looks dirty."
                                        $ Girl.Statup("Lust", 89, 10)
                                else:
                                        $ Girl.FaceChange("confused")
                                        if Girl == RogueX: 
                                                ch_r "Hmm, I have heard some good things about this one. I'll give it a quick read."  
                                        elif Girl == KittyX:          
                                                ch_k "Hmm, I guess I could read a few chapters."       
                                        elif Girl == EmmaX:    
                                                ch_e "I've heard of that one."    
                                        elif Girl == LauraX: 
                                                ch_l "I'll give it a look."  
                                        $ Girl.FaceChange("bemused")             
                                $ Player.Inventory.remove("256 Shades of Grey")
                                $ Girl.Inventory.append("256 Shades of Grey")                    
                                $ Girl.Statup("Obed", 200, 50)  
                                if Girl.Obed >= 1000:
                                    $ Girl.Obed = 1000
                            else: 
                                if Girl == EmmaX:   
                                        ch_e "You're repeating yourself."      
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")                 
                            
                        "Give her the \"Avengers Tower Penthouse\" book." if "Avengers Tower Penthouse" in Player.Inventory: 
                            #If you have a book, you'll give it.
                            if "Avengers Tower Penthouse" not in Girl.Inventory:                            
                                "You give [Girl.Name] the book."
                                $ Girl.Blush = 1
                                if ApprovalCheck(Girl, 500, "I"):                    
                                        $ Girl.FaceChange("bemused")
                                        if Girl == RogueX: 
                                                ch_r "Oh. . . I think I can work with this. . ."
                                        elif Girl == KittyX:   
                                                ch_k "This should be fun. . ."            
                                        elif Girl == EmmaX:    
                                                ch_e "Perhaps don't visit unannounced. . ."  
                                        elif Girl == LauraX: 
                                                ch_l "This is pretty hot. . ."
                                        $ Girl.Statup("Lust", 89, 10)
                                else:
                                        $ Girl.FaceChange("confused")
                                        if Girl == RogueX: 
                                                ch_r "Well. . . this is a bit. . . I think I'll keep this for research."  
                                        elif Girl == KittyX:    
                                                ch_k "Well. . . this is a bit. . . I could maybe learn a few things."             
                                        elif Girl == EmmaX:   
                                                ch_e "I normally confiscate such things. . . I'll just do that now. . ."     
                                        elif Girl == LauraX: 
                                                ch_l "Huh. . . ok."  
                                        $ Girl.FaceChange("bemused")               
                                $ Player.Inventory.remove("Avengers Tower Penthouse")
                                $ Girl.Inventory.append("Avengers Tower Penthouse")                    
                                $ Girl.Statup("Inbt", 200, 50)  
                                if Girl.Inbt >= 1000:
                                    $ Girl.Inbt = 1000
                            else: 
                                if Girl == EmmaX:   
                                        ch_e "You're repeating yourself."      
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")    
                    
                        "Never mind":
                            pass
                #End Toys and Books
                
                "Clothing":    
                    menu:
                        "Give her the green nighty." if Girl.Tag + " nighty" in Player.Inventory: 
                                #If you have a nighty, you'll give it.
                                if "nighty" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the nighty."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 600):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                            $ Girl.Inventory.append("nighty")
                                            $ Girl.Statup("Love", 200, 40)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            ch_r "I bet I'd look good in this. . ."
                                            $ Girl.Statup("Lust", 89, 10)
                                    else:
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " nighty")
                                            $ Girl.Inventory.append("nighty")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            ch_r "Well, it's a little revealing, but still pretty cute."  
                                            $ Girl.FaceChange("bemused")
                                else: 
                                            call AnyLine(Girl,"I already have one of those.")
                            
                        "Give her the corset." if Girl.Tag + " corset" in Player.Inventory: 
                                #If you have a bra, you'll give it.
                                if "corset" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the corset."
                                    if ApprovalCheck(Girl, 1000):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            ch_l "I'd look good in this, right?"
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.Statup("Love", 200, 15)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            ch_l "This is. . . kinda cool. . ."                    
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 600):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " corset")
                                            $ Girl.Inventory.append("corset")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 15)
                                            $ Girl.Statup("Inbt", 200, 15)
                                            ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."                     
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_l "I just told you no."   
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -10)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)  
                                            if "no gift panties" in Girl.DailyActions:                    
                                                ch_l "I don't want this either."                       
                                            else:                   
                                                ch_l "You have too much time on your hands."                     
                                            $ Girl.Statup("Lust", 89, 5)
                                            $ Girl.Blush = 1
                                            "She hands it back to you."
                                            $ Girl.RecentActions.append("no gift bra")                      
                                            $ Girl.DailyActions.append("no gift bra") 
                                else: 
                                            call AnyLine(Girl,"I already have one of those.")           
                        #End Corset
                        
                        "Give her the lace corset." if Girl.Tag + " lace corset" in Player.Inventory: 
                                #If you have a bra, you'll give it.
                                if "lace corset" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the lace corset."
                                    if ApprovalCheck(Girl, 1200):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.Statup("Love", 200, 25)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            ch_l "You think this'd look good on me?"
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 1000):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 30)
                                            $ Girl.Statup("Inbt", 200, 15)
                                            ch_l "This is. . . kinda flimsy. . ."                    
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " lace corset")
                                            $ Girl.Inventory.append("lace corset")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 25)
                                            ch_l "I don't know why you'd give me this, it's not like I'd wear it. . ."                     
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_l "I just told you no."   
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -10)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)  
                                            if "no gift panties" in Girl.DailyActions:                    
                                                ch_l "I don't want this either."                       
                                            else:                   
                                                ch_l "You have too much time on your hands."                     
                                            $ Girl.Statup("Lust", 89, 5)
                                            $ Girl.Blush = 1
                                            "She hands it back to you."
                                            $ Girl.RecentActions.append("no gift bra")                      
                                            $ Girl.DailyActions.append("no gift bra") 
                                else: 
                                            call AnyLine(Girl,"I already have one of those.")   
                        #End Lace Corset
                        
                        "Give her the lace bra." if Girl.Tag + " lace bra" in Player.Inventory: 
                                #If you have a bra, you'll give it. (not laura)
                                if "lace bra" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the lace bra."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1000):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                            $ Girl.Inventory.append("lace bra")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl == RogueX:  
                                                    ch_r "Hmm, this really shows off the assets. . ."
                                            elif Girl == KittyX:    
                                                    ch_k "At least you appreciate what I've got."         
                                            elif Girl == EmmaX:    
                                                    ch_e "I'm impressed, you got the size correct. . ." 
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 700,Alt=[[EmmaX],600]):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace bra")
                                            $ Girl.Inventory.append("lace bra")
                                            $ Girl.Statup("Love", 200, 25)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            if Girl == RogueX:  
                                                    ch_r "I don't know that I'd wear this out, but maybe in private." 
                                            elif Girl == KittyX:    
                                                    ch_k "This is. . . see-through. . ."         
                                                    ch_k "I don't know why you'd give me this, it's not like I'd wear it. . ."      
                                            elif Girl == EmmaX:  
                                                if ApprovalCheck(Girl, 700):
                                                    ch_e "I'm not exactly running low on this sort of thing. . ." 
                                                else:
                                                    ch_e "This is an . . . unusual gift from a student. . ."    
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl == RogueX:  
                                                    ch_r "You can't even give me 24 hours?!"  
                                            elif Girl == KittyX:   
                                                    ch_k "I haven't changed my mind, stop bothering me!"           
                                            elif Girl == EmmaX:  
                                                    ch_e "This still isn't an appropriate gift from a student."   
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)  
                                            if Girl == RogueX:  
                                                    if "no gift panties" in Girl.DailyActions:                    
                                                        ch_r "I don't want these neither!" 
                                                    else:                  
                                                        ch_r "I don't know why you would focus on my rack, [Girl.Petname]"  
                                            elif Girl == KittyX: 
                                                    if "no gift panties" in Girl.DailyActions:                    
                                                        ch_k "I don't want these either!"                       
                                                    else:                   
                                                        ch_k "You just- just don't be thinking about my breasts!"             
                                            elif Girl == EmmaX:    
                                                    if "no gift panties" in Girl.DailyActions:                    
                                                        ch_e "This isn't any better than the last."                       
                                                    else:                   
                                                        ch_e "I don't think it's appropriate for you to be so focused on my breasts." 
                                            $ Girl.Statup("Lust", 89, 5)
                                            "She hands it back to you."
                                            $ Girl.RecentActions.append("no gift bra")                      
                                            $ Girl.DailyActions.append("no gift bra") 
                                    $ Girl.FaceChange("bemused")
                                else: 
                                            call AnyLine(Girl,"I already have one of those.")   
                        #End Lace Bra
                                    
                        "Give her the lace panties." if Girl.Tag + " lace panties" in Player.Inventory: 
                                #If you have panties, you'll give it.
                                if "lace panties" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the lace panties."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1100):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                            $ Girl.Inventory.append("lace panties")
                                            $ Girl.Statup("Love", 200, 30)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 30)
                                            if Girl == RogueX:  
                                                    ch_r "Hmm, these really put the goods on display. . ."
                                            elif Girl == KittyX:  
                                                    ch_k "These don't leave much to the imagination. . ."           
                                            elif Girl == EmmaX: 
                                                    ch_e "Not entirely out of place in my wardrobe. . ."     
                                            elif Girl == LauraX: 
                                                    ch_l "These are pretty hot. . ."
                                            $ Girl.Statup("Lust", 89, 10)
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("confused")
                                            $ Player.Inventory.remove(Girl.Tag + " lace panties")
                                            $ Girl.Inventory.append("lace panties")
                                            $ Girl.Statup("Love", 200, 25)
                                            $ Girl.Statup("Obed", 200, 20)
                                            $ Girl.Statup("Inbt", 200, 20)
                                            if Girl == RogueX:  
                                                    ch_r "These are a bit flimsy. . ." 
                                            elif Girl == KittyX:   
                                                    ch_k "I- I wouldn't wear something like these. . ."                  
                                                    $ KittyX.FaceChange("bemused",1)
                                                    ch_k "But I'll hold on to them. . ."          
                                            elif Girl == EmmaX: 
                                                    ch_e "This is an. . . unsual gift."                  
                                                    $ EmmaX.FaceChange("sly",1)
                                                    ch_e "But I'll hold on to them. . ."   
                                            elif Girl == LauraX:          
                                                    ch_l "I don't think I'd wear these. . ."              
                                                    $ Girl.FaceChange("bemused",1)      
                                                    ch_l "But I might need to do laundry. . ."  
                                    elif "no gift panties" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl == RogueX:  
                                                    ch_r "Not today, [Girl.Petname]!"  
                                            elif Girl == KittyX:     
                                                    ch_k "Look, my answer's still no, stop asking!"            
                                            elif Girl == EmmaX:   
                                                    ch_e "I don't recommend trying again any time soon."   
                                            elif Girl == LauraX:   
                                                    ch_l "My answer's still no, stop asking!"     
                                    else:
                                            $ Girl.FaceChange("angry")
                                            $ Girl.Statup("Love", 50, -20)
                                            $ Girl.Statup("Obed", 20, 10)
                                            $ Girl.Statup("Inbt", 20, 20)  
                                            if Girl == RogueX:  
                                                    if "no gift bra" in Girl.DailyActions:                    
                                                        ch_r "I don't want these neither!" 
                                                    else:
                                                        ch_r "I think I'll pick out my own unmentionables, thank you." 
                                            elif Girl == KittyX:     
                                                    if "no gift bra" in Girl.DailyActions:                    
                                                        ch_k "I don't want these either!" 
                                                    elif Girl.SeenPanties:
                                                        ch_k "Just because you've seen my panties doesn't mean you get to pick them out."                          
                                                    else:
                                                        ch_k "Oh, don't you worry what I've got on down there."          
                                            elif Girl == EmmaX:    
                                                    if "no gift bra" in Girl.DailyActions:                    
                                                        ch_e "These aren't appropriate either." 
                                                    elif Girl.SeenPanties:
                                                        ch_e "Just because you've seen my panties doesn't mean you get to pick them out."                          
                                                    else:
                                                        ch_e "I don't believe these are appropriate thoughts for you to be having."  
                                            elif Girl == LauraX:      
                                                    if "no gift bra" in Girl.DailyActions:                    
                                                        ch_l "I don't want these either!" 
                                                    elif Girl.SeenPanties:
                                                        ch_l "Did you not like the ones I had?"                          
                                                    else:
                                                        ch_l "You don't need to worry about my underwear."                    
                                            $ Girl.Statup("Lust", 89, 5)
                                            "She hands them back to you."
                                            $ Girl.RecentActions.append("no gift panties")                      
                                            $ Girl.DailyActions.append("no gift panties") 
                                    $ Girl.FaceChange("bemused")
                                else: 
                                            call AnyLine(Girl,"I already have one of those.")         
                        #End Lace Panties
                             
                        "Give her the stockings and garterbelt." if "stockings and garterbelt" in Player.Inventory: 
                                #If you have a stockings, you'll give it. (Rogue and Emma)
                                if "stockings and garterbelt" not in Girl.Inventory:                            
                                        "You give [Girl.Name] the stockings."
                                        $ Girl.Blush = 1                 
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove("stockings and garterbelt")
                                        $ Girl.Inventory.append("stockings and garterbelt")
                                        $ Girl.Statup("Love", 200, 5)
                                        $ Girl.Statup("Obed", 200, 5)
                                        $ Girl.Statup("Inbt", 200, 5)
                                        if Girl == EmmaX:  
                                                ch_e "These are lovely. . ."
                                        else:
                                                call AnyLine(Girl,"These are pretty nice. . .") 
                                        $ Girl.Statup("Lust", 89, 5)
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")    
                             
                        "Give her the pantyhose." if Girl.Tag + " pantyhose" in Player.Inventory: 
                                #If you have a stockings, you'll give it. (emma)
                                if "pantyhose" not in Girl.Inventory:                            
                                        "You give [Girl.Name] the pantyhose."
                                        $ Girl.FaceChange("bemused")
                                        $ Player.Inventory.remove(Girl.Tag + " pantyhose")
                                        $ Girl.Inventory.append("pantyhose")
                                        $ Girl.Statup("Love", 200, 5)
                                        $ Girl.Statup("Obed", 200, 5)
                                        $ Girl.Statup("Inbt", 200, 5)
                                        call AnyLine(Girl,"These are lovely. . .")
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")
                                
                        "Give her the bikini top." if Girl.Tag + " bikini top" in Player.Inventory: 
                                #If you have a bra, you'll give it.
                                if "bikini top" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the bikini top."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1200):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl == RogueX:  
                                                    ch_r "This is a nice color. . ."
                                            elif Girl == KittyX:      
                                                    ch_k "This is pretty cute. . ."       
                                            elif Girl == EmmaX:   
                                                    ch_e "This does show off my assets, doesn't it. . ." 
                                            elif Girl == LauraX: 
                                                    ch_l "\"X\", cute. . ."
                                    elif ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl == RogueX:  
                                                    ch_r "A little skimpy. . ."   
                                            elif Girl == KittyX:     
                                                    ch_k "Kinda visible, maybe. . ."           
                                            elif Girl == EmmaX:    
                                                    ch_e "This is my style. . ."       
                                            elif Girl == LauraX: 
                                                    ch_l "Ok, cool. . ."                                             
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini top")
                                            $ Girl.Inventory.append("bikini top")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl == RogueX:  
                                                    ch_r "I was thinking about a tan. . ."  
                                            elif Girl == KittyX:   
                                                    ch_k "Aw, a cute Kitty. . . hole. . ."            
                                            elif Girl == EmmaX:       
                                                    ch_e "An interesting. . . gift. . ."    
                                            elif Girl == LauraX: 
                                                    ch_l "I could use one of these. . ."                    
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift bra" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl == RogueX:  
                                                    ch_r "My answer's still no, stop asking!" 
                                            elif Girl == KittyX:     
                                                    ch_k "Look, my answer's still no, stop asking!"         
                                            elif Girl == EmmaX:    
                                                    ch_e "I don't recommend trying again any time soon."
                                            elif Girl == LauraX: 
                                                    ch_l "My answer's still no, stop asking!"                              
                                    else:
                                        $ Girl.FaceChange("angry",2)
                                        $ Girl.Statup("Love", 50, -5)
                                        $ Girl.Statup("Obed", 20, 5)
                                        $ Girl.Statup("Inbt", 20, 10)
                                        if "no gift panties" in Girl.DailyActions:  
                                                call AnyLine(Girl,"I don't want these either!")                                                         
                                        else:
                                                if Girl == RogueX:  
                                                        ch_r "Don't you worry what I've got on down there."  
                                                elif Girl == KittyX:         
                                                        ch_k "Oh, don't you worry what I've got on down there."    
                                                elif Girl == EmmaX:    
                                                        ch_e "I don't think my swimwear is any concern of yours."  
                                                elif Girl == LauraX:        
                                                        ch_l "Don't worry about what I wear." 
                                        $ Girl.Blush = 1
                                        "She hands it back to you."
                                        $ Girl.RecentActions.append("no gift bra")                      
                                        $ Girl.DailyActions.append("no gift bra") 
                                    if "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                        if Girl == KittyX:
                                            if Girl.Inbt >= 400 or "blue skirt" in Girl.Inventory:
                                                    $ Girl.Swim[0] = 1
                                        else:
                                                    $ Girl.Swim[0] = 1
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")     
                                
                        #end bikini top
                        
                        "Give her the bikini bottoms." if Girl.Tag + " bikini bottoms" in Player.Inventory: 
                                #If you have a bra, you'll give it.
                                if "bikini bottoms" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the bikini bottoms."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1200):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            if Girl == RogueX:  
                                                    ch_r "These are pretty nice. . ."
                                            elif Girl == KittyX:   
                                                    ch_k "These are pretty cute. . ."          
                                            elif Girl == EmmaX:   
                                                    ch_e "These are quite stylish. . ." 
                                            elif Girl == LauraX: 
                                                    ch_l "Huh, nice cut. . ."
                                    elif ApprovalCheck(Girl, 900):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl == RogueX:  
                                                    ch_r "Kinda tiny, aren't they. . ." 
                                            elif Girl == KittyX:        
                                                    ch_k "A little snug, maybe. . ."        
                                            elif Girl == EmmaX:           
                                                    ch_e "Rather daring. . ."    
                                            elif Girl == LauraX:         
                                                    ch_l "Ok, cool. . ."                                
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 700):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " bikini bottoms")
                                            $ Girl.Inventory.append("bikini bottoms")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            if Girl == RogueX:  
                                                    ch_r "I was thinking about a tan. . ."  
                                            elif Girl == KittyX:         
                                                    ch_k "Well, it is bikini weather. . ."      
                                            elif Girl == EmmaX:  
                                                    ch_e "I don't know that a student should be buying me swimwear. . ."    
                                            elif Girl == LauraX: 
                                                    ch_l "Weird gift, but is it warm out. . ."                    
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift panties" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            if Girl == RogueX:  
                                                    ch_r "My answer's still no, stop asking!"  
                                            elif Girl == KittyX:    
                                                    ch_k "Look, my answer's still no, stop asking!"           
                                            elif Girl == EmmaX:  
                                                    ch_e "I don't recommend trying again any time soon."    
                                            elif Girl == LauraX: 
                                                    ch_l "My answer's still no, stop asking!"                             
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -5)
                                            $ Girl.Statup("Obed", 20, 5)
                                            $ Girl.Statup("Inbt", 20, 10)
                                            if "no gift bra" in Girl.DailyActions:  
                                                call AnyLine(Girl,"I don't want these either!")                                                         
                                            else:
                                                if Girl == RogueX:  
                                                        ch_r "Don't you worry what I've got on down there."  
                                                elif Girl == KittyX:         
                                                        ch_k "Oh, don't you worry what I've got on down there."    
                                                elif Girl == EmmaX:    
                                                        ch_e "I don't think my swimwear is any concern of yours."  
                                                elif Girl == LauraX:        
                                                        ch_l "Don't worry about what I wear." 
                                            $ Girl.Blush = 1
                                            "She hands them back to you."
                                            $ Girl.RecentActions.append("no gift panties")                      
                                            $ Girl.DailyActions.append("no gift panties") 
                                    if "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                        if Girl == KittyX:
                                            if Girl.Inbt >= 400 or "blue skirt" in Girl.Inventory:
                                                    $ Girl.Swim[0] = 1
                                        else:
                                                    $ Girl.Swim[0] = 1
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")     
                        #end bikini bottoms
                        
                        "Give her the blue skirt." if Girl.Tag + " blue skirt" in Player.Inventory: 
                                #If you have a bra, you'll give it.
                                if "blue skirt" not in Girl.Inventory:                            
                                    "You give [Girl.Name] the blue skirt."
                                    $ Girl.Blush = 1
                                    if ApprovalCheck(Girl, 1000):                    
                                            $ Girl.FaceChange("bemused")
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 10)
                                            ch_k "This is a cute skirt. . ."
                                    elif ApprovalCheck(Girl, 800):
                                            $ Girl.FaceChange("confused",1)
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.Statup("Love", 200, 20)
                                            $ Girl.Statup("Obed", 200, 10)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            ch_k "This is kinda daring. . ."                  
                                            $ Girl.FaceChange("bemused",1)
                                    elif ApprovalCheck(Girl, 600):
                                            $ Girl.FaceChange("confused",2)
                                            $ Player.Inventory.remove(Girl.Tag + " blue skirt")
                                            $ Girl.Inventory.append("blue skirt")
                                            $ Girl.Statup("Love", 200, 10)
                                            $ Girl.Statup("Obed", 200, 5)
                                            $ Girl.Statup("Inbt", 200, 5)
                                            ch_k "It'd go well with a swimsuit. . ."                  
                                            $ Girl.FaceChange("bemused",1)
                                    elif "no gift skirt" in Girl.RecentActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_k "I just don't want that."
                                    elif "no gift skirt" in Girl.DailyActions:
                                            $ Girl.FaceChange("angry",2)
                                            ch_k "Look, my answer's still no, stop asking!"                      
                                    else:
                                            $ Girl.FaceChange("angry",2)
                                            $ Girl.Statup("Love", 50, -5)
                                            $ Girl.Statup("Obed", 20, 5)
                                            $ Girl.Statup("Inbt", 20, 10)
                                            ch_k "Oh, don't you worry what I'm wearing."    
                                            $ Girl.Blush = 1
                                            "She hands them back to you."
                                            $ Girl.RecentActions.append("no gift skirt")                      
                                            $ Girl.DailyActions.append("no gift skirt") 
                                    if Girl == KittyX and "bikini top" in Girl.Inventory and "bikini bottoms" in Girl.Inventory:
                                            $ Girl.Swim[0] = 1
                                else: 
                                        call AnyLine(Girl,"I already have one of those.")    
                        #end blue skirt
                        
                        "Never mind":
                            pass 
                    #end Clothing
                
                "Switch to. . .":
                        call Switch_Chat 
                        ch_p "I'd like to give you something."
                        if Girl.Loc != bg_current:
                                call AnyLine(Girl,"I don't see how, if I'm not there.")
                                return
                        jump Gifts
                "Exit":
                    return      
    return

#End Gift Menu / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Girl Settings / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Settings:
    if Girl not in TotalGirls:
        $ Girl == Ch_Focus   
    call Shift_Focus(Girl)
    while True:
        menu:
            ch_p "Let's talk about you."
            "Wardrobe":
                        ch_p "I wanted to talk about your style."
                        call Taboo_Level
                        call expression Girl.Tag + "_Clothes" #call Rogue_Clothes
                                                    
            "Shift her Personality" if ApprovalCheck(Girl, 900, "L", TabM=0) or ApprovalCheck(Girl, 900, "O", TabM=0)or ApprovalCheck(Girl, 900, "I", TabM=0):
                        ch_p "Could we talk about us?"
                        call expression Girl.Tag + "_Personality" #call Rogue_Personality
                
            "Your Petname":
                        ch_p "Could we talk about my pet name?"
                        call expression Girl.Tag + "_Names"  #call Rogue_Names  
                    
            "[Girl.Name]'s Petname":
                        ch_p "I've got a pet name for you, you know?"    
                        call expression Girl.Tag + "_Pet" #call Rogue_Pet  
                        
            "[Girl.Name]'s name" if len(Girl.Names) > 1:
                        ch_p "You know how you told me you went by a different name?"    
                        call expression Girl.Tag + "_Rename" #call Rogue_Rename  
                                        
            "Follow options" if "follow" in Girl.Traits:
                        ch_p "You know how you ask if I want to follow you sometimes?"
                        $ Line = 0
                        if Girl == RogueX:
                                ch_r "Yes?"
                        elif Girl == KittyX:
                                ch_k "Yeah?"
                        elif Girl == EmmaX:
                                ch_e "Yes?"
                        elif Girl == LauraX:
                                ch_l "Yeah?"
                        menu:
                            extend ""
                            "You can go where you want, I'll catch up later." if "freetravels" not in Girl.Traits:
                                    $ Girl.FaceChange("perplexed")
                                    if Girl == RogueX:
                                            ch_r "Oh, ok, not a problem."
                                    elif Girl == KittyX:
                                            ch_k "Um[Girl.like]okay."
                                    elif Girl == EmmaX:
                                            ch_e "Fine, I'll leave some mystery."
                                    elif Girl == LauraX:
                                            ch_l "Oh. . . okay."
                                    if "follow" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 90, -2)
                                        $ Girl.Statup("Obed", 30, 5) 
                                    $ Line = "free"
                                    
                            "You can ask if I want to follow you." if "asktravels" not in Girl.Traits or "freetravels" in Girl.Traits:
                                    $ Girl.FaceChange("perplexed")
                                    if Girl == RogueX:
                                            ch_r "Oh, ok, not a problem."
                                    elif Girl == KittyX:
                                            ch_k "Um[Girl.like]okay."
                                    elif Girl == EmmaX:
                                            ch_e "Don't want to be left behind?"
                                    elif Girl == LauraX:
                                            ch_l "Right. . ."
                                    if "follow" not in Girl.DailyActions:
                                        $ Girl.Statup("Love", 70, 2) 
                                        $ Girl.Statup("Inbt", 60, 2) 
                                    $ Line = "ask"
                                                        
                            "Don't ever leave when I'm around." if "lockedtravels" not in Girl.Traits or "freetravels" in Girl.Traits:
                                if ApprovalCheck(Girl, 500, "O",Alt=[[EmmaX],600]) or ApprovalCheck(Girl, 900, "L"):   
                                    $ Girl.FaceChange("sexy")
                                    if Girl == RogueX:
                                            ch_r "Oh, Ok."
                                    elif Girl == KittyX:
                                            ch_k "Aw, you miss me when I'm not around!"  
                                    elif Girl == EmmaX:
                                            $ Girl.FaceChange("angry", Eyes="side")
                                            ch_e "I don't know why I put up with your nonsense."
                                            $ Girl.FaceChange("sexy",1)
                                            ch_e "But {i}fine.{/i}"
                                    elif Girl == LauraX:
                                            ch_l "That's sweet."
                                    if "follow" not in Girl.DailyActions:
                                        if Girl.Love > 90:
                                            $ Girl.Statup("Love", 99, 2)
                                        $ Girl.Statup("Obed", 60, 5)                             
                                    $ Girl.Statup("Inbt", 50, -5, 1) 
                                    $ Line = "lock"
                                else:
                                    $ Girl.FaceChange("angry")
                                    if Girl == RogueX:
                                            ch_r "Well, I don't really care what you think on the matter."  
                                    elif Girl == KittyX:
                                            ch_k "Well, who cares what you think?"    
                                    elif Girl == EmmaX:
                                            ch_e "Where I go is my own business." 
                                    elif Girl == LauraX:       
                                            ch_l "Well, who cares what you think?"
                                    
                            "Never mind.":
                                    if Girl == RogueX:
                                            ch_r "Oh, ok."
                                    elif Girl == KittyX:
                                            ch_k "Ooookay."
                                    elif Girl == EmmaX:
                                            ch_e "Whatever."
                                    elif Girl == LauraX:
                                            ch_l "Right. . ."
                        
                        if Line:
                                    $ Girl.DailyActions.append("follow")                
                                    if "freetravels" in Girl.Traits:
                                        $ Girl.Traits.remove("freetravels") 
                                    if "asktravels" in Girl.Traits:
                                        $ Girl.Traits.remove("asktravels") 
                                    if "lockedtravels" in Girl.Traits:
                                        $ Girl.Traits.remove("lockedtravels") 
                                
                                    if Line == "free":
                                        $ Girl.Traits.append("freetravels")            
                                    elif Line == "ask":
                                        $ Girl.Traits.append("asktravels")                
                                    elif Line == "lock":
                                        $ Girl.Traits.append("lockedtravels")    
                                    $ Line = 0
                
            "\"Like\" options" if Girl == KittyX:    
                    ch_p "So you[Girl.like]say \"[Girl.like]\" a lot. . ."      
                    if ApprovalCheck(Girl, 800):
                            call KittyLike
                    else:
                            ch_k "[Girl.Like]what's it to you?"
                    
            "Switch to. . .":
                    call Switch_Chat
                        
            "Never mind.":
                        return  
    #end loop

# End Girl_Settings / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


#Labels:
#Chat
#Chat_Menu
#Girl_Dismissed
#Flirt
#Compliment
#Love_You
#TouchCheek
#Hold_Hands
#Girl_Headpat
#AskPanties
#Remove_Panties
#Favorite_Actions
#Gifts
#Girl_Settings