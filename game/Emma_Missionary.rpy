# Start Emma Sex pose //////////////////////////////////////////////////////////////////////////////////
# E_Missionary_P //////////////////////////////////////////////////////////////////////

label E_Missionary_P:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Sex >= 7: # She loves it
        $ Tempmod += 15
    elif E_Sex >= 3: #You've done it before several times
        $ Tempmod += 12
    elif E_Sex: #You've done it before
        $ Tempmod += 10

    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 20
    elif E_Addict >= 75:
        $ Tempmod += 15

    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5

    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (4*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount



    if Taboo and "tabno" in E_DailyActions:
        $ Tempmod -= 10

    if "no sex" in E_DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no sex" in E_RecentActions else 0


    $ Approval = ApprovalCheck("Emma", 1400, TabM = 5) # 135, 150, 165, Taboo -200(335)

    if Situation == "auto":
                call Emma_Missionary_Launch("L")
                if E_Legs == "blue skirt":
                    "You press Emma down onto her back, sliding her skirt up as you go."
                    $ E_Upskirt = 1
                elif E_Legs == "capris" or E_Legs == "black jeans":
                    "You press Emma down onto her back, sliding her pants down as you do."
                    $ E_Upskirt = 1
                elif E_Legs == "shorts":
                    "You press Emma down onto her back, sliding her shorts down as you do."
                    $ E_Upskirt = 1
                else:
                    "You press Emma down onto her back."
                $ E_SeenPanties = 1
                "You rub the tip of your cock against her moist slit."
                call EmmaFace("surprised", 1)

                if (E_Sex and Approval) or (Approval > 1):
                    #this is not the first time you've had sex, or she's into it
                    "Emma is briefly startled, but melts into a sly smile."
                    call EmmaFace("sexy")
                    call Statup("Emma", "Obed", 70, 3)
                    call Statup("Emma", "Inbt", 50, 3)
                    call Statup("Emma", "Inbt", 70, 1)
                    ch_e "Oh. . . game on, [E_Petname]."
                    jump E_Missionary_SexPrep
                else:
                    #she's questioning it
                    $ E_Brows = "angry"
                    menu:
                        ch_e "Um, what do you think you're doing?"
                        "Sorry, sorry! Never mind.":
                            if Approval:
                                    call EmmaFace("sexy", 1)
                                    call Statup("Emma", "Obed", 70, 3)
                                    call Statup("Emma", "Inbt", 50, 3)
                                    call Statup("Emma", "Inbt", 70, 1)
                                    ch_e "{i}Well. . .{/i} I didn't say I didn't want to. . ."
                                    jump E_Missionary_SexPrep
                            else:
                                    "You pull back before you really get it in."
                                    call EmmaFace("bemused", 1)
                                    if E_Sex:
                                        ch_e "Maybe you could warn me?"
                                    else:
                                        ch_e "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."
                        "Just fucking.":
                            call Statup("Emma", "Love", 80, -10, 1)
                            call Statup("Emma", "Love", 200, -10)
                            "You press inside some more."
                            call Statup("Emma", "Obed", 70, 3)
                            call Statup("Emma", "Inbt", 50, 3)
                            if not ApprovalCheck("Emma", 700, "O", TabM=1):   #Checks if Obed is 700+
                                call EmmaFace("angry")
                                "Emma shoves you away and slaps you in the face."
                                ch_e "Jerk!"
                                ch_e "I am not putting up with that shit!"
                                call Statup("Emma", "Love", 50, -10, 1)
                                call Statup("Emma", "Obed", 50, 3)
                                $ renpy.pop_call()
                                if Situation:
                                    $ renpy.pop_call()
                                call Emma_Sex_Reset
                                $ E_RecentActions.append("angry")
                                $ E_DailyActions.append("angry")
                            else:
                                call EmmaFace("sad")
                                "Emma doesn't seem to be into this, you're lucky she's so obedient."
                                jump E_Missionary_SexPrep
                return
    #End Auto


    if not E_Sex and "no sex" not in E_RecentActions:
            #first time
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "I haven't really had much experience with this. . . "
            if E_Forced:
                call EmmaFace("sad")
                ch_e "You'd really do this when you have me over a barrel?"


    if not E_Sex and Approval:
            #First time dialog
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -30, 1)
                call Statup("Emma", "Love", 20, -20, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile"
                ch_e "I don't want you to think I'm some kind of slut. . ."
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "I suppose if it's you, [E_Petname]. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1)
                ch_e "I have kind of been hoping you might. . ."
            else: # Uninhibited
                call EmmaFace("sad")
                $ E_Mouth = "smile"
                ch_e "I can't say it hasn't crossed my mind. . ."
            #End first time dialog

    elif Approval:
            #Second time+ dialog
            call EmmaFace("sexy", 1)
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
                ch_e "Again? Why do you do this to me?"
            elif not Taboo and "tabno" in E_DailyActions:
                ch_e "I guess this is more secluded. . ."
            elif "sex" in E_RecentActions:
                ch_e "Another round? {i}Fine.{/i}"
                jump E_Missionary_SexPrep
            elif "sex" in E_DailyActions:
                $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You can't stay away from this. . .",
                    "Didn't get enough earlier?",
                    "You're wearing me out here!"])
                ch_e "[Line]"
            elif E_Sex < 3:
                $ E_Brows = "confused"
                $ E_Mouth = "kiss"
                ch_e "So you'd like another round?"
            else:
                $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You can't stay away from this. . .",
                    "You gonna make me purr?",
                    "You wanna slide into me?"])
                ch_e "[Line]"
            $ Line = 0
            #end Second time+ dialog

    if Approval >= 2:
            #She's into it. . .
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 60, 1)
                ch_e "Ok, fiiiiine."
            elif "no sex" in E_DailyActions:
                ch_e "You've made your case. . ."
            else:
                call EmmaFace("sexy", 1)
                call Statup("Emma", "Love", 90, 1)
                call Statup("Emma", "Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_e "[Line]"
                $ Line = 0
            call Statup("Emma", "Obed", 20, 1)
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 70, 2)
            jump E_Missionary_SexPrep

    else:
            #She's not into it, but maybe. . .
            call EmmaFace("angry")
            if "no sex" in E_RecentActions:
                ch_e "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in E_DailyActions and "no sex" in E_DailyActions:
                ch_e "I already told you. . .not in public!"
            elif "no sex" in E_DailyActions:
                ch_e "I already told you \"no.\""
            elif Taboo and "tabno" in E_DailyActions:
                ch_e "I already told you this is too public!"
            elif not E_Sex:
                call EmmaFace("bemused")
                ch_e "I don't know that I'm. . . ready? . ."
            else:
                call EmmaFace("bemused")
                ch_e "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no sex" in E_DailyActions:
                        call EmmaFace("bemused")
                        ch_e "It's cool."
                        return
                "Maybe later?" if "no sex" not in E_DailyActions:
                        call EmmaFace("sexy")
                        ch_e "Maybe, you never know."
                        call Statup("Emma", "Love", 80, 2)
                        call Statup("Emma", "Inbt", 70, 2)
                        if Taboo:
                            $ E_RecentActions.append("tabno")
                            $ E_DailyActions.append("tabno")
                        $ E_RecentActions.append("no sex")
                        $ E_DailyActions.append("no sex")
                        return
                "I think you'd enjoy it as much as I would. . .":
                        if Approval:
                            call EmmaFace("sexy")
                            call Statup("Emma", "Obed", 90, 2)
                            call Statup("Emma", "Obed", 50, 2)
                            call Statup("Emma", "Inbt", 70, 3)
                            call Statup("Emma", "Inbt", 40, 2)
                            $ Line = renpy.random.choice(["That's. . . true. . .",
                                "I suppose. . .",
                                "That's. . . that's a good point. . ."])
                            ch_e "[Line]"
                            $ Line = 0
                            jump E_Missionary_SexPrep
                "Just deal with it.":                                               # Pressured into it
                        $ Approval = ApprovalCheck("Emma", 1150, "OI", TabM = 3) # 115, 130, 145, -120(235)
                        if Approval > 1 or (Approval and E_Forced):
                            call EmmaFace("sad")
                            call Statup("Emma", "Love", 70, -5, 1)
                            call Statup("Emma", "Love", 200, -5)
                            ch_e "Well! . .  ok, fine, stick it in."
                            call Statup("Emma", "Obed", 80, 4)
                            call Statup("Emma", "Inbt", 80, 1)
                            call Statup("Emma", "Inbt", 60, 3)
                            $ E_Forced = 1
                            jump E_Missionary_SexPrep
                        else:
                            call Statup("Emma", "Love", 200, -20)
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")
                #end menu
    #end Approval check

    #She refused all offers.
    $ Emma_Arms = 1
    if "no sex" in E_DailyActions:
        ch_e "Maybe take \"no\" for an answer?"
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Not even."
        call Statup("Emma", "Lust", 200, 5)
        if E_Love > 300:
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")
        $ E_DailyActions.append("tabno")
        ch_e "I can't believe you'd even consider it around here!"
        call Statup("Emma", "Lust", 200, 5)
        call Statup("Emma", "Obed", 50, -3)
    elif E_Sex:
        call EmmaFace("sad")
        ch_e "Maybe just fuck yourself, huh?"
    else:
        call EmmaFace("normal", 1)
        ch_e "Nuhuh."
    $ E_RecentActions.append("no sex")
    $ E_DailyActions.append("no sex")
    $ Tempmod = 0
    return

