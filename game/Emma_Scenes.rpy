# start EmmaMeet //////////////////////////////////////////////////////////
# Check  #Emma_Update   to see what needs fixing still
label EmmaMeet:    
    $ bg_current = "bg classroom"   
    call CleartheRoom("Emma",0,1)
    $ E_Loc = "bg emma"  
    $ E_Love = 300        
    $ E_Obed = 0            
    $ E_Inbt = 200 
    call Shift_Focus("Emma")    
    call Set_The_Scene
    $ ESpriteLoc = StageRight
    call LastNamer                         
    $ E_Petnames.append(_return)
    $ E_Petname = _return
        
    "You enter the classroom and have a seat." 
    "The bell to class rings, but Professor McCoy seems to be late."
    "A strange woman enters the room and heads to the podium with a regal stride."
    call EmmaFace("normal")
    show Emma_Sprite at SpriteLoc(ESpriteLoc) with easeinright     
    $ E_Loc = "bg classroom" 
    $ Emma_Arms = 1
    ch_u "Hello students. My name is Emma Frost, and I have been invited to conduct this class."
    ch_e "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect." 
    "She scans her eyes over the room, passing over each student."    
    call EmmaFace("surprised")
    pause 1
    call EmmaFace("sly",Mouth="sad")
    call Statup("Emma", "Love", 90, -10)     
    $ E_Lust += 5
    "As her eyes pass over you, they briefly widen and then narrow."
    call EmmaFace("sly")
    ch_e "Very well, let us begin, class."
    call EmmaFace("normal") 
    "The class is pretty basic today, mostly a lecture on her areas of expertise, psychology and literature."
    $ E_Lust += 5
    "She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."
    $ E_Lust += 5
    call Wait 
    call CleartheRoom("Emma",0,1)
    $ E_Loc = "bg classroom" 
    call Set_The_Scene
    ch_e "All right students, class dismissed."
    ch_e "[E_Petname], could you wait a moment, I have something to discuss with you."    
    menu:
        extend ""
        "Yes?":
                call Statup("Emma", "Love", 70, 10) 
                call EmmaFace("normal")  
        "I've got places to be.":
                call Statup("Emma", "Love", 70, -15) 
                call Statup("Emma", "Obed", 80, 10)
                call EmmaFace("angry") 
                ch_e "MR. [Playername], do not take that attitude with me."
                "She places herself in the doorway, preventing you from leaving."
        "For such a sexy teacher? I've got some time.":
                call Statup("Emma", "Love", 70, -5) 
                call Statup("Emma", "Obed", 80, 5)
                call EmmaFace("angry",1, Mouth="smirk") 
                ch_e "That's rather. . . inappropriate."
                call EmmaFace("bemused", Mouth="smile") 
                call Statup("Emma", "Love", 70, 20) 
                call Statup("Emma", "Lust", 50, 5) 
                call Statup("Emma", "Inbt", 25, 15)  
                ch_e "But also obvious, so I can't criticize you too harshly."
    
    ch_e "I've heard about you from Professor Xavier and. . . others." 
    
    if P_Rep <= 200:
        call Statup("Emma", "Obed", 80, 10)
        call Statup("Emma", "Inbt", 90, 15) 
        call Statup("Emma", "Lust", 50, 5) 
        call EmmaFace("angry", Brows="confused") 
        ch_e "You seem to be a bit of a scoundrel. . ."        
    elif P_Rep < 600:
        call Statup("Emma", "Obed", 80, 5)
        call Statup("Emma", "Inbt", 90, 5) 
        call Statup("Emma", "Lust", 50, 5) 
        call EmmaFace("sly") 
        ch_e "You have quite a reputation around campus. . ."
    else:
        call EmmaFace("smile") 
        ch_e "You have managed a reasonble reputation. . ."
        
    if R_SEXP >= 60 and K_SEXP >= 60:
        call Statup("Emma", "Love", 70, 5) 
        call Statup("Emma", "Obed", 80, 10)
        call Statup("Emma", "Inbt", 200, 10) 
        call Statup("Emma", "Lust", 50, 5) 
        call EmmaFace("sly") 
        ch_e "and a number of conquests to your name. . ."
    elif R_SEXP >= 60 or K_SEXP >= 60:
        call Statup("Emma", "Love", 70, 5) 
        call Statup("Emma", "Obed", 80, 5)
        call Statup("Emma", "Inbt", 200, 5) 
        call Statup("Emma", "Lust", 50, 2) 
        call EmmaFace("smile") 
        ch_e "and are not without some romantic entanglements. . ."
    else:
        call EmmaFace("smile", Brows="confused") 
        ch_e "though I haven't heard of much of a romantic life. . ."
        
    if P_Lvl >= 7:
        call Statup("Emma", "Love", 70, 5) 
        call Statup("Emma", "Obed", 80, 5)
        call EmmaFace("smile") 
        ch_e "but your grades have been excellent."
    elif P_Lvl >= 3:
        call EmmaFace("normal", Brows="confused") 
        ch_e "but your grades been marginal at best."
    else:
        call Statup("Emma", "Love", 70, -5) 
        call Statup("Emma", "Lust", 10, -5, 1)  
        call EmmaFace("normal", Brows="sad") 
        ch_e "but you haven't been living up to your potential in class."
    
    call EmmaFace("normal", Eyes="side") 
    ch_e "My particular interest in this case, however. . ."
    call EmmaFace("sly") 
    ch_e "is that I cannot get a \"read\" on you."
    call EmmaFace("sly", Mouth="normal") 
    ch_e "My mutant power is telepathy, the same as Professor Xavier's."
    ch_e "I've grown accustomed to knowing what those around me are thinking."
    call EmmaFace("bemused", Eyes="side") 
    ch_e "With you. . . I cannot do that, which presents an interesting. . ."
    call EmmaFace("sly") 
    ch_e "challenge. . ."
    menu:
        extend ""
        "I imagine it would.":
                call Statup("Emma", "Love", 70, 5) 
                call Statup("Emma", "Inbt", 200, 5) 
                call EmmaFace("normal") 
                ch_e "Hmm, yes."
        "Huh.":
                call Statup("Emma", "Love", 70, -1) 
                call Statup("Emma", "Obed", 80, -1)
                call EmmaFace("confused", Mouth="normal") 
                ch_e ". . . yes."
                call EmmaFace("normal") 
        "So you can't see what I'm picturing right now?":
                call Statup("Emma", "Obed", 80, 5)
                call EmmaFace("bemused") 
                pause 0.5
                call EmmaFace("bemused", Eyes="down") 
                "She glances downward."
                call EmmaFace("sly") 
                call Statup("Emma", "Love", 70, 10) 
                call Statup("Emma", "Inbt", 200, 10) 
                call Statup("Emma", "Lust", 50, 15) 
                ch_e "I can't read your mind, but I'm not blind, [E_Petname]."
    ch_e "In any case, I think we should set aside some time to talk."
    ch_e "I'd like to make you a personal project, so I can see how you tick."
    menu:
        extend ""
        "I'd be ok with that.": 
                call Statup("Emma", "Love", 70, 5) 
                call Statup("Emma", "Inbt", 200, 5) 
                call EmmaFace("smile") 
                ch_e "Excellent, I look forward to it."
        "I don't know if you should experiment on your students.":
                call Statup("Emma", "Love", 70, -5) 
                call EmmaFace("normal", Mouth="sad") 
                ch_e "There's nothing for you to worry about."
                call EmmaFace("sly") 
                ch_e "I'll be. . . gentle."
        "If it means spending more time with you. . .":
                if ApprovalCheck("Emma", 295, "L"):
                    call Statup("Emma", "Inbt", 200, 5) 
                    call Statup("Emma", "Lust", 50, 5) 
                    call EmmaFace("sly") 
                    ch_e "Oh, I believe we'll be spending a good deal of time together. . ."
                else:
                    call EmmaFace("angry") 
                    ch_e "Much as it may pain me, it would. . ."
                    call EmmaFace("normal") 
        "What do I get out of it?":
                if not ApprovalCheck("Emma", 290, "L"):
                    call Statup("Emma", "Love", 70, -5) 
                    call Statup("Emma", "Obed", 80, 5)
                    call Statup("Emma", "Inbt", 200, 5) 
                    call EmmaFace("angry") 
                    ch_e "You'll stand some chance of passing this class, [E_Petname]."
                    call EmmaFace("normal") 
                else:
                    if E_Obed > 0:
                        call EmmaFace("confused", Mouth="smirk") 
                        ch_e "What would you {i}like{/i} to \"get out of it?\""
                        menu:
                            extend ""
                            "I guess if it helps your \"research.\" . .":
                                    call Statup("Emma", "Love", 70, 10) 
                                    call Statup("Emma", "Obed", 80, -5)
                                    call EmmaFace("smile") 
                                    ch_e "I'm glad to see that you can be reasonable."
                            "Spending more time with you would be plenty. . .":
                                    call Statup("Emma", "Love", 70, 5) 
                                    call Statup("Emma", "Obed", 80, 5)
                                    call Statup("Emma", "Lust", 20, 5) 
                                    call EmmaFace("sly") 
                                    ch_e "It certainly should be."
                            "A kiss?":
                                    call Statup("Emma", "Love", 70, -5) 
                                    call Statup("Emma", "Obed", 80, 10)
                                    call EmmaFace("surprised",1, Mouth="surprised") 
                                    ch_e "[E_Petname], that is incredibly inappropriate!"
                                    call EmmaFace("sadside",0,Brows="angry") 
                                    ch_e "I would {i}never{/i} consider such a thing with a student."
                                    if ApprovalCheck("Emma", 220, "I"):
                                        call EmmaFace("sly",1) 
                                        call Statup("Emma", "Love", 70, 5) 
                                        call Statup("Emma", "Obed", 80, 5)
                                        call Statup("Emma", "Inbt", 200, 5) 
                                        call Statup("Emma", "Lust", 50, 5) 
                                        ch_e ". . .never. . ."
                            "I think you know what I'd want. . .":
                                    call Statup("Emma", "Obed", 80, 5)
                                    call Statup("Emma", "Lust", 50, 5) 
                                    call EmmaFace("sly",Brows="angry") 
                                    ch_e "Yes, I imagine that I do. . ."
                                    if ApprovalCheck("Emma", 220, "I"):
                                        call EmmaFace("sly",1) 
                                        call Statup("Emma", "Love", 70, 5) 
                                        call Statup("Emma", "Obed", 80, 5)
                                        call Statup("Emma", "Inbt", 200, 10) 
                                        call Statup("Emma", "Lust", 50, 5) 
                                        ch_e "And we may be able to come to some sort of \"mutually beneficial\" arrangement."
                                    else:
                                        call EmmaFace("bemused",0) 
                                        call Statup("Emma", "Love", 70, -5) 
                                        ch_e "But figuring out whether I'm correct is the entire point here."
                    else: #if 0 Obedience
                        call EmmaFace("normal") 
                        ch_e "The satisfaction of helping my. . . studies."
                        if ApprovalCheck("Emma", 300, "L"):
                            call EmmaFace("sly") 
                            call Statup("Emma", "Obed", 80, 5)
                            call Statup("Emma", "Inbt", 200, 5) 
                            call Statup("Emma", "Lust", 50, 5) 
                            ch_e "-and maybe if you're good. . ."
                        else:
                            ch_e "-and nothing more."
     
    call EmmaFace("normal",0) 
    ch_e "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."   
    ch_e ". . . later. . ."
    hide Emma_Sprite with easeoutright 
    "She strides out of the room and down the hall."
    $ E_Loc = "bg emma"         
    $ E_History.append("met")          
    $ Round -= 10      
    return
            
# end EmmaMeet //////////////////////////////////////////////////////////            
           

# Event Emma_Teacher_Caught /////////////////////////////////////////////////////         
label Emma_Teacher_Caught(Girl = "That girl"):
    #add this scene for when Emma is a teacher, and catches one of the girls fucking around in class.
    ch_e "[Playername]? [Girl]? Could you stop what you're doing immediately?" 
    call Checkout(1)
    
#    if Girl == "Rogue":
#            call RogueFace("bemused", 2, Eyes="side")            
#            call AllReset("Rogue")
#            $ renpy.pop_call()        
#            $ renpy.pop_call()
#            if ApprovalCheck("Rogue", 700, "I"): 
#                    call RogueFace("bemused", 1)  
#                    "Rogue shrugs and returns to her seat."
#                    $ R_LikeEmma += 2
#            else: 
#                    "Rogue jumps and dashes out of the room."
#                    $ R_LikeEmma -= 2
#                    $ R_Loc = "bg rogue"
#                    hide Rogue
#                    if "Rogue" in Party:
#                        $ Party.remove("Rogue")
#            $ R_Rep -= 1
#            $ E_LikeRogue += 2
#    elif Girl == "Kitty":
#            call KittyFace("bemused", 2, Eyes="side")  
#            call AllReset("Kitty")
#            $ renpy.pop_call()        
#            $ renpy.pop_call()
#            if ApprovalCheck("Kitty", 700, "I"): 
#                    call KittyFace("bemused", 1) 
#                    "Kitty shrugs and returns to her seat."
#                    $ K_Loc = "bg kitty"
#                    hide Kitty_Sprite
#                    if "Kitty" in Party:
#                        $ Party.remove("Kitty")
            
    call AnyFace(Girl,"bemused", 2, Eyes="side")
    call AllReset(Girl)
    if ApprovalCheck(Girl, 700, "I"): 
            call AnyFace(Girl,"bemused", 1)
            "[Girl] shrugs and returns to her seat."
            call Partner_Like("Emma",2,-1,500,1,Girl) #if likes emma 500+, +2, else -1                   
    else: 
            "[Girl] jumps and dashes out of the room."
            call Partner_Like("Emma",-2,-3,500,1,Girl) #if likes emma 500+, -2, else -3  
            call Remove_Girl(Girl)       
            
    if Girl == "Rogue":
            $ R_Rep -= 1
    elif Girl == "Kitty":        
            $ K_Rep -= 1
    elif Girl == "Laura":
            $ L_Rep -= 1
    call Partner_Like(Girl,3,2,800,1,"Emma")  #if likes the girl 800+, +3, else +2
        
    $ P_Rep -= 1             
    ch_e "Thank you."
    ch_e "And [Playername], see me after class for detention. . ."
    
    $ renpy.pop_call()        
    $ renpy.pop_call()
    $ P_Traits.append("detention")    
    $ P_DailyActions.append("detention") 
    jump Class_Room
    
# end Emma_Teacher_Caught //////////////////////////////////////////////////////////            
           
# Event Emma_Caught_Masturbating  /////////////////////////////////////////////////////  

label Emma_Caught_Masturbating: #Emma_Update   
            #This label is called from a Location
            call Shift_Focus("Emma")
            "You hear some odd noises coming from Emma's room as you enter."                           #fix this scene, pants option    
            show blackscreen onlayer black
            call EmmaOutfit(Changed=1)    
            $ E_Upskirt = 1
            $ E_PantiesDown = 1
            call Set_The_Scene
            call EmmaFace("sexy")
            $ E_Eyes = "closed"
            $ Emma_Arms = 2
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ E_DailyActions.append("unseen")
            $ E_RecentActions.append("unseen")    
            call Emma_SexAct("masturbate")
            if "angry" in E_RecentActions:
                return
        
#After caught masturbating. . .
            $ E_Eyes = "sexy"
            $ E_Brows = "confused"
            $ E_Mouth = "smile"
            if E_Mast == 1:        
                    $ E_Mouth = "kiss"
                    ch_e "I wasn't expecting visitors. . ."
                    $ E_Eyes = "side"
                    $ E_Mouth = "lipbite"        
                    ch_e "although for you I could make an exception. . ."
                    $ E_Eyes = "sexy"
                    $ E_Brows = "normal"         
                    $ E_Mouth = "smile"
                    ch_e "Perhaps next time you could knock?" 
            else:
                    ch_e "I notice you make a habit of dropping in."           
            $ Emma_Arms = 1  
            call EmmaOutfit    
            return
    
# end Emma_Caught_Masturbating/////////////////////////////////////////////////////




# Event Emma_Caught_Classroom  /////////////////////////////////////////////////////  

label Emma_Caught_Classroom:  
            #This label is called from a Location
            call Shift_Focus("Emma")
            "As you walk down the halls, you hear some odd noises coming from the classroom."                           #fix this scene, pants option    
            show blackscreen onlayer black
            $ bg_current = "bg classroom"            
            call CleartheRoom("Emma",0,1)
            call EmmaOutfit(Changed=1)     
            $ E_Loc = 0
            call Set_The_Scene
            $ E_Loc = "bg desk"
            $ Taboo = 0
            call EmmaFace("sexy")
            $ E_Eyes = "closed"
            $ Emma_Arms = 1
            $ Count = 0   
            hide blackscreen onlayer black
            $ Trigger = "masturbation"
            $ Trigger3 = "fondle pussy"
            $ Trigger5 = "fondle breasts"
            $ E_RecentActions.append("classcaught") 
            $ E_DailyActions.append("unseen")
            $ E_RecentActions.append("unseen")    
            $ Line = 0
            call DrainWord("Emma","no masturbation")
            $ E_RecentActions.append("masturbation")                      
            $ E_DailyActions.append("masturbation") 
            "You see Ms Frost leaning back against her desk, her hands tracing slow paths across her body."
            
            if "Historia" in P_Traits:
                    call EM_Interupted
            else:
                    call EM_Cycle
            if "angry" in E_RecentActions:
                return
        
