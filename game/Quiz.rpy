﻿
# Start Main Phase / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Group_Strip_Study(BO=[],QuizOrder=[]):    
    $ Count = 0
    $ Count2 = 1
    $ QuizOrder = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  # The entire list of objects. . .
    $ renpy.random.shuffle(QuizOrder)  # . . .shuffled randomly. . .
    if EmmaX in Party and Party[0] != EmmaX: 
            # Forces Emma into the lead
            $ Party.reverse()
            call Shift_Focus(Party[0])
          
    # intros
    if Party[0] == RogueX:
            if not RogueX.Over and not RogueX.Legs and RogueX.PantiesNum <= 5:
                    #if she's mostly naked, cheat
                    $ RogueX.FaceChange("sly")                                
                    ch_r "Well, I did consider suggesting we do some \"strip studying,\". . ." 
                    $ RogueX.Eyes = "down"
                    ch_r "but it looks like I got ahead of myself. . ."
                    $ RogueX.Eyes = "squint"
                    ch_r "Did you have anything else in mind?"                                
                    call Rogue_SexMenu 
                    return
            else:
                    "[RogueX.Name] moves a bit closer to you, and then suggests \"strip studying.\""
            ch_r "Alright, [RogueX.Petname], I'll make this simple. I'll ask you a quiz question, get it right, I take something off. . ."
            ch_r "Get three wrong, and we're done for the night. Good luck."
    elif Party[0] == KittyX: 
            "[KittyX.Name] takes the book from your hand, and sets it aside."
            if not KittyX.Over and not KittyX.Legs:
                    #if she's mostly naked, cheat
                    $ KittyX.FaceChange("sly")                                
                    ch_k "I was[KittyX.like]thinking about maybe \"strip studying,\". . ." 
                    $ KittyX.Eyes = "down"
                    ch_k "but it would be a pretty short game. . ."
                    $ KittyX.Eyes = "squint"
                    ch_k "Was there something you'd rather do?"                                
                    call Kitty_SexMenu   
            else:
                    "She then asks if maybe you want to do some \"strip studying?\""
            $ KittyX.FaceChange("perplexed", 2)
            ch_k "Ok, so[KittyX.like]if you get a question right. . . I'll take off a piece of clothing. . ."
            ch_k "But you only get three tries." 
            $ KittyX.FaceChange("sly", 1)
    elif Party[0] == EmmaX:    
            call Emma_StripStudy_Intro #special intro for Emma. . .
            if not _return:
                    #if you aren't on board, it reverts to the previous scene
                    return
            ch_e "I take the education process very seriously."    
            $ EmmaX.FaceChange("bemused", Eyes="side")
            ch_e "So you get a question right. . . "
            ch_e ". . ."
            $ EmmaX.FaceChange("sly")
            ch_e "I'll take off a piece of clothing. . ."
            ch_e "But you only get three tries." 
    elif Party[0] == LauraX:
            #Laura does not do Strip Study solo, she's not interested.
            $ LauraX.FaceChange("sly", 1)
            "[LauraX.Name] takes the book from your hand, and sets it aside."
            ch_l "I'm kinda bored, did you just wanna feel me up or something?"
            menu:
                "Sure?":
                        ch_l "Good."
                        "Laura grabs your hand and presses it against her breast."
                        call Date_Sex_Break(LauraX,Second)
                        if _return == 4:                            
                                "Laura stops what she's doing."
                                ch_l "Be that way."     
                                return                                    
                        if _return == 3:
                                #if the other girl took off. . .
                                menu:
                                    ch_l "Keep going?"
                                    "Go ahead.":
                                            ch_l "Un."
                                    "We should stop.":
                                            ch_l "Grr."
                                            return    
                        call Laura_FB_Prep
                        if Situation: 
                                #if she quits back having wanted to try something else. . .
                                jump Laura_SexMenu
                "I really think we should be studying.":            
                        $ LauraX.FaceChange("perplexed", 1)
                        ch_l "?"           
                        $ LauraX.Statup("Love", 80, -5)
                        $ LauraX.Statup("Obed", 70, 10)
                        $ LauraX.Statup("Inbt", 70, -5)
                        if ApprovalCheck(LauraX,600,"L"): 
                                $ LauraX.FaceChange("sadside", 1)
                        else:
                                $ LauraX.FaceChange("angry", 1)                
                        ch_l "Huh. Ok. Be that way."            
            return
    # end Intro
    
    $ BO = Party[:]
    while BO:            
            $ BO[0].AddWord(1,0,"stripstudy",0,"stripstudy") #adds to Daily and History
            $ BO.remove(BO[0])
            
    if len(Party) >= 2:
            if Cnt == 3:
                    #if from the Emma menu she didn't agree to participate. . .
                    pass
            elif ApprovalCheck(Party[1], 1300) or ApprovalCheck(Party[1], 500,"I"):
                    if Party[1] == RogueX:
                            ch_r "I guess we'll take turns."
                    elif Party[1] == KittyX: 
                            ch_k "So[KittyX.like]I guess we take turns?" 
                    elif Party[1] == EmmaX:    
                            "Let Oni know that Emma was in second please." 
                    elif Party[1] == LauraX:
                            ch_l "I will also take a turn."
            else:
                    #she refuses            
                    if Party[1] == RogueX:
                            ch_r "I'm not comfortable with this."
                    elif Party[1] == KittyX: 
                            ch_k "Um, I'm not really into this?" 
                    elif Party[1] == EmmaX:    
                            "Let Oni know that Emma was in second please." 
                    elif Party[1] == LauraX:
                            ch_l "I don't think so."
                    "[Party[1].Name] leaves the room"
                    call Remove_Girl(Party[1])
    
    #Primary loop
    while Count2:        
            #"Question [Count2]. . ."
            call expression Party[0].Tag + "_Quiz_Question"
                                      
            $ Count2 += 1
            
            if _return:            
                    call Strip_Study_Right
            else:
                    $ Count += 1
                    call Strip_Study_Wrong   
                    if Count2 == 0 and len(Party) >= 2 and not Party[1].ClothingCheck:
                            #if you failed out, but the other girl is nude. . .
                            menu:
                                "Well, [Party[1].Name], you and I could still have some fun. . .":
                                        $ Tempmod = 50
                                        call expression Party[0].Tag + "_SexMenu"
                                "Bummer":
                                        pass
                
            if len(Party) >= 2 and Cnt != 3 and not Party[1].ClothingCheck:
                    #if there are multiple girls, and the other girl is not nude, alternate        
                    $ Party.reverse()
                    call Shift_Focus(Party[0])            
    #Loop ends when Count2 is 0 due to failures, returns to sender
    
    return