label E_Missionary_SexPrep:
    call Seen_First_Peen("Emma",Partner,React=Situation)
    call Emma_Missionary_Launch("hotdog")

    if Situation == "Emma":
            #Emma auto-starts
            $ Situation = 0
            if E_Legs == "blue skirt":
                "Emma rolls back and pulls you toward her, sliding her skirt up as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "capris" or E_Legs == "black jeans":
                "Emma rolls back and pulls you against her, sliding her pants off as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "shorts":
                "Emma rolls onto her back and pulls you against her, sliding her shorts off as she does so."
                $ E_Upskirt = 1
            else:
                "Emma rolls back and pulls you toward her."
            $ E_SeenPanties = 1
            "She slides the tip along her pussy and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":
                    call Statup("Emma", "Inbt", 80, 3)
                    call Statup("Emma", "Inbt", 50, 2)
                    "Emma slides it in."
                "Praise her.":
                    call EmmaFace("sexy", 1)
                    call Statup("Emma", "Inbt", 80, 3)
                    ch_p "Oh yeah, [E_Pet], let's do this."
                    call Emma_Namecheck
                    "Emma slides it in."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")
                    call Statup("Emma", "Inbt", 70, 1)
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma pulls back."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")
                    call AnyWord("Emma",1,"refused","refused")
                    return
            $ E_PantiesDown = 1
            call Emma_First_Bottomless(1)

    elif Situation != "auto":
        call Emma_Bottoms_Off


        if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt) or HoseNum("Emma") >= 6: #If she refuses to take off her pants but agreed to anal
            ch_e "We can't exactly do much like this, huh."

            if (E_Panties and not E_PantiesDown) and (PantsNum("Emma") > 5 and not E_Upskirt):
                "She quickly drops her pants and her [E_Panties]."
            elif (E_Panties and not E_PantiesDown) and (E_Legs == "shorts" and not E_Upskirt):
                "She quickly drops her shorts and her [E_Panties]."
            elif PantsNum("Emma") > 5 and not E_Upskirt:
                "She shrugs and her pants drop through her, exposing her bare pussy."
            elif E_Legs == "shorts" and not E_Upskirt:
                "She shrugs and her shorts drop through her, exposing her bare pussy."
            elif HoseNum("Emma") >= 6 and (E_Panties and not E_PantiesDown):
                "She shrugs and her [E_Hose] and [E_Panties] fall to the ground."
                $ E_Hose = 0
            elif HoseNum("Emma") >= 6:
                "She shrugs and her [E_Hose] fall to the ground."
                $ E_Hose = 0
            elif (E_Panties and not E_PantiesDown):
                "She shrugs as her [E_Panties] fall to the ground."

        $ E_Upskirt = 1
        $ E_PantiesDown = 1
        $ E_SeenPanties = 1
        call Emma_First_Bottomless

        if Taboo: # Emma gets started. . .
            if not E_Sex:
                "Emma glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            else:
                "Emma glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."
            $ E_Inbt += int(Taboo/10)
            $ E_Lust += int(Taboo/5)
        else:
            if not E_Sex:
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
                "You press her folds aside and nudge your cock in."
            else:
                "Emma leans back and presses against you suggestively."
                "You take careful aim and then ram your cock in."

    else:  #if Situation == "auto"
        if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
            "You quickly pull down her pants and her [E_Panties] and press against her slit."
        elif (E_Panties and not E_PantiesDown):
            "You quickly pull down her [E_Panties] and press against her slit."
        $ E_Upskirt = 1
        $ E_PantiesDown = 1
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1)

    if not E_Sex:
        if E_Forced:
            call Statup("Emma", "Love", 90, -150)
            call Statup("Emma", "Obed", 70, 60)
            call Statup("Emma", "Inbt", 80, 50)
        else:
            call Statup("Emma", "Love", 90, 30)
            call Statup("Emma", "Obed", 70, 30)
            call Statup("Emma", "Inbt", 80, 60)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "in"
    $ Trigger = "sex"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no sex")
    $ E_RecentActions.append("sex")
    $ E_DailyActions.append("sex")

label E_Missionary_Sex_Cycle: #Repeating strokes
    while Round >=0:
        call Shift_Focus("Emma")
        call Emma_Missionary_Launch("sex")
        call EmmaLust
        $ P_Cock = "in"
        $ Trigger = "sex"
        $ E_Upskirt = 1
        $ E_PantiesDown = 1

        if  P_Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call E_Slap_Ass
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump E_Missionary_Sex_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."
                                    $ P_FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm kinda tired here? Could we wrap it up?"

                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about anal?":
                                                                $ Situation = "shift"
                                                                call E_Missionary_SexAfter
                                                                call E_Missionary_A
                                                        "Just stick it in her ass [[without asking].":
                                                                $ Situation = "auto"
                                                                call E_Missionary_SexAfter
                                                                call E_Missionary_A
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call E_Missionary_SexAfter
                                                                call E_Missionary_H
                                                        "Never Mind":
                                                                jump E_Missionary_Sex_Cycle
                                            else:
                                                ch_e "I'm kinda tired here? Could we wrap it up?"
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump E_Missionary_Sex_Cycle
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_Missionary_Sex_Cycle
                                            "Never mind":
                                                        jump E_Missionary_Sex_Cycle
                                    "Undress Emma":
                                            call E_Undress
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")
                                    "Never mind":
                                            jump E_Missionary_Sex_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Missionary_SexAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump E_Missionary_SexAfter
        #End menu (if Line)

        call Shift_Focus("Emma")
        call Sex_Dialog("Emma",Partner)

        $ Cnt += 1
        $ Round -= 1

        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:
                    #If either of you could cum
                    if P_Focus >= 100:
                            #If you can cum:
                            call PE_Cumming
                            if "angry" in E_RecentActions:
                                call Emma_Sex_Reset
                                return
                            call Statup("Emma", "Lust", 200, 5)
                            if 100 > E_Lust >= 70 and E_OCount < 2:
                                $ E_RecentActions.append("unsatisfied")
                                $ E_DailyActions.append("unsatisfied")

                            if P_Focus > 80:
                                jump E_Missionary_SexAfter
                            $ Line = "came"

                    if E_Lust >= 100:
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Missionary_SexAfter

                    if Line == "came": #ex P_Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_Missionary_SexAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it"
                                        jump E_Missionary_Sex_Cycle
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_Missionary_SexAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_Missionary_SexAfter
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")
        #End orgasm

        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0

        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Sex):
                    $ E_Brows = "confused"
                    ch_e "So are we getting close here?"
        elif Cnt == (10 + E_Sex):
                    $ E_Brows = "angry"
                    ch_e "I'm . . .getting . . kinda tired. . . here. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Missionary_SexAfter
                                call E_Blowjob
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump E_Missionary_Sex_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_Missionary_SexAfter
                        "No, get back down there.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_e "Not with that attitude, mister!"
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)
                                    call Statup("Emma", "Obed", 50, -1, 1)
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")
                                    jump E_Missionary_SexAfter
        #End Count check

        call Escalation("Emma","K") #sees if she wants to escalate things

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."