#After caught masturbating. . .
            $ E_Eyes = "sexy"
            $ E_Brows = "confused"
            $ E_Mouth = "normal"             
            $ Emma_Arms = 1  
            call EmmaOutfit    
            $ bg_current = "bg classroom"  
            call Display_Emma 
            if "classcaught" in E_History: 
                    ch_e "I notice you make a habit of dropping in."  
                    call EmmaOutfit      
            else:
                    # First time caught
                    $ E_History.append("classcaught") 
                    if "Historia" not in P_Traits:
                        $ Tempmod = 25
                    ch_e "Well."
                    call EmmaFace("angry", Eyes="side")
                    ch_e "It appears that you've caught me in a somewhat. . . compromising position. . ."
                    menu:
                        extend ""
                        "Yup.":
                                call EmmaFace("perplexed", Mouth="normal")         
                                call Statup("Emma", "Love", 70, -1)
                                call Statup("Emma", "Obed", 50, -2)
                                call Statup("Emma", "Lust", 80, -5)
                                ch_e "Er, well. . ."
                        "Are you supposed to be shlicking it in class?":
                                call EmmaFace("angry", Eyes="side")
                                call Statup("Emma", "Obed", 50, 5)
                                call Statup("Emma", "Inbt", 70, 5) 
                                ch_e "Hrm."
                                call EmmaFace("sly", Brows="angry")
                                call Statup("Emma", "Lust", 80, 3)
                                ch_e "I imagine I shouldn't, but you know how it can be,"
                                $ E_Brows = "normal"
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "-surrounded by attractive co-eds all day long. . ."
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "yourself included. . ."
                        "I think it was pretty hot.":
                                call EmmaFace("sly")
                                call Statup("Emma", "Love", 70, 5)
                                call Statup("Emma", "Obed", 50, 10)
                                call Statup("Emma", "Inbt", 70, 10) 
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "Hmm, well I suppose I can't blame you for that. . ."
                        "What do you mean?":
                                call EmmaFace("angry")
                                call Statup("Emma", "Love", 70, -10)
                                call Statup("Emma", "Obed", 50, -5)
                                ch_e "I mean how I was. . ."
                                call EmmaFace("surprised")
                                call Statup("Emma", "Love", 70, 15)
                                call Statup("Emma", "Obed", 50, 15)
                                call Statup("Emma", "Inbt", 70, 5) 
                                ch_e "Oh!"
                                call EmmaFace("perplexed")
                                ch_e "Yes, obviously it was nothing, just getting some. . ."
                                $ E_Eyes = "side"
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "paperwork done. . ."
                                call EmmaFace("sly")
                                $ Line = 1
                    ch_e "So how did you want to handle this. . . situation?"
                    menu:
                        extend ""
                        "I think I can forget all about it.":
                                call EmmaFace("smile")
                                call Statup("Emma", "Love", 80, 10)
                                call Statup("Emma", "Obed", 60, 10)
                                call Statup("Emma", "Inbt", 70, 15) 
                                ch_e "Thank you, [E_Petname]. I appreciate your discretion."
                                call EmmaFace("sly")
                                ch_e "Are you {i}certain{/i} there's nothing I could do to thank you?"
                        "What solution did you have in mind?":
                                call EmmaFace("sly")
                                call Statup("Emma", "Love", 70, 5)
                                call Statup("Emma", "Obed", 60, 15)
                                call Statup("Emma", "Inbt", 70, 15) 
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "Oh, I'm sure I could make it worth your while. . ."
                        "What situation?":
                                if Line != 1:
                                        call EmmaFace("confused")
                                        call Statup("Emma", "Love", 70, -10)
                                        call Statup("Emma", "Obed", 50, -5)
                                        ch_e "I mean how I was. . ."
                                        call EmmaFace("surprised")
                                        call Statup("Emma", "Love", 70, 15)
                                        call Statup("Emma", "Obed", 50, 15)
                                        call Statup("Emma", "Inbt", 70, 5) 
                                        ch_e "Oh!"
                                        call EmmaFace("perplexed")
                                        ch_e "Yes, obviously it was nothing, just getting some. . ."
                                        $ E_Eyes = "side"
                                        call Statup("Emma", "Lust", 80, 5)
                                        ch_e "paperwork done. . ."
                                        call EmmaFace("sly")
                                else:
                                        call EmmaFace("angry")
                                        call Statup("Emma", "Love", 70, -5)
                                        call Statup("Emma", "Inbt", 70, 5) 
                                        ch_e "I do wonder if you're just being dense. . ."
                                        call EmmaFace("sly")
                                        ch_e "Still. . ."
                    $ Line = 0
                    $ MultiAction = 0
                    menu:
                        extend ""
                        "Could you strip?":
                                call Statup("Emma", "Love", 70, 5)
                                call Statup("Emma", "Obed", 50, 10)
                                call Statup("Emma", "Inbt", 70, 15) 
                                ch_e "So you wanted a better view of the action?"
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "I suppose I could accomodate that. . ."
                                ch_e "to a point. . ."
                                "Ms Frost walks to the door and locks it behind her."
                                if "Historia" in P_Traits:
                                        return 1
                                call E_Strip
                        "Could you just keep going?":
                                call Statup("Emma", "Love", 70, 10)
                                call Statup("Emma", "Obed", 50, 15)
                                call Statup("Emma", "Inbt", 70, 15) 
                                ch_e "Oh, you wanted to watch some more?"
                                ch_e "I can't exactly blame you."    
                                $ E_Eyes = "down"
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "Were you going to put on a show as well?"
                                menu:
                                    "Yeah!":
                                        call Statup("Emma", "Love", 70, 5)
                                        call Statup("Emma", "Inbt", 70, 10) 
                                        call Statup("Emma", "Lust", 80, 5)
                                        ch_e "Excellent."
                                        if "Historia" not in P_Traits:
                                            call Seen_First_Peen("Emma")
                                        "You begin to stroke your cock."
                                        $ Trigger2 = "jackin"
                                    "No, you go ahead.":
                                        call EmmaFace("sad")
                                        call Statup("Emma", "Love", 70, -10)
                                        call Statup("Emma", "Obed", 50, 5)
                                        call Statup("Emma", "Inbt", 70, 5) 
                                        ch_e "Pity."
                                call EmmaFace("sly")
                                "Ms Frost walks to the door and locks it behind her."
                                $ Taboo = 0
                                $Trigger = "masturbation"
                                $Trigger3 = "fondle breasts"
                                "Ms Frost leans back and runs her fingertips along her breasts."
                                if "Historia" in P_Traits:
                                        return 1
                                call EM_Cycle
                        "Could I feel you up?":
                                call Statup("Emma", "Love", 70, 5)
                                call Statup("Emma", "Obed", 50, 10)
                                call Statup("Emma", "Inbt", 70, 10) 
                                ch_e "Hmm, I could use some help . . .around the office. . . "
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "perhaps you have some suggestions?"
                                "Ms Frost walks to the door and locks it behind her."
                                $ Taboo = 0
                                if "Historia" in P_Traits:
                                        return 1
                                call E_FB_Prep
                        "Could you give me a hand? [[point to your cock]":
                                call Statup("Emma", "Love", 70, -5)
                                call Statup("Emma", "Obed", 50, 5)
                                $ E_Brows = "surprised"
                                ch_e "I appreciate boldness, [E_Petname], but be a bit more realistic." 
                                $ E_Brows = "normal"
                                call Statup("Emma", "Love", 70, 10)
                                call Statup("Emma", "Inbt", 70, 5) 
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "Perhaps instead I could just offer a little. . . token of my appreciation."
                                "Ms Frost walks to the door and locks it behind her."
                                if "Historia" in P_Traits:
                                        return 1
                                call E_Strip
                        "I should just get going then.":
                                call EmmaFace("surprised")
                                call Statup("Emma", "Obed", 50, 5)
                                ch_e "Oh."
                                call EmmaFace("confused")
                                call Statup("Emma", "Love", 70, -5)
                                call Statup("Emma", "Inbt", 70, -5) 
                                ch_e "Well, I suppose. . ."
                                call EmmaFace("perplexed")
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "I'll see you. . . in class then. . ."
                    call EmmaOutfit     
                    "Afterwards, Ms Frost collects her things and strides toward the door."
                    "She turns back with her hand on the door."
                    call EmmaFace("sly")
                    ch_e "Oh, and [E_Petname]?"
                    ch_e "You can just call me \"Emma.\""
                    $ EmmaName = "Emma"
                    $ E_Loc = "bg emma"
                    hide Emma_Sprite with easeoutleft
                    $ Round = 20 if Round > 20 else Round
                    $ MultiAction = 1
            return
    
# end Emma_Caught_Classroom/////////////////////////////////////////////////////


# Event Emma_Detention  /////////////////////////////////////////////////////  

label Emma_Detention:  
            #This label is called from a Location
            call Shift_Focus("Emma")
            call CleartheRoom("Emma",0,1)
            if "traveling" in P_RecentActions:
                "You enter the room and see [EmmaName] waiting for you at the back of the room."
            else:
                "After class, the students file out, and you wait a few minutes until they're all gone."
                "Once the last student leaves, [EmmaName] approaches you."
            show blackscreen onlayer black
            $ bg_current = "bg classroom"
            $ E_Loc = "bg classroom"
            call EmmaOutfit    
            call Set_The_Scene     
            call EmmaFace("sly")
            $ Emma_Arms = 2
            $ Count = 0  
            call CleartheRoom("Emma",0,1)
            hide blackscreen onlayer black
            $ Line = 0
            if "detention" in P_DailyActions:
                ch_e "I'm glad you take your. . . education seriously."
            else:
                #if you skipped detention
                call EmmaFace("surprised")  
                ch_e "Oh, [E_Petname], you really shouldn't skip your detention like that. . ."            
            $ P_Traits.remove("detention") 
            $ E_RecentActions.append("detention") 
            $ E_DailyActions.append("detention") 
            call EmmaFace("sly")  
            call Statup("Emma", "Lust", 80, 3)
            ch_e "You've been such a naughty pupil. . ."
            $ Emma_Arms = 1
            call EmmaFace("sadside", Brows="normal")  
            call Statup("Emma", "Lust", 80, 5)
            ch_e "Chasing after those young girls. . ."            
            call EmmaFace("sly")  
            call Statup("Emma", "Lust", 80, 3)
            if "detention" in E_History:
                ch_e "How will we deal with it this time?"
            else:
                #first time
                ch_e "What am I to do with you. . ."
                $ E_History.append("detention") 
            
            "[EmmaName] walks to the door and locks it behind her."
            $ Taboo = 0
            menu:
                extend ""
                "I guess I should focus on my studies.":  
                        if ApprovalCheck("Emma", 900) and "classcaught" in E_History:
                                call EmmaFace("perplexed")   
                                call Statup("Emma", "Inbt", 70, -3) 
                                call Statup("Emma", "Lust", 80, 5)
                                ch_e "Oh. Really? I was thinking of a more. . . recreational punishment."
                                menu:
                                    extend ""
                                    "Kidding, of course, what should we do? [[sex stuff]":
                                        call EmmaFace("sly")  
                                        call Statup("Emma", "Love", 90, 3)
                                        call Statup("Emma", "Obed", 60, 5)
                                        call Statup("Emma", "Inbt", 70, 5) 
                                        ch_e "Why do I put up with you?"
                                        call Emma_SexMenu
                                    "No, you're right, I take my education too lightly.":
                                        call Statup("Emma", "Love", 80, 1) 
                                        call Statup("Emma", "Inbt", 70, -2) 
                                        call Statup("Emma", "Lust", 80, 5)
                                        ch_e "Oh. Ok. Um. . ."
                                        call EmmaFace("sad")  
                                        call Statup("Emma", "Obed", 60, 5)
                                        call Statup("Emma", "Lust", 80, 5)
                                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                                        call Statup("Emma", "Lust", 80, 5)
                                        $ P_XP += 10
                        else:
                                        #She's not into you yet.
                                        call EmmaFace("sad", Mouth="normal")  
                                        call Statup("Emma", "Love", 50, 5) 
                                        call Statup("Emma", "Love", 80, 5) 
                                        call Statup("Emma", "Obed", 60, 5)
                                        call Statup("Emma", "Lust", 80, 5)
                                        ch_e "Yes. . . Exactly. . ."
                                        call Statup("Emma", "Inbt", 50, 5) 
                                        call Statup("Emma", "Lust", 80, 5)
                                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                                        call Statup("Emma", "Inbt", 70, 5) 
                                        call Statup("Emma", "Lust", 80, 5)
                                        $ P_XP += 10
                "I could think of a few things. . . [[sex stuff]":
                        if ApprovalCheck("Emma", 900) and "classcaught" in E_History:
                                call EmmaFace("sly")  
                                call Statup("Emma", "Lust", 80, 5)
                                call Statup("Emma", "Love", 90, 5)
                                call Statup("Emma", "Obed", 60, 5)
                                call Statup("Emma", "Inbt", 70, 5) 
                                ch_e "I just bet you can. . ."
                                call Emma_SexMenu
                        else:
                            #She's not into you yet.
                            call EmmaFace("sad", Mouth="smirk")  
                            call Statup("Emma", "Love", 80, 5) 
                            call Statup("Emma", "Obed", 60, 5)
                            call Statup("Emma", "Lust", 80, 5)
                            ch_e "I'm sure you could. . . but unfortunately this isn't the time for it."
                            call Statup("Emma", "Inbt", 50, 5) 
                            call Statup("Emma", "Inbt", 70, 5) 
                            call Statup("Emma", "Lust", 80, 5)
                            ch_e "We'll just have to settle for going over some of the topics from today's class. . ."
                            call Statup("Emma", "Inbt", 50, 5) 
                            call Statup("Emma", "Lust", 80, 5)
                            $ P_XP += 10                            
            $ Round = 20 if Round > 20 else Round 
            ch_e "Ok, I think that's plenty for now. . ."
            ch_e "You wouldn't want to make this a habit. . ."
            $ Tempmod = 0
            call EmmaOutfit  
            return            
    
# end Emma_Detention/////////////////////////////////////////////////////


# Event Emma_Key /////////////////////////////////////////////////////  

#Not updated

label Emma_Key: #Emma_Update   
            call Shift_Focus("Emma")
            call Set_The_Scene
            call EmmaFace("bemused")
            $ Emma_Arms = 2
            ch_e "You've been coming by fairly often. . ."
            ch_e ". . . you might want a key. . ."
            ch_p "Thanks."
            $ Emma_Arms = 1    
            $ Keys.append("Emma")
            $ E_Event[0] = 1
            return
# end Event Emma_Key /////////////////////////////////////////////////////


# Event Emma_Caught /////////////////////////////////////////////////////  