# End Main Phase / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start "Question right" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Strip_Study_Right:
        if Party[0].Hose: 
                # Will she lose the hose?
                $ Line = Party[0].Hose           
                $ Party[0].Hose = 0
                "She slowly removes her [Line]. . ."
                $ Party[0].Statup("Lust", 50, 3)
                return    
            
        if Party[0].Over: 
            #will she lose the top?
            if Party[0].SeenChest or (Party[0].Chest and ApprovalCheck(Party[0], 300)) or ApprovalCheck(Party[0], 850):
                $ Party[0].Statup("Inbt", 25, 1)
                $ Party[0].Statup("Inbt", 50, 1)
                $ Line = Party[0].Over           
                $ Party[0].Over = 0
                "She pulls her [Line] off and throws it aside."   
                if not Party[0].Chest:                            
                    call expression Party[0].Tag + "_First_Topless"              
            else:
                if Party[0] == RogueX:
                        ch_r "You know, I don't really think I'm ready for this, sorry [Party[0].Petname]. I shouldn't have led you on."             
                elif Party[0] == KittyX:
                        ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."  
                elif Party[0] == EmmaX:
                        ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."  
                elif Party[0] == LauraX:
                        $ LauraX.FaceChange("sly", 2)
                        ch_l "Heh, got you going, right?."  
                        $ LauraX.FaceChange("bemused", 1)
                $ Count2 = 0
            return   
            
        if Party[0].Legs:   
            #will she lose the pants/skirt?
            if (Party[0].SeenPanties and Party[0].SeenPussy) or (Party[0].Panties and (ApprovalCheck(Party[0], 700) or Party[0].SeenPanties)) or ApprovalCheck(Party[0], 950):  
                    $ Party[0].Statup("Lust", 50, 5)
                    $ Party[0].Statup("Inbt", 30, 1)
                    $ Party[0].Statup("Inbt", 50, 1)
                    $ Line = Party[0].Legs           
                    $ Party[0].Legs = 0
                    "She unfastens her [Line] and slides them down her legs." 
                    if Party[0].Panties:
                        if not Party[0].SeenPanties:   
                                $ Party[0].Statup("Inbt", 200, 2)
                                $ Party[0].Statup("Inbt", 50, 3)  
                                $ Party[0].SeenPanties = 1
                    else:
                        #R seen pussy
                        $ Party[0].Blush = 1
                        "You notice that she apparently isn't wearing any panties, and she flushes a bit."
                        call expression Party[0].Tag + "_First_Bottomless"
            else:
                    if Party[0] == RogueX:    
                            ch_r "You know, I don't really think I'm ready for this, sorry [Party[0].Petname]. I shouldn't have led you on."         
                    elif Party[0] == KittyX:
                            ch_k "Sorry,I don't mean to be a tease, but I just can't handle this yet."  
                    elif Party[0] == EmmaX:
                            ch_e "Sorry, I don't mean to be a tease, but I doubt you can handle this yet."  
                    elif Party[0] == LauraX:                    
                            ch_l "Nah, that's all for now." 
                    $ Count2 = 0
            return     
        
        if Party[0].Chest: # Will she go topless?
            if ApprovalCheck(Party[0], 900) or (Party[0].SeenChest and ApprovalCheck(Party[0], 600)):
                    $ Party[0].Statup("Lust", 60, 5)
                    $ Party[0].Statup("Inbt", 50, 2)
                    $ Party[0].Statup("Inbt", 200, 1)
                    $ Line = Party[0].Chest           
                    $ Party[0].Chest = 0
                    "She pulls her [Line] over her head and tosses it aside."  
                    if not Party[0].SeenChest:   
                            $ Party[0].Statup("Inbt", 200, 3)
                            $ Party[0].Statup("Inbt", 50, 1)  
                            call expression Party[0].Tag + "_First_Topless"
                    $ Player.Statup("Focus", 80, 15)
            else:
                    if Party[0] == RogueX:       
                            ch_r "I know a deal's a deal, but I'd like to keep my top on, ok [Party[0].Petname]? Sorry about that."      
                    elif Party[0] == KittyX:
                            ch_k "So. . . I know this is a bit late to mention it, but I'd like to keep my top on?"
                    elif Party[0] == EmmaX:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "Hmm. . . better than I thought." 
                            $ EmmaX.FaceChange("sly", 1)
                            ch_e "But I doubt you're ready for this yet."
                    elif Party[0] == LauraX:
                             ch_l "Yeah, that's enough for now."
                    $ Count2 = 0
            return  
                
        if Party[0].Panties: # Will she go bottomless?
            if ApprovalCheck(Party[0], 950) or (Party[0].SeenPussy and ApprovalCheck(Party[0], 600)):    
                    $ Party[0].Statup("Lust", 70, 10)
                    $ Party[0].Statup("Inbt", 70, 2)
                    $ Party[0].Statup("Inbt", 200, 2)    
                    $ Line = Party[0].Panties           
                    $ Party[0].Panties = 0
                    "She slides her [Line] off, leaving her pussy bare."    
                    if not Party[0].SeenPussy:
                            $ Party[0].Statup("Inbt", 50, 4)
                            $ Party[0].Statup("Inbt", 200, 4)
                            call expression Party[0].Tag + "_First_Bottomless"
                    $ Player.Statup("Focus", 75, 20)
            else:
                    if Party[0] == RogueX:   
                            ch_r "Look, this has gone a bit far, [Party[0].Petname]. I'd like to call it a night."          
                    elif Party[0] == KittyX:
                            ch_k "Wow, I. . . I'm not really ready for this sort of thing, I'm sorry!"
                    elif Party[0] == EmmaX:
                            $ EmmaX.FaceChange("perplexed", 1)
                            ch_e "Hmm. . . better than I thought." 
                            $ EmmaX.FaceChange("sly", 1)
                            ch_e "But I doubt you're ready for this yet."
                    elif Party[0] == LauraX:             
                            $ LauraX.FaceChange("perplexed", 2)
                            ch_l "I think you've had enough."
                            $ LauraX.FaceChange("perplexed", 1)
                    $ Count2 = 0
            return  
                
        if Party[0] == RogueX:          
                $ KittyX.FaceChange("sly", 1)    
                ch_r "Well, that's another right answer, but I don't have a stitch left to take off. . ."    
        elif Party[0] == KittyX:
                ch_k "So. . . you got that one right. . ."
                $ KittyX.Eyes = "down"
                ch_k ". . . but I'm not[KittyX.like]wearing anything else. . ."        
                $ KittyX.FaceChange("sly", 1)
        elif Party[0] == EmmaX:
                $ EmmaX.FaceChange("sly", 1)
                ch_e "Hmm. . . another correct answer. . ."
                $ EmmaX.Eyes = "down"
                ch_e ". . . but I don't have anything else to remove. . ."     
                $ EmmaX.FaceChange("sly", 1)
        elif Party[0] == LauraX:
                $ LauraX.FaceChange("sly", 1)
                ch_l "So. . . you got that one right. . ."
                $ LauraX.Eyes = "down"
                ch_l ". . . but it looks like I'm out of clothes. . ."     
                $ LauraX.FaceChange("sly", 1)
        if len(Party) >= 2:
                menu:
                    "Well I could think of something else you could do. . .":
                            pass
                    "It looks like [Party[1].Name] has some questions for me. . ." if Party[1].ClothingCheck: 
                            #if the other girl has anything on. . .
                            return
        $ Count2 = 0
        $ Tempmod = 50
        call expression Party[0].Tag + "_SexMenu"
        if Party[0] == RogueX:    
                ch_r "Well I sure enjoyed that."         
        elif Party[0] == KittyX:
                ch_k "I think I learned a few things there. . ."
        elif Party[0] == EmmaX:
                ch_e "I hope you picked up a few things. . ."
        elif Party[0] == LauraX:
                ch_l "Well, better than studying. . ."
        $ Count2 = 0
        return