label E_Missionary_SexAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset

    call EmmaFace("sexy")

    $ E_Sex += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
    call Statup("Emma", "Inbt", 30, 2)
    call Statup("Emma", "Inbt", 70, 1)

    call Partner_Like("Emma",3,2)

    if "Emma Sex Addict" in Achievements:
            pass

    elif E_Sex >= 10:
        $ E_SEXP += 5
        $ Achievements.append("Emma Sex Addict")
        if not Situation:
            call EmmaFace("smile", 1)
            ch_e "I just can't seem to quit you."
    elif E_Sex == 1:
            $E_SEXP += 20
            if not Situation:
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I feel like I've been waiting a million years for that."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "I hope that was worth the wait."
    elif E_Sex == 5:
            ch_e "Why did we not do this sooner?!"
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e "Could you have maybe paid more attention? . ."

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_e "Did you want to try something else?"
    call Checkout
    return

# End Emma sex //////////////////////////////////////////////////////////////////////////////////


# Emma anal //////////////////////////////////////////////////////////////////////

label E_Missionary_A:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Anal >= 7: # She loves it
        $ Tempmod += 20
    elif E_Anal >= 3: #You've done it before several times
        $ Tempmod += 17
    elif E_Anal: #You've done it before
        $ Tempmod += 15

    if E_Addict >= 75 and (E_CreamP + E_CreamA) >=3: #She's really strung out and has creampied
        $ Tempmod += 25
    elif E_Addict >= 75:
        $ Tempmod += 15

    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5

    if E_Loose:
        $ Tempmod += 10
    elif "anal" in E_RecentActions:
        $ Tempmod -= 20
    elif "anal" in E_DailyActions:
        $ Tempmod -= 10

    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (5*Taboo)

    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount

    if Taboo and "tabno" in E_DailyActions:
        $ Tempmod -= 10
    if "no anal" in E_DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no anal" in E_RecentActions else 0

    $ Approval = ApprovalCheck("Emma", 1550, TabM = 5) # 155, 170, 185, Taboo -200(355)

    if Situation == "auto":
            call Emma_Missionary_Launch("L")
            if E_Legs == "blue skirt":
                "You press Emma down onto her back, sliding her skirt up as you go."
                $ E_Upskirt = 1
            elif E_Legs == "capris" or E_Legs == "black jeans":
                "You press Emma down onto her back, sliding her pants down as you do."
                $ E_Upskirt = 1
            elif E_Legs == "shorts":
                "You press Emma down onto her back, sliding her shorts down as you do."
                $ E_Upskirt = 1
            else:
                "You press Emma down onto her back."
            $ E_SeenPanties = 1
            "You press the tip of your cock against her tight rim."
            call EmmaFace("surprised", 1)

            if (E_Anal and Approval) or (Approval > 1):
                #this is not the first time you've had sex, or she's into it
                call Statup("Emma", "Obed", 70, 3)
                call Statup("Emma", "Inbt", 50, 3)
                call Statup("Emma", "Inbt", 70, 1)
                if E_Loose:
                    "Emma is briefly startled, but melts into a sly smile."
                    ch_e "Hmm, stick it in. . ."
                else:
                    "Emma is briefly startled, but shrugs."
                    ch_e "Oookay. . ."
                jump E_Missionary_AnalPrep
            else:
                #she's questioning it
                $ E_Brows = "angry"
                menu:
                    ch_e "Um what are you doing back there?!"
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            call EmmaFace("sexy", 1)
                            call Statup("Emma", "Obed", 70, 3)
                            call Statup("Emma", "Inbt", 50, 3)
                            call Statup("Emma", "Inbt", 70, 1)
                            ch_e "Well just take it easy, ok? . ."
                            jump E_Missionary_AnalPrep
                        "You pull back before you really get it in."
                        call EmmaFace("bemused", 1)

                        if E_Anal:
                            ch_e "Maybe you could warn me?"
                        else:
                            ch_e "Maybe you could warn me? I don't know that I'm ready for that sort of thing. . ."
                    "Just fucking.":
                        call Statup("Emma", "Love", 80, -10, 1)
                        call Statup("Emma", "Love", 200, -8)
                        "You press into her."
                        call Statup("Emma", "Obed", 70, 3)
                        call Statup("Emma", "Inbt", 50, 3)
                        if not ApprovalCheck("Emma", 700, "O", TabM=1):
                            call EmmaFace("angry")
                            "Emma shoves you away and slaps you in the face."
                            ch_e "Asshole!"
                            ch_e "You need to ask nicer than that!"
                            call Statup("Emma", "Love", 50, -10, 1)
                            call Statup("Emma", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Sex_Reset
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")
                        else:
                            call EmmaFace("sad")
                            "Emma doesn't seem to be into this, you're lucky she's so obedient."
                            jump E_Missionary_AnalPrep
            return
            #end "auto"


    if not E_Anal and "no anal" not in E_RecentActions:
            #first time
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "You want to go in the \"out\" door?!"

            if E_Forced:
                call EmmaFace("sad")
                ch_e "Anal? Really?"

    if not E_Loose and ("dildo anal" in E_DailyActions or "anal" in E_DailyActions):
            #if she's done anal stuff today
            call EmmaFace("bemused", 1)
            ch_e "I'm not really over the last time."
    elif "anal" in E_RecentActions:
            call EmmaFace("sexy", 1)
            ch_e "Again? K."
            jump E_Missionary_AnalPrep


    if not E_Anal and Approval:
            #First time dialog
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile"
                ch_e "I guess? . ."
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "Well. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1)
                ch_e "I. . . if that's how you want to do it. . . maybe?"
            else: # Uninhibited
                call EmmaFace("sad")
                $ E_Mouth = "smile"
                ch_e "Anything's worth a shot. . ."

    elif Approval:
            #Second time+ dialog
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
                ch_e "You really ask a lot here. . ."
            elif not Taboo and "tabno" in E_DailyActions:
                ch_e "I guess this is out of the way. . ."
            elif "anal" in E_DailyActions and not E_Loose:
                pass
            elif "anal" in E_RecentActions:
                ch_e "I guess I'm warmed up. . ."
                jump E_Missionary_AnalPrep
            elif "anal" in E_DailyActions:
                call EmmaFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "I'm still a little sore from earlier.",
                    "Didn't get enough earlier?",
                    "You're wearing me out here!"])
                ch_e "[Line]"
            else:
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "I do have booty for days. . .",
                    "You gonna make me purr?",
                    "You wanna slide into me?"])
                ch_e "[Line]"
            $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Obed", 90, 1)
                call Statup("Emma", "Inbt", 60, 1)
                ch_e "Ok, fine."
            elif "no anal" in E_DailyActions:
                ch_e "Well, ok, I've given it some thought, fine. . ."
            else:
                call EmmaFace("sexy", 1)
                call Statup("Emma", "Love", 90, 1)
                call Statup("Emma", "Inbt", 50, 3)
                $ Line = renpy.random.choice(["Well. . . ok.",
                    "Sure!",
                    "You could, I guess.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_e "[Line]"
                $ Line = 0
            call Statup("Emma", "Obed", 20, 1)
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 70, 2)
            jump E_Missionary_AnalPrep

    else:
            #She's not into it, but maybe. . .
            call EmmaFace("angry")
            if "no anal" in E_RecentActions:
                ch_e "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in E_DailyActions and "no anal" in E_DailyActions:
                ch_e "I already told you. . .not in public!"
            elif "no anal" in E_DailyActions:
                ch_e "I already told you \"no.\""
            elif Taboo and "tabno" in E_DailyActions:
                ch_e "I already told you this is too public!"
            elif not E_Anal:
                call EmmaFace("bemused")
                ch_e "I don't know that I'm. . . that kind of girl?"
            elif not E_Loose and "anal" not in E_DailyActions:
                call EmmaFace("perplexed")
                ch_e "That was kind of. . . rough last time?"
            else:
                call EmmaFace("bemused")
                ch_e "Maybe not right now? . ."
            menu:
                extend ""
                "Sorry, never mind." if "no anal" in E_DailyActions:
                    call EmmaFace("bemused")
                    ch_e "It's cool."
                    return
                "Maybe later?" if "no anal" not in E_DailyActions:
                    call EmmaFace("sexy")
                    ch_e "Maybe, you never know."
                    call Statup("Emma", "Love", 80, 2)
                    call Statup("Emma", "Inbt", 70, 2)
                    if Taboo:
                        $ E_RecentActions.append("tabno")
                        $ E_DailyActions.append("tabno")
                    $ E_RecentActions.append("no anal")
                    $ E_DailyActions.append("no anal")
                    return
                "I bet it would feel really good. . .":
                    if Approval:
                        call EmmaFace("sexy")
                        call Statup("Emma", "Obed", 90, 2)
                        call Statup("Emma", "Obed", 50, 2)
                        call Statup("Emma", "Inbt", 70, 3)
                        call Statup("Emma", "Inbt", 40, 2)
                        $ Line = renpy.random.choice(["That's. . . true. . .",
                            "I suppose. . .",
                            "That's. . . that's a good point. . ."])
                        ch_e "[Line]"
                        $ Line = 0
                        jump E_Missionary_AnalPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 1250, "OI", TabM = 3) # 125, 140, 155, -120(245)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        call Statup("Emma", "Love", 70, -5, 1)
                        call Statup("Emma", "Love", 200, -5)
                        ch_e "Well! . .  ok, fine, stick it in."
                        call Statup("Emma", "Obed", 80, 4)
                        call Statup("Emma", "Inbt", 80, 1)
                        call Statup("Emma", "Inbt", 60, 3)
                        $ E_Forced = 1
                        jump E_Missionary_AnalPrep
                    else:
                        call Statup("Emma", "Love", 200, -20)
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")

    #She refused all offers.
    $ Emma_Arms = 1
    if "no anal" in E_DailyActions:
        ch_e "Maybe take \"no\" for an answer?"
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")
    elif E_Forced:
        call EmmaFace("angry", 1)
        ch_e "That's a bit much, even for you."
        call Statup("Emma", "Lust", 200, 5)
        if E_Love > 300:
                call Statup("Emma", "Love", 70, -2)
        call Statup("Emma", "Obed", 50, -2)
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")
    elif Taboo:
        # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")
        $ E_DailyActions.append("tabno")
        ch_e "You're being ridiculous. That? Here?!"
        call Statup("Emma", "Lust", 200, 5)
        call Statup("Emma", "Obed", 50, -3)
    elif not E_Loose and "anal" in E_DailyActions:
        call EmmaFace("bemused")
        ch_e "I'm a little sore here?"
    elif E_Anal:
        call EmmaFace("sad")
        ch_e "That's totally off the table."
    else:
        call EmmaFace("normal", 1)
        ch_e "Noooope."
    $ E_RecentActions.append("no anal")
    $ E_DailyActions.append("no anal")
    $ Tempmod = 0
    return