label Emma_Caught(TotalCaught=0): #Emma_Update   
    $ TotalCaught = R_Caught + K_Caught + E_Caught + L_Caught
    call Shift_Focus("Emma")
    call Checkout
    ch_e "!!!"        
    $ Line = Trigger
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    call EmmaOutfit
    if R_Loc == bg_current:         
        $ R_Loc = "bg study"
    if K_Loc == bg_current:                
        $ K_Loc = "bg study"  
    if L_Loc == bg_current:                
        $ L_Loc = "bg study"       
    $ bg_current = "bg study"  
    $ E_Loc = "bg study"
    call Set_The_Scene(0)
    show Professor at SpriteLoc(StageLeft)    
    show Emma_Sprite at SpriteLoc(StageRight) with ease    
    if R_Loc == bg_current:         
        show Rogue at SpriteLoc(StageFarRight) with ease
    if K_Loc == bg_current:         
        show Kitty_Sprite at SpriteLoc(StageFarRight) with ease
    if L_Loc == bg_current:         
        show Laura_Sprite at SpriteLoc(StageFarRight) with ease
    call XavierFace("shocked")
    call EmmaFace("sad")
    ch_x "I'm very disappointed in your behavior, particularly yours, Emma."
    
    if Line == "fondle thighs" or Line == "fondle breasts" or Line == "fondle pussy" or Line == "hotdog" or Line == "hand":
        ch_x "The two of you, feeling each other up like animals!"
    elif Line == "dildo pussy" or Line == "dildo anal":
        ch_x "Using those. . . devices on each other, unsanitary!"
    elif Line == "lick pussy":
        ch_x "Engaging in. . . cunnilingus. . . dripping everywhere. . ."
    elif Line == "blow":
        ch_x "Right there in public with his {i}penis{/i} in your mouth. . ."
    else:
        ch_x "Having sexual relations in such a public location, it shows very poor character of you!"
    
    if E_Shame >= 40:
        ch_x "Emma, my dear, you're practically naked! At least throw a towel on!"
        "He throws Emma a towel."
        show blackscreen onlayer black 
        $ E_Over = "towel"         
        hide blackscreen onlayer black
        ch_x "Well that's hardly any better."        
    elif E_Shame >= 20:
        ch_x "Emma, that attire is positively scandalous."
    
    if E_Caught:
        "And this isn't even the first time this has happened!"
    
    if R_Loc == bg_current:             #fix, might not currently work?
        call RogueFace("surprised",2)
        if "Rogue" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Rogue, you were just watching this occur!"        
        call RogueFace("bemused",1,Eyes="side")
    elif K_Loc == bg_current:             #fix, might not currently work?
        call KittyFace("surprised",2)
        if "Kitty" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Kitty, you were just watching this occur!"        
        call KittyFace("bemused",1,Eyes="side")
    elif L_Loc == bg_current:             #fix, might not currently work?
        call LauraFace("surprised",2)
        if "Laura" not in Rules:
            ch_x "And. . .hm, I could have sworn there was someone else. . ."  
        else:
            ch_x "And Laura, you were just watching this occur!"        
        call LauraFace("bemused",1, Eyes="side")
    
    if "rules" in Rules: #if the rules had been removed in a previous game
            call XavierFace("hypno")
            ch_x ". . ."
            ch_x "Hmm, I seem to be having a bit of deja vu here. . ."
            ch_x "I could swear that we've had a conversation like this before, but I cannot recall when. . ."
            call XavierFace("angry")
            ch_x "Regardless, this is a serious issue."
            $ Rules.remove("rules")
            
    if not E_Caught:
            ch_x "Emma, you are entrusted as a teacher here, I can't have you fraternizing with the students."
            ch_x "This is especially true in the school's public spaces!"
            ch_x "What sort of message does that send?"
            ch_x "How appropriate would it be if I were to just wander the halls with Miss Grey on my lap?"
            call XavierFace("hypno")
            ch_x "Just. . . running my hands along her firm little body without a care in the world. . ."
            call XavierFace("happy")
            ch_x ". . ."
            call XavierFace("shocked")
            ch_x "Yes, well, as I was saying! . ."
    $ Count = E_Caught
    menu:
        "Well what have you to say for yourselves?"
        "Sorry sir, won't do it again.":
                if E_Caught < 5:
                    call Statup("Emma", "Love", 70, 5)
                    call Statup("Emma", "Inbt", 30, -15) 
                call XavierFace("happy")  
                if E_Caught:
                    ch_x "But you know you've done this before. . . at least [E_Caught] times. . ." 
                elif TotalCaught:
                    ch_x "Not with Ms. Frost, perhaps, but you know you've done this before. . ."
                    ch_x "at least [TotalCaught] times. . ." 
                    call EmmaFace("sexy",Brows="confused")                 
                else:
                    ch_x "Very well, just don't let it happen again."
                $ Count += 5
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."
                ch_x "Now return to your room and reflect on what you've done."
                ch_x "Emma, I'd like you to stay after for a brief discussion about \"boundaries\". . ."
            
        "Just having a little fun, right [E_Pet]?":
                call Emma_Namecheck
                call EmmaFace("sly")  
                call Statup("Emma", "Lust", 90, 5)       
                if E_Caught < 5:
                    call Statup("Emma", "Inbt", 90, 10)   
                    call Statup("Emma", "Love", 90, 10) 
                call XavierFace("angry")
                $ Count += 10
                ch_x "If that's your attitude, harsher methods might be necessary."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."          
                if E_Caught < 5:            
                    call Statup("Emma", "Obed", 50, 20)
                    call Statup("Emma", "Obed", 90, 20)
                    call Statup("Emma", "Inbt", 30, -20)   
                ch_x "I've had enough of you, begone."
            
        "Just this. . . Plan Psi, Emma!" if P_Lvl >= 5:
                if ApprovalCheck("Emma", 1500, TabM=1, Loc="No"):                   
                        jump Plan_Psi
                elif ApprovalCheck("Emma", 1000, TabM=1, Loc="No"):
                        call EmmaFace("perplexed") 
                        $ E_Brows = "sad"
                        ch_e "Um, I don't believe we're quite at that point yet, [E_Petname]. . ."
                        menu:
                            "Dammit Emma. . .":
                                    call EmmaFace("angry")
                                    call Statup("Emma", "Obed", 50, 5)
                                    call Statup("Emma", "Love", 90, -5) 
                            "Yeah, I guess you're right. . .":
                                    call EmmaFace("bemused") 
                else:
                        call EmmaFace("confused") 
                        ch_e "Lord child, what are you talking about now?"
                        ch_p "Plan {i}Psi!{/i} . . you know. . ."
                        ch_e "I wish that I did."
                        ch_p "Oh, yeah, I guess I haven't mentioned that. . ."
                        call EmmaFace("bemused") 
                call XavierFace("angry")
                $ Count += 10
                ch_x "I have no idea what that was about, but it sounds like you haven't learned."
                if PunishmentX:
                    ch_x "I'm extending your punishment by [Count] days."
                else:
                    ch_x "I'm halving your daily stipend for [Count] days."           
                if E_Caught < 5:           
                    call Statup("Emma", "Obed", 50, 10)
                    call Statup("Emma", "Inbt", 50, -5)   
                ch_x "I've had enough of you, begone."
                        
            
        "You can suck it, old man.":
            call EmmaFace("surprised")      
            call Statup("Emma", "Lust", 90, 10)
            if E_Caught < 5:
                call Statup("Emma", "Love", 90, 5) 
                call Statup("Emma", "Obed", 50, 20)
                call Statup("Emma", "Obed", 90, 30)  
            call XavierFace("angry")
            $ Count += 20
            ch_x "If that's your attitude, harsher methods might be necessary."
            if PunishmentX:
                ch_x "I'm extending your punishment by [Count] days!"
            else:
                ch_x "I'm halving your daily stipend for [Count] days!"       
            if E_Caught < 5:
                if E_Inbt > 50:
                    call Statup("Emma", "Inbt", 90, 15)             
                call Statup("Emma", "Inbt", 30, -20)
                call Statup("Emma", "Inbt", 50, -10)    
            ch_x "Now get out of my sight."
            
    $ PunishmentX += Count            
    $ E_Caught += 1
    $ E_RecentActions.append("caught")
    $ E_DailyActions.append("caught")    
    call Remove_Girl("All")  
    "You return to your room"
    jump Player_Room
#    $ bg_current = "bg player"
#    return
    
label Plan_Psi: #Emma_Update   
    call EmmaFace("sly")         
    "As you say this, a sly grin crosses Emma's face."
    $ E_Arms = 0
    $ Emma_Arms = 2
    "You quickly approach Xavier and place your hands on his head."
    call XavierFace("psychic")
    ch_x ". . ."
    call XavierFace("shocked")
    "Xavier realizes with a shock that with your powers, his telepathy is useless."    
    $ Emma_Arms = 2
    show Emma_Sprite at SpriteLoc(StageLeft+100,85) zorder 24 with ease
    "Emma moves behind Xavier and activates her own telepathy."
    if R_Loc == bg_current and "Omega" not in P_Traits:        
        call RogueFace("surprised")      
        "Rogue looks a bit caught off guard, but goes along with the idea."        
        call RogueFace("sly")
    elif K_Loc == bg_current and "Kappa" not in P_Traits:        
        call KittyFace("surprised")      
        "Kitty looks a bit caught off guard, but goes along with the idea."        
        call KittyFace("sly")
    elif L_Loc == bg_current and "Chi" not in P_Traits:        
        call LauraFace("surprised")      
        "Laura looks a bit caught off guard, but goes along with the idea."        
        call LauraFace("sly")
    call XavierFace("angry")
    
    if "Psi" in P_Traits or "Omega" in P_Traits:
            ch_x "Oh, not again. . ."
            call Statup("Emma", "Obed", 80, 3)
            call Statup("Emma", "Inbt", 80, 1)  
    else:
            call Statup("Emma", "Obed", 50, 40)
            call Statup("Emma", "Inbt", 70, 30)
            call Statup("Emma", "Obed", 200, 30)
            call Statup("Emma", "Inbt", 200, 10)   
    $ Count = 3
    $ PunishmentX = 0
    ch_e "I think we can get 3 demands out of him, like a genie!"
    while Count:
        $ Count -= 1
        menu:
            ch_e "Well, [E_Petname], what should we ask for?"
            "Don't bother us anymore when we're having fun." if "Emma" not in Rules:
                    $ Rules.append("Emma")
            "You know, it's kinda fun dodging you, catch us if you can." if "Emma" in Rules:
                    $ Rules.remove("Emma")
                    if "taboo" in E_History:
                            #this resets the taboo conversation too
                            $ E_History.remove("taboo") 
                            $ E_History.append("taboocheck") 
            "Raise my stipend." if P_Income < 30 and "Psi" not in P_Traits:       
                    $ P_Income += 2
            "Raise my stipend. [[Used](locked)" if P_Income >= 30 or "Psi" in P_Traits:           
                    pass
            "In was interested in a key. . . ":
                menu:
                    "Give me the key to your study." if "Xavier" not in Keys:  
                            $ Keys.append("Xavier")
                    "Give me the key to your study.[[Owned] (locked)" if "Xavier" in Keys:  
                            pass
                            
                    "Give me the key to Rogue's room." if "Rogue" not in Keys:  
                            $ Keys.append("Rogue")
                    "Give me the key to Rogue's room.[[Owned] (locked)" if "Rogue" in Keys:  
                            pass
                    
                    "Give me the key to Kitty's room." if "Kitty" not in Keys:  
                            $ Keys.append("Kitty")
                    "Give me the key to Kitty's room.[[Owned] (locked)" if "Kitty" in Keys:  
                            pass
                    
                    "Never mind the keys.":
                            $ Count += 1
            "That should do it.":
                $ Count = 0
    ch_p "Ok, that's enough. Make Xavier forget that any of this happened, and then let's get out of here." 
    if "Psi" not in P_Traits:
        call Statup("Emma", "Lust", 90, 10)
        call Statup("Emma", "Inbt", 80, 10)
        call Statup("Emma", "Love", 70, 10)
        call Statup("Emma", "Love", 200, 20)
        $ P_Traits.append("Psi")
    $ Emma_Arms = 1
    "You return to your room"
    jump Player_Room
                              
# end Emma_Caught/////////////////////////////////////////////////////



# Emma Taboo Talk Start < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

label Emma_Taboo_Talk:
    # This scene plays when you first try to do sexy stuff with Emma in public
        
    if "taboo" in E_History:  
        return
        
    call EmmaFace("sly")  
    if "taboocheck" not in E_History:   
            ch_e "[E_Petname], I know that we've had some. . . fun,"   
            call EmmaFace("sly", Eyes="side")      
            ch_e "but that was between us, in private."     
            call EmmaFace("sly")  
            ch_e "I can't have our trysts become. . . public knowledge." 
            ch_e "I am a teacher here, you understand."
            ch_e "You're a student."   
            call EmmaFace("sadside")  
            ch_e "It's complicated." 
            ch_e "So I'm afraid that we can only. . ."    
            call EmmaFace("sad")  
            ch_e ". . .interact, when we're alone."
            ch_e "Do you understand?"
    else:
            ch_e "I believe I made clear why I couldn't do anything like that in public. . ."
    
    $ Line = 1
    while Line >= 1:
        menu:
            extend ""
            "Yeah, I suppose.":   
                call EmmaFace("smile") 
                if "taboocheck" in E_History:  
                        pass
                elif Line != 4:
                        #if you didn't ask all the questions first
                        call Statup("Emma", "Love", 60, 10)
                        call Statup("Emma", "Love", 70, 10)
                        call Statup("Emma", "Love", 90, 10)
                        call Statup("Emma", "Obed", 60, 5)
                        call Statup("Emma", "Inbt", 70, 5)  
                else:                    
                        call Statup("Emma", "Love", 60, 10)
                        call Statup("Emma", "Love", 90, 10)  
                    
                ch_e "Thank you for your discretion."
                call EmmaFace("sly")  
                if ApprovalCheck("Emma", 2000) and "taboocheck" in E_History:
                        ch_e "Although. . . I suppose we could make an exception. . ."
                        call Statup("Emma", "Inbt", 90, 10)  
                        $ Line = -1                
                else:
                        ch_e "I do hope that we can still find some time to meet up."
                        $ Line = 0                
                
            "I don't care who sees us." if Line != 2 and Line != 4: 
                if "taboocheck" in E_History:  
                        ch_e "I'm aware. . ."
                        if ApprovalCheck("Emma", 500, "I"):
                                call EmmaFace("sly")  
                                ch_e "Frankly, I don't either."
                                call EmmaFace("angry", Eyes="side")  
                                ch_e "It's not about that though, if we get caught, I get fired." 
                                call EmmaFace("angry")  
                                ch_e "If I get fired, then I can't stay here." 
                                call EmmaFace("sly")  
                                ch_e "So that really isn't an option."
                        else:
                                call EmmaFace("confused", 1)  
                                ch_e "You might not, but I have a reputation to maintain."                        
                elif ApprovalCheck("Emma", 500, "I"):
                        call Statup("Emma", "Lust", 80, 5)
                        call Statup("Emma", "Inbt", 70, 5) 
                        call EmmaFace("sly")  
                        ch_e "Frankly, I don't either."
                        call EmmaFace("angry", Eyes="side")  
                        ch_e "It's not about that though, if we get caught, I get fired." 
                        call EmmaFace("angry")  
                        call Statup("Emma", "Love", 90, 10)
                        call Statup("Emma", "Obed", 60, 10)
                        ch_e "If I get fired, then I can't stay here." 
                        call EmmaFace("sly")  
                        ch_e "So that really isn't an option."
                else:
                        call Statup("Emma", "Lust", 80, 5)
                        call Statup("Emma", "Love", 90, 10)
                        call Statup("Emma", "Obed", 60, 10)
                        call EmmaFace("confused", 1)  
                        ch_e "Well you might not, but I have a reputation to maintain."
                call EmmaFace("sly")  
                ch_e "So can you understand why we must be discrete?"
                $ Line = 4 if Line != 1 else 2 
                        
            "Couldn't you just mindwipe anyone who sees?" if Line != 3 and Line != 4:
                if "taboocheck" in E_History:  
                        ch_e "Yes, we've been over why that wouldn't exactly be an option."
                else:
                        if ApprovalCheck("Emma", 500, "I"):
                            call EmmaFace("sly")  
                            call Statup("Emma", "Lust", 80, 5)
                            call Statup("Emma", "Love", 80, 5)
                            call Statup("Emma", "Obed", 60, 5)
                            call Statup("Emma", "Inbt", 70, 5) 
                            ch_e "You must have read my mind."
                        elif ApprovalCheck("Emma", 800, "LO"):
                            call EmmaFace("sly",1)  
                            call Statup("Emma", "Lust", 80, 5)
                            call Statup("Emma", "Love", 90, 10)
                            call Statup("Emma", "Obed", 60, 10)
                            call Statup("Emma", "Inbt", 70, 5) 
                            ch_e "Oh, you naughty boy." 
                        else:
                            call EmmaFace("surprised",1)  
                            call Statup("Emma", "Lust", 80, 5)
                            call Statup("Emma", "Obed", 60, 10)
                            call Statup("Emma", "Inbt", 50, 15) 
                            call Statup("Emma", "Inbt", 70, 10) 
                            ch_e "What? I would never!"
                        call EmmaFace("angry",Eyes="side")  
                        ch_e "Either way though, that's not really an option either."
                ch_e "I can't muck about with the students' minds too much without Charles catching on."
                ch_e "Casually mindwiping students certainly wouldn't pass unnoticed."
                if "Emma" in Rules:
                    #if Xavier ignores you
                    ch_p "But Xavier is off the board now. . ."
                    call EmmaFace("sly")  
                    ch_e "I suppose that's true. . ."
                    ch_e "A little helpful editing might not hurt. . ."
                    $ Line = -1
                else:
                    call EmmaFace("confused",Mouth="normal")  
                    ch_e "So are we on the same page here?"
                    $ Line = 4 if Line != 1 else 3
            
            "I don't care, let's do it." if Line == 4:
                $ Line = 0
                if ApprovalCheck("Emma", 2000):
                        call EmmaFace("surprised", Eyes="side")  
                        call Statup("Emma", "Lust", 80, 5)
                        call Statup("Emma", "Inbt", 50, 15) 
                        call Statup("Emma", "Inbt", 70, 10) 
                        ch_e "Oh, I will get in so much trouble for this. . ."
                        call Statup("Emma", "Love", 90, 5)
                        call Statup("Emma", "Obed", 60, 15)
                        call EmmaFace("sly")  
                        ch_e "but you're worth it."
                        $ Line = -1
                elif ApprovalCheck("Emma", 800, "I"):
                        call EmmaFace("surprised", Eyes="side")  
                        call Statup("Emma", "Lust", 80, 5)
                        call Statup("Emma", "Obed", 60, 15)
                        ch_e "Oh, I will get in so much trouble for this. . ."
                        call EmmaFace("sly")  
                        ch_e "but it will be so much fun."
                        $ Line = -1
                elif "taboocheck" in E_History:  
                        call EmmaFace("angry")  
                        call Statup("Emma", "Love", 90, -5)
                        call Statup("Emma", "Obed", 60, -5)
                        ch_e "You're going to have to respect my boundaries on this one."
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")
                        $ renpy.pop_call() #drops it past the sex menu
                else:
                        call EmmaFace("angry")  
                        call Statup("Emma", "Love", 90, -5)
                        call Statup("Emma", "Obed", 60, -5)
                        call Statup("Emma", "Inbt", 70, 10) 
                        ch_e "Well that's just too bad."
                        ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                        $ E_RecentActions.append("angry")
                        $ E_DailyActions.append("angry")
                        $ renpy.pop_call() #drops it past the sex menu    
    #end loop if Line < 1
    
    if "taboocheck" not in E_History:    
            $ E_History.append("taboocheck") 
    if Line == -1:
            #if she agrees to do it
            $ E_History.append("taboo") 
            $ E_History.remove("taboocheck") 
    return