# End "Question right" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
      
            
# Start "Question wrong" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Strip_Study_Wrong:
        $ Party[0].FaceChange("sly", 1)
        if Count == 1:        
                if Party[0] == RogueX:
                        ch_r "Bzzt, too bad, [RogueX.Petname]."
                elif Party[0] == KittyX:
                        ch_k "Nope."
                elif Party[0] == EmmaX:    
                        ch_e "Unfortunately. . . no."
                elif Party[0] == LauraX:
                        ch_l "What?"
        elif Count == 2:
                if Party[0] == RogueX:
                        ch_r "Oh, you're really not good at this. Come on, you've only got one more shot."
                elif Party[0] == KittyX:
                        ch_k "{i}So{/i} close. One more try."
                elif Party[0] == EmmaX:    
                        ch_e "I'm afraid not, one more try."
                elif Party[0] == LauraX:
                        ch_l ". . . how did you even. . ."
        elif Count > 2:
                if Party[0] == RogueX:
                        ch_r "And you are out of here! Sorry, [RogueX.Petname], thanks for playing, you're done."
                elif Party[0] == KittyX:
                        ch_k "Aw, too bad, so sad. Maybe next time."
                elif Party[0] == EmmaX:    
                        ch_e "Pity, I expected better of you."
                elif Party[0] == LauraX:
                        ch_l "What? Fuck this."
                $ Count2 = 0
        return
    