label E_Missionary_AnalPrep:
    call Seen_First_Peen("Emma",Partner,React=Situation)
    call Emma_Missionary_Launch("hotdog")

    if Situation == "Emma":
            #Emma auto-starts
            $ Situation = 0

            if E_Legs == "blue skirt":
                "Emma rolls back and pulls you toward her, sliding her skirt up as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "capris" or E_Legs == "black jeans":
                "Emma rolls back and pulls you against her, sliding her pants off as she does so."
                $ E_Upskirt = 1
            elif E_Legs == "shorts":
                "Emma rolls onto her back and pulls you against her, sliding her shorts off as she does so."
                $ E_Upskirt = 1
            else:
                "Emma rolls back and pulls you toward her."
            $ E_SeenPanties = 1
            "She slides the tip along her ass and seems to want you to insert it."
            menu:
                "What do you do?"
                "Go with it.":
                    call Statup("Emma", "Inbt", 80, 3)
                    call Statup("Emma", "Inbt", 50, 2)
                    "Emma slides it in."
                "Praise her.":
                    call EmmaFace("sexy", 1)
                    call Statup("Emma", "Inbt", 80, 3)
                    ch_p "Oh yeah, [E_Pet], let's do this."
                    call Emma_Namecheck
                    "Emma slides it in."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")
                    call Statup("Emma", "Inbt", 70, 1)
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma pulls back."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")
                    call AnyWord("Emma",1,"refused","refused")
                    return
            $ E_PantiesDown = 1
            call Emma_First_Bottomless(1)

    elif Situation != "auto":
        call Emma_Bottoms_Off
        if (E_Panties and not E_PantiesDown) or (E_Legs and not E_Upskirt) or HoseNum("Emma") >= 6: #If she refuses to take off her pants but agreed to anal
            ch_e "We can't exactly do much like this, huh."

            if (E_Panties and not E_PantiesDown) and (PantsNum("Emma") > 5 and not E_Upskirt):
                "She quickly drops her pants and her [E_Panties]."
            elif (E_Panties and not E_PantiesDown) and (E_Legs == "shorts" and not E_Upskirt):
                "She quickly drops her shorts and her [E_Panties]."
            elif PantsNum("Emma") > 5 and not E_Upskirt:
                "She shrugs and her pants drop through her, exposing her bare pussy."
            elif E_Legs == "shorts" and not E_Upskirt:
                "She shrugs and her shorts drop through her, exposing her bare pussy."
            elif HoseNum("Emma") >= 6 and (E_Panties and not E_PantiesDown):
                "She shrugs and her [E_Hose] and [E_Panties] fall to the ground."
                $ E_Hose = 0
            elif HoseNum("Emma") >= 6:
                "She shrugs and her [E_Hose] fall to the ground."
                $ E_Hose = 0
            elif (E_Panties and not E_PantiesDown):
                "She shrugs as her [E_Panties] fall to the ground."

        $ E_Upskirt = 1
        $ E_PantiesDown = 1
        $ E_SeenPanties = 1
        call Emma_First_Bottomless

        if Taboo: # Emma gets started. . .
            if E_Anal:
                "Emma glances around to see if anyone notices what she's doing, then presses firmly against your cock."
                "You guide your cock into place and ram it home."

            else:
                "Emma glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
                "You guide it into place and slide it in."
            $ E_Inbt += int(Taboo/10)
            $ E_Lust += int(Taboo/5)
        else:
            if not E_Anal:
                "Emma leans back and presses against you suggestively."
                "You take careful aim and then push your cock in."
            else:
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants slowly presses against your rigid member."
                "You press against her rim and nudge your cock in."

    else: #if Situation == "auto"
        if (E_Legs == "pants" and not E_Upskirt) and (E_Panties and not E_PantiesDown):
            "You quickly pull down her pants and her [E_Panties] and press against her back door."
        elif (E_Panties and not E_PantiesDown):
            "You quickly pull down her [E_Panties] and press against her back door."
        $ E_Upskirt = 1
        $ E_PantiesDown = 1
        $ E_SeenPanties = 1
        call Emma_First_Bottomless(1)

    if not E_Anal:                                                      #First time stat buffs
        if E_Forced:
            call Statup("Emma", "Love", 90, -150)
            call Statup("Emma", "Obed", 70, 70)
            call Statup("Emma", "Inbt", 80, 40)
        else:
            call Statup("Emma", "Love", 90, 10)
            call Statup("Emma", "Obed", 70, 30)
            call Statup("Emma", "Inbt", 80, 70)
    elif not E_Loose:                                                   #first few times stat buffs
        if E_Forced:
            call Statup("Emma", "Love", 90, -20)
            call Statup("Emma", "Obed", 70, 10)
            call Statup("Emma", "Inbt", 80, 5)
        else:
            call Statup("Emma", "Obed", 70, 7)
            call Statup("Emma", "Inbt", 80, 5)

    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ P_Cock = "anal"
    $ Trigger = "anal"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no anal")
    $ E_RecentActions.append("anal")
    $ E_DailyActions.append("anal")