# Emma Taboo Talk End < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Emma Threesome Talk Start < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
label Emma_ThreeCheck(Pass=3, Quest = [], B=0):
    # This is called when Emma is asked whether to do a threesome
    if E_SEXP <= 30:
        call EmmaFace("confused")
        ch_e "[E_Petname], I barely put up with you, don't try to bring other girls into this."
        return
    if "three" in E_History:  
        return
    
    if R_Loc == bg_current:
        $ B = (E_LikeRogue - 500)
    elif K_Loc == bg_current:
        $ B = (E_LikeKitty - 500)
    else:
        # skips the girls question if no girls are present
        $ Quest.append(2) 
    
    if "noticed girl" in E_DailyActions:
        call EmmaFace("angry", Eyes = "side") 
        $ Line = 0
        if "noticed Rogue" in E_RecentActions:
                $ Line = "I saw you with Rogue"
        elif "noticed Kitty" in E_RecentActions:
                $ Line = "I saw you with Kitty"
        elif "noticed Laura" in E_RecentActions:
                $ Line = "I saw you with Laura"
        else:
                $ Line = "I saw you with that other girl"
        $ Line = Line + " earlier, I'm not sure how I feel about that."
        ch_e "[Line]"
        $ Line = 0
    if "sleeptime" in E_History:
            # if you tried to have a sleepover
            ch_e "I saw you considering having me sleep over with that. . . girl. . ."
            $ E_History.remove("sleeptime")
            
    
    if "threecheck" not in E_History:   
            call EmmaFace("bemused", Eyes = "side") 
            "Emma moves close to you and whispers. . ."
            if ApprovalCheck("Emma", 900, "L"):
                    ch_e "[E_Petname], I really do. . . care for you. . ."
            elif ApprovalCheck("Emma", 800, "L"):
                    ch_e "[E_Petname], I do think you're. . . interesting. . ."
            elif ApprovalCheck("Emma", 500, "O"):
                    ch_e "[E_Petname], there is something. . . compelling about you. . ."
            elif ApprovalCheck("Emma", 500, "I"):
                    ch_e "[E_Petname], you know that I'm. . . flexible,"
            else:
                    ch_e "[E_Petname], I don't know what this even is yet, but. . ."
            ch_e "I'm a teacher at this school, and I can't exactly be caught forming some sort of. . ."
            ch_e "harem with the students." 
            ch_e "Just you and I would be scandalous, but multiple students?"
            ch_e "That could be a disaster." 
    else:
            ch_e "I already explained why I couldn't do this around other girls."
    while Pass > 0:
        menu:
            extend ""
            "Yeah, I suppose.":
                    call EmmaFace("smile")   
                    if "threecheck" not in E_History:      
                        call Statup("Emma", "Love", 60, 10)
                        call Statup("Emma", "Love", 90, 10)  
                        
                    ch_e "Thank you for not insisting."
                    call EmmaFace("sly")  
                    if Pass == 1 and ApprovalCheck("Emma", 2000):
                        ch_e "though I suppose. . . perhaps I could make an exception. . ."
                        $ Pass = 0   
                    else:
                        ch_e "I do hope that we can still find some. . . personal time?"
                        $ Pass = -1     
                
            "But she's cool with it." if 2 not in Quest:
                    # This can add up to 2 if both girls refuse, or -2 if both are really into it.
                    # -1 more likely
                    $ Quest.append(2)  
                    if R_Loc == bg_current:
                            $ Pass -= 1 
                            if "poly Emma" in R_Traits: 
                                    #If Rogue is already on board
                                    ch_r "Yeah, like I said, ready when you are."
                            else:
                                    $ R_Traits.append("poly Emma") 
                                    if ApprovalCheck("Rogue", 1500) and R_LikeEmma >= 800:
                                        ch_r "I really am."
                                    elif ApprovalCheck("Rogue", 1500) and R_LikeEmma >= 600:
                                        ch_r "Yeah, you'll do."
                                    elif ApprovalCheck("Rogue", 2000):
                                        ch_r "You and I get along like cats and bitches. . ."
                                        ch_r "but I do want to make him happy."
                                    elif ApprovalCheck("Rogue", 500) and R_LikeEmma >= 800:
                                        ch_r "This guy I could take or leave, but you clean up real nice."
                                    else:
                                        ch_k "I said no such thing!"
                                        $ R_Traits.remove("poly Emma") 
                                        $ Pass += 1
                            #End Rogue
                    elif K_Loc == bg_current:
                            $ Pass -= 1
                            if "poly Emma" in K_Traits: 
                                    #If Kitty is already on board
                                    ch_k "Yup, sounds fun."
                            else:
                                    $ K_Traits.append("poly Emma") 
                                    if ApprovalCheck("Kitty", 1500) and K_LikeEmma >= 800:
                                        ch_k "Yeah, you bet."
                                    elif ApprovalCheck("Kitty", 1500) and K_LikeEmma >= 600:
                                        ch_k "Yeah, you're ok."
                                    elif ApprovalCheck("Kitty", 2000):
                                        ch_k "I don't like you much, but I do want him to be happy."
                                    elif ApprovalCheck("Kitty", 500) and K_LikeEmma >= 800:
                                        ch_k "Well, I don't know about this guy, but. . . you're pretty."
                                    else:
                                        ch_k "I didn't say anything like that!"
                                        $ K_Traits.remove("poly Emma") 
                                        $ Pass += 1
                            #End Kitty
                            
                    if B >= 400:
                        ch_e "And you're quite fetching yourself dear. . ."
                        $ Pass -= 1 if Pass > 0 else 0
                    elif B >= 0:
                        ch_e "And you're. . . acceptable. . ."
                    else:
                        ch_e "And that's just lovely, really. . ."
                        $ Pass += 1
                    ch_e "But I'm afraid that any sort of dalliance would be an issue."
            #end "she's cool with it"
            
            "Xavier doesn't care." if Taboo and "Emma" in Rules and 3 not in Quest:
                    $ Quest.append(3)  
                    ch_e "Well, that may be, but it could still get out."
                    $ Pass -= 1
                    
            "Xavier won't find out here." if not Taboo and 3 not in Quest:
                    $ Quest.append(3)  
                    ch_e "Well, that may be, but it could still get out."
                    $ Pass -= 1
                    
            "I don't care, let's do this." if Quest:
                    if ApprovalCheck("Emma", 2000) and Pass <= 2:
                            call EmmaFace("surprised", Eyes="side")  
                            call Statup("Emma", "Lust", 80, 5)
                            call Statup("Emma", "Inbt", 50, 15) 
                            call Statup("Emma", "Inbt", 70, 10) 
                            call Statup("Emma", "Love", 90, 5)
                            call Statup("Emma", "Obed", 60, 15)
                            ch_e "Oh, I could get in so much trouble for this. . ."
                            call EmmaFace("sly")  
                            ch_e "but you're worth it."
                            $ Pass = 0
                    elif ApprovalCheck("Emma", 800, "I") and Pass <= 2:
                            call EmmaFace("surprised", Eyes="side")  
                            call Statup("Emma", "Lust", 80, 5)
                            call Statup("Emma", "Obed", 60, 15)
                            ch_e "Oh, I could get in so much trouble for this. . ."
                            call EmmaFace("sly")  
                            ch_e "but it will be so much fun."
                            $ Pass = 0
                    elif "threecheck" not in E_History:  
                            call EmmaFace("angry")  
                            call Statup("Emma", "Love", 90, -5)
                            call Statup("Emma", "Obed", 60, -5)
                            ch_e "You're going to have to learn to take \"no\" for an answer on this one."
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")
                            $ Pass = -1
                    else:
                            call EmmaFace("angry")  
                            call Statup("Emma", "Love", 90, -5)
                            call Statup("Emma", "Obed", 60, -5)
                            call Statup("Emma", "Inbt", 70, 10) 
                            ch_e "Well that's just too bad."
                            ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                            $ E_RecentActions.append("angry")
                            $ E_DailyActions.append("angry")
                            $ Pass = -1
    
    if "threecheck" not in E_History:    
            $ E_History.append("threecheck") 
    if Pass == -1:
        # if the conditions added up to failure state, it exits the sex menu
        $ renpy.pop_call() #drops it past the sex menu  
    else:
        #if the conditions don't add up to failure, then it results in a success state
        $ E_History.append("three") 
        $ E_History.remove("threecheck") 
        if R_Loc == bg_current:
            if "poly Rogue" not in E_Traits: 
                    $ E_Traits.append("poly Rogue") 
            $ E_RecentActions.append("noticed Rogue")
            $ R_RecentActions.append("noticed Emma")
        elif K_Loc == bg_current:
            if "poly Kitty" not in E_Traits: 
                    $ E_Traits.append("poly Kitty") 
            $ E_RecentActions.append("noticed Kitty")
            $ K_RecentActions.append("noticed Emma")
            
    return
# Emma Threesome Talk End < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# start Emma_BF//////////////////////////////////////////////////////////


label Emma_BF:
    call Shift_Focus("Emma")
    
    if E_Loc != bg_current:
        $ E_Loc = bg_current
        if "Emma" not in Party:
            "Emma approaches you and asks if the two of you can talk."
        else:   
            "Emma turns towards you and asks if the two of you can talk."
                
    call Set_The_Scene(0)
    call Display_Emma
    "You can tell she's a bit uncomfortable about whatever she has to say." 
    call Taboo_Level
    call CleartheRoom("Emma")
    $ E_DailyActions.append("relationship")
    call EmmaFace("bemused", 1)
    
    ch_e "[E_Petname], we've been. . . enjoying ourselves for a while now."
    ch_e ". . ."
    $ E_Eyes = "sexy"
    menu:
        ch_e "You have been enjoying yourself?"
        "Yeah. And it's been amazing.":
            call Statup("Emma", "Love", 200, 20)
        "Yeah, I guess":
            call Statup("Emma", "Love", 200, 10)
        "Uhm. . .maybe?":
            call Statup("Emma", "Love", 200, -10)
            call Statup("Emma", "Obed", 200, 30)
    if E_SEXP >= 10:
        ch_e "I think we've been engaging in some rather inappropriate behavior. . ."
    if E_SEXP >= 15:
        ch_e "-for a student and teacher, at least. . ."
    if len(P_Harem) >= 2:
        ch_e "I understand that this isn't an exclusive deal for you. . ."
    elif P_Harem:
            ch_e "I understand that you've been dating [P_Harem[0]]. . ."
        
    if not E_Event[5]:
        ch_e "So, that being the case. . ."
        ch_e "I was wondering if you'd like to make this a bit more official."
        ch_e "If I could perhaps consider you my. . ."
        ch_e "Boyfriend?"
        ch_e "-or something to that effect."
    elif P_Harem: 
        ch_e ". . . but I would still like to also consider you my boyfriend as well."
    else:        
        ch_e "I don't know why I put up with you, but I do still want to be your girlfriend."
    $ E_Event[5] += 1
    menu: 
        extend ""
        "Are you kidding? I'd love to!":
            call Statup("Emma", "Love", 200, 25)
            "Emma wraps her arms around you and starts kissing you passionately."
            call EmmaFace("kiss") 
            call E_Kissing_Launch("kiss you")
            $ E_Kissed += 1
        "Uhm, okay.":
            $E_Brows = "confused"
            "Emma seems a little put off by how casually you’re taking all this."  
        "I'm with someone else now." if P_Harem:             
            call EmmaFace("sad",1)    
            ch_e "I understand.  I thought that perhaps you could go out with me as well?"
            menu:
                extend ""
                "Yes. Absolutely." if "EmmaYes" in P_Traits:
                    call Statup("Emma", "Love", 200, 30)
                    "Emma wraps her arms around you and starts kissing you passionately."
                    call EmmaFace("kiss") 
                    call E_Kissing_Launch("kiss you")
                    $ E_Kissed += 1
                "She wouldn't understand." if len(P_Harem) == 1:
                    $ Line = "no."
                "They wouldn't be cool with that." if len(P_Harem) > 1:
                    $ Line = "no."
                "I'm sorry, but. . . no." if E_Event[5] != 20:
                    $ Line = "no."
                "No way.":
                    jump Emma_BF_Jerk
            if Line == "no":                
                    call Statup("Emma", "Love", 200, -10)
                    ch_e "Well. . ." 
                    ch_e "I suppose I understand." 
                    $ E_Event[5] = 20 
                    call Remove_Girl("Emma")  
                    $ Line = 0
                    return
        "Not really.":
            jump Emma_BF_Jerk
    
    if "Historia" not in P_Traits:
            $ P_Harem.append("Emma")
            if "EmmaYes" in P_Traits:       
                    $ P_Traits.remove("EmmaYes")
    $ E_Petnames.append("boyfriend")
    $ E_Traits.append("dating")
    call EmmaFace("sexy")    
    ch_e "So then. . . how would you like to celebrate?"
    if "Historia" in P_Traits:
            return 1
    $ Tempmod = 10
    call Emma_SexMenu
    $ Tempmod = 0
    return
    
label Emma_BF_Jerk:
    call EmmaFace("angry", 1)
    ch_e "Well! Suit yourself." 
    call Statup("Emma", "Obed", 50, 40)
    if E_Event[5] != 20:
            call Statup("Emma", "Obed", 200, (20* E_Event[5]))
    if 20 > E_Event[5] >= 3:
            call EmmaFace("sad")
            ch_e "You know, I'm tired of caring what you think about the matter." 
            ch_e "I'm doing to consider us a couple whether you approve or not."
            ch_e "And with that, adieu."        
            if "Historia" in P_Traits:
                    return 1  
            $ E_Petnames.append("boyfriend")
            $ E_Traits.append("dating")
            $ Achievements.append("I am not your Boyfriend!")
            $ bg_current = "bg player"  
            call Remove_Girl("Emma")   
            call Set_The_Scene
            $ renpy.pop_call()
            jump Player_Room
    if E_Event[5] > 1:
            ch_e "It was such a mistake asking you again.  You still need to mature."
    if E_Event[5] != 20:
            call Statup("Emma", "Love", 200, -(50* E_Event[5]))
    else:
            call Statup("Emma", "Love", 200, -50)
    ch_e "Get away from me."
    if "Historia" in P_Traits:
            return
    $ bg_current = "bg player"  
    call Remove_Girl("Emma")  
    $ renpy.pop_call()
    jump Player_Room
    
## start Emma_Love//////////////////////////////////////////////////////////
label Emma_Love(Shipping=[],Shipshape=0):   
    # SHipping is used to track who else you're involved with
    if ApprovalCheck("Rogue", 1200, "LO"):
            $ Shipping.append("Rogue") 
    if ApprovalCheck("Kitty", 1200, "LO"):
            $ Shipping.append("Kitty")
    if ApprovalCheck("Laura", 1200, "LO"):
            $ Shipping.append("Laura")
    $ Shipshape = len(Shipping)
        
    if E_Loc == bg_current or "Emma" in Party:
            "Emma glances over at you with an apprising look on her face."
    else:
            "Emma turns a corner and notices you."
    if bg_current != "bg emma" and bg_current != "bg player":           
            "With little word, she takes your hand and pulls you back to her room."
            $ bg_current = "bg emma"
    $ E_Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Emma")
    call Taboo_Level
    $ E_DailyActions.append("relationship")
        
    call EmmaFace("sexy",Eyes="side")
    ch_e "As you are aware, this. . . situation has been going for a while now."
    ch_e "It's been very. . . comfortable for me."
    call EmmaFace("sexy")
    ch_e "I have enjoyed your company. . . is what I'm trying to say."
    menu:
            extend ""
            "It's more than just company, we're together in this.":
                call EmmaFace("smile",1)
                call Statup("Emma", "Love", 200, 10)
                call Statup("Emma", "Inbt", 90, 5)
                ch_e "Yes!"
                ch_e "Yes, we certainly are more than that."                
                call EmmaFace("sly")
                ch_e "You must have read my mind."
            "I've enjoyed it a lot too.":
                call EmmaFace("sly")
                call Statup("Emma", "Love", 200, 5)
                call Statup("Emma", "Obed", 90, 2)
                ch_e "Yes, I imagine you have." 
                ch_e "Perhaps it was more than that though. . ."
            "Yeah, it's been fun.":
                call EmmaFace("confused")
                call Statup("Emma", "Obed", 90, 5)
                ch_e "Yes, \"fun.\""
                call EmmaFace("angry",Eyes="side")
                ch_e "It is fun, but I was thinking. . ."
                call EmmaFace("sly")
            "Oh, ok.":
                call EmmaFace("confused",Eyes="side")
                ch_e "Um, yes. . ."
                ch_e ". . ."
                call EmmaFace("confused")
                ch_e "I'm not sure I was clear. . ."
            "Yeah, you're a good ride.":
                call EmmaFace("angry")
                if not ApprovalCheck("Emma", 1600):
                        call Statup("Emma", "Obed", 90, -5)
                        call Statup("Emma", "Inbt", 90, -5)
                        $ E_Eyes="side"
                        ch_e "Never mind, this was a bad idea."
                        jump Emma_Love_End 
                ch_e "Such impertinence!"      
                if ApprovalCheck("Emma", 1000, "OI"):
                        call EmmaFace("sly",2)
                        call Statup("Emma", "Obed", 90, 10)
                        call Statup("Emma", "Inbt", 90, 5)
                        call Statup("Emma", "Lust", 70, 5)
                        ch_e "I am though, yes."
                        $ E_Blush = 1
                else:
                        call EmmaFace("sexy")
                        call Statup("Emma", "Obed", 90, 5)
                        call Statup("Emma", "Inbt", 90, 5)
                        ch_e "I suppose that's part of your charm though."
                    
    ch_e "I certainly do care for you. . ."
    ch_e "Perhaps more than I have for anyone else in a long time."
    if ApprovalCheck("Emma", 1600):
            call EmmaFace("sexy",Eyes="side")
            ch_e "Perhaps more than I ever have."
    ch_e ". . ."
    ch_e "What I'm trying to say is. . ."
    call EmmaFace("sexy",Brows="sad")
    ch_e "I love you."
    
    menu:
            extend ""
            "I love you too, [E_Pet]!":
                call EmmaFace("smile",2)
                call Statup("Emma", "Love", 200, 20)
                call Statup("Emma", "Inbt", 90, 10)
                ch_e "I dearly hoped that you did!"
                $ E_Petnames.append("lover")
                jump Emma_Love_End
            "Wow! That's cool.":
                call EmmaFace("confused")
                call Statup("Emma", "Love", 200, 5)
                ch_e "Cool?"
                ch_e "Don't you have anything else you'd like to say to me?"                
                call EmmaFace("sadside",2)
            "Oh, ok.":
                call EmmaFace("confused",2)
                call Statup("Emma", "Obed", 90, 5)
                call Statup("Emma", "Inbt", 90, -5)
                ch_e "Ok?"
                call EmmaFace("angry")
                ch_e "Is that all the response you have for me?"
            "Ha!":
                call EmmaFace("surprised",2)
                call Statup("Emma", "Love", 200, -5)
                call Statup("Emma", "Obed", 90, 10)
                call Statup("Emma", "Inbt", 90, -5)
                ch_e "!"
                call EmmaFace("angry",2)
                ch_e "Well that's hardly the response I expected."
                      
    ch_e "I would hope that you also love me. . ."
    
    menu:
            extend ""
            "Oh! Yes, of course I love you, [E_Pet]!":
                call EmmaFace("smile",2)
                call Statup("Emma", "Love", 90, 15)
                call Statup("Emma", "Obed", 90, 2)
                ch_e "I dearly hoped that you did!"
                $ E_Petnames.append("lover")
                jump Emma_Love_End              
            "Oh. Oooooh! Yeah, sure.":
                if ApprovalCheck("Emma", 1200, "OI"):
                        call EmmaFace("sly",1)
                        call Statup("Emma", "Love", 200, 5)
                        call Statup("Emma", "Obed", 90, 10)
                if ApprovalCheck("Emma", 1200, "OI"):
                        call EmmaFace("sly",1,Brows="angry")
                        call Statup("Emma", "Love", 200, 5)
                        call Statup("Emma", "Obed", 90, 5)
                        call Statup("Emma", "Inbt", 90, -5)
                ch_e "I'm glad to see that you caught up with the situation."
            "Oh. That's awkward.":
                call EmmaFace("angry",2)
                call Statup("Emma", "Love", 200, -15)
                call Statup("Emma", "Obed", 90, 15)
                call Statup("Emma", "Inbt", 90, -10)
                ch_e "Awkward?!"
                ch_e "This situation is about to become considerably more \"awkward.\""
                $ E_Blush = 1
                $ Line = "angry"    
        
    ch_e "I'm giving you one last chance here."
    ch_e "This is not a time for fooling around."
    ch_e "Do you love me, or not?"
        
    menu:
            extend ""
            "Yes, of course I love you, [E_Pet]!":
                call EmmaFace("sly",2)
                call Statup("Emma", "Love", 90, 5)
                call Statup("Emma", "Obed", 90, 15)
                call Statup("Emma", "Inbt", 90, 5)
                ch_e "Took you long enough to get there."
                $ E_Petnames.append("lover")
                jump Emma_Love_End            
            "I can't really say yet.":
                if Line != "angry" or ApprovalCheck("Emma", 800, "OI"):                    
                    call EmmaFace("sadside")
                    call Statup("Emma", "Obed", 90, 5)
                else:
                    call EmmaFace("angry") 
                    call Statup("Emma", "Love", 200, -5)
                    call Statup("Emma", "Obed", 90, 5)
                    call Statup("Emma", "Inbt", 90, -5)                 
                ch_e "Oh." 
            "No.":
                if Line == "angry" or not ApprovalCheck("Emma", 800, "OI"): 
                    call EmmaFace("angry")  
                    call Statup("Emma", "Love", 200, -10)
                    call Statup("Emma", "Obed", 90, 10)
                    call Statup("Emma", "Inbt", 90, -5)          
                else:        
                    call EmmaFace("sadside")
                    call Statup("Emma", "Love", 200, -10)
                    call Statup("Emma", "Obed", 90, 10)
                    call Statup("Emma", "Inbt", 90, -5)
                ch_e "Oh."
    
       
    ch_e "Is it because of someone else?"
    $ Line = 0
    menu:
            extend ""
            "Yes, it's Rogue." if "Rogue" in Shipping and Shipshape < 3:
                $ Line = "Rogue"
            "Yes, it's Kitty." if "Kitty" in Shipping and Shipshape < 3:
                $ Line = "Kitty"
            "Yes, it's Laura." if "Laura" in Shipping and Shipshape < 3:
                $ Line = "Laura"
            "Yes, it's the others" if Shipshape > 1:
                call Statup("Emma", "Obed", 90, 15)
                call Statup("Emma", "Inbt", 90, 5)
                call Statup("Emma", "Lust", 90, 5)
                ch_e "I suppose I can't blame you there."
            "There's nobody else.":
                call EmmaFace("sadside")
                call Statup("Emma", "Love", 200, -15)
                call Statup("Emma", "Obed", 90, 15)
                call Statup("Emma", "Inbt", 90, 5)
                if ApprovalCheck("Emma", 1000, "OI"):
                    ch_e "Hmmm. . . well I suppose I can take solace in that."
                else:
                    ch_e "I see."
            "It's a \"you\" problem.":
                call EmmaFace("angry")
                call Statup("Emma", "Love", 200, -25)
                call Statup("Emma", "Obed", 90, 15)
                ch_e "Oh is it now?" 
                call Statup("Emma", "Love", 200, -10)
                ch_e "I can think of a great many ways to make this a \"you\" problem."
                $ E_RecentActions.append("angry")
                $ E_DailyActions.append("angry")
   
   
    if Line:        
            #If you called out a girl,
            if GirlLikeCheck("Emma",Line) >= 800:
                    call Statup("Emma", "Love", 200, 5)
                    call Statup("Emma", "Obed", 90, 20)
                    call Statup("Emma", "Inbt", 90, 5)
                    call Statup("Emma", "Lust", 90, 5)
                    ch_e "Yes, she is lovely."
            else:
                    call EmmaFace("angry",Eyes="side") 
                    call Statup("Emma", "Love", 200, -5)
                    call Statup("Emma", "Obed", 90, 20)          
                    ch_e "That cow!"
                    $ E_RecentActions.append("angry")
                    call GirlLikesGirl("Emma",Line,800,-50,1)                    
    ch_e "I suppose I'll just have to let this go."
    ch_e "I'll. . . see you in a bit."
    ch_e "I need some time to consider this."
        
            