# End "Question wrong" / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_Quiz_Question:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_r "Who was the first person who I used my powers on?"
            "A. Colby":
                return 0
            "B. Renly":
                return 0
            "C. Remy":
                return 0
            "D. Cody":
                return 1
    if QuizOrder[Count2] == 2:
        menu:
            ch_r "Where did I live before moving to Xaviers?"
            "A. Lousiana":
                return 0
            "B. Mississippi":
                return 1
            "C. Connecticut":
                return 0
            "D. Tennessee":
                return 0
    if QuizOrder[Count2] == 3:
        menu:
            ch_r "What was the first power I. . . borrowed?"
            "A. Mystique's shape shifting":
                return 0
            "B. Shadowcat's phasing":
                return 0
            "C. Nightcrawler's teleport":
                return 1
            "D. Cyclops's eyebeams":
                return 0
    if QuizOrder[Count2] == 4:
        menu:
            ch_r "What mutant raised me as my parent before my powers manifested."
            "A. Magneto":
                return 0
            "B. Mystique":
                return 1
            "C. Xavier":
                return 0
            "D. Belasco":
                return 0
    if QuizOrder[Count2] == 5:
        menu:
            ch_r "I eventually joined the X-Men after Mystique attacked me, where?"
            "A. At school":
                return 0
            "B. At the beach":
                return 0
            "C. In the mountains":
                return 1
            "D. In the bayou":
                return 0
    if QuizOrder[Count2] == 6:
        menu:
            ch_r "When Magneto was selecting the fittest mutants for Asteroid M, I was captured after beating which member of the Brotherhood?"
            "A. Blob":
                return 0
            "B. Avalanche":
                return 0
            "C. Toad":
                "That's right, [RogueX.Petname], I slammed that frog tongue in a car door"
                "Better not make me angry."
                return 1
            "D. Quicksilver":
                return 0
                
    #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1