label E_Missionary_Anal_Cycle: #Repeating strokes
    while Round >=0:
        call Shift_Focus("Emma")
        call Emma_Missionary_Launch("anal")
        call EmmaLust
        $ P_Cock = "anal"
        $ Trigger = "anal"

        if  P_Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call E_Slap_Ass
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump E_Missionary_Anal_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."
                                    $ P_FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm kinda tired here? Could we wrap it up?"

                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                                $ Situation = "shift"
                                                                call E_Missionary_AnalAfter
                                                                call E_Missionary_P
                                                        "Just stick it in her pussy [[without asking].":
                                                                $ Situation = "auto"
                                                                call E_Missionary_AnalAfter
                                                                call E_Missionary_P
                                                        "Pull back to hotdog her.":
                                                                $ Situation = "pullback"
                                                                call E_Missionary_AnalAfter
                                                                call E_Missionary_H
                                                        "Never Mind":
                                                                jump E_Missionary_Anal_Cycle
                                            else:
                                                ch_e "I'm kinda tired here? Could we wrap it up?"
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump E_Missionary_Anal_Cycle
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_Missionary_Anal_Cycle
                                            "Never mind":
                                                        jump E_Missionary_Anal_Cycle
                                    "Undress Emma":
                                            call E_Undress
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")
                                    "Never mind":
                                            jump E_Missionary_Anal_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Missionary_AnalAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump E_Missionary_AnalAfter
        #End menu (if Line)

        call Shift_Focus("Emma")
        call Sex_Dialog("Emma",Partner)

        $ Cnt += 1
        $ Round -= 1

        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:
                    #If either of you could cum
                    if P_Focus >= 100:
                            #If you can cum:
                            call PE_Cumming
                            if "angry" in E_RecentActions:
                                call Emma_Sex_Reset
                                return
                            call Statup("Emma", "Lust", 200, 5)
                            if 100 > E_Lust >= 70 and E_OCount < 2:
                                $ E_RecentActions.append("unsatisfied")
                                $ E_DailyActions.append("unsatisfied")

                            if P_Focus > 80:
                                jump E_Missionary_AnalAfter
                            $ Line = "came"

                    if E_Lust >= 100:
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Missionary_AnalAfter

                    if Line == "came": #ex P_Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_Missionary_AnalAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it"
                                        jump E_Missionary_Anal_Cycle
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_Missionary_AnalAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_Missionary_AnalAfter
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")
        #End orgasm

        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0

        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Anal):
                    $ E_Brows = "confused"
                    if E_Loose:
                        ch_e "So are we getting close here?"
                    else:
                        ch_e "So are we getting close here? This is not super pleasant. . ."
        elif Cnt == (10 + E_Anal):
                    $ E_Brows = "angry"
                    ch_e "I'm . . .getting . . kinda tired. . . of this. . ."
                    menu:
                        ch_e "Can we. . . do something. . . else?"
                        "How about a BJ?" if E_Action and MultiAction:
                                if E_Anal >= 5 and E_Blow >= 10 and E_SEXP >= 50:
                                    $ Situation = "shift"
                                    call E_Missionary_AnalAfter
                                    call E_Blowjob
                                else:
                                    ch_e "No thanks, [E_Petname]. Maybe a Handy instead?"
                                    $ Situation = "shift"
                                    call E_Missionary_AnalAfter
                                    call KHJ_Prep
                        "How about a Handy?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Missionary_AnalAfter
                                call E_Handjob
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump E_Missionary_Anal_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_Missionary_AnalAfter
                        "No, get back down there.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls out."
                                    ch_e "Not with that attitude, mister!"
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)
                                    call Statup("Emma", "Obed", 50, -1, 1)
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")
                                    jump E_Missionary_AnalAfter
        #End Count check

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."

label E_Missionary_AnalAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset

    call EmmaFace("sexy")

    $ E_Anal += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
    call Statup("Emma", "Inbt", 30, 3)
    call Statup("Emma", "Inbt", 70, 1)

    if Partner == "Emma":
        call Partner_Like("Emma",4,3)
    else:
        call Partner_Like("Emma",3,3)

    if "Emma Anal Addict" in Achievements:
            pass

    elif E_Anal >= 10:
        $ E_SEXP += 7
        $ Achievements.append("Emma Anal Addict")
        if not Situation:
            call EmmaFace("bemused", 1)
            ch_e "I didn't think I'd love this so much!"
    elif E_Anal == 1:
            $E_SEXP += 25
            if not Situation:
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "Anal. . . huh, who knew?"
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Ouch."
                    ch_e "I guess you got what you needed?"
    elif E_Anal == 5:
            ch_e "I'm really starting to love this."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e  "Hmm, you seemed to get more out of that than me. . ."

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return


# End Emma Anal //////////////////////////////////////////////////////////////////////////////////



# Emma hotdog //////////////////////////////////////////////////////////////////////