label Emma_Love_End:
    if "lover" not in E_Petnames:  
            hide Emma_Sprite with easeoutright
            call Remove_Girl("Emma")
            $ E_Loc = "hold" #puts her off the board for the day
            return
        
    "Emma pulls closer to you and snuggles into your arms."
    call Statup("Emma", "Love", 200, 25)
    call Statup("Emma", "Lust", 90, 5)
    ch_e "So. . . now that we have some time together. . ."
    call Statup("Emma", "Lust", 90, 10)
    
    if not E_Sex:
        ch_e "I think we've certainly waited long enough. . ."
    else:
        ch_e "Whatever do you intend to do about it?"        
    menu:
            extend ""
            "Yeah, let's do this. . . [[have sex]":      
                call Statup("Emma", "Inbt", 30, 20) 
                call Statup("Emma", "Obed", 70, 10)
                ch_e "Hmm. . ."  
                call Emma_SexAct("sex")
            "I have something else in mind. . .[[choose another activity]":
                $ E_Brows = "confused"
                call Statup("Emma", "Obed", 70, 25)
                ch_e "Something like. . ."    
                $ Tempmod = 20
                call Emma_SexMenu   
    return
        
label Emma_Love_Redux:  
     #this is for if you rejected her but want a second chance
    $ Line = 0
    $ E_DailyActions.append("relationship")
    if E_Event[6] >= 25:
            #if this is the second time through
            ch_p "I hope you've forgiven me, I still love you."
            call Statup("Emma", "Love", 95, 10) 
            if ApprovalCheck("Emma", 950, "L"):
                $ Line = "love"
            else:
                call EmmaFace("angry")   
                ch_e "I don't believe you're sufficiently contrite, [E_Petname]."
                $ E_Eyes="side"
                ch_e ". . ."                
                call EmmaFace("angry",Mouth="lipbite") 
                ch_e "I didn't tell you to stop." 
    else:
            ch_p "Remember when I told you that I didn't love you?"
            call EmmaFace("perplexed",1)   
            ch_e ". . ."
            call EmmaFace("angry", Eyes="side")               
            ch_e "I believe I do remember something to that effect, yes."
    if Line != "love":
            menu:
                extend ""
                "I'm sorry, I didn't mean it.":
                    $ E_Eyes = "surprised"
                    ch_e "Oh? So you do love me?"
                    ch_p "Yeah. I mean, yes, I love you, Emma."
                    call Statup("Emma", "Love", 200, 10) 
                    if ApprovalCheck("Emma", 950, "L"):
                        $ Line = "love"
                    else:
                        call EmmaFace("sadside")   
                        ch_e "I'm not sure that I still do. . ."                        
                "I've changed my mind, so. . .":
                    if ApprovalCheck("Emma", 950, "L"):
                        $ Line = "love"
                        $ E_Eyes = "surprised"
                        ch_e "Oh?"
                    else:
                        $ E_Mouth = "sad"
                        ch_e "Oh, you've changed your mind. Lovely."
                        call Statup("Emma", "Inbt", 90, 10) 
                        call EmmaFace("sadside")    
                        ch_e "Perhaps I have too. . ."
                "Um, never mind.":
                    call Statup("Emma", "Love", 200, -30) 
                    call Statup("Emma", "Obed", 50, 10)  
                    call EmmaFace("angry")   
                    ch_e "Don't you dare."
                    $ E_RecentActions.append("angry")
    if Line == "love":
            call Statup("Emma", "Love", 200, 40) 
            call Statup("Emma", "Obed", 90, 10)
            call Statup("Emma", "Inbt", 90, 10) 
            call EmmaFace("smile")    
            ch_e "I couldn't be happier!"
            ch_e "I love you too, [E_Petname]!"
            if E_Event[6] < 25:             
                call EmmaFace("sly")   
                "She grabs the back of your head and pulls you close."
                ch_e "You shouldn't have kept me waiting."
            $ E_Petnames.append("lover")       
    $ E_Event[6] = 25
    return

# start Emma_Sub//////////////////////////////////////////////////////////

label Emma_Sub:     #Emma_Update   
    call Shift_Focus("Emma")        
    
    $ E_Loc = bg_current
    call Set_The_Scene    
    if E_Loc != bg_current and "Emma" not in Party:
        "Emma shows up and says she needs to talk to you."
    else:
        "Emma approaches you, looking to talk."
    call CleartheRoom("Emma")
    call Taboo_Level
    $ E_DailyActions.append("relationship")
    call EmmaFace("bemused", 1)
    
    $ Line = 0
    ch_e "I've been noticing, you have a sort of"
    ch_e ". . . commanding air about you, [E_Petname]."
    menu:    
        extend ""        
        "I guess. That's just kind of what comes naturally for me.":   
                call Statup("Emma", "Obed", 200, 10)
                call Statup("Emma", "Inbt", 50, 5)
        "Sorry. I didn't mean to come off like that.":
                call EmmaFace("startled", 2)
                call Statup("Emma", "Love", 80, 5)
                call Statup("Emma", "Obed", 200, -5)
                call Statup("Emma", "Inbt", 50, -5)
                ch_e "Oh, don't apologize. . ." 
        "Yup. Deal with it.": 
                if ApprovalCheck("Emma", 1000, "LO"):
                        call Statup("Emma", "Obed", 200, 20)
                        call Statup("Emma", "Inbt", 50, 10)
                        ch_e "Ehem. . ."
                else:
                        call Statup("Emma", "Love", 200, -10)
                        call Statup("Emma", "Obed", 200, 10)
                        call Statup("Emma", "Inbt", 50, 5)
                        call EmmaFace("angry")
                        ch_e "Well, that wasn't exactly what I had in mind." #(Loss of points)
                        menu:        
                            extend ""
                            "Guess you don't know me so well, huh?":
                                    ch_e "I suppose that I don't."
                                    $ Line = "rude"
                            "Sorry.  I kind of thought you were getting into me being like that.": 
                                    call EmmaFace("sexy", 2)
                                    $ E_Eyes = "side"
                                    call Statup("Emma", "Love", 95, 5)
                                    call Statup("Emma", "Obed", 200, 5)
                                    call Statup("Emma", "Inbt", 50, 5)
                                    ch_e "Not. . . quite like that, no. . ."
           
    if not Line:
            # She's advancing to the next stage            
            ch_e "What I was getting at, is that I think that I tend to. . ."
            call EmmaFace("sly", 2)
            ch_e "-enjoy when you take a firm hand with me."
            call EmmaFace("smile", 1)
            menu:
                extend ""
                "Good. If you wanna be with me, that's how it'll be.":
                        if ApprovalCheck("Emma", 1000, "LO"):
                            call Statup("Emma", "Obed", 200, 15)
                            call Statup("Emma", "Inbt", 50, 10)                    
                        else:
                            call EmmaFace("sadside", 1)
                            call Statup("Emma", "Love", 200, -5)
                            call Statup("Emma", "Obed", 200, 10) 
                        ch_e "Perhaps with a touch more class, [E_Petname]. . ." 
                        menu:      
                            extend ""
                            "Whatever.  That's how it is.  Take it or leave it.":
                                    call EmmaFace("angry")
                                    call Statup("Emma", "Love", 200, -10)
                                    call Statup("Emma", "Obed", 200, 5)
                                    ch_e "I suppose you could use a bit more maturity first." 
                                    $ Line = "rude"
                            "I think I could maybe do that." : 
                                    call EmmaFace("bemused", 2)
                                    $ E_Eyes = "side"
                                    call Statup("Emma", "Love", 95, 5)
                                    call Statup("Emma", "Obed", 200, 3)
                                    call Statup("Emma", "Inbt", 50, 5)
                                    ch_e "That's good to hear."
                                
                "Yeah?  You think it's sexy?":
                            call EmmaFace("bemused", 2)
                            $ E_Eyes = "side"
                            call Statup("Emma", "Obed", 200, 5)
                            call Statup("Emma", "Inbt", 50, 10)
                            
                        
                "You sure you don't want me to back off a little?":  
                        call EmmaFace("startled", 1)
                        call Statup("Emma", "Obed", 200, -5)
                        menu:
                            ch_e "I wouldn't want to make you. . . uncomfortable."
                            "Only if you're okay with it.":
                                call EmmaFace("bemused", 2)
                                call Statup("Emma", "Love", 95, 10)
                                call Statup("Emma", "Inbt", 50, 10)
                                $ Line = 0
                            "Uhm. . .yeah.  I {i}do{/i} think it's weird.  Sorry.":                                
                                call Statup("Emma", "Love", 200, -15)
                                call Statup("Emma", "Obed", 200, -5)
                                call Statup("Emma", "Inbt", 50, -10)
                                $ Line = "embarrassed"
                        
                "I don't really care what you like.  I do what I want.":
                            call Statup("Emma", "Love", 200, -10)
                            call Statup("Emma", "Obed", 200, 15)
                            call EmmaFace("angry")
                            ch_e "Ugh. I think I may have misjudged you." 
                            $ Line = "rude"
                                        
    if not Line:
        call EmmaFace("bemused", 1, Eyes="side")
        ch_e "I'm more used to being in charge of the sitation."
        ch_e "When you take control of things. . ."
        ch_e "I find it quite. . . exciting."
        menu:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                    call Statup("Emma", "Love", 200, -5)
                    call Statup("Emma", "Inbt", 50, -15)
                    ch_e "Not at all, just perhaps a bit. . . unconventional."
            "I think I could get used to that kinda thing.":
                    call Statup("Emma", "Obed", 200, 5)
                    call Statup("Emma", "Inbt", 50, 5)
                    call EmmaFace("smile", 1)

    if not Line:
        call EmmaFace("smile", 1)
        ch_e "That sounds delightful. If you don't mind, could I refer to you as. . . sir?"
        call EmmaFace("sly", 2)
        ch_e "Would you enjoy that?"        
        $ E_Blush = 1  
        menu:
            extend ""
            "That has a nice ring to it.":
                    call Statup("Emma", "Love", 95, 5)
                    call Statup("Emma", "Obed", 200, 15)
                    call Statup("Emma", "Inbt", 50, 5)
                    ch_e "Very well then. . .{i}sir{/i}."              
                    $ E_Petname = "sir"
            "I think I'd rather stick with what we've got going.":
                call EmmaFace("confused", 2)
                ch_e "Hmm."
                call Statup("Emma", "Inbt", 50, -5)
                call EmmaFace("sadside", 1)
                menu:
                    ch_e ". . . could you perhaps still take the lead in things?"
                    "I like that idea.":
                            call Statup("Emma", "Obed", 200, 10)
                            call EmmaFace("smile", 1)
                            ch_e "That should do then, [E_Petname]."
                    "This is getting really awkward.":
                            call Statup("Emma", "Love", 200, -10)
                            call Statup("Emma", "Obed", 200, -50)
                            call Statup("Emma", "Inbt", 50, -15)
                            $Line = "embarrassed"
        
#Emma_Sub_Bad_End:
    $ E_History.append("sir")
    if not Line:
            $ E_Blush = 1  
            "She gives you a piece of paper with the password for her cellphone calender."
            "Apparently, whatever you enter into it, she intends to do. . . within reason."
            $ E_Petnames.append("sir")
            #put in stuff that happens if this succeeds
    elif Line == "rude":        
            hide Emma_Sprite with easeoutright                    
            call Remove_Girl("Emma")
            $ renpy.pop_call()
            "Emma marches out the door in a huff, leaving you alone."
    elif Line == "embarrassed":
            call EmmaFace("sad", 2)
            ch_e "Well, I. . . um. . .."
            call EmmaFace("sly", 1)
            ch_e "I was testing you. Obviously. That would be unprofessional."
            call EmmaFace("sadside", 2)
            ch_e "I should go.  I think I see a student over there in need."
            $ E_Blush = 1            
            hide Emma_Sprite with easeoutright                     
            call Remove_Girl("Emma")
            $ renpy.pop_call()
            "Emma dashes out the door, leaving you alone. It didn't look like she could get away fast enough."
    return