# Kitty Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
label Kitty_Quiz_Question:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_k "Ok, do you[KittyX.like]know where I come from? What's my home town?"
            "A. Chicago, Illinois": 
                return 0 
            "B. Deerfield, Illinois": 
                return 1 
            "C. New York City, New York":        
                return 0 
            "D. St. Louis, Missouri": 
                return 0 
    if QuizOrder[Count2] == 2:          
        menu: 
            ch_k "What's my mutant power called?"
            "A. Disappearing": 
                return 0 
            "B. Ghosting": 
                return 0 
            "C. Phasing": 
                return 1 
            "D. Shifting": 
                return 0 
    if QuizOrder[Count2] == 3: 
        ch_k "So. . . don't laugh, but I have this stuffed animal I sleep with[KittyX.like]every night."
        menu:
            ch_k "Know his name?"
            "A. Draco": 
                return 0 
            "B. Flipper": 
                return 0 
            "C. Lockheed": 
                return 1 
            "D. N'gari": 
                return 0 
                    
    if QuizOrder[Count2] == 4: 
        ch_k "Okay. Did you know that Dr. McCoy takes a handful of students on a private tutoring retreat?"
        menu:                
            ch_k "Know where he takes them?"
            "A. The Great Redwood Forest, California": 
                return 1 
            "B. Mount McKinley, Alaska": 
                return 0 
            "C. Mount Rushmore, South Dakota": 
                return 0 
            "D. Yellowstone National Park, Wyoming": 
                return 0 
    if QuizOrder[Count2] == 5: 
        ch_k "One of the worst threats we have to worry about as mutants are the giant robots called Sentinels."
        menu:
            ch_k "Do you know who built them?"
            "A. Arcade": 
                return 0 
            "B. Bolivar Trask": 
                return 1 
            "C. Magneto": 
                return 0 
            "D. Unus the Untouchable": 
                return 0 
    if QuizOrder[Count2] == 6: 
        ch_k "Y'know, we didn't always have classes here at the Institute." 
        ch_k "For a while, all the students here went to a local public school." 
        menu:
            ch_k "Know which one?" 
            "A. Bayville High School": 
                return 1 
            "B. King Memorial High School":
                return 0 
            "C. Riverside High School": 
                return 0 
            "D. Seth Paine High School": 
                return 0 
    if QuizOrder[Count2] == 7: 
        menu:
            ch_k "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
            "A. Jean Grey": 
                return 0 
            "B. Lance Alvers": 
                return 1 
            "C. Mystique": 
                return 0 
            "D. Professor Xavier": 
                return 0 
    if QuizOrder[Count2] == 8: 
        ch_k "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation." 
        ch_k "Even though it was a lot of fun, we ended up disbanding after that." 
        menu:
            ch_k "Anyway, know what the name we chose for the group was?"
            "A. The Bayville Avengers": 
                return 0 
            "B. The Bayville Brawlers": 
                return 0 
            "C. The Bayville Harpies": 
                return 0 
            "D. The Bayville Sirens": 
                return 1 
    if QuizOrder[Count2] == 9: 
        menu:
            ch_k "Okay[KittyX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
            "A. A hot shower": 
                return 0 
            "B. Methyl Ethyl Ketone": 
                return 0 
            "C. Isolation": 
                return 1 
            "D. Tomato Juice": 
                return 0 
    if QuizOrder[Count2] == 10: 
        ch_k "When I'm using my powers, I'm not[KittyX.like]{i}totally{/i} invulnerable."
        menu:
            ch_k "Who has powers that can still affect me?"
            "A. Blob": 
                return 0 
            "B. Magneto": 
                return 0 
            "C. Quicksilver": 
                return 0 
            "D. Scarlet Witch": 
                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1
    
# Emma Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_Quiz_Question:   
    ch_e "Question [Count2]. . ." 
    if QuizOrder[Count2] == 1:
        menu:
            ch_e "So, do you know where I lived as a child?"
            "A. Manchester, England": 
                return 0 
            "B. New York City, New York":        
                return 0 
            "C. Boston, Massachusetts": 
                return 1 
            "D. London, England": 
                return 0 
    if QuizOrder[Count2] == 2:          
        menu: 
            ch_e "What's my mutant power?"
            "A. Telekinesis": 
                return 0 
            "B. Ice Powers": 
                return 0 
            "C. Telepathy": 
                return 1 
            "D. Baking": 
                return 0 
    if QuizOrder[Count2] == 3: 
        ch_e "I was once a leader in a. . . social club."
        menu:
            ch_e "What was the name of that club?"
            "A. Akatsuki": 
                return 0 
            "B. The Pride": 
                return 0 
            "C. The Hellfire Club": 
                return 1 
            "D. The Sinister Six": 
                return 0 
                    
    if QuizOrder[Count2] == 4: 
        ch_e "I was once a leader in a. . . social club."
        menu:                
            ch_e "What was my title in that organization?"
            "A. The Black Queen": 
                return 0 
            "B. The White Queen": 
                return 1 
            "C. The Red Queen": 
                return 0 
            "D. Princess Powerful": 
                return 0 
    if QuizOrder[Count2] == 5: 
        ch_e "I have some clones wandering around. . . somewhere."
        menu:
            ch_e "What are they called?"
            "A. Kagebunshin": 
                return 0 
            "B. The Stepford Cuckoos": 
                return 1 
            "C. Jamie Maddrox": 
                return 0 
            "D. The Spice Girls": 
                return 0 
    if QuizOrder[Count2] == 6: 
        menu:
            ch_e "What is it called when a mutant develops a new ability, unrelated to their original one?" 
            "A. Secondary Mutation": 
                return 1 
            "B. Level-Up":
                return 0 
            "C. Digivolution": 
                return 0 
            "D. Super-Mutant": 
                return 0 
    if QuizOrder[Count2] == 7: 
        ch_e "I used to teach on an island nation of all mutants."
        menu:
            ch_e "What was it called?"
            "A. Australia": 
                return 0 
            "B. Genosha": 
                return 1 
            "C. Martinique": 
                return 0 
            "D. Whole Cake Island": 
                return 0 
    if QuizOrder[Count2] == 8: 
        menu:
            ch_e "When we first met, how did I trim my pubic hair?" 
            "A. Left natural": 
                return 0 
            "B. Shaved into an \"X\"": 
                return 0 
            "C. I don't know":    
                $ EmmaX.FaceChange("sadside", 1)
                if not EmmaX.SeenPussy:
                    ch_e "Boo, I thought you might at least take a guess. . ." 
                else:                    
                    ch_e "Clearly you weren't paying enough attention."
                $ EmmaX.FaceChange("normal")
                return 0 
            "D. Waxed clean":    
                $ EmmaX.FaceChange("sly", 1)
                ch_e "Someone was paying attention. . ."    
                return 1 
    if QuizOrder[Count2] == 9: 
        menu:
            ch_e "Name one of my horrible sisters."
            "A. Drucilla": 
                return 0 
            "B. Elsa": 
                return 0 
            "C. Adrienne": 
                return 1 
            "D. Cordelia": 
                return 1 
    if QuizOrder[Count2] == 10: 
        menu:
            ch_e "My previous teaching experience was at which Ivy League school?"
            "A. Deerfield Community College": 
                return 0 
            "B. Princeton": 
                return 0 
            "C. Empire State University": 
                return 0 
            "D. The Massachusetts Academy": 
                return 1

 #remove this once I have enough questions
    "She asked an obscure question but you answer the question correctly."
    return 1