label E_Missionary_H:
    $ Round -= 5 if Round > 5 else (Round-1)
    call Shift_Focus("Emma")
    if E_Hotdog >= 3: #You've done it before several times
        $ Tempmod += 10
    elif E_Hotdog: #You've done it before
        $ Tempmod += 5

    if E_Lust > 85:
        $ Tempmod += 10
    elif E_Lust > 75: #She's really horny
        $ Tempmod += 5
    if Situation == "shift":
        $ Tempmod += 10
    if "exhibitionist" in E_Traits:
        $ Tempmod += (3*Taboo)
    if "dating" in E_Traits or "sex friend" in E_Petnames:
        $ Tempmod += 10
    elif "ex" in E_Traits:
        $ Tempmod -= 40
    if E_ForcedCount and not E_Forced:
        $ Tempmod -= 5 * E_ForcedCount

    if Taboo and "tabno" in E_DailyActions:
        $ Tempmod -= 10

    if "no hotdog" in E_DailyActions:
        $ Tempmod -= 5
        $ Tempmod -= 10 if "no hotdog" in E_RecentActions else 0

    $ Approval = ApprovalCheck("Emma", 1000, TabM = 3) # 100, 115, 130, Taboo -120(220)

    if Situation == "auto":
            call Emma_Missionary_Launch("L")
            "You press Emma down onto her back and press your cock against her."
            call EmmaFace("surprised", 1)

            if (E_Hotdog and Approval) or (Approval > 1):                                                                      #this is not the first time you've had sex, or she's into it
                "Emma is briefly startled, but melts into a sly smile."
                call EmmaFace("sexy")
                call Statup("Emma", "Obed", 70, 3)
                call Statup("Emma", "Inbt", 50, 3)
                call Statup("Emma", "Inbt", 70, 1)
                ch_e "Hmm, I've apparently got someone's attention. . ."
                jump E_Missionary_HotdogPrep
            else:                                                                                                            #she's questioning it
                $ E_Brows = "angry"
                menu:
                    ch_e "Hmm, kinda rude, [E_Petname]."
                    "Sorry, sorry! Never mind.":
                        if Approval:
                            call EmmaFace("sexy", 1)
                            call Statup("Emma", "Obed", 70, 3)
                            call Statup("Emma", "Inbt", 50, 3)
                            call Statup("Emma", "Inbt", 70, 1)
                            ch_e "I guess it doesn't feel so bad. . ."
                            jump E_Missionary_HotdogPrep
                        "You pull back from her."
                        call EmmaFace("bemused", 1)
                        ch_e "Thanks, not that it's {i}so{/i} bad, just maybe ask first?"
                    "You'll see.":
                        call Statup("Emma", "Love", 80, -10, 1)
                        call Statup("Emma", "Love", 200, -8)
                        "You grind against her crotch."
                        call Statup("Emma", "Obed", 70, 3)
                        call Statup("Emma", "Inbt", 50, 3)
                        if not ApprovalCheck("Emma", 500, "O", TabM=1): #Checks if Obed is 700+
                            call EmmaFace("angry")
                            "Emma shoves you away."
                            ch_e "Jerk!"
                            ch_e "I'm not into that!"
                            call Statup("Emma", "Love", 50, -10, 1)
                            call Statup("Emma", "Obed", 50, 3)
                            $ renpy.pop_call()
                            if Situation:
                                $ renpy.pop_call()
                            call Emma_Sex_Reset
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")
                        else:
                            call EmmaFace("sad")
                            "Emma doesn't seem to be into this, but she knows her place."
                            jump E_Missionary_HotdogPrep
            return
            #end auto


    if not E_Hotdog and "no hotdog" not in E_RecentActions:
            #first time
            call EmmaFace("surprised", 1)
            $ E_Mouth = "kiss"
            ch_e "So, just grinding against me?"

            if E_Forced:
                call EmmaFace("sad")
                ch_e ". . . That's it?"


    if not E_Hotdog and Approval:
            #First time dialog
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
            elif E_Love >= (E_Obed + E_Inbt):
                call EmmaFace("sexy")
                $ E_Brows = "sad"
                $ E_Mouth = "smile"
                ch_e "It does look a bit swolen. . ."
            elif E_Obed >= E_Inbt:
                call EmmaFace("normal")
                ch_e "If you want. . ."
            elif E_Addict >= 50:
                call EmmaFace("manic", 1)
                ch_e "Hmmm. . ."
            else: # Uninhibited
                call EmmaFace("sad")
                $ E_Mouth = "smile"
                ch_e "Hmm, you look ready to go. . ."

    elif Approval:
            #Second time+ dialog
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Love", 70, -3, 1)
                call Statup("Emma", "Love", 20, -2, 1)
                ch_e "That's {i}all{/i} you want?"
            elif not Taboo and "tabno" in E_DailyActions:
                ch_e "I guess this is a better location . ."
            elif "hotdog" in E_RecentActions:
                call EmmaFace("sexy", 1)
                ch_e "Again? Ok."
                jump E_Missionary_HotdogPrep
            elif "hotdog" in E_DailyActions:
                call EmmaFace("sexy", 1)
                $ Line = renpy.random.choice(["Back again so soon?",
                    "So you'd like another round?",
                    "You're really digging this. . .",
                    "Are you sure that's all you want?"])
                ch_e "[Line]"
            else:
                call EmmaFace("sexy", 1)
                $ Emma_Arms = 2
                $ Line = renpy.random.choice(["Oooh, you want some of this?",
                    "So you'd like another round?",
                    "You're really digging this. . .",
                    "You want another rub?"])
                ch_e "[Line]"
            $ Line = 0

    if Approval >= 2:
            #She's into it. . .
            if E_Forced:
                call EmmaFace("sad")
                call Statup("Emma", "Obed", 80, 1)
                call Statup("Emma", "Inbt", 60, 1)
                ch_e "Ok, fine."
            elif "no hotdog" in E_DailyActions:
                ch_e "Well, I guess it's not so bad. . ."
            else:
                call EmmaFace("sexy", 1)
                call Statup("Emma", "Love", 80, 1)
                call Statup("Emma", "Inbt", 50, 2)
                $ Line = renpy.random.choice(["Well, sure, give it a rub.",
                    "Well. . . ok.",
                    "Sure!",
                    "I guess we could do that.",
                    "Um, yeah.",
                    "Heh, ok, ok."])
                ch_e "[Line]"
                $ Line = 0
            call Statup("Emma", "Obed", 60, 1)
            call Statup("Emma", "Inbt", 70, 2)
            jump E_Missionary_HotdogPrep

    else:
            #She's not into it, but maybe. . .
            call EmmaFace("angry")
            if "no hotdog" in E_RecentActions:
                ch_e "I{i}just{/i} told you \"no!\""
            elif Taboo and "tabno" in E_DailyActions and "no hotdog" in E_DailyActions:
                ch_e "I{i}just{/i} told, not in public!"
            elif "no hotdog" in E_DailyActions:
                ch_e "I{i}just{/i} told you \"no\" earlier!"
            elif Taboo and "tabno" in E_DailyActions:
                ch_e "I{i}just{/i} told you, not in public!"
            elif not E_Hotdog:
                call EmmaFace("bemused")
                ch_e "That's kinda hot, [E_Petname]. . ."
            else:
                call EmmaFace("bemused")
                ch_e "Not. . . now. . ."
            menu:
                extend ""
                "Sorry, never mind." if "no hotdog" in E_DailyActions:
                    call EmmaFace("bemused")
                    ch_e "No problem."
                    return
                "Maybe later?" if "no hotdog" not in E_DailyActions:
                    call EmmaFace("sexy")
                    ch_e "Yeah, maybe, [E_Petname]."
                    call Statup("Emma", "Love", 80, 1)
                    call Statup("Emma", "Inbt", 50, 1)
                    if Taboo:
                        $ E_RecentActions.append("tabno")
                        $ E_DailyActions.append("tabno")
                    $ E_RecentActions.append("no hotdog")
                    $ E_DailyActions.append("no hotdog")
                    return
                "You might like it. . .":
                    if Approval:
                        call EmmaFace("sexy")
                        call Statup("Emma", "Obed", 60, 2)
                        call Statup("Emma", "Inbt", 50, 2)
                        $ Line = renpy.random.choice(["Well, sure, ok.",
                            "I suppose. . .",
                            "That's. . . that's a good point. . ."])
                        ch_e "[Line]"
                        $ Line = 0
                        jump E_Missionary_HotdogPrep
                    else:
                        pass

                "Just deal with it.":                                               # Pressured into it
                    $ Approval = ApprovalCheck("Emma", 350, "OI", TabM = 3) # 35, 50, 65, -120(155)
                    if Approval > 1 or (Approval and E_Forced):
                        call EmmaFace("sad")
                        call Statup("Emma", "Love", 70, -2, 1)
                        call Statup("Emma", "Love", 200, -2)
                        ch_e "Ok, fine. Whatever."
                        call Statup("Emma", "Obed", 80, 4)
                        call Statup("Emma", "Inbt", 60, 2)
                        $ E_Forced = 1
                        jump E_Missionary_HotdogPrep
                    else:
                        call Statup("Emma", "Love", 200, -10)
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")

    #She refused all offers.
    $ Emma_Arms = 1

    if "no hotdog" in E_DailyActions:
        ch_e "I'm just not into that."
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")
    if E_Forced:
        call EmmaFace("angry", 1)
        ch_e "Yeah, not happening."
        call Statup("Emma", "Lust", 200, 5)
        if E_Love > 300:
                call Statup("Emma", "Love", 70, -1)
        call Statup("Emma", "Obed", 50, -1)
        $ E_RecentActions.append("angry")
        $ E_DailyActions.append("angry")
    elif Taboo:                             # she refuses and this is too public a place for her
        call EmmaFace("angry", 1)
        $ E_RecentActions.append("tabno")
        $ E_DailyActions.append("tabno")
        ch_e " not here though?"
        call Statup("Emma", "Lust", 200, 5)
        call Statup("Emma", "Obed", 50, -3)
    elif E_Hotdog:
        call EmmaFace("sad")
        ch_e "Yeah, not again."
    else:
        call EmmaFace("normal", 1)
        ch_e "Noooope."
    $ E_RecentActions.append("no hotdog")
    $ E_DailyActions.append("no hotdog")
    $ Tempmod = 0
    return