label Emma_Sub_Asked: #Emma_Update   
    $ Line = 0
    call EmmaFace("sadside", 1)
    ch_e "I might."
    ch_e "If I did, I would also remember that you seemed unprepared for the role."
    menu:
        extend ""
        "Well, I wanted to say I was sorry.  And I was hoping maybe we could give it another shot.":
                if "sir" in E_Petnames and ApprovalCheck("Emma", 850, "O"): 
                        #if this is asking about the "master" name, and her Obedience is higher than 700
                        pass
                elif ApprovalCheck("Emma", 550, "O"): 
                        #if it's instead about earning the "sir" title, and her approval is over 500 
                        pass
                else: #if it failed both those things,    
                        ch_e "Perhaps when you've done a bit more soul-searching. . ." #Failed again. :(       
                        $ Line = "rude"
                        
                if Line != "rude":    
                        call Statup("Emma", "Love", 90, 10)
                        call EmmaFace("sly", 1)
                        ch_e "I suppose I could give you another chance."                         
                        ch_e "I appreciate that you recognize you made an error."
                        #Blushing expression.  Emma kisses player and big addition of points
                        ch_e "Fine, we can give it another try." 

        "Listen. . .I know it's what you want.  Do you want to try again, or not?":
                call EmmaFace("bemused", 1)
                if "sir" in E_Petnames and ApprovalCheck("Emma", 850, "O"): 
                        ch_e "Ok, fine."
                elif not ApprovalCheck("Emma", 600, "O"): 
                        ch_e "Not at the moment, no."
                        $ Line = "rude"
                else: 
                        #if it's instead about earning the "sir" title, and her approval is over 500
                        call EmmaFace("sadside", 1) 
                        ch_e "You do tend to push your luck."
                        $ E_Eyes = "squint"
                        ch_e "Perhaps you are right, but I do think an apology is still in order."
                        menu:
                            extend ""
                            "Okay, I'm sorry I was so rude about it.":
                                    call Statup("Emma", "Love", 90, 15)
                                    call Statup("Emma", "Inbt", 50, 10)
                                    call EmmaFace("bemused", 1, Eyes="side")
                                    ch_e "Apology accepted. . ."
                            "Not gonna happen.":
                                    if "sir" in E_Petnames and ApprovalCheck("Emma", 900, "O"): 
                                            call Statup("Emma", "Love", 200, -5)
                                            call Statup("Emma", "Obed", 200, 10)
                                            ch_e ". . ."
                                    elif ApprovalCheck("Emma",650, "O"):  
                                            call Statup("Emma", "Love", 200, -5)
                                            call Statup("Emma", "Obed", 200, 10)
                                            ch_e "I- um. . .hmmm. . ."    
                                    else: #if it failed both those things,     
                                            call Statup("Emma", "Love", 200, -10)
                                            call Statup("Emma", "Obed", 90, -10)
                                            call Statup("Emma", "Obed", 200, -10)
                                            call Statup("Emma", "Inbt", 50, -15)                       
                                            "Emma sighs and rolls her eyes."
                                            call EmmaFace("angry", 1, Eyes="side")
                                            ch_e "You really don't learn, do you?"    
                                            $ Line = "rude"
                            "Ok, never mind then.":    
                                    call EmmaFace("angry", 1)
                                    call Statup("Emma", "Love", 200, -10)
                                    call Statup("Emma", "Obed", 90, -10)
                                    call Statup("Emma", "Obed", 200, -10)
                                    call Statup("Emma", "Inbt", 50, -15)
                                    ch_e "I don't know what I saw in you."
                                    $ Line = "rude"
    
    $ E_RecentActions.append("asked sub")   
    $ E_DailyActions.append("asked sub")     
    if Line == "rude":            
            #If line hasn't been set to "rude" by something above, then it skips right past this
            hide Emma_Sprite with easeoutright                    
            call Remove_Girl("Emma")
            $ E_RecentActions.append("angry")
            $ renpy.pop_call()
            "Emma marches out the door, leaving you alone.  She looked pretty upset."
    elif "sir" in E_Petnames:
            #it didn't fail and "sir" was covered
            call Statup("Emma", "Obed", 200, 50)
            $ E_Petnames.append("master")  
            $ E_Petname = "master"
            $ E_Eyes = "sly"
            ch_e ". . . master. . ."
    else:
            #it didn't fail
            call Statup("Emma", "Obed", 200, 30)
            $ E_Petnames.append("sir")  
            $ E_Petname = "sir"
            $ E_Eyes = "sly"
            ch_e ". . . sir."
    return

# end Emma_Sub//////////////////////////////////////////////////////////


# start Emma_Master//////////////////////////////////////////////////////////

label Emma_Master:  #Emma_Update   
    call Shift_Focus("Emma")
    $ E_Loc = bg_current
    call Set_The_Scene
    if E_Loc != bg_current and "Emma" not in Party:
        "Emma shows up and says she needs to talk to you."
    else:
        "Emma approaches you, looking to talk."        
    call CleartheRoom("Emma")
    $ E_DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0
    call EmmaFace("bemused", 1)
    ch_e "[E_Petname], if you don't mind my saying so. . ."
    ch_e "I do think that your more. . . assertive direction has been quite. . ."
    ch_e ". . . exhilarating." 
    menu:
        extend ""
        "I like it too.":
                call EmmaFace("sly", 1)
                ch_e "Good, good. . ."
                ch_e "That being the case, perhaps we would be able to. . ."
                ch_e "Go a bit deeper?"
                menu:
                    extend ""
                    "Nah.  This is just about perfect.":
                            call EmmaFace("sad", 1)
                            call Statup("Emma", "Obed", 200, -15)
                            call Statup("Emma", "Inbt", 50, 10)
                            ch_e "Oh? I suppose. . ."     
                            $ Line = "fail"                      
                    "What'd you have in mind?":
                            $ E_Eyes = "side"
                            ch_e "Hmm, well I was just considering, perhaps I could refer to you as. . ."
                            ch_e ". . . {i}master{/i}?"
                            $ E_Eyes = "squint"
                            ch_e "Would you like that? Would that appeal to you?"
                            menu:
                                extend ""
                                "Oh, yeah.  I'd like that.":
                                        ch_e "Lovely. . ."
                                "Uhm. . .nah.  That's too much.":
                                        call EmmaFace("sad", 1)
                                        call Statup("Emma", "Obed", 200, -15)
                                        call Statup("Emma", "Inbt", 50, 5)
                                        ch_e "Oh. Very well then, forget I said anything about it."
                                        ch_e "Forget. . . forget. . . "                                        
                                        ch_e "Oh, never mind, I forgot that doesn't actually work on you."
                                        ch_e "Just, be discreet." 
                                        $ Line = "fail"

                    "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":
                            call EmmaFace("sly", 1)
                            call Statup("Emma", "Love", 200, 15)
                            call Statup("Emma", "Obed", 200, -10)
                            call Statup("Emma", "Inbt", 50, 10)
                            ch_e "Well, I suppose you must be true to your nature. . ."
                            $ Line = "fail"
                            
                    "Actually, let's stop that. It's creeping me out.":
                            call EmmaFace("perplexed", 2)
                            call Statup("Emma", "Love", 200, -10)
                            call Statup("Emma", "Obed", 200, -50)
                            call Statup("Emma", "Inbt", 50, -15)
                            ch_e "Well. We wouldn't want that now."
                            $ E_Blush = 1
                            $ Line = "embarrassed"
                            
        "As if I care what you think, slut.":
                call EmmaFace("angry", 1)
                call Statup("Emma", "Love", 200, -20)
                call Statup("Emma", "Obed", 200, 10)
                call Statup("Emma", "Inbt", 50, -10)
                menu:
                    ch_e "What was that?"
                    "Sorry. I just don't care what you want.":
                            if ApprovalCheck("Emma", 1400, "LO"): 
                                    call Statup("Emma", "Obed", 200, 10)
                                    ch_e "That's. . ." 
                                    call EmmaFace("sly", 1)
                                    call Statup("Emma", "Love", 200, 20)
                                    call Statup("Emma", "Inbt", 50, 15)
                                    ch_e ". . .not entirely off the mark." 
                            else:
                                    call Statup("Emma", "Love", 200, -15)
                                    call Statup("Emma", "Obed", 200, -10)
                                    call Statup("Emma", "Inbt", 50, 5)
                                    call EmmaFace("angry", 1)
                                    ch_e "!!!"
                                    $ Line = "rude"

                    "Sorry. I'm just trying to do the \"control\" thing.  I thought you'd like it. Too much?":
                            call Statup("Emma", "Love", 200, 10)
                            call Statup("Emma", "Obed", 200, 10)
                            call Statup("Emma", "Inbt", 50, 5)
                            ch_e "You. . . may have a bit of work to do on that." 

        "Not me.  It's kind of creepy.":
                    call EmmaFace("sad", 2)
                    call Statup("Emma", "Love", 200, -10)
                    call Statup("Emma", "Obed", 200, -20)
                    call Statup("Emma", "Inbt", 50, -25)
                    ch_e "Oh.  Well we wouldn't want that. . ."
                    $ Line = "embarrassed"
    
    $ E_History.append("master")
    if Line == "rude":
            $ E_RecentActions.append("angry")                  
            call Remove_Girl("Emma")
            $ renpy.pop_call()
            "Emma storms out the door in a huff."
    elif Line == "embarrassed":                      
            call Remove_Girl("Emma")
            $ renpy.pop_call()
            "Emma dashed out of the room, leaving you alone.  She looked really embarrassed."
    elif Line != "fail":
            call Statup("Emma", "Obed", 200, 50)
            $ E_Petnames.append("master")
            $ E_Petname = "master"
            ch_e ". . .master."
    return

# end Emma_Master//////////////////////////////////////////////////////////


# start Emma_Sexfriend//////////////////////////////////////////////////////////

label Emma_Sexfriend:   #Emma_Update 
    #set this to occur after class
    $ E_Loc = bg_current
    call Set_The_Scene
    call CleartheRoom("Emma",1,1)
    $ E_DailyActions.append("relationship")
    call Taboo_Level
    $ Line = 0 
    "After class, the students file out of the room."
    call EmmaFace("bemused", 1)
    ch_e "[Playername], could I have a word with you?" #blushing expression
    menu:
            extend ""
            "I'm in a hurry.":
                call EmmaFace("angry", 1)
                ch_e "That's. . . not an appropriate response." #Angry expression.  Loss of points                
                call Statup("Emma", "Love", 200, -20) 
                call Statup("Emma", "Obed", 50, 3)           
                $ Line = "rude"

            "This doesn't sound good.":
                call EmmaFace("sly", 1)
                ch_e "Settle down, it's nothing. . . unpleasant." 
                    
            "Yeah.  What's up?":
                pass
                
    if not Line: #all this gets skipped if the "rude" response was procced above
            if ApprovalCheck("Emma", 850, "L"):                  
                    call EmmaFace("sly", 1)
                    ch_e "I just, enjoy spending time with you, as you're aware?" #Sexy expression.  This is Emma's "High Like" response
                    menu:
                        extend ""
                        "I thought so.":
                            call EmmaFace("sexy", 1)
                            call Statup("Emma", "Love", 90, 10) 
                            call Statup("Emma", "Inbt", 80, 5)    
                            ch_e "I {i}was{/i} hoping you'd be aware, [E_Petname]." #Blushing expression
                
                        "Really?":
                            call EmmaFace("perplexed", 1)
                            ch_e "Um, yes." #Blushing expression

                        "Don't complicate things.":
                            call EmmaFace("angry", 1)
                            call Statup("Emma", "Love", 200, -10) 
                            call Statup("Emma", "Obed", 50, 5)
                            call Statup("Emma", "Inbt", 80, -5)   
                            ch_e "I'm sorry if you find this discussion too \"complicated.\"" #Angry expression.  Big loss of points
                            $ Line = "rude"
                            
            elif ApprovalCheck("Emma", 1000, "LI"): 
                    call EmmaFace("sexy", 1)
                    ch_e "I just thought you should know how. . . intriguing I find you." 
                    menu:
                        extend ""
                        "That's really nice of you to say.":
                            call Statup("Emma", "Love", 80, 5) 
                            call Statup("Emma", "Inbt", 80, 5)   
                            ch_e "Certainly." #Blushing expression

                        "Me?  You really think so?":
                            ch_e "Don't be overly modest, [E_Petname]." #Blushing expression
                
                        "Are you going somewhere with this?":
                            call EmmaFace("angry")
                            ch_e "Perhaps not." #Angry expression.  Loss of points
                            $ Line = "rude"
                            
            else: #if it reaches this block, it's because it failed the "like" check above.                    
                    $ E_Mouth = "smile"
                    $ E_Brows = "sad"
                    $ E_Eyes = "side"
                    ch_e "This may sound a bit. . . unconventional."
                    menu:
                        extend ""
                        "Well, you've got me intrigued.  Now you {i}have{/i} to tell me.":
                            ch_e "You'll keep this between the two of us?"  #Nervous expression
                            menu:
                                extend ""
                                "Emma. . . I really like you.  I promise.":
                                    call EmmaFace("smile")
                                    call Statup("Emma", "Love", 90, 10) 
                                    call Statup("Emma", "Inbt", 80, 5)    
                                    ch_e "Very well. . ."  #Blushing expression.  Gain of points.

                                "Uhm. . . okay?":
                                    ch_e "Well. .  ." #Nervous expression

                                "No promises.":
                                    call EmmaFace("perplexed",2)
                                    call Statup("Emma", "Inbt", 80, -5)  
                                    ch_e "Hmm. . . never mind, then."  #Embarrassed expression.  Minor loss of points
                                    $ Line = "embarrassed"

                        "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                            call EmmaFace("angry",1)
                            ch_e "Live in suspense then."
                            $ Line = "rude"
                                
    if not Line:            
            ch_e "I was considering. . . "
            ch_e "Perhaps we could take our relationship a little further, if you wanted to."
            menu:
                extend ""
                "You mean. . . like, being {i}friends with benefits{/i}?":
                        ch_e "I supposeyou could put it that way."
                        ch_e "What do you think?" #Blushing expression
                        menu:
                            extend ""
                            "Sounds amazing!  Count me in.":
                                    call EmmaFace("smile",1)
                                    call Statup("Emma", "Love", 80, 10) 
                                    call Statup("Emma", "Obed", 50, 10)
                                    call Statup("Emma", "Inbt", 200, 50)             
                                    call Statup("Emma", "Lust", 200, 5) 
                                    "Emma leans in and gives you a passionate kiss."
                                    $ E_Kissed += 1
                                    ch_e "I can't wait to get started, [E_Petname]."

                            "That's pretty slutty, Emma.":
                                    if ApprovalCheck("Emma", 2000):                                        
                                        call EmmaFace("angry",1,Brows="confused")
                                        call Statup("Emma", "Love", 200, -10) 
                                        call Statup("Emma", "Obed", 50, 15)  
                                        ch_e "I suppose you're not wrong."
                                    else:
                                        call EmmaFace("angry",1)
                                        call Statup("Emma", "Love", 200, -30) 
                                        call Statup("Emma", "Obed", 50, 10)
                                        call Statup("Emma", "Inbt", 80, -20)  
                                        ch_e "Then I suppose I'll have to take care of that elsewhere!" #Angry expression.  HUGE loss of points
                                        $ Line = "rude"

                "Uhm, to be honest, I'd rather not.":
                        call EmmaFace("sadside",2)
                        call Statup("Emma", "Obed", 50, 15)
                        call Statup("Emma", "Inbt", 80, -15)  
                        ch_e "Oh. Suit yourself, I suppose."  #Sad expression
                        ch_e "I should be leaving."
                        $ Line = "sad"

    if Line == "rude":    
            call EmmaFace("angry",1)
            $ E_RecentActions.append("angry")
            call Statup("Emma", "Love", 200, -20) 
            call Statup("Emma", "Obed", 50, 5)
            call Statup("Emma", "Inbt", 80, -10) 
            hide Emma_Sprite with easeoutright  
            $ E_RecentActions.append("angry")
            "Emma storms off in a huff.  She seemed pretty mad at you."
    elif Line == "embarrassed":
            call EmmaFace("perplexed",1)
            call Statup("Emma", "Love", 200, -10) 
            call Statup("Emma", "Obed", 50, 5)
            call Statup("Emma", "Inbt", 80, -20)   
            hide Emma_Sprite with easeoutright
            "Emma dashes out of the room, leaving you alone.  That was very strange."
    elif Line == "sad":    
            hide Emma_Sprite with easeoutbottom
            "Emma wanders into the hall, leaving you alone.  You think you may have hurt her feelings."
    else: #if you kept Line unused throughout, then you passed all the checks, so. . .
            $ E_Petnames.append("sex friend")             
            call EmmaFace("sly",2)
            call Statup("Emma", "Inbt", 80, 10)             
            call Statup("Emma", "Lust", 80, 10)   
            "Emma leans in and carresses your body."
            "As she does so, you feel a tickle as if her mouth is surrounding your cock."
            "You look back at her and she winks." 
            ch_e "I do have a few tricks up my sleeves, [E_Petname]."
            ch_e "I'll see you later, I hope."  
            hide Emma_Sprite with easeoutright
            "She leaves the room, and the phantom \"lips\" give you one final kiss. "            
    call Remove_Girl("Emma")
    return
    
# end Emma_Sexfriend//////////////////////////////////////////////////////////


# start Emma_Fuckbuddy//////////////////////////////////////////////////////////

label Emma_Fuckbuddy:   #Emma_Update   
    $ E_DailyActions.append("relationship")
    "Out of nowhere, you feel a tongue sliding across your cock."
    "Even though you're fully dressed, it definitely feels like a mouth has enveloped your cock."
    "You look down, but can't see any movement, although your cock has become diamond hard."
    "As you try to control your obvious erection, a voice tickles the back of your mind,"
    ch_e "To me, my X-Man. . ."
    "-and suddenly the pressure is gone." 
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on Emma later. . ."
    $ E_Petnames.append("fuck buddy")  
    $ E_Event[10] += 1
    return
# end Emma_Fuckbuddy//////////////////////////////////////////////////////////

# start Emma_Daddy//////////////////////////////////////////////////////////

#Not updated