# Laura Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Laura_Quiz_Question:    
    if QuizOrder[Count2] == 1:
        menu:
            ch_l "I don't know. . . what color are my eyes?"
            "A. Blue": 
                return 0 
            "B. Green": 
                return 1 
            "C. Brown":        
                return 0 
            "D. Red": 
                return 0 
    if QuizOrder[Count2] == 2:    
        $ LauraX.FaceChange("perplexed",1,Eyes="side")
        ch_l "Um. . ."
        $ LauraX.FaceChange("sly")      
        menu: 
            ch_l "Say my name."
            "A. [LauraX.Pet]": 
                ch_l "Close enough."
                return 1 
            "B. Esme": 
                return 0 
            "C. Laura": 
                return 1 
            "D. . . .": 
                return 0 
    if QuizOrder[Count2] == 3: 
        menu:
            ch_l "What do you think about my ass?"
            "A. Kind of flat?": 
                return 0 
            "B. Tight?": 
                return 1 
            "C. Hot?": 
                return 1 
            "D. I don't know?": 
                return 0 
                    
    if QuizOrder[Count2] == 4: 
        menu:                
            ch_l "What number am I thinking of?"
            "A. 23?": 
                $ LauraX.FaceChange("surprised")
                ch_l "How did you guess?"
                $ LauraX.FaceChange("sly")
                return 1 
            "B. 2?": 
                $ LauraX.FaceChange("sly")
                ch_l "Mmmm, you and me?"
                return 1
            "C. 8?": 
                $ LauraX.FaceChange("perplexed")
                ch_l ". . . What? Why?"
                $ LauraX.FaceChange("bemused")
                return 0 
            "D. Green?": 
                ch_l ". . ."
                return 0 
#    if QuizOrder[Count2] == 5: 
#        menu:
#            ch_l "Do you know who built them?"
#            "A. Arcade": 
#                return 0 
#            "B. Bolivar Trask": 
#                return 1 
#            "C. Magneto": 
#                return 0 
#            "D. Unus the Untouchable": 
#                return 0 
#    if QuizOrder[Count2] == 6: 
#        ch_l "Y'know, we didn't always have classes here at the Institute." 
#        ch_l "For a while, all the students here went to a local public school." 
#        menu:
#            ch_l "Know which one?" 
#            "A. Bayville High School": 
#                return 1 
#            "B. King Memorial High School":
#                return 0 
#            "C. Riverside High School": 
#                return 0 
#            "D. Seth Paine High School": 
#                return 0 
#    if QuizOrder[Count2] == 7: 
#        menu:
#            ch_l "It seems like it happened so long ago, but do you know who the first mutant I ever met was?"
#            "A. Jean Grey": 
#                return 0 
#            "B. Lance Alvers": 
#                return 1 
#            "C. Mystique": 
#                return 0 
#            "D. Professor Xavier": 
#                return 0 
#    if QuizOrder[Count2] == 8: 
#        ch_l "Rogue, Boom-Boom, Magma, Jean, and I once put together a crime-fighting team and took down a local chop shop operation." 
#        ch_l "Even though it was a lot of fun, we ended up disbanding after that." 
#        menu:
#            ch_l "Anyway, know what the name we chose for the group was?"
#            "A. The Bayville Avengers": 
#                return 0 
#            "B. The Bayville Brawlers": 
#                return 0 
#            "C. The Bayville Harpies": 
#                return 0 
#            "D. The Bayville Sirens": 
#                return 1 
#    if QuizOrder[Count2] == 9: 
#        menu:
#            ch_l "Okay[LauraX.like]..not that I'd know, but do you know the remedy for stink bomb aroma?"
#            "A. A hot shower": 
#                return 0 
#            "B. Methyl Ethyl Ketone": 
#                return 0 
#            "C. Isolation": 
#                return 1 
#            "D. Tomato Juice": 
#                return 0 
#    if QuizOrder[Count2] == 10: 
#        ch_l "When I'm using my powers, I'm not[LauraX.like]{i}totally{/i} invulnerable."
#        menu:
#            ch_l "Who has powers that can still affect me?"
#            "A. Blob": 
#                return 0 
#            "B. Magneto": 
#                return 0 
#            "C. Quicksilver": 
#                return 0 
#            "D. Scarlet Witch": 
#                return 1

 #remove this once I have enough questions
    ch_l ". . . I can't think of anything, skip my turn."
    return 1
          