label E_Missionary_HotdogPrep:
    call Seen_First_Peen("Emma",Partner,React=Situation)
    call Emma_Missionary_Launch("hotdog")


    if Situation == "Emma":
            #Emma auto-starts
            $ Situation = 0
            "Emma rolls back and pulls you toward her, rubbing her pussy against your cock."
            menu:
                "What do you do?"
                "Go with it.":
                    call Statup("Emma", "Inbt", 80, 3)
                    call Statup("Emma", "Inbt", 50, 2)
                    "Emma keeps grinding."
                "Praise her.":
                    call EmmaFace("sexy", 1)
                    call Statup("Emma", "Inbt", 80, 3)
                    ch_p "Oh yeah, [E_Pet], let's do this."
                    call Emma_Namecheck
                    "Emma keeps grinding."
                    call Statup("Emma", "Love", 85, 1)
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 2)
                "Ask her to stop.":
                    call EmmaFace("surprised")
                    call Statup("Emma", "Inbt", 70, 1)
                    ch_p "Let's not do that right now, [E_Pet]."
                    call Emma_Namecheck
                    "Emma pulls back."
                    call Statup("Emma", "Obed", 90, 1)
                    call Statup("Emma", "Obed", 50, 1)
                    call Statup("Emma", "Obed", 30, 2)
                    $ P_RecentActions.append("nope")
                    call AnyWord("Emma",1,"refused","refused")
                    return
    elif Situation != "auto":
#        call Emma_Bottoms_Off

        if Taboo: # Emma gets started. . .
            if E_Hotdog:
                "Emma glances around to see if anyone notices what she's doing, then presses firmly against your cock."

            else:
                "Emma glances around for voyeurs. . ."
                if "cockout" in P_RecentActions:
                    "Emma slowly presses against your rigid member."
                else:
                    "Emma hesitantly pulls down your pants and slowly presses against your rigid member."
            $ E_Inbt += int(Taboo/10)
            $ E_Lust += int(Taboo/5)
        else:
            if "cockout" in P_RecentActions:
                "Emma slowly presses against your rigid member."
            else:
                "Emma hesitantly pulls down your pants slowly presses against your rigid member."

    else: #if Situation == "auto"
        "You press yourself against her mound."

    if not E_Hotdog:                                                      #First time stat buffs
        if E_Forced:
            call Statup("Emma", "Love", 90, -5)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 10)
        else:
            call Statup("Emma", "Love", 90, 20)
            call Statup("Emma", "Obed", 70, 20)
            call Statup("Emma", "Inbt", 80, 20)


    if Situation:
        $ renpy.pop_call()
        $ Situation = 0
    $ Line = 0
    $ Cnt = 0
    $ Trigger = "hotdog"
    $ Speed = 1
    if Taboo:
        call DrainWord("Emma","tabno")
    call DrainWord("Emma","no hotdog")
    $ E_RecentActions.append("hotdog")
    $ E_DailyActions.append("hotdog")