label Emma_Daddy:       #Emma_Update   
    $ E_DailyActions.append("relationship")
    call Shift_Focus("Emma")
    ch_e ". . ."
    if "dating" in E_Traits:
        ch_e "We have been dating a while, [E_Petname],"  
    else:    
        ch_e "We have been enjoying ourselves," 
    if E_Love > E_Obed and E_Love > E_Inbt:
        ch_e "and you certainly are sweet. . ."
    elif E_Obed > E_Inbt:
        ch_e "and you know how to keep me interested. . ."
    else:
        ch_e "and I've been. . . exploring. . ."        
    ch_e "I was thinking, would you mind if I call you \"daddy?\""  
    menu:
        extend ""
        "Ok, go right ahead?":            
            call EmmaFace("smile") 
            call Statup("Emma", "Love", 90, 20)          
            call Statup("Emma", "Obed", 60, 10)            
            call Statup("Emma", "Inbt", 80, 30) 
            ch_e "Excellent."            
        "What do you mean by that?": 
            call EmmaFace("bemused") 
            ch_e "I just find it to be a turn-on, being your baby girl. . ."
            ch_e "I'd prefer to call you that sometimes."
            menu:
                extend ""
                "Sounds interesting, fine by me.":     
                    call EmmaFace("smile") 
                    call Statup("Emma", "Love", 90, 15)          
                    call Statup("Emma", "Obed", 60, 20)            
                    call Statup("Emma", "Inbt", 80, 25) 
                    ch_e "Great!"   
                    call EmmaFace("sly",2) 
                    ch_e " . . . daddy."  
                    call EmmaFace("sly",1) 
                    $ E_Petname = "daddy"
                "Could you not, please?":             
                    call Statup("Emma", "Love", 90, 5)
                    call Statup("Emma", "Obed", 80, 40)            
                    call Statup("Emma", "Inbt", 80, 20)  
                    call EmmaFace("sad") 
                    ch_e "   . . .   "
                    ch_e "Well, ok."
                "You've got some real daddy issues, uh?":    
                    call Statup("Emma", "Love", 90, -15)          
                    call Statup("Emma", "Obed", 80, 45)            
                    call Statup("Emma", "Inbt", 70, 5)  
                    call EmmaFace("angry") 
                    ch_e "Let's not get into it." 
        "Aren't you a bit old for that?":
            call Statup("Emma", "Love", 90, -15)          
            call Statup("Emma", "Obed", 80, 40)            
            call Statup("Emma", "Inbt", 70, 10) 
            call EmmaFace("angry") 
            ch_e "Perhaps this was a bad idea."  
    $ E_Petnames.append("daddy")
    return

# end Emma_Daddy//////////////////////////////////////////////////////////

# Start EmmaBreakup //////////////////////////////////////////////////////////  
 #Emma_Update   