# End of  Questions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Emma Intro / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Emma_StripStudy_Intro:     
    if Party[0] != EmmaX:
            $ Party.reverse()                  
    call Shift_Focus(Party[0])           
    if not EmmaX.Over and not EmmaX.Legs:
            #if she's mostly naked, cheat
            $ EmmaX.FaceChange("sly")                                
            ch_e "I was considering some way of. . . motivating you. . ." 
            $ EmmaX.Eyes = "down"
            ch_e "but but I suppose we're already past that. . ."
            $ EmmaX.Eyes = "squint"
            ch_e "Do you have any ideas?"                                
            call Emma_SexMenu   
    else:
            "[EmmaX.Name] moves a bit closer to you. . ."
            ch_e "I was curious, [EmmaX.Petname]. . ."
            ch_e "do you feel that a little \"motivation\" might help you to learn?"
            if "stripstudy" not in EmmaX.History:
                menu:
                    extend ""                                        
                    "What sort of motivation?": 
                        if "frisky" not in EmmaX.History:
                            $ EmmaX.FaceChange("sly") 
                            $ Line = "ask"                                                
                        else:                                   
                            $ EmmaX.Statup("Obed", 80, 3)
                            $ EmmaX.FaceChange("confused",1)  
                            "She strokes at the edges of her clothes."
                            ch_e "You aren't going to make me say it, are you. . ."
                            menu:
                                extend ""
                                "Um. . . oh, OH! Yeah, sounds good. [[Strip tutoring]":
                                            $ Line = "strip"
                                "Looks like I am. . .":
                                    if ApprovalCheck(EmmaX, 500, "O"):                              
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            $ EmmaX.Statup("Inbt", 50, 5)  
                                            $ EmmaX.FaceChange("sly", 2)  
                                            $ Line = "ask"
                                    elif ApprovalCheck(EmmaX, 500, "LO"):
                                            $ EmmaX.FaceChange("confused", 2)            
                                            $ EmmaX.Statup("Love", 70, -5) 
                                            $ EmmaX.Statup("Obed", 80, 5)  
                                            ch_e "Very well. . ."
                                            $ Line = "ask"                                                            
                                    else:          
                                            $ EmmaX.Statup("Love", 200, -5) 
                                            $ EmmaX.Statup("Inbt", 50, -5)  
                                            $ EmmaX.FaceChange("angry", 1)  
                                            ch_e "Oh, never mind then."
                                ". . .":
                                    if ApprovalCheck(EmmaX, 400, "O"):           
                                            $ EmmaX.FaceChange("confused", 2)            
                                            $ EmmaX.Statup("Inbt", 50, 5)  
                                            $ Line = "ask"
                                    elif ApprovalCheck(EmmaX, 500, "LO"):
                                            $ EmmaX.FaceChange("confused", 1, Brows="angry")           
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, 5)  
                                            $ Line = "ask"                                                            
                                    else:          
                                            $ EmmaX.Statup("Love", 200, -5) 
                                            $ EmmaX.Statup("Inbt", 50, -5)  
                                            $ EmmaX.FaceChange("angry", 1)  
                                            ch_e "Oh, never mind then."
                            
                    "I think it might." if "frisky" in EmmaX.History:
                            $ EmmaX.FaceChange("sly")           
                            $ EmmaX.Statup("Love", 80, 5) 
                            $ EmmaX.Statup("Obed", 80, 3)
                            $ EmmaX.Statup("Inbt", 50, 5)  
                            ch_e "I was hoping you would. . ."
                            $ Line = "strip"                                            
                    "No, I've got this.":
                            $ EmmaX.FaceChange("confused", Eyes="side")    
                            if "frisky" in EmmaX.History:
                                    $ EmmaX.Statup("Love", 200, -10) 
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Inbt", 50, -5)   
                            else:
                                    $ EmmaX.Statup("Love", 200, -5) 
                                    $ EmmaX.Statup("Inbt", 50, -5)   
                            ch_e "Oh. . . Very well then."
                            $ EmmaX.FaceChange("confused")  
                if Line == "ask":
                    ch_e "Well, perhaps I could quiz you about mutant psychology. . ."
                    $ EmmaX.Eyes = "side"
                    ch_e "and, perhaps, if you were to get a question right. . ."
                    $ EmmaX.Eyes = "squint"
                    ch_e "I could. . ."
                    menu:
                        extend ""
                        "Take off some clothes?":
                                $ EmmaX.Statup("Inbt", 50, 5)   
                                ch_e "Yes."
                                $ Line = "strip"
                        "Yes? . .":
                                if ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.FaceChange("confused", 2) 
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Love", 200, -5) 
                                            $ EmmaX.Statup("Obed", 80, 10)   
                                    else:
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)  
                                    $ Line = "ask"
                                elif ApprovalCheck(EmmaX, 500, "LO"):
                                    $ EmmaX.FaceChange("confused", 1, Brows="angry") 
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Love", 200, -5) 
                                            $ EmmaX.Statup("Obed", 80, 5)  
                                    else:
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)  
                                    $ Line = "ask"            
                        ". . .":
                                if ApprovalCheck(EmmaX, 500, "O"):
                                    $ EmmaX.FaceChange("confused", 2) 
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)   
                                    else:
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)  
                                    $ Line = "ask"
                                elif ApprovalCheck(EmmaX, 500, "LO"):
                                    $ EmmaX.FaceChange("confused", 1, Brows="angry") 
                                    if "frisky" in EmmaX.History:
                                            $ EmmaX.Statup("Love", 200, -5) 
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)   
                                    else:
                                            $ EmmaX.Statup("Obed", 50, 5)
                                            $ EmmaX.Statup("Inbt", 50, -5)  
                                    $ Line = "ask"   
                    if Line == "ask":
                                    $ EmmaX.FaceChange("bemused", Eyes="side") 
                                    ch_e "Take off some clothes. . ."
                                    $ Line = "strip"
                    $ EmmaX.FaceChange("sly", Brows="confused") 
                    menu:
                        ch_e "Would that interest you?"
                        "Definitely!":
                            $ EmmaX.FaceChange("sly",Mouth="smile")    
                            $ EmmaX.Statup("Love", 50, 5)
                            $ EmmaX.Statup("Love", 80, 5) 
                            $ EmmaX.Statup("Inbt", 50, 5)                                               
                        "Yeah.":
                            $ EmmaX.FaceChange("sly")     
                            $ EmmaX.Statup("Love", 80, 3) 
                            $ EmmaX.Statup("Obed", 50, 3)
                            $ EmmaX.Statup("Inbt", 50, 3)                                              
                        "No thanks.":
                            if "frisky" in EmmaX.History:
                                    $ EmmaX.Statup("Love", 200, -10) 
                                    $ EmmaX.Statup("Obed", 80, 10)
                                    $ EmmaX.Statup("Inbt", 50, -5)   
                            else:
                                    $ EmmaX.Statup("Love", 200, -5) 
                                    $ EmmaX.Statup("Obed", 80, 5)
                                    $ EmmaX.Statup("Inbt", 50, -5)  
                            $ EmmaX.FaceChange("angry") 
                            ch_e "Hrm."
                            $ Line = "no"
                    
            if Line == "strip":
                    $ EmmaX.FaceChange("sly", 0) 
                    if len(Party) >= 2:
                        ch_e "And you, [Party[1].Name]? Care to participate?"                     
                        call Date_Sex_Break(EmmaX,Party[1])
                        if _return == 4:
                                #you stop it because of the other girl
                                ch_e "Well I suppose we can. . . postone that."
                                return
                        elif _return == 3:
                                #the other girl is mad
                                ch_e "Well I suppose that answers that."
                                $ Cnt = 3
                        elif _return == 2:
                                #the other girl will watch
                                ch_e "I suppose you can just watch then. . ."    
                                $ Cnt = 3                                                
                        elif _return == 1 and len(Party) >= 2:
                                if Party[1] == RogueX:
                                    ch_r "I guess I could join in."
                                elif Party[1] == KittyX:
                                    ch_k "It could be fun. . ."
                                elif Party[1] == LauraX:
                                    ch_l "Yeah, ok. . ."
                    return 1
            else: 
                    return 0
    return 0
# End Emma_Strip_Study Intro / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