label E_Missionary_Hotdog_Cycle: #Repeating strokes
    while Round >=0:
        call Shift_Focus("Emma")
        call Emma_Missionary_Launch("hotdog")
        call EmmaLust
        $ P_Cock = "out"
        $ Trigger = "hotdog"

        if  P_Focus < 100:
                    #Player Command menu
                    menu:
                        "Keep going. . ." if Speed:
                                    pass
                        "Keep going. . . (locked)" if not Speed:
                                    pass

                        "Start moving? . ." if not Speed:
                                    $ Speed = 1
                        "Speed up. . ." if 0 < Speed < 3:
                                    $ Speed += 1
                                    "You ask her to up the pace a bit."
                        "Speed up. . . (locked)" if Speed >= 3:
                                    pass

                        "Slow Down. . ." if Speed:
                                    $ Speed -= 1
                                    "You ask her to slow it down a bit."
                        "Slow Down. . . (locked)" if not Speed:
                                    pass

                        "Slap her ass":
                                    call E_Slap_Ass
                                    $ Cnt += 1
                                    $ Round -= 1
                                    jump E_Missionary_Hotdog_Cycle

                        "Focus to last longer [[not unlocked]. (locked)" if "focus" not in P_Traits:
                                    pass
                        "Focus to last longer." if not P_FocusX and "focus" in P_Traits:
                                    "You concentrate on not burning out too quickly."
                                    $ P_FocusX = 1
                        "Release your focus." if P_FocusX:
                                    "You release your concentration. . ."
                                    $ P_FocusX = 0

                        "Other options":
                                menu:
                                    "Offhand action":
                                            if E_Action and MultiAction:
                                                call Emma_Offhand_Set
                                                if Trigger2:
                                                     $ E_Action -= 1
                                            else:
                                                ch_e "I'm kinda tired here? Could we wrap it up?"

                                    "Shift primary action":
                                            if E_Action and MultiAction:
                                                    menu:
                                                        "How about sex?":
                                                            $ Situation = "shift"
                                                            call E_Missionary_HotdogAfter
                                                            call E_Missionary_P
                                                        "Just stick it in her pussy [[without asking].":
                                                            $ Situation = "auto"
                                                            call E_Missionary_HotdogAfter
                                                            call E_Missionary_P
                                                        "How about anal?":
                                                            $ Situation = "shift"
                                                            call E_Missionary_HotdogAfter
                                                            call E_Missionary_A
                                                        "Just stick it in her ass [[without asking].":
                                                            $ Situation = "auto"
                                                            call E_Missionary_HotdogAfter
                                                            call E_Missionary_A
                                                        "Never Mind":
                                                                jump E_Missionary_Hotdog_Cycle
                                            else:
                                                ch_e "I'm kinda tired here? Could we wrap it up?"
                                    "Threesome actions (locked)" if not Partner:
                                        pass
                                    "Threesome actions" if Partner:
                                        menu:
                                            "Ask Emma to do something else with [Partner]" if Trigger == "lesbian":
                                                        call Emma_Les_Change
                                            "Ask Emma to do something else with [Partner] (locked)" if Trigger != "lesbian":
                                                        pass
                                            "Ask [Partner] to do something else":
                                                        call Partner_Threechange("Emma")

                                            "Don't stop what you're doing. . .(locked)" if not ThreeCount or not Trigger4:
                                                        $ ThreeCount = 0
                                            "Don't stop what you're doing. . ." if ThreeCount and Trigger4:
                                                        $ ThreeCount = 0

                                            "Swap to [Partner]":
                                                        call Trigger_Swap("Emma")
                                            "Undress [Partner]":
                                                        call Partner_Undress
                                                        jump E_Missionary_Hotdog_Cycle
                                            "Clean up Partner":
                                                        call Partner_Cleanup
                                                        jump E_Missionary_Hotdog_Cycle
                                            "Never mind":
                                                        jump E_Missionary_Hotdog_Cycle
                                    "Undress Emma":
                                            call E_Undress
                                    "Clean up Emma (locked)" if not E_Spunk:
                                            pass
                                    "Clean up Emma" if E_Spunk:
                                            call Emma_Cleanup("ask")
                                    "Never mind":
                                            jump E_Missionary_Hotdog_Cycle

                        "Back to Sex Menu" if MultiAction:
                                    ch_p "Let's try something else."
                                    call Emma_Sex_Reset
                                    $ Situation = "shift"
                                    $ Line = 0
                                    jump E_Missionary_HotdogAfter
                        "End Scene" if not MultiAction:
                                    ch_p "Let's stop for now."
                                    call Emma_Sex_Reset
                                    $ Line = 0
                                    jump E_Missionary_HotdogAfter
        #End menu (if Line)

        call Shift_Focus("Emma")
        call Sex_Dialog("Emma",Partner)

        $ Cnt += 1
        $ Round -= 1

        $ P_Focus = 50 if not P_Semen and P_Focus >= 50 else P_Focus #Resets P_Focus if can't get it up
        if P_Focus >= 100 or E_Lust >= 100:
                    #If either of you could cum
                    if P_Focus >= 100:
                            #If you can cum:
                            call PE_Cumming
                            if "angry" in E_RecentActions:
                                call Emma_Sex_Reset
                                return
                            call Statup("Emma", "Lust", 200, 5)
                            if 100 > E_Lust >= 70 and E_OCount < 2:
                                $ E_RecentActions.append("unsatisfied")
                                $ E_DailyActions.append("unsatisfied")

                            if P_Focus > 80:
                                jump E_Missionary_HotdogAfter
                            $ Line = "came"

                    if E_Lust >= 100:
                            #If you're still going at it and Emma can cum
                            call E_Cumming
                            if Situation == "shift" or "angry" in E_RecentActions:
                                jump E_Missionary_HotdogAfter

                    if Line == "came": #ex P_Focus <= 20:
                            #If you've just cum,
                            $ Line = 0
                            if not P_Semen:
                                "She's emptied you out, you'll need to take a break."
                                jump E_Missionary_HotdogAfter
                            elif "unsatisfied" in E_RecentActions:
                                #And Emma is unsatisfied,
                                $ Line = renpy.random.choice(["She continues to shake a little with pleasure.",
                                    "She is breathing heavily as your cock rubs inside her.",
                                    "She slowly turns back towards you and smiles.",
                                    "She doesn't seem ready to stop."])
                                "[Line] Keep going?"
                                menu:
                                    extend ""
                                    "Yes, keep going for a bit." if P_Semen:
                                        $ Line = "You get back into it"
                                        jump E_Missionary_Hotdog_Cycle
                                    "No, I'm done." if P_Semen:
                                        "You pull back."
                                        jump E_Missionary_HotdogAfter
                                    "No, I'm spent." if not P_Semen:
                                        "You pull back."
                                        jump E_Missionary_HotdogAfter
        if Partner:
                #Checks if partner could orgasm
                call Partner_Cumming("Emma")
        #End orgasm

        $ P_Focus -= 12 if P_FocusX and P_Focus > 50 else 0

        if E_SEXP >= 100 or ApprovalCheck("Emma", 1200, "LO"):
            pass
        elif Cnt == (5 + E_Hotdog):
                    $ E_Brows = "confused"
                    ch_e "Are you getting close here?"
        elif Cnt == (10 + E_Hotdog):
                    $ E_Brows = "angry"
                    menu:
                        ch_e "This is getting a bit dull."
                        "How about a BJ?" if E_Action and MultiAction:
                                $ Situation = "shift"
                                call E_Missionary_HotdogAfter
                                call E_Blowjob
                        "Finish up." if P_FocusX:
                                "You release your concentration. . ."
                                $ P_FocusX = 0
                                $ P_Focus += 15
                                $ Cnt += 1
                                jump E_Missionary_Hotdog_Cycle
                        "Let's try something else." if MultiAction:
                                $ Line = 0
                                call Emma_Sex_Reset
                                $ Situation = "shift"
                                jump E_Missionary_HotdogAfter
                        "No, get back down there.":
                                if ApprovalCheck("Emma", 1200) or ApprovalCheck("Emma", 500, "O"):
                                    call Statup("Emma", "Love", 200, -5)
                                    call Statup("Emma", "Obed", 50, 3)
                                    call Statup("Emma", "Obed", 80, 2)
                                    "She grumbles but keeps moving."
                                else:
                                    call EmmaFace("angry", 1)
                                    call Emma_Sex_Reset
                                    "She scowls at you and pulls away."
                                    ch_e "Not with that attitude, mister!"
                                    call Statup("Emma", "Love", 50, -3, 1)
                                    call Statup("Emma", "Love", 80, -4, 1)
                                    call Statup("Emma", "Obed", 30, -1, 1)
                                    call Statup("Emma", "Obed", 50, -1, 1)
                                    $ E_RecentActions.append("angry")
                                    $ E_DailyActions.append("angry")
                                    jump E_Missionary_HotdogAfter
        #End Count check

        call Escalation("Emma","K") #sees if she wants to escalate things

        if Round == 10:
            ch_e "You might want to wrap this up, it's getting late."
        elif Round == 5:
            ch_e "Seriously, it'll be time to stop soon."

    #Round = 0 loop breaks
    call EmmaFace("bemused", 0)
    $ Line = 0
    ch_e "Ok, [E_Petname], that's enough of that for now."

label E_Missionary_HotdogAfter:
    if not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        $ P_Sprite = 0
        $ P_Cock = "out"
        call Emma_Sex_Reset

    call EmmaFace("sexy")

    $ E_Hotdog += 1
    $ E_Action -=1
    $ E_Addictionrate += 1
    if "addictive" in P_Traits:
        $ E_Addictionrate += 1
    call Statup("Emma", "Inbt", 30, 1)
    call Statup("Emma", "Inbt", 70, 1)

    call Partner_Like("Emma",2)

    if E_Hotdog == 10:
        $ E_SEXP += 5
    elif E_Hotdog == 1:
            $E_SEXP += 10
            if not Situation:
                if E_Love >= 500 and "unsatisfied" not in E_RecentActions:
                    ch_e "I. . . liked that a lot."
                elif E_Obed <= 500 and P_Focus <= 20:
                    $ E_Mouth = "sad"
                    ch_e "Well, did that work for you?"
    elif E_Hotdog == 5:
            ch_e "I'm surprised how much I enjoy this."
    elif not Situation: #fix  Situation != "shift" and Situation != "auto" and Situation != "pullback":
        if "unsatisfied" in E_RecentActions:
            call EmmaFace("angry")
            $ E_Eyes = "side"
            ch_e "I didn't get much out of that. . ."

    $ Tempmod = 0
#    if Situation == "shift":
#        ch_e "Mmm, so what else did you have in mind?"
    call Checkout
    return

# End Emma hotdogging //////////////////////////////////////////////////////////////////////////////////