label Emma_Cheated(Other = "Rogue", Resolution = 0, B = 0):  #Other is the other girl, Resolution is Resolution count, you want this over 2 at least. B is the bonus modifier
    #Scene for if Emma catches you with Rogue and confronts you about it. 
    return
    $ E_DailyActions.append("relationship")
    $ Line = 0
    call EmmaFace("angry")
    
    if Other == "Rogue":
        if E_LikeRogue >= 900:
            $ Resolution += 2
        elif E_LikeRogue >= 800:
            $ Resolution += 1
        $ B = int((E_LikeRogue - 500)/2)
    
    $ Resolution -= E_Cheated if E_Cheated <= 3 else 3 #Adds to Resolution 3 or less based on cheating
    
    if E_Cheated:
        call Statup("Emma", "Love", 200, -50) 
        call Statup("Emma", "Obed", 80, -25)
        call Statup("Emma", "Inbt", 50, -50)   
    else:
        call Statup("Emma", "Love", 200, -120) 
        call Statup("Emma", "Obed", 80, -30)
        call Statup("Emma", "Inbt", 50, -20)  
        
    "Emma stomps up to you and stares you down for a moment."
    ch_e "Well?!" 
    ch_e "Wanna tell me what that was all about?"
    menu:
        extend ""
        "Uhm. . .sorry?":
                ch_e "Is that {i}really{/i} all you have to say for yourself?"
                ch_p "I don't know? It would kinda help if I knew what you were upset about."
                if ApprovalCheck("Emma", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Line = "angry"
        "I have no idea what you're talking about.":
                ch_e "I can't believe you just said that. I gave you[E_like]a lot more credit than that."
                ch_p "[E_Pet], I'm being serious. Why're you so upset?"
                if ApprovalCheck("Emma", 900, "LO"):
                    $ Resolution += 1
                else:
                    $ Resolution -= 2
                    $ Line = "angry"
        "Could you chill out and tell me what you mean?":
                call EmmaFace("sad",2)                
                call Statup("Emma", "Love", 200, -10) 
                call Statup("Emma", "Obed", 40, 5, 1) 
                ch_e "I didn't like what happened already. How much[E_like]worse can it get?"
                ch_p "You'd better start making some sense, or you're gonna find out."
                if ApprovalCheck("Emma", 500, "O"):
                    $ Resolution += 1  
                elif ApprovalCheck("Emma", 1200, "LO"):
                    $ Resolution -= 1    
                else:
                    $ Resolution -= 3
                    $ Line = "angry"
                    
    if not Line:
            #this section only triggers if you didn't trigger the "angry" response in the previous section
            call EmmaFace("angry",2)
            if Other == "Rogue":
                ch_e "I {i}saw{/i} you and Rogue! I can't[E_like]believe you'd do that, [E_Petname]."
            else:
                ch_e "I {i}saw{/i} you with her! I can't[E_like]believe you'd do that, [E_Petname]."
            ch_e "I thought we had something. . . [E_like]{i}special{/i} going on."
            menu:
                extend ""
                "I'm sorry. . . ":
                        $ Resolution += 1                        
                        call Statup("Emma", "Love", 90, 5) 
                        call Statup("Emma", "Obed", 80, 5)  
                        if not ApprovalCheck("Emma", 900, "L"):
                                #if love is less than 900
                                $ Line = "sad"
                        else:
                                call EmmaFace("sad")
                                ch_e "Me too. I thought you. . . "
                                call EmmaFace("sadside")
                                ch_e ". . . I thought you maybe loved me."
                                menu:
                                    extend ""
                                    "You weren't wrong, [E_Pet].":
                                            $ Resolution += 1                                            
                                            call Statup("Emma", "Love", 200, 5) 
                                            call Statup("Emma", "Inbt", 50, 5)   
                                            call EmmaFace("embarrassed")
                                            ch_e "[E_Like]. . . really?"
                                            menu:
                                                extend ""
                                                "[E_Like]really.":
                                                        call EmmaFace("embarrassed")
                                                        if Other == "Rogue":
                                                            ch_e "Then. . .[E_like]why did you do that with {i}Rogue?{/i} You had to know that would[E_like]hurt me."
                                                        else:
                                                            ch_e "Then. . .[E_like]why did you do that with {i}her?{/i} You had to know that would[E_like]hurt me."                                                        
                                                        menu:
                                                            extend ""
                                                            "It was a mistake. And I promise I'll never do it again.":
                                                                    $ Resolution += 2                                                                    
                                                                    call Statup("Emma", "Love", 200, 5)
                                                                    call Statup("Emma", "Inbt", 50, 5)   
                                                                    call EmmaFace("happy",2)
                                                                    ch_e "Okay. I understand. Just. . .[E_like]remember how much I care about you, 'kay?"
                                                                    ch_e "I can forgive you[E_like]this time."
                                                                    ch_e "Because I'm[E_like]in love with you, too."
                                                                    call E_Kissing_Launch("kiss you")
                                                                    call E_Pos_Reset
                                                            "I was trying to maybe include her in what we have going.":
                                                                    call Statup("Emma", "Obed", 80, 5)
                                                                    $ Line = "maybe"
                                                            "I don't know, seemed fun at the time.":
                                                                    $ Resolution -= 1
                                                                    call Statup("Emma", "Love", 200, -10) 
                                                                    call Statup("Emma", "Obed", 80, -5)
                                                                    $ Line = "angry"          
                                                "Had you going, there, didn't I? {i}Hell{/i}, no, I don't!":
                                                        $ Resolution -= 3
                                                        call Statup("Emma", "Love", 200, -20) 
                                                        call Statup("Emma", "Obed", 80, 5)
                                                        call Statup("Emma", "Inbt", 50, 5)   
                                                        $ Line = "angry"                                                                   
                                    "Yeah, well. .  . I don't.":
                                            $ Resolution -= 1
                                            call Statup("Emma", "Love", 200, -10) 
                                            call Statup("Emma", "Obed", 80, 5)   
                                            $ Line = "sad"  
                        #end "sorry."
                "Whatever.":
                        call Statup("Emma", "Love", 200, -10) 
                        call Statup("Emma", "Inbt", 50, 5)   
                        if ApprovalCheck("Emma", 900, "L") and not ApprovalCheck("Emma", 500, "O"):
                                $ Resolution -= 2
                                $ Line = "angry"
                        else:
                                call Statup("Emma", "Obed", 80, 10) 
                                $ Resolution -= 1
                                $ Line = "sad"
                "We do. And now, it can be even {b}more{/b} special.":
                                $ Resolution += 1
                                $ Line = "maybe"
            #end "questioning", for long blocks like this, it helps to put a comment at the end to explain what was going on, so I don't get lost. ;)
            
    if Line == "maybe":
            # Maybe threesome?            
            if ApprovalCheck("Emma", 1250):
                    call EmmaFace("confused")
                    ch_e "What're you even[E_like]{i}talking{/i} about?"
                    if Other == "Rogue":
                        ch_p "Look. . .be totally honest with me for a second. Rogue's your best friend, right?"
                    else:
                        ch_p "Look. . .be totally honest with me for a second. She's kinda hot, right?"
                    ch_e "Yeah. . ."
                    ch_p "Right. And when you saw us together. . . you have to admit, you thought it was pretty hot on some level, right?"
                    call EmmaFace("angry")
                    ch_e "No. It pissed me off is what it did."
                    ch_p "C'mon, [E_Pet]. Haven't you ever thought about it?"
                    call EmmaFace("confused")
                    ch_e "Thought about what?"
                    if Other == "Rogue":
                        ch_p "Thought about what it might be like if we invited Rogue into what we have together."
                    else:
                        ch_p "Thought about what it might be like if we invited her into what we have together."                    
                    if ApprovalCheck("Emma", 1500) and Resolution >= 3:
                            call EmmaFace("embarrassed")
                            ch_e "You mean[E_like]. . .a {i}threesome{/i}?"
                            call EmmaFace("sly")
                            ch_e "I can't believe I'm saying this but. . . I'm[E_like]vaguely intrigued."
                            if Other == "Rogue":
                                ch_e "Assuming I'm interested. . . how're you going to convince Rogue?"
                            else:
                                ch_e "Assuming I'm interested. . . how're you going to convince her?"
                            ch_p "If you see us together again, just play it cool."
                            ch_p "Make sure she notices that you're watching us, but don't give her the impression it puts you off."
                            call EmmaFace("sly",1)
                            ch_e ". . . which should[E_like]make her wonder what's up."
                            ch_p "Right. Eventually, she'll ask me what our arrangement is."
                            ch_e "By then, with any luck, she'll be comfortable enough with me that I can ask her how she feels about it."
                            call EmmaFace("sly",2)
                            ch_e "Gotta admit, [E_Petname]. . . you're pretty smooth."
                            ch_e "Consider me[E_like]on board with that plan."
                            ch_e "Just be sure to be careful with her. She's still my friend."
                            #have Emma kiss the Player here.
                            ch_e "And remember, you're still {i}my{/i} guy."                            
                            $ E_Traits.append("poly Rogue")
                            $ E_Traits.append("ask Rogue")
                            $ Line = 0
            if Line:
                    #this section will only trigger if the "maybe" line above triggered BUT both of the stat checks above failed. 
                    #If you don't even ask about a threesome then this check gets skipped, and if you ask, but succeed both checks,
                    #then this section gets skipped. 
                    call EmmaFace("angry")
                    if Other == "Rogue":
                        ch_e "So, you're telling me[E_like]you being with Rogue like that was your way of seeing if I'd be up for a threesome?"
                    else:
                        ch_e "So, you're telling me[E_like]you being with her like that was your way of seeing if I'd be up for a threesome?"
                    ch_p "Pretty much. I. . .take it you're not down with that?"
                    $ Line = "angry"
            # End "maybe threesome?"
    
    elif Resolution >= 4:
        if Other == "Rogue" and E_LikeRogue >= 800:
                call Statup("Emma", "Inbt", 80, 25)   
                ch_e "Well, maybe Rogue and I can work something out. . ."                            
                $ E_Traits.append("poly Rogue")
                $ E_Traits.append("ask Rogue")                
        
    $ E_Cheated += 1
    if "saw with Rogue" in E_Traits: 
            #Clean up the trait for this event
            $ E_Traits.remove("saw with Rogue")
            if "poly Rogue" not in E_Traits:
                $ E_LikeRogue -= 50
            
    if not Line:
            #a neutral ending if you wrap things up without really effecting much
            pass                
    elif Line == "angry":
            #Angry ending
            call EmmaFace("angry",2)
            ch_e "You are {b}SUCH{/b} an asshole, [E_Petname]!"
            ch_e "I never wanna see you again, as long as I live!"
            "Emma phases through the floor leaving you standing alone."
            "Whatever you once had is over now, for sure."     
            $ E_RecentActions.append("angry")
            $ E_Break[0] = 7 + E_Break[1] + E_Cheated
            $ E_Traits.remove("dating")
            $ E_Traits.append("ex")         
    elif Line == "sad":
            # Sad ending
            call EmmaFace("sad",2)
            "Emma phases through the floor leaving you standing alone."
            "You're pretty sure she was crying as she left."
            "You're also pretty sure you seriously damaged your relationship with her."
            if Resolution <= 3:
                $ E_Break[0] = 5 + E_Break[1] + E_Cheated
                $ E_Traits.remove("dating")
                $ E_Traits.append("ex")                
    return

# end EmmaBreakup //////////////////////////////////////////////////////////    


label Emma_Strip_Study_Intro:     
    if Party[0] != "Emma":
            $ Party.reverse()                  
    call Shift_Focus(Party[0])           
    if not E_Over and not E_Legs:
            #if she's mostly naked, cheat
            call EmmaFace("sly")                                
            ch_e "I was considering some way of. . . motivating you. . ." 
            $ E_Eyes = "down"
            ch_e "but but I suppose we're already past that. . ."
            $ E_Eyes = "squint"
            ch_e "Do you have any ideas?"                                
            call Emma_SexMenu   
    else:
            "Emma moves a bit closer to you. . ."
            ch_e "I was curious, [E_Petname]. . ."
            ch_e "do you feel that a little \"motivation\" might help you to learn?"
            if "stripstudy" not in E_History:
                menu:
                    extend ""                                        
                    "What sort of motivation?": 
                        if "frisky" not in E_History:
                            call EmmaFace("sly") 
                            $ Line = "ask"                                                
                        else:                                   
                            call Statup("Emma", "Obed", 80, 3)
                            call EmmaFace("confused",1)  
                            "She strokes at the edges of her clothes."
                            ch_e "You aren't going to make me say it, are you. . ."
                            menu:
                                extend ""
                                "Um. . . oh, OH! Yeah, sounds good. [[Strip tutoring]":
                                    $ Line = "strip"
                                "Looks like I am. . .":
                                    if ApprovalCheck("Emma", 500, "O"):                              
                                            call Statup("Emma", "Obed", 80, 5)
                                            call Statup("Emma", "Inbt", 50, 5)  
                                            call EmmaFace("sly", 2)  
                                            $ Line = "ask"
                                    elif ApprovalCheck("Emma", 500, "LO"):
                                            call EmmaFace("confused", 2)            
                                            call Statup("Emma", "Love", 70, -5) 
                                            call Statup("Emma", "Obed", 80, 5)  
                                            ch_e "Very well. . ."
                                            $ Line = "ask"                                                            
                                    else:          
                                            call Statup("Emma", "Love", 200, -5) 
                                            call Statup("Emma", "Inbt", 50, -5)  
                                            call EmmaFace("angry", 1)  
                                            ch_e "Oh, never mind then."
                                ". . .":
                                    if ApprovalCheck("Emma", 400, "O"):           
                                            call EmmaFace("confused", 2)            
                                            call Statup("Emma", "Inbt", 50, 5)  
                                            $ Line = "ask"
                                    elif ApprovalCheck("Emma", 500, "LO"):
                                            call EmmaFace("confused", 1, Brows="angry")           
                                            call Statup("Emma", "Obed", 50, 5)
                                            call Statup("Emma", "Inbt", 50, 5)  
                                            $ Line = "ask"                                                            
                                    else:          
                                            call Statup("Emma", "Love", 200, -5) 
                                            call Statup("Emma", "Inbt", 50, -5)  
                                            call EmmaFace("angry", 1)  
                                            ch_e "Oh, never mind then."
                            
                    "I think it might." if "frisky" in E_History:
                            call EmmaFace("sly")           
                            call Statup("Emma", "Love", 80, 5) 
                            call Statup("Emma", "Obed", 80, 3)
                            call Statup("Emma", "Inbt", 50, 5)  
                            ch_e "I was hoping you would. . ."
                            $ Line = "strip"                                            
                    "No, I've got this.":
                        call EmmaFace("confused", Eyes="side")    
                        if "frisky" in E_History:
                                call Statup("Emma", "Love", 200, -10) 
                                call Statup("Emma", "Obed", 80, 5)
                                call Statup("Emma", "Inbt", 50, -5)   
                        else:
                                call Statup("Emma", "Love", 200, -5) 
                                call Statup("Emma", "Inbt", 50, -5)   
                        ch_e "Oh. . . Very well then."
                        call EmmaFace("confused")  
                if Line == "ask":
                    ch_e "Well, perhaps I could quiz you about mutant psychology. . ."
                    $ E_Eyes = "side"
                    ch_e "and, perhaps, if you were to get a question right. . ."
                    $ E_Eyes = "squint"
                    ch_e "I could. . ."
                    menu:
                        extend ""
                        "Take off some clothes?":
                                call Statup("Emma", "Inbt", 50, 5)   
                                ch_e "Yes."
                                $ Line = "strip"
                        "Yes? . .":
                                if ApprovalCheck("Emma", 500, "O"):
                                    call EmmaFace("confused", 2) 
                                    if "frisky" in E_History:
                                            call Statup("Emma", "Love", 200, -5) 
                                            call Statup("Emma", "Obed", 80, 10)   
                                    else:
                                            call Statup("Emma", "Obed", 80, 5)
                                            call Statup("Emma", "Inbt", 50, -5)  
                                    $ Line = "ask"
                                elif ApprovalCheck("Emma", 500, "LO"):
                                    call EmmaFace("confused", 1, Brows="angry") 
                                    if "frisky" in E_History:
                                            call Statup("Emma", "Love", 200, -5) 
                                            call Statup("Emma", "Obed", 80, 5)  
                                    else:
                                            call Statup("Emma", "Obed", 80, 5)
                                            call Statup("Emma", "Inbt", 50, -5)  
                                    $ Line = "ask"            
                        ". . .":
                                if ApprovalCheck("Emma", 500, "O"):
                                    call EmmaFace("confused", 2) 
                                    if "frisky" in E_History:
                                            call Statup("Emma", "Obed", 50, 5)
                                            call Statup("Emma", "Inbt", 50, -5)   
                                    else:
                                            call Statup("Emma", "Obed", 50, 5)
                                            call Statup("Emma", "Inbt", 50, -5)  
                                    $ Line = "ask"
                                elif ApprovalCheck("Emma", 500, "LO"):
                                    call EmmaFace("confused", 1, Brows="angry") 
                                    if "frisky" in E_History:
                                            call Statup("Emma", "Love", 200, -5) 
                                            call Statup("Emma", "Obed", 50, 5)
                                            call Statup("Emma", "Inbt", 50, -5)   
                                    else:
                                            call Statup("Emma", "Obed", 50, 5)
                                            call Statup("Emma", "Inbt", 50, -5)  
                                    $ Line = "ask"   
                    if Line == "ask":
                        call EmmaFace("bemused", Eyes="side") 
                        ch_e "Take off some clothes. . ."
                        $ Line = "strip"
                    call EmmaFace("sly", Brows="confused") 
                    menu:
                        ch_e "Would that interest you?"
                        "Definitely!":
                            call EmmaFace("sly",Mouth="smile")    
                            call Statup("Emma", "Love", 50, 5)
                            call Statup("Emma", "Love", 80, 5) 
                            call Statup("Emma", "Inbt", 50, 5)                                               
                        "Yeah.":
                            call EmmaFace("sly")     
                            call Statup("Emma", "Love", 80, 3) 
                            call Statup("Emma", "Obed", 50, 3)
                            call Statup("Emma", "Inbt", 50, 3)                                              
                        "No thanks.":
                            if "frisky" in E_History:
                                    call Statup("Emma", "Love", 200, -10) 
                                    call Statup("Emma", "Obed", 80, 10)
                                    call Statup("Emma", "Inbt", 50, -5)   
                            else:
                                    call Statup("Emma", "Love", 200, -5) 
                                    call Statup("Emma", "Obed", 80, 5)
                                    call Statup("Emma", "Inbt", 50, -5)  
                            call EmmaFace("angry") 
                            ch_e "Hrm."
                            $ Line = "no"
                    
            if Line == "strip":
                    call EmmaFace("sly", 0) 
                    if len(Party) >= 2:
                        ch_e "And you, [Party[1]]? Care to participate?"                     
                        call Date_Sex_Break("Emma",Party[1])
                        if _return == 4:
                            #you stop it because of the other girl
                            ch_e "Well I suppose we can. . . postone that."
                            return
                        else:
                            if _return == 3:
                                #the other girl is mad
                                ch_e "Well I suppose that answers that."
                                $ Cnt = 3
                            elif _return == 2:
                                #the other girl will watch
                                ch_e "I suppose you can just watch then. . ."    
                                $ Cnt = 3                                                
                            elif _return == 1 and len(Party) >= 2:
                                if Party[1] == "Rogue":
                                    ch_r "I guess I could join in."
                                elif Party[1] == "Kitty":
                                    ch_k "It could be fun. . ."
                                elif Party[1] == "Laura":
                                    ch_l "Yeah, ok. . ."
                    jump Group_Strip_Study
            else: 
                    return
    return
## End Emma_Strip_Study Intro

#label Emma_Study:                       #study events
#            call Shift_Focus("Emma")
#            if Current_Time == "Night":
#                ch_e "It's a little late for a study session, maybe tomorrow."
#                return
#            elif Round <= 30:        
#                ch_e "I'm afraid I was just about to take a break, perhaps another time. . ."
#                return
#            elif bg_current in (R_Loc,K_Loc): 
#                ch_e "I suppose you could both use some work."
#            else:
#                ch_e "Very well."
            
#            $ P_RecentActions.append("study")
#            $ P_XP += 5
#            $ Trigger = 0
#            $ Line = renpy.random.choice(["She runs you through the routines, it's fairly uneventful.", 
#                    "You study up for the mutant biology test.", 
#                    "You study for the math quiz.",
#                    "You get bored and discuss student gossip instead.",
#                    "You study for a few hours, that was fun.",
#                    "You spend the next few hours studying the lit test."
#                    "You study for the game design course."]) 
#            "[Line]"       
#            $ Line = 0
#            call Statup("Emma", "Love", 80, 2)
#            $ D20 = renpy.random.randint(1, 20)    
#            if D20 > 10:
#                if bg_current in (R_Loc,K_Loc):  
#                    #if there are other girls in the room
#                    if "three" in E_History:
#                        if R_Loc == bg_current:
#                            if D20 > 15 and R_LikeEmma >= 700:  
#                                    $ Line = 0
#                                    call Rogue_Frisky_Study                                
#                                    $ Line = "no"
#                            elif E_LikeRogue >= 700:
#                                    $ Line = "Rogue"
#                        elif K_Loc == bg_current:
#                            if D20 > 15 and K_LikeEmma >= 700:  
#                                    $ Line = 0
#                                    call Kitty_Frisky_Study                                
#                                    $ Line = "no"
#                            elif E_LikeKitty >= 700:
#                                    $ Line = "Kitty"
#                    if Line:         
#                        if Line != "no": 
#                            call Emma_Frisky_Study(Line)                     
#                        $ Line = 0
#                    else:
#                            #if she's uncomfortable around the other girl
#                            ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
#                            $ P_XP += 5 
#                else:
#                    call Emma_Frisky_Study   
#            else:        
#                ch_e "I'm afraid it's getting a bit late, we should wrap this up. . ."
#                $ P_XP += 5  
#            call Wait 
#            call Girls_Location
#            return
##End Emma Study
            
#label Emma_Frisky_Study(Girl=0,Line=0,Prime_Bonus=0,Second_Bonus=0):
#            #Girl is a potential second girl, Prime_Bonus is needed by the Datebreak code but does nothing
#            if D20 > 17 and ApprovalCheck("Emma", 1000) and E_Blow > 5:
#                        call EmmaFace("sly")
#                        "Emma get predatory grin, and begins to unzip your pants."
#                        "She pulls your dick out and pops it into her mouth."     
#                        $ Line = "blow"
#            elif D20 > 14 and ApprovalCheck("Emma", 1000) and E_Hand >= 5:
#                        call EmmaFace("sly")
#                        "Emma get predatory grin, and begins to unzip your pants."
#                        "She pulls your dick out and begins to slowly stroke it."     
#                        $ Line = "hand"
#            elif D20 > 10 and (ApprovalCheck("Emma", 1300) or (E_Mast and ApprovalCheck("Emma", 1000))) and E_Lust >= 70:
#                        call EmmaFace("sly", Eyes="side")
#                        "Emma leans back a bit and starts to rub herself."          
#                        $ E_RecentActions.remove("unseen") if "unseen" in E_RecentActions else E_RecentActions #she sees you're there
#                        $ Trigger = "masturbation"    
#                        $ Line = "masturbate" 
#            elif D20 > 10 and ApprovalCheck("Emma", 1200) and E_Lust >= 30:                
#                        if not E_Over and not E_Legs:
#                                #if she's mostly naked, cheat
#                                call EmmaFace("sly")                                
#                                ch_e "I was considering some way of. . . motivating you. . ." 
#                                $ E_Eyes = "down"
#                                ch_e "but but I suppose we're already past that. . ."
#                                $ E_Eyes = "squint"
#                                ch_e "Do you have any ideas?"                                
#                                call Emma_SexMenu   
#                        else:
#                                "Emma moves a bit closer to you. . ."
#                                ch_e "I was curious, [E_Petname]. . ."
#                                ch_e "do you feel that a little \"motivation\" might help you to learn?"
#                                menu:
#                                    extend ""                                        
#                                    "What sort of motivation?": 
#                                            if "frisky" not in E_History:
#                                                call EmmaFace("sly") 
#                                                $ Line = "ask"                                                
#                                            else:                                   
#                                                call Statup("Emma", "Obed", 80, 3)
#                                                call EmmaFace("confused",1)  
#                                                "She strokes at the edges of her clothes."
#                                                ch_e "You aren't going to make me say it, are you. . ."
#                                                menu:
#                                                    extend ""
#                                                    "Um. . . oh, OH! Yeah, sounds good. [[Strip tutoring]":
#                                                        $ Line = "strip"
#                                                    "Looks like I am. . .":
#                                                        if ApprovalCheck("Emma", 500, "O"):                              
#                                                                call Statup("Emma", "Obed", 80, 5)
#                                                                call Statup("Emma", "Inbt", 50, 5)  
#                                                                call EmmaFace("sly", 2)  
#                                                                $ Line = "ask"
#                                                        elif ApprovalCheck("Emma", 500, "LO"):
#                                                                call EmmaFace("confused", 2)            
#                                                                call Statup("Emma", "Love", 70, -5) 
#                                                                call Statup("Emma", "Obed", 80, 5)  
#                                                                ch_e "Very well. . ."
#                                                                $ Line = "ask"                                                            
#                                                        else:          
#                                                                call Statup("Emma", "Love", 200, -5) 
#                                                                call Statup("Emma", "Inbt", 50, -5)  
#                                                                call EmmaFace("angry", 1)  
#                                                                ch_e "Oh, never mind then."
#                                                    ". . .":
#                                                        if ApprovalCheck("Emma", 400, "O"):           
#                                                                call EmmaFace("confused", 2)            
#                                                                call Statup("Emma", "Inbt", 50, 5)  
#                                                                $ Line = "ask"
#                                                        elif ApprovalCheck("Emma", 500, "LO"):
#                                                                call EmmaFace("confused", 1, Brows="angry")           
#                                                                call Statup("Emma", "Obed", 50, 5)
#                                                                call Statup("Emma", "Inbt", 50, 5)  
#                                                                $ Line = "ask"                                                            
#                                                        else:          
#                                                                call Statup("Emma", "Love", 200, -5) 
#                                                                call Statup("Emma", "Inbt", 50, -5)  
#                                                                call EmmaFace("angry", 1)  
#                                                                ch_e "Oh, never mind then."
                                                
#                                    "I think it might." if "frisky" in E_History:
#                                                call EmmaFace("sly")           
#                                                call Statup("Emma", "Love", 80, 5) 
#                                                call Statup("Emma", "Obed", 80, 3)
#                                                call Statup("Emma", "Inbt", 50, 5)  
#                                                ch_e "I was hoping you would. . ."
#                                                $ Line = "strip"                                            
#                                    "No, I've got this.":
#                                            call EmmaFace("confused", Eyes="side")    
#                                            if "frisky" in E_History:
#                                                    call Statup("Emma", "Love", 200, -10) 
#                                                    call Statup("Emma", "Obed", 80, 5)
#                                                    call Statup("Emma", "Inbt", 50, -5)   
#                                            else:
#                                                    call Statup("Emma", "Love", 200, -5) 
#                                                    call Statup("Emma", "Inbt", 50, -5)   
#                                            ch_e "Oh. . . Very well then."
#                                            call EmmaFace("confused")  
#                                if Line == "ask":
#                                        ch_e "Well, perhaps I could quiz you about mutant psychology. . ."
#                                        $ E_Eyes = "side"
#                                        ch_e "and, perhaps, if you were to get a question right. . ."
#                                        $ E_Eyes = "squint"
#                                        ch_e "I could. . ."
#                                        menu:
#                                            extend ""
#                                            "Take off some clothes?":
#                                                    call Statup("Emma", "Inbt", 50, 5)   
#                                                    ch_e "Yes."
#                                                    $ Line = "strip"
#                                            "Yes? . .":
#                                                    if ApprovalCheck("Emma", 500, "O"):
#                                                        call EmmaFace("confused", 2) 
#                                                        if "frisky" in E_History:
#                                                                call Statup("Emma", "Love", 200, -5) 
#                                                                call Statup("Emma", "Obed", 80, 10)   
#                                                        else:
#                                                                call Statup("Emma", "Obed", 80, 5)
#                                                                call Statup("Emma", "Inbt", 50, -5)  
#                                                        $ Line = "ask"
#                                                    elif ApprovalCheck("Emma", 500, "LO"):
#                                                        call EmmaFace("confused", 1, Brows="angry") 
#                                                        if "frisky" in E_History:
#                                                                call Statup("Emma", "Love", 200, -5) 
#                                                                call Statup("Emma", "Obed", 80, 5)  
#                                                        else:
#                                                                call Statup("Emma", "Obed", 80, 5)
#                                                                call Statup("Emma", "Inbt", 50, -5)  
#                                                        $ Line = "ask"            
#                                            ". . .":
#                                                    if ApprovalCheck("Emma", 500, "O"):
#                                                        call EmmaFace("confused", 2) 
#                                                        if "frisky" in E_History:
#                                                                call Statup("Emma", "Obed", 50, 5)
#                                                                call Statup("Emma", "Inbt", 50, -5)   
#                                                        else:
#                                                                call Statup("Emma", "Obed", 50, 5)
#                                                                call Statup("Emma", "Inbt", 50, -5)  
#                                                        $ Line = "ask"
#                                                    elif ApprovalCheck("Emma", 500, "LO"):
#                                                        call EmmaFace("confused", 1, Brows="angry") 
#                                                        if "frisky" in E_History:
#                                                                call Statup("Emma", "Love", 200, -5) 
#                                                                call Statup("Emma", "Obed", 50, 5)
#                                                                call Statup("Emma", "Inbt", 50, -5)   
#                                                        else:
#                                                                call Statup("Emma", "Obed", 50, 5)
#                                                                call Statup("Emma", "Inbt", 50, -5)  
#                                                        $ Line = "ask"   
#                                        if Line == "ask":
#                                            call EmmaFace("bemused", Eyes="side") 
#                                            ch_e "Take off some clothes. . ."
#                                            $ Line = "strip"
#                                        call EmmaFace("sly", Brows="confused") 
#                                        menu:
#                                            ch_e "Would that interest you?"
#                                            "Definitely!":
#                                                call EmmaFace("sly",Mouth="smile")    
#                                                call Statup("Emma", "Love", 50, 5)
#                                                call Statup("Emma", "Love", 80, 5) 
#                                                call Statup("Emma", "Inbt", 50, 5)                                               
#                                            "Yeah.":
#                                                call EmmaFace("sly")     
#                                                call Statup("Emma", "Love", 80, 3) 
#                                                call Statup("Emma", "Obed", 50, 3)
#                                                call Statup("Emma", "Inbt", 50, 3)                                              
#                                            "No thanks.":
#                                                if "frisky" in E_History:
#                                                        call Statup("Emma", "Love", 200, -10) 
#                                                        call Statup("Emma", "Obed", 80, 10)
#                                                        call Statup("Emma", "Inbt", 50, -5)   
#                                                else:
#                                                        call Statup("Emma", "Love", 200, -5) 
#                                                        call Statup("Emma", "Obed", 80, 5)
#                                                        call Statup("Emma", "Inbt", 50, -5)  
#                                                call EmmaFace("angry") 
#                                                ch_e "Hrm."
#                                                $ Line = "no"
                                        
#                                if Line == "strip":
#                                        call EmmaFace("sly", 0) 
#                                        if Girl:
#                                            ch_e "And you, [Girl]? Care to participate?"                     
#                                            call Date_Sex_Break("Emma",Girl)
#                                            if _return == 4:
#                                                #you stop it because of the other girl
#                                                ch_e "Well I suppose we can. . . postone that."
#                                            else:
#                                                if _return == 3:
#                                                    #the other girl is mad
#                                                    ch_e "Well I suppose that answers that."
#                                                elif _return == 2:
#                                                    #the other girl will watch
#                                                    ch_e "I suppose you can just watch then. . ."                                                    
#                                                elif _return == 1:
#                                                    if Girl == "Rogue":
#                                                        ch_r "I guess I could join in."
#                                                    elif Girl == "Kitty":
#                                                        ch_k "It could be fun. . ."
#                                                call Emma_Strip_Study
#                                        else:            
#                                            call Emma_Strip_Study
#                                else: 
#                                        return
#            elif ApprovalCheck("Emma", 700) and E_Kissed > 1:
#                        "Emma leans close to you, and leans in for a kiss."   
#                        $ Line = "kissing"
#            elif ApprovalCheck("Emma", 500):
#                        "Emma leans close to you and you spend the rest of the study session nuzzled close."                        
#                        call Date_Sex_Break("Emma",Girl,2)
#                        if _return == 3:
#                                "[Girl] glowers at you a bit."
#            if Line == "strip":
#                    pass
#            elif Line:
#                    #if something sexual is happening. . .
#                    call Date_Sex_Break("Emma",Girl)
#                    if _return == 4:
#                            if Line == "blow":
#                                    "Emma lets your dick fall out of her mouth."
#                                    "You zip your pants back up." 
#                            elif Line == "hand":
#                                    "Emma lets your dick drop into your lap"
#                                    "You zip your pants back up." 
#                            else:
#                                    "Emma stops what she's doing."
#                            ch_e "Oh, very well."                                               
#                    else:
#                        if _return == 3:
#                            #if the other girl took off. . .
#                            menu:
#                                ch_e "You don't mind if I continue?"
#                                "Go ahead.":
#                                        ch_e "Lovely."
#                                        call Emma_SexAct(Line) 
#                                "We should stop.":
#                                        ch_e "Spoil sport."
#                        else:
#                                        call Emma_SexAct(Line) 
#            else:
#                    return
                
#            if "frisky" not in E_History:
#                    $ E_History.append("frisky")
#            "Well that was certainly a productive use of your study time. . ."    
#            return
            

    