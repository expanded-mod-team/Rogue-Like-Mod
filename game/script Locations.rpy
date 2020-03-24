# //////////////////////////////////////////////////////////////////////                World Map Interface 

label Worldmap:  
    scene bg_campus onlayer backdrop   
    scene 
    $ Taboo = 0
    menu:
        "Where would you like to go?"
        "My Room":
                    $ renpy.pop_call() 
                    jump Player_Room_Entry  
        "Testbed" if config.developer:          
                    $ renpy.pop_call() 
                    jump Rogue_Room_Test
        "Girl's Rooms":
            menu:
                "[RogueX.Name]'s Room":   
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History:  
                            call Girls_Room_Entry(KittyX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call Girls_Room_Entry(EmmaX)  
                "[LauraX.Name]'s Room" if "met" in LauraX.History:  
                            call Girls_Room_Entry(LauraX)  
                "Back":
                            jump Worldmap
        "University Square":
                    $ renpy.pop_call() 
                    jump Campus_Entry 
        "Class":
            if Current_Time != "Night":
                $ renpy.pop_call() 
                jump Class_Room_Entry 
            elif "Xavier" in Keys:
                        "The door is locked, but you were able to use Xavier's key to get in."
                        $ renpy.pop_call() 
                        jump Class_Room_Entry 
            else:
                        "It's late for classes and the classrooms are locked down."
                        jump Worldmap
        "The Danger Room":         
                    $ renpy.pop_call()    
                    jump Danger_Room_Entry
        "The showers":
                    $ renpy.pop_call() 
                    jump Shower_Room_Entry    
        "The pool": 
                    $ renpy.pop_call() 
                    jump Pool_Entry           
        "Xavier's Study":
                    $ renpy.pop_call() 
                    jump Study_Room_Entry 
        "Stay where I am.":
                    return
    return          
                    
# end World Map Interface //////////////////////////////////////////////////////////////////////

# start Misplaced location checker  //////////////////////////////////////////////////////////////////////
label Misplaced:
        if Trigger and Trigger in TotalGirls:
                #sent here by a broken sex action, Trigger should be girl's name
                call expression  Trigger.Tag + "_SexMenu"
        #if "Historia" in Player.Traits:
                #call Historia_Clear
        $ Player.DrainWord("locked",0,0,1)
        $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
        while StackDepth > 0:
            $ StackDepth -= 1
            $ renpy.pop_call()
        if bg_current == "bg player":
                jump Player_Room 
        if bg_current == "bg rogue":
                jump Rogue_Room 
        if bg_current == "bg kitty":
                jump Kitty_Room 
        if bg_current == "bg emma":
                jump Emma_Room 
        if bg_current == "bg laura":
                jump Laura_Room 
        if bg_current == "bg dangerroom":
                jump Danger_Room 
        if bg_current == "bg classroom":
                jump Class_Room 
        if bg_current == "bg showerroom":
                jump Shower_Room 
        if bg_current == "bg study":
                jump Study_Room 
        if bg_current == "bg pool":
                jump Pool_Entry
        jump Campus 
            
        return
# end Misplaced location checker  //////////////////////////////////////////////////////////////////////


# Player's Room Interface //////////////////////////////////////////////////////////////////////
label Player_Room_Entry:
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg player"   
    call Gym_Clothes
    $ Player.RecentActions.append("traveling")
    $ Nearby = []
    call EventCalls
    call Set_The_Scene
    jump Clear_Stack #removes stray calls in the call stack
    
label Player_Room:
    $ bg_current = "bg player"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls                
    call GirlsAngry      

# Player Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in your room. What would you like to do?"
        "Chat":
                    call Chat
            
        "Would you like to study?":
                    call Study_Session
                
        "Lock the door" if "locked" not in Player.Traits:
                    "You lock the door"
                    $ Player.Traits.append("locked")
                    call Taboo_Level
                            
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level
                    
        "Sleep" if Current_Time == "Night":            
                    call Round10
                    call Girls_Location
                    call EventCalls  
        "Wait" if Current_Time != "Night":
                    "You wait around a bit."
                    call Wait                 
                    call Girls_Location
                    call EventCalls      
            
        "Shop":
                    call Shop                
        "Special Options":
                    call SpecialMenu #found in Rogue Scenes
        
        
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":   
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History:   
                            call Girls_Room_Entry(KittyX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call Girls_Room_Entry(EmmaX)  
                "[LauraX.Name]'s Room" if "met" in LauraX.History: 
                            call Girls_Room_Entry(LauraX)  
                "Back":
                            pass
        "Go to the Showers" if TravelMode:         
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
                    
    jump Player_Room

# end Player's Room Interface //////////////////////////////////////////////////////////////////////


# University Square Interface //////////////////////////////////////////////////////////////////////

label Campus_Map:
    $ Line = 0
    $ Trigger = 0
    $ Trigger2 = 0
    $ Trigger3 = 0
    $ Trigger4 = 0
    $ Trigger5 = 0
    $ bg_current = "bg campus"    
    $ Player.DrainWord("locked",0,0,1)
    call Set_The_Scene
    if not TravelMode: 
        call Worldmap
    jump Campus
    
label Campus_Entry:
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg campus"        
    $ Nearby = []             
    call Gym_Clothes  
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene
    
label Campus:
    $ bg_current = "bg campus"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents    
    call Checkout(1)    
    call GirlsAngry    
    if Current_Time == "Evening" and "yesdate" in Player.DailyActions:
            #if it's evening and you have a date lined up. . .
            menu:
                "Ready to go on that date?"
                "Yes":
                        call DateNight
                        if "yesdate" in Player.DailyActions:
                                $ Player.DailyActions.remove("yesdate")
                "One moment. . .":
                        pass
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location
    #End date code

# Uni Square Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You are in the university square. What would you like to do?"
        
        "Chat":
            call Chat
            
        "Wait." if Current_Time != "Night":
            "You wait around a bit."
            call Wait   
            call EventCalls            
            call Girls_Location
            
        "Go to my Room" if TravelMode:
                    jump Player_Room_Entry  
        "Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":   
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History:   
                            call Girls_Room_Entry(KittyX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call Girls_Room_Entry(EmmaX)  
                "[LauraX.Name]'s Room" if "met" in LauraX.History: 
                            call Girls_Room_Entry(LauraX)  
                "Back":
                            pass
        "Go to the classroom" if TravelMode: 
                    if Current_Time != "Night":
                        jump Class_Room_Entry 
                    elif "Xavier" in Keys:
                        "The door is locked, but you were able to use Xavier's key to get in."
                        jump Class_Room_Entry 
                    else:
                        "It's late for classes and the classrooms are locked down."   
        "Go to the Danger Room" if TravelMode: 
                    jump Danger_Room_Entry
        "Go to the showers" if TravelMode: 
                    jump Shower_Room_Entry   
        "Go to the pool" if TravelMode: 
                    jump Pool_Entry         
        "Xavier's Study" if TravelMode: 
                    jump Study_Room_Entry 
                    
        "Leave" if not TravelMode:
                    call Worldmap
                    
    jump Campus

# end University Square Interface //////////////////////////////////////////////////////////////////////


# Classroom Interface //////////////////////////////////////////////////////////////////////

label Class_Room_Entry:
    $ Player.DrainWord("locked",0,0,1)
    $ Present = []
    $ bg_current = "bg classroom"       
    $ Nearby = []               
    call Gym_Clothes 
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    call EventCalls
    call Set_The_Scene(0) #won't display characters yet)
    $ Line = "entry"
                
label Class_Room:    
    $ bg_current = "bg classroom"    
    if "goto" in Player.RecentActions or "traveling" in Player.RecentActions:
            $ Present = []        
            if Current_Time != "Night" and Current_Time != "Evening" and Weekday < 5:   
                    call Class_Room_Seating    
            $ Player.DrainWord("goto",1,0)
            $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents    
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location
    call GirlsAngry  
    
    if Line == "entry":
            if EmmaX.Loc == "bg teacher":
                    $ Line = "As you sit down, you see "+ EmmaX.Name +" at the podium. What would you like to do?" 
            elif Current_Time == "Evening" or Weekday > 5:   
                    $ Line = "You enter the classroom. What would you like to do?" 
            else:
                    $ Line = "You sit down at a desk. What would you like to do?" 
    else:
            if Line != "What would you like to do next?":
                    $ Line = "You are in class right now. What would you like to do?" 
    #End Room Set-up
    
# Class Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<        
    menu:
        "[Line]" 
        "Take the morning class" if Weekday < 5 and Current_Time == "Morning":
                if Round >= 30:
                    jump Take_Class
                else: 
                    "Class is already letting out. You can hang out until the next one."             
        "Take the afternoon class" if Weekday < 5 and Current_Time == "Midday":
                if Round >= 30:
                    jump Take_Class
                else: 
                    "Class is already letting out. You can hang out until they lock up for the night." 
        "There are no classes right now (locked)" if Weekday >= 5 or Current_Time == "Evening" or Current_Time == "Night":
                pass
            
        "Chat":
                call Chat
                $ Line = "You are in class right now. What would you like to do?" 
           
        "Lock the door" if "locked" not in Player.Traits:
                    if Current_Time == "Evening" or Current_Time == "Night" or Weekday >=5:
                            "You lock the door"
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during class."
                            
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level                    
                    
        "Wait" if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls            
                call Girls_Location 
                    
                if Current_Time == "Midday":
                            $ Line = "A new class is in session. What would you like to do?"
                if Current_Time == "Evening":
                            $ Line = "Classes have let out for the day. What would you like to do?"
                                
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    $ Line = 0
    jump Class_Room

# End Core Classroom menu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
label Take_Class:                       #Class events 
    call Set_The_Scene  
    if "class" in Player.DailyActions:
            $ Line = "The session begins."
    elif Round >= 80:
            $ Line = "You make it in time for the start of the class."
    elif Round >= 50:
            $ Line = "You get in a bit late, but there's plenty of class left."
    elif Round >= 30:
            $ Line = "You're pretty late, but catch the tail end of the class."
    $ Trigger = 0
    
    $ D20 = renpy.random.randint(1, 20)
    if RogueX in Present and D20 > 10 and RogueX.Inbt >= 500 and RogueX.Loc == "bg classroom":        
        "[Line]"    
        call Rogue_Frisky_Class
    else:        
        $ Line = Line + renpy.random.choice([" It was fairly boring.", 
                " It was a lesson in mutant biology.", 
                " You took a math course.",
                " You watched a movie about sealions.",
                " That was fun.",
                " Applied trigonometry is surprisingly interesting, especially when Cyclops demonstrates using it for trick shots.",
                " Geopolitical science: Latveria to Madripoor.",
                " Today's lecture is on reading body language. You suppose if anyone would know about reading people. . .",
                " The topic of the day is Mutants and the larger superhuman community.", 
                " Capes: What Your Name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
                " The topic is \"Mutants VS Mutates.\" As it turns out, the terms aren’t interchangeable.",  
                " Today's class is on how to present yourself to the public. She uses Spider-Man as an example of how bad PR makes your life harder than it needs to be.",                     
                " Mutant History, Apocalypse to Dark Phoenix.",
                " You spend some time learning about politics. Senator Trask seems like a real piece of work.",
                " You spend class learning about Aristotelian philosophy. Or about "+EmmaX.Name+"'s breasts.",
                " You learn how civil laws apply to mutant powers by studying some high profile case studies. It's surprisingly interesting.",
                " You listen as a guest speaker describes working with a Genosha-based NGO trying to rehabilitate mutants in the States.",
                " Today the teacher is describing the theory behind mutant powers. For some reason, you get the impression she is glancing at you during the lecture.",                                                                                                 
                " Game writing for dummies, eh?"]) 
        "[Line]"    
    $ Player.RecentActions.append("class")                      
    $ Player.DailyActions.append("class")   
    $ Player.XP += (5 + (int(Round / 10)))
        
    call Wait   
    call Girls_Location
    call Set_The_Scene 
    call EventCalls
    $ Line = "What would you like to do next?"    
    jump Class_Room
    
# End "Taking Class" <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<          


label Class_Room_Seating(Girls=[],GirlB=0,GirlLike=0,Line=0,D20=0):
    # Girls is the amount of girls in the room. 
    # active ones get priority, then shuffled, then nearby girls
    $ Present = []
    if RogueX.Loc == bg_current:  
                $ Girls.append(RogueX)
    if KittyX.Loc == bg_current:
                $ Girls.append(KittyX)
    if LauraX.Loc == bg_current:
                $ Girls.append(LauraX) 
        
    $ renpy.random.shuffle(Girls)
    
    if RogueX in Nearby and RogueX not in Girls: 
                $ Girls.append(RogueX)
    if KittyX in Nearby and KittyX not in Girls:
                $ Girls.append(KittyX)
    if LauraX in Nearby and LauraX not in Girls:
                $ Girls.append(LauraX)   
    #End Girl selections
        
    $ Nearby = []
    
    if len(Girls) == 2:
            # there are two girls
            $ D20 = renpy.random.randint(500, 1500)
            if (Girls[0].GirlLikeCheck(Girls[1]) + Girls[1].GirlLikeCheck(Girls[0])) >= D20:
                "You see that [Girls[0].Name] and [Girls[1].Name] are sitting next to each other, which do you sit next to?"
            else:
                "You see that [Girls[0].Name] and [Girls[1].Name] are in the room, but on opposite sides."               
                if RogueX in Girls and RogueX not in Nearby:
                            $ Nearby.append(RogueX) 
                if KittyX in Girls and KittyX not in Nearby:
                            $ Nearby.append(KittyX)    
                if LauraX in Girls and LauraX not in Nearby:
                            $ Nearby.append(LauraX)  
            menu:
                extend ""
                "[Girls[0].Name]":
                        $ Present = [Girls[0]]
                        if Girls[0] in Nearby:
                            $ Nearby.remove(Girls[0])
                "[Girls[1].Name]":
                        $ Present = [Girls[1]]   
                        if Girls[1] in Nearby:
                            $ Nearby.remove(Girls[1])
                "Between them." if not Nearby:
                        $ Present = [Girls[0],Girls[1]] 
                        if Girls[1] in Nearby: 
                            $ Nearby.remove(Girls[1])
                        if Girls[0] in Nearby:
                            $ Nearby.remove(Girls[0])                                  
                "Neither":
                        "You decide to sit a distance away from either of them."
                        if RogueX in Girls and RogueX not in Nearby:
                                    $ Nearby.append(RogueX) 
                        if KittyX in Girls and KittyX not in Nearby:
                                    $ Nearby.append(KittyX)    
                        if LauraX in Girls and LauraX not in Nearby:
                                    $ Nearby.append(LauraX)  

    #end two-girl option
    elif len(Girls) > 2:
            # there are two+ girls
            "You see several girls are in the room, who would you like to sit near?"                            
            while len(Present) < 2:
                    menu:
                        "Select up to two."
                        "[RogueX.Name]" if RogueX in Girls:
                                $ RogueX.Loc = "bg classroom"
                                $ Present.append(RogueX)
                        "[KittyX.Name]" if KittyX in Girls:
                                $ KittyX.Loc = "bg classroom"
                                $ Present.append(KittyX)    
                        "[LauraX.Name]" if LauraX in Girls:
                                $ LauraX.Loc = "bg classroom"
                                $ Present.append(LauraX)                                
                        "Done":                                
                                $ Present.append("junk")      
                                $ Present.append("junk2") 
                    
            if "junk" in Present:
                    $ Present.remove("junk")
            if "junk2" in Present:
                    $ Present.remove("junk2") 
            if len(Present) == 2:
                    "You sit between [Present[0].Name] and [Present[1].Name]."
            elif Present:
                    "You sit next to [Present[0].Name]."
            else:
                    "You sit off to the side."
                                
            if len(Girls) > len(Present):
                
                    #if there were girls not picked
                    "The rest are scattered around the room."                    
                    if RogueX in Girls and RogueX not in Present and RogueX not in Nearby:
                                $ Nearby.append(RogueX) 
                    if KittyX in Girls and KittyX not in Present and KittyX not in Nearby:
                                $ Nearby.append(KittyX)    
                    if LauraX in Girls and LauraX not in Present and LauraX not in Nearby:
                                $ Nearby.append(LauraX)    
                                
    #end two-girl option
    elif Girls:
            # there is one girl
            menu:
                "You see [Girls[0].Name] is there, do you sit next to her?"
                "Yes":
                        $ Present.append(Girls[0])
                "No, I'll sit away from her a bit.":
                        $ Nearby.append(Girls[0]) 
    #end one-girl option
    #else: no girls at all
    
    if RogueX in Girls and RogueX in Nearby:
            $ RogueX.Loc = "nearby"
    if KittyX in Girls and KittyX in Nearby:
            $ KittyX.Loc = "nearby"   
    if LauraX in Girls and LauraX in Nearby:
            $ LauraX.Loc = "nearby"
           
    if Present:
            call Shift_Focus(Present[0])
    call Set_The_Scene(Quiet=1)
    
    return
    
# end Class Room Interface //////////////////////////////////////////////////////////////////////


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Danger_Room_Entry:
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg dangerroom"       
    $ Nearby = []     
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    call EventCalls
    call Gym_Clothes("pre")#Automatically puts them in gym clothes if they've been here
    call Set_The_Scene
    
label Danger_Room:
    $ bg_current = "bg dangerroom"  
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1) 
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location 
                call Gym_Clothes                
    call GirlsAngry  
    #End Room Set-up
    
# Danger Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu:
        "This is the Danger Room. What would you like to do?" 
#        extend ""        
        "Train":
                if Current_Time == "Night":
                        "The Danger Room has been powered off for the night, maybe take a break."
                elif Round >= 30:
                        jump Training
                else:
                        "There really isn't time to do much before the next rotation, maybe wait a bit."
                    
        "Chat":
                call Chat
        "Historical Simulator":    
                    ch_danger "This function allows you to revisit previous events in your history."
                    ch_danger "Unfortunately, this function is temporarily disabled."
                    #call Danger_Room_Historia
              
        "Lock the door" if "locked" not in Player.Traits:
                    if Current_Time == "Night":
                            "You lock the door"
                            $ Player.Traits.append("locked")
                            call Taboo_Level
                    else:
                            "You can't really do that during free hours."
                            
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level        
                    
        "Wait. (locked)" if Current_Time == "Night":
                    pass
        "Wait." if Current_Time != "Night":
                    "You hang out for a bit."
                    call Wait   
                    call EventCalls
                    call Girls_Location 
                    call Gym_Clothes
                      
        "Leave" if not TravelMode:       
                    call Gym_Clothes("change")
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:         
                    call Gym_Clothes("change")
                    jump Campus_Entry
                    
        "Go to the showers" if TravelMode:             
                    call Gym_Clothes("change")
                    jump Shower_Room_Entry         
    jump Danger_Room

label Training:
    $ D20 = renpy.random.randint(1, 20)
#    if D20 > 10 and RogueX.Inbt >= 500:
#        call Rogue_Frisky_Danger
        
    $ Player.XP += (5 + (int(Round / 10)))
    $ Player.DailyActions.append("dangerroom")
    call Set_The_Scene
    
    if Round >= 80:
            $ Line = "You have a long session in the Danger Room."
    elif Round >= 50:
            $ Line = "You have a short workout in the Danger Room."
    else:
            $ Line = "You squeeze in a quick session in the Danger Room."
        
    $ Trigger = 0
    if D20 >= 18:
            #if "cyclops":
            "[Line] During the exercise, Cyclops accidentally shoots you."
            "Luckily you're immune to the beams, but your clothes weren't so lucky."
            call RoomStatboost("Love",80,2)
            call RoomStatboost("Lust",80,5)
    elif D20 >= 17:
            "[Line] You participate in a hand-to-hand combat class." 
            "Before you begin, Cyclops explains that it’s always good to know how to defend yourself when you can’t rely on your powers."
            "It sounds like there’s a story there."
    elif D20 >= 16:
            "Some of the senior students walk over to talk about your powers."
            "Nightcrawler wonders aloud what would happen if he grabbed you and tried to teleport while you tried to disable his powers."
            "You succeed in freaking each other out."
    else:
            $ Line = Line + renpy.random.choice([" It was fairly boring.", 
                    " You do some training with basic firearms.", 
                    " You run the obstacle course.",
                    " You fight in a simulated battle against the Brotherhood.",
                    " You help take down a holographic Sentinel.",
                    " You take part in a training exercise against the Avengers. As if the X-Men and Avengers would ever fight.",                     
                    " You and some of the others take part in a survival exercise. . . also known as \"try to last as long as you can while Wolverine hunts you down one by one.\"",
                    " You decide to test yourself by facing off against Magneto solo. It goes about as well as you’d expect.",
                    " You use the Danger Room’s holograms to relive some of the original X-Men’s biggest battles. You learn quite a bit about teamwork.", 
                    " Beast is teaching a class on parkour. You take part and pick up a few pointers. You’re no Spider-Man, but at least you pick up a few things.",  
                    " You participate in an emergency drill. You pick up quite a few tips about first aid, triage and the proper way to move injured people.", 
                    " You take part in an urban emergency situation exercise. Cyclops takes the time to explain to you how to use cover to get close enough to use your powers.", 
                    " You take part in a jungle simulation exercise under Wolverine. You learn some basic survival techniques, but you privately hope you never need them.", 
                    " Your team fight a simulation of Magneto."])   
            "[Line]"    
    if RogueX.Loc == bg_current:
        call Rogue_TightsRipped
    
    call Wait
    call Girls_Location 
    call Set_The_Scene
    $ Line = "The training session has ended, what would you like to do next?"
    
    jump Danger_Room

label Rogue_TightsRipped(Count = 0):
        if RogueX.Hose == "tights":
                $ Count = 1
                $ RogueX.Hose = "ripped tights"    
                $ RogueX.FaceChange("angry")
                if "ripped tights" in RogueX.Inventory:  
                    ch_r "Damnation, that's another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "Well that's a good pair of tights down the chute."                
        elif RogueX.Hose == "pantyhose":
                $ Count = 1
                $ RogueX.Hose = "ripped pantyhose"              
                $ RogueX.FaceChange("angry")
                if "ripped pantyhose" in RogueX.Inventory:  
                    ch_r "Tsk, another pair ruined!"
                else:
                    $ Count = 2               
                    ch_r "I hate getting a run in these things."     
        if Count:
                #If they ripped
                if not RogueX.Legs and RogueX.Panties != "shorts":
                        if RogueX.Panties: 
                            if RogueX.SeenPanties:
                                $ Count = 3 if not ApprovalCheck(RogueX, 600) else Count
                            else:
                                $ RogueX.SeenPanties = 1
                                $ Count = 3 if not ApprovalCheck(RogueX, 900) else Count                            
                            $ RogueX.Statup("Lust", 60, 2)
                        else:
                            if RogueX.SeenPussy:
                                $ Count = 3 if not ApprovalCheck(RogueX, 900) else Count
                            else:
                                call Rogue_First_Bottomless 
                                $ Count = 3 if not ApprovalCheck(RogueX, 1400) else Count
                            
                if Count == 2: 
                        #first time
                        menu:
                            extend ""
                            "I think those look really good on you.":                
                                $ RogueX.FaceChange("smile", 1)                     
                                $ RogueX.Inventory.append(RogueX.Hose) 
                                ch_r "You think so? That's sweet, maybe I'll keep them on hand." 
                            "Yeah, too bad.":             
                                $ RogueX.FaceChange("bemused")    
                                ch_r ". . ."         
                            "Ha! Those don't leave much to the imagination!":                        
                                ch_r "Thanks for that. . ."
                                
                elif Count == 3: #She is embarassed and takes off             
                    $ RogueX.FaceChange("startled", 2)  
                    ch_r "I, um, I should get out of here."
                    $ RogueX.Blush = 1
                    call Remove_Girl(RogueX)
                    $ RogueX.OutfitChange()
                #end "if they ripped"
        return
                
# end Danger Room Interface //////////////////////////////////////////////////////////////////////


# Danger Room Interface //////////////////////////////////////////////////////////////////////

label Pool_Entry:
    $ Player.DrainWord("locked",0,0,1)
    $ bg_current = "bg pool"       
    $ Nearby = []     
    call Taboo_Level
    $ Player.RecentActions.append("traveling")
    call EventCalls
    call Gym_Clothes
    call Set_The_Scene
    
label Pool_Room:
    $ bg_current = "bg pool"  
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1,Dress=0) 
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location            
    call GirlsAngry  
    #End Room Set-up
    
# Pool Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    menu:
        "You're at the pool. What would you like to do?" 
                    
        "Chat":
                call Chat    
        
        "Want to sunbathe?" if Time_Count < 2:
                call Pool_Sunbathe
                $ Round -= 20 if Round >= 20 else Round  
                "You just hang out for a little while."
        "Want to swim?":
            if Current_Time == "Night" and AloneCheck():
                "It's a bit late for a swim." 
            else:                
                call Pool_Swim
        "Want to skinnydip?":
                call Pool_Skinnydip
                        
        "Wait. (locked)" if Current_Time == "Night":
                pass
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                call Wait   
                call EventCalls
                call Girls_Location 
                      
        "Leave" if not TravelMode:       
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:      
                    jump Campus_Entry
                    
        "Go to the showers" if TravelMode:   
                jump Shower_Room_Entry         
    jump Pool_Room

label Pool_Swim(Swimmers=[],BO=[]):
    $ D20 = renpy.random.randint(1, 20)
        
    $ Player.DailyActions.append("swim")
    call Set_The_Scene
        
    $ Line = ""
    $ PassLine = 0
    $ BO = TotalGirls[:]      
    while BO:                              
            if bg_current == BO[0].Loc and ApprovalCheck(BO[0], 700): 
                    if BO[0].Chest == BO[0].Swim[5] and BO[0].Panties == BO[0].Swim[6]:
                                # if she's already in swimwear . . .
                                $ Swimmers.append(BO[0])
                    elif not BO[0].ChestNum() and not BO[0].OverNum() and not BO[0].PantiesNum() and not BO[0].PantsNum() and not BO[0].HoseNum():
                                # or is nude. . .
                                $ Swimmers.append(BO[0])
                    else:                        
                        if Line or PassLine:
                                #if it's second time through
                                call Display_Girl(BO[0],0,0,950,150)
                        else:
                                call Display_Girl(BO[0],0,0,800,150)
                        if BO[0].OutfitChange("swimwear"):
                                #if changed into swimsuit. . . 
                                $ Line = "" if Swimmers and not PassLine else "s" #whole point of this is to change the plaurals
                                $ Swimmers.append(BO[0])
                        else:
                                #If she doesn't swim. . .
                                $ Line = "" if PassLine and not Swimmers else "s"
                                $ PassLine = PassLine + " and " + BO[0].Name if PassLine else BO[0].Name 
            $ BO.remove(BO[0])
                    
    if len(Swimmers) >= 2:
            "The girls get[Line] changed and join you."
    elif Swimmers:
            "[Swimmers[0].Name] get[Line] changed and joins you." 
    if PassLine:
            "[PassLine] chill[Line] out poolside."
    $ PassLine = 0
    $ Line = 0
    
    call ShowPool(Swimmers[:]) #displays pool graphics
    
    if D20 >= 15 and Swimmers:
            call Pool_Topless(Swimmers[0])            
    if D20 >= 11:
            "You take a nice, refreshing swim." 
    elif D20 == 2:
            "You join some of the others in a rousing game of Marco Polo."
    elif D20 == 3:
            "You manage to snag one of the floating chairs and drift lazily on the water." 
    elif D20 == 4:
            "You manage to snag one of the floating chairs and drift lazily on the water."
            "Until, that is, Kurt teleports up in the air nearby and performs an admittedly awesome cannonball."
            "Too bad it capsizes your chair."
    elif D20 == 5:
            "You test yourself by swimming from one end of the pool to the other."
    elif D20 == 6:
            "You try to impress some of the girls by doing a running jump into the pool."
            "You wind up triggering a cannonball competition that’s ironically NOT won by Cannonball, much to his shock." 
    elif D20 == 7:
            "You are about to get into the pool when you hear annoyed cries and shouts of, \"Bobby!\""
            "Looks like Iceman made himself a floating chair again."
            "You stick to the far end of the pool, where it isn’t freezing cold."
    elif D20 == 8:
            "You relax on one of the poolside chairs instead." 
    elif D20 == 9:
            "Cyclops is instructing some of the other students in water rescues."
            "You listen in as he talks about approaching a drowning victim from behind so that their panicked flailing won’t cause you injury."  
    elif D20 == 10:
            "You decide to make use of the diving board. You do a couple of dives before taking it easy and just swimming around." 
            
    call GirlWaitUp(1,80,3) #makes any girls in the room like each other a bit more.
    call RoomStatboost("Love",80,3)
    call RoomStatboost("Lust",30,5)
    $ Round -= 20 if Round >= 20 else Round    
    hide FullPool
    call Set_The_Scene(1,0,0)
    "You all get out of the pool and rest for a bit."
    return   
                
# end Pool Interface //////////////////////////////////////////////////////////////////////


image FullPool:
        #water
        AlphaMask("bg_pool", "images/PoolMask.png")
        
label ShowPool(BO=[],Loc=0):
        #displays the pool with girls in it
        #if not BO:
                #$ BO = TotalGirls[:] 
        while BO:  
                if BO[0].Loc == bg_current:
                            $ BO[0].AddWord(0,"swim","swim",0,0) #adds "swim" tag to recent and daily actions  
                            $ BO[0].Water = 1                            
                            $ DLoc = 500 if len(BO) > 1 else 650  
                            if BO[0] == RogueX:
                                    show Rogue_Sprite at Pool_Bob(DLoc) zorder 50 
                            elif BO[0] == KittyX:
                                    show Kitty_Sprite at Pool_Bob(DLoc) zorder 50                            
                            elif BO[0] == EmmaX:
                                    show Emma_Sprite at Pool_Bob(DLoc) zorder 50 
                            elif BO[0] == LauraX: 
                                    show Laura_Sprite at Pool_Bob(DLoc) zorder 50 #BO[0].Layer  
                $ BO.remove(BO[0])
        show FullPool zorder 60        #should put masked pool above girls #175?
        return
        
        
#                                    show Rogue_Sprite zorder BO[0].Layer:
#                                            alpha 1
#                                            zoom .45
#                                            offset (0,0)
#                                            anchor (0.5, 0.0)  
#                                            pos (DLoc,450)   
#                                    show Rogue_Sprite at Pool_Bob

transform Pool_Bob(DLoc=500):     
        subpixel True 
        pos (DLoc,450)
        alpha 1
        zoom .45
        offset (0,0)
        anchor (0.5, 0.0)  
        xoffset 0
        yoffset 0
        choice:
            yoffset 0
        choice:
            pause .3
        choice:
            pause .5
        block:     
            ease 1 yoffset 10 
            ease 1.5 yoffset 0 
            repeat
        
# Showers Interface //////////////////////////////////////////////////////////////////////
label Shower_Room_Entry:
    $ bg_current = "bg showerroom"      
    $ Player.DrainWord("locked",0,0,1)
    $ Nearby = []     
    $ Present = []
    call Gym_Clothes  
    call Taboo_Level
    call Set_The_Scene(0,1,0)
    if Round <= 10 or len(Party) >= 2:         
            jump Shower_Room
        
    $ Options = []
    $ Line = ActiveGirls[:]   #make sure this is initialized
    while Line:
            #loops through and adds populates Occupants with locals   
            if Line[0] not in Party and "showered" not in Line[0].DailyActions and (Line[0].Loc == Line[0].Home or Line[0].Loc == "bg dangerroom"):  
                    #Checks if girl is in the shower
                    $ Options.append(Line[0])   
            $ Line.remove(Line[0])   
    $ Line = 0
    
    if Options:        
                $ renpy.random.shuffle(Options)
    
    $ D20 = renpy.random.randint(1, 20) 
    # <5 is they show up late, 5-10 is they haven't showered yet, 10-15 is they finished, 
    # >15 is you walk in on them, >17 they might be masturbating
        
    if D20 < 5 or (len(Options) + len(Party) > 2):  #not Options or 
                # if < 5, they show up late, or if there are more potential girls than room for them
                while Options and (D20 < 5 or len(Options) + len(Party) > 2):
                        #Loops through while Options and Party are more than 2
                        $ Nearby.append(Options[0])     #adds this girl to the nearby roster
                        $ Options[0].Loc = "nearby"     #adds this girl to the nearby roster
                        $ Options.remove(Options[0])    #subs this girl from Options
                
    if not Party and D20 > 15 and Options and Options[0] in TotalGirls:               
                call Girl_Caught_Shower(Options[0])
                jump Shower_Room
    #End Caught Check
    
    # If none of the caught dialogs plays, checks to see if anyone is in the room, and allows them to be there if they are. 
    $ Line = Options[:]
    while Line:
            #loops through and adds populates nearby with locals  
            $ Line[0].Loc = bg_current  
            $ Line.remove(Line[0])   
    $ Line = 0
    
    call Present_Check(0)
            
    $ Line = Options[:] 
    while Line:
            #loops through and puts towels on them, maybe the "showered" trait
            if Line[0].Loc == bg_current and Line[0] not in Party:
                    if D20 >= 10:
                            $ Line[0].RecentActions.append("showered")                      
                            $ Line[0].DailyActions.append("showered")  
                    $ Line[0].OutfitChange("towel")                     
            $ Line.remove(Line[0])   
    $ Line = 0     
    #End Count set-up
    
    call Set_The_Scene(Dress=0)
    if Party:
        $ Line = " and " + Party[0].Name
    else:
        $ Line = ""
    if len(Options) >= 2:    
        "As you enter, you[Line] see [Options[0].Name] and [Options[1].Name] standing there."           
    elif Options:
        "As you enter, you[Line] see [Options[0].Name] standing there."
    $ Line = 0
    
    if Options:          
            $ Line = 0
            if Options[0] == RogueX:
                    ch_r "Hey, [RogueX.Petname]."
                    if "showered" in RogueX.RecentActions:                    
                            ch_r "I was just getting ready to head out."
                    if not ApprovalCheck(Options[0], 900):
                            ch_r "See ya later."
            if Options[0]  == KittyX:
                    ch_k "Hey, [KittyX.Petname]."
                    if "showered" in KittyX.RecentActions:
                            ch_k "I just got finished."
                    if not ApprovalCheck(Options[0], 900):
                            ch_k "Oh, um, I should get out of your way. . ."
            if Options[0]  == EmmaX:
                    ch_e "Oh, hello, [EmmaX.Petname]." 
                    if "showered" in EmmaX.RecentActions:
                            ch_e "I was about finished here." 
                    if not ApprovalCheck(Options[0], 900):
                            ch_e "I should get going."
            if Options[0]  == LauraX:
                    ch_l "Oh, hey." 
                    if "showered" in LauraX.RecentActions:
                            ch_l "I'm done here."   
                    if not ApprovalCheck(Options[0], 900):
                            ch_l "See you later."                          
            if len(Options) >= 2:                               
                    if Options[1] == RogueX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    #if both decide to leave
                                    ch_r "Yeah, I'll see you too."            
                            elif not ApprovalCheck(Options[1], 900):
                                    #if only person 2 decides to leave
                                    ch_r "Yeah, I should get going though." 
                            else:
                                    #if both stay
                                    ch_r "Yeah, hey."
                    if Options[1] == KittyX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_k "Yeah, see ya."            
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_k "Oh, well. . . I should get going." 
                            else:
                                    ch_k "Yeah, hi."
                    if Options[1] == EmmaX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_e "Yes, I should alo get going."            
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_e "You two look like you have some business. . ." 
                            else:
                                    ch_e "Yes, hello."
                    if Options[1] == LauraX:
                            if not ApprovalCheck(Options[0], 900) and not ApprovalCheck(Options[1], 900):
                                    ch_l "Yeah, I'm heading out too."            
                            elif not ApprovalCheck(Options[1], 900):
                                    ch_l "I'll get out of your way." 
                            else:
                                    ch_l "Hey."  
                                    
                    if not ApprovalCheck(Options[1], 900):                        
                            call Remove_Girl(Options[1])
            if not ApprovalCheck(Options[0], 900):                        
                            call Remove_Girl(Options[0])
            # End welcomes
            if Options:
                    if RogueX in Party:
                            ch_r "Hey, [Options[0].Name]."
                    if KittyX in Party:
                            ch_k "Hi, [Options[0].Name]."
                    if EmmaX in Party:
                            ch_e "Oh, hello, [Options[0].Name]."
                    if LauraX in Party:
                            ch_l "Hey."                    
    $ Line = 0             
    # End Reply portion    
    $ Options = []
            
    
# Shower Room Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Shower_Room:
    $ bg_current = "bg showerroom" 
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level 
    call Set_The_Scene(Dress=0)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:
                if Current_Time == "Night":   
                    "You're getting tired, you head back to your room."
                    jump Player_Room
                call Wait   
                call EventCalls
                call Girls_Location 
    call GirlsAngry      
    #End Room Set-up
    
# Shower Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    menu:
        "You're in the showers. What would you like to do?"

        "Chat":
                call Chat
            
        "Shower" if Round > 30:             
                call Showering
        "Shower [[no time](locked)" if Round <= 30:            
                pass
            
        "Lock the door" if "locked" not in Player.Traits:
                    "You lock the door"
                    $ Player.Traits.append("locked")                    
                    $ Nearby = []             
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level      
                    
        "Wait." if Current_Time != "Night":
                "You hang out for a bit."
                "In the showers."
                "Not gonna lie, kinda weird."
                call Wait   
                call EventCalls            
                call Girls_Location 
                
                #this bit sets up drop-in characters
                if renpy.random.randint(1, 20) < 5:
                        $ Nearby = []
                        $ Line = ActiveGirls[:]   #make sure this is initialized
                        while Line:
                                #loops through and adds populates Occupants with locals   
                                if Line[0].Loc != bg_current and "showered" not in Line[0].DailyActions and (Line[0].Loc == Line[0].Home or Line[0].Loc == "bg dangerroom"):  
                                        #Checks if girl is in the shower
                                        $ Nearby.append(Line[0])   
                                $ Line.remove(Line[0])   
                        $ Line = 0
                        if Nearby:        
                                $ renpy.random.shuffle(Nearby)
                                while len(Nearby) > 2:        
                                            # culls out list to 2 if there is a party
                                            $ Nearby.remove(Nearby[0])
                                if len(Nearby) > 1:
                                        $ Nearby[1].Loc = "nearby" 
                                $ Nearby[0].Loc = "nearby" 
        "Wait.  [[no time](locked)" if Current_Time == "Night":
                pass
                
        "Go to the Danger Room" if TravelMode: 
                call No_Towels
                jump Danger_Room_Entry 
        "Return to Your Room" if TravelMode:  
                call No_Towels
                jump Player_Room_Entry   
        "Girl's Rooms" if TravelMode:
            menu:                            
                "[RogueX.Name]'s Room":
                            call No_Towels
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History: 
                            call No_Towels  
                            call Girls_Room_Entry(KittyX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call No_Towels
                            call Girls_Room_Entry(EmmaX) 
                "[LauraX.Name]'s Room" if "met" in LauraX.History: 
                            call No_Towels
                            call Girls_Room_Entry(LauraX)   
                            
                "Back":
                            pass                              
        "Leave" if not TravelMode:
                call QuickEvents  
                call No_Towels        
                call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                call QuickEvents   
                call No_Towels       
                jump Campus_Entry
                    
    jump Shower_Room

# Shower Room Menu End <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label No_Towels:
    #Removes their towels if player is leaving the showers
    $ BO = TotalGirls[:]   
    while BO:
            #loops through and adds populates Occupants with locals   
            if BO[0].Over == "towel":
                    $ BO[0].Outfit = BO[0].OutfitDay
                    $ BO[0].Loc = BO[0].Schedule[Weekday][Time_Count] 
                    $ BO[0].OutfitChange()
                    $ BO[0].Water = 0
                    $ BO[0].AddWord(1,"showered","showered")                    
            $ BO.remove(BO[0])    
    return
    
label Showering(Occupants = [], StayCount=[] , Showered = 0, Line = 0, BO=[]):
    # Occupants tallies how many girls are here. 
    # StayCount tallies how many girls are willing to stick around.                    
    $ BO = TotalGirls[:]   
    while BO:
            #loops through and adds populates Occupants with locals 
            if BO[0] not in ActiveGirls:
                    $ BO[0].Loc = "hold"
            if BO[0].Loc == "bg showerroom" and BO[0] not in Occupants:
                    $ Occupants.append(BO[0])
            $ BO.remove(BO[0])     
    if Occupants:
            ch_p "I'm taking a shower, care to join me?" 
            if Occupants[0] == RogueX and "showered" in RogueX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_r "We actually just finished up, so we'll head out."
                    else:
                        ch_r "I actually just finished up, so I'll head out."
                    $ Showered = 1
            elif Occupants[0] == KittyX and "showered" in KittyX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there
                        ch_k "We actually just showered, so we're heading out."
                    else:
                        ch_k "I actually just showered, so I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == EmmaX and "showered" in EmmaX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there                        
                        ch_e "We were actually finishing up, so we're heading out."
                    else:
                        ch_e "I was actually finishing up, so I'm heading out."
                    $ Showered = 1
            elif Occupants[0] == LauraX and "showered" in LauraX.RecentActions:
                    if len(Occupants) > 1:
                        #if there are multiple girls in there                        
                        ch_l "We were done, actually."
                    else:
                        ch_l "I'm heading out now."
                    $ Showered = 1
            else:
                #None of them have showered yet
                if Occupants[0] == RogueX:
                        if ApprovalCheck(RogueX, 1200) or (ApprovalCheck(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):
                                    # Rogue says yes
                                    ch_r "I suppose I could stick around. . ."
                                    $ StayCount.append(RogueX) 
                        else:
                                    # Rogue says no
                                    ch_r "Nah, I should probably get going."                            
                elif Occupants[0] == KittyX:
                        if ApprovalCheck(KittyX, 1400) or (ApprovalCheck(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                                    ch_k "Yeah, I could stick around."
                                    $ StayCount.append(KittyX)
                        else:
                                    ch_k "I've got to get going."                                
                elif Occupants[0] == EmmaX:
                        if not "classcaught" in EmmaX.History or "three" not in EmmaX.History:
                                ch_e "I really should be going. . ."
                        elif ApprovalCheck(EmmaX, 1400) or (ApprovalCheck(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                                    ch_e "I suppose I could stay, for a bit."
                                    $ StayCount.append(EmmaX)
                        else:
                                    ch_e "I'm afraid I really must be going."                                    
                elif Occupants[0] == LauraX:
                        if ApprovalCheck(LauraX, 1400) or (ApprovalCheck(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                                    ch_l "I got nothing better to do."
                                    $ StayCount.append(LauraX)
                        else:
                                    ch_l "I gotta get going."
                #end first girls
                          
                if len(Occupants) >= 2:
                    #seond girls
                    if Occupants[1] == RogueX:
                        if ApprovalCheck(RogueX, 1200) or (ApprovalCheck(RogueX, 600) and RogueX.SeenChest and RogueX.SeenPussy):
                                if StayCount:                          
                                    #If Rogue said yes
                                    ch_r "I could stick around too. . ."
                                else:                     
                                    #If Rogue said no
                                    ch_r "Well, I could probably stay."
                                $ StayCount.append(RogueX)
                        else:
                                if StayCount:#RogueCount > 1:                          
                                    #If Rogue said yes
                                    ch_r "I can't though . ."
                                else:                     
                                    #If Rogue said no
                                    ch_r "I should get going too."
                            
                    if Occupants[1] == KittyX:
                        if ApprovalCheck(KittyX, 1400) or (ApprovalCheck(KittyX, 700) and KittyX.SeenChest and KittyX.SeenPussy):
                                if StayCount:                          
                                    #If Kitty said yes
                                    ch_k "I guess I could stay too. . ."
                                else:                     
                                    #If Kitty said no
                                    ch_k "Well, I could stay though."
                                $ StayCount.append(KittyX)
                        else:
                                if StayCount:#RogueCount > 1:                          
                                    #If Kitty said yes
                                    ch_k "I've really got to go though. . ."
                                else:                     
                                    #If Kitty said no
                                    ch_k "Yeah, I should head out too."
                                
                    elif Occupants[1] == EmmaX:
                        if not "classcaught" in EmmaX.History or "three" not in EmmaX.History:
                                ch_e "I really should be going. . ."
                        elif ApprovalCheck(EmmaX, 1400) or (ApprovalCheck(EmmaX, 700) and EmmaX.SeenChest and EmmaX.SeenPussy):
                                if StayCount:                          
                                    #If Emma said yes
                                    ch_e "I suppose I could also stay. . ."
                                else:                     
                                    #If Emma said no
                                    ch_e "But {i}I{/i} could stick around. . ."
                                $ StayCount.append(EmmaX)
                        else:
                                if StayCount:                       
                                    #If Emma said yes
                                    ch_e "But I really must be going. . ."
                                else:                     
                                    #If Emma said no
                                    ch_e "Yes, let's go."
                                    
                    elif Occupants[1] == LauraX:
                        if ApprovalCheck(LauraX, 1400) or (ApprovalCheck(LauraX, 700) and LauraX.SeenChest and LauraX.SeenPussy):
                                if StayCount:                          
                                    #If Laura said yes
                                    ch_l "I could stay too. . ."
                                else:                     
                                    #If Laura said no
                                    ch_l "I could stick around."
                                $ StayCount.append(LauraX)
                        else:
                                if StayCount:                        
                                    #If Laura said yes
                                    ch_l "I gotta get going though. . ."
                                else:                     
                                    #If Laura said no
                                    ch_l "Yeah, me too."
                #end none have showered yet                            
            if len(Occupants) > len(StayCount):                    
                    #if either said no. If they're at StayCount = 2 here, they have already agreed.
                    menu:
                        extend ""
                        "Ok, see you later then.":
                                if RogueX.Loc == bg_current and RogueX not in StayCount:
                                    ch_r "Yeah, later."
                                if KittyX.Loc == bg_current and KittyX not in StayCount:
                                    ch_k "Bye!"
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    ch_e "Yes, later."
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    ch_l "Yup."
                            
                        "Sure you got every spot?" if Showered:
                                $ Line = "spot"
                                                            
                        #fix Add "Take off your own clothes" option.
                        
                        "Maybe you could stay and watch?":
                                $ Line = "watch me"
                            
                        "But I didn't get to watch." if Showered:
                                $ Line = "watch you"                            
                    if Line:                        
                        $ BO = Occupants[:]   
                        while BO:
                                #loops through and adds populates Occupants with locals  
                                if BO[0].Loc == bg_current and BO[0] not in StayCount:                     
                                        if BO[0] == EmmaX and (not "classcaught" in EmmaX.History or (StayCount and "three" not in EmmaX.History)):
                                            #if it's Emma, and she isn't comfortable with threesomes or public stuff, skip her
                                            pass
                                        elif ApprovalCheck(BO[0], 1200,Alt=[[KittyX],1400]) or (ApprovalCheck(BO[0], 600,Alt=[[KittyX],700]) and BO[0].SeenChest and BO[0].SeenPussy): #1400/700 for Kitty?
                                            $ StayCount.append(BO[0]) 
                                        elif Line == "spot" and ApprovalCheck(BO[0], 1000, "LI",Alt=[[KittyX],1200]):   #1200 for Kitty?
                                            $ StayCount.append(BO[0]) 
                                        elif Line == "watch you" and ApprovalCheck(BO[0], 600, "O",Alt=[[EmmaX],500]):   #500 for Emma?
                                            $ StayCount.append(BO[0]) 
                                        #else, she doesn't agree                                
                                $ BO.remove(BO[0])    
                                     
                        if Line == "spot":      
                                #"Sure you got every spot?"
                                if StayCount:
                                        #if at least one girl agreed to stay
                                        if StayCount[0] == RogueX: #RogueCount == 2:                                 
                                            #Rogue agreed
                                            ch_r "Fine, I could use another scrub."                                                
                                        elif StayCount[0] == KittyX:                               
                                            #Kitty agreed
                                            ch_k "Oh, I guess I could take another pass at it."                                            
                                        elif StayCount[0] == EmmaX:                               
                                            #Emma agreed
                                            ch_e "I suppose we could take a look. . ."                                         
                                        elif StayCount[0] == LauraX:                               
                                            #Laura agreed
                                            ch_l "Well, maybe. . ."   
                                if RogueX.Loc == bg_current and RogueX not in StayCount: #RogueCount == 1:                                  
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Well, [RogueX.Petname], I think I'm fine."
                                    else:
                                            ch_r "No, [RogueX.Petname], I think I'm covered."
                                if KittyX.Loc == bg_current and KittyX not in StayCount: # KittyCount == 1:                                  
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Oh, well I think I[KittyX.like]got it?"
                                            ch_k "See you later, [KittyX.Petname]."
                                    else:
                                            ch_k "Ha, I'm squeeky clean, [KittyX.Petname], see you later."       
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "Well it appears you'll be taken care of."
                                            ch_e "I'll be going, [EmmaX.Petname]."
                                    else:
                                            ch_e "I'm afraid not, [EmmaX.Petname], I'll be going."       
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "Looks like you got this handled."
                                            ch_l "I'm out, [LauraX.Petname]."
                                    else:
                                            ch_l "I'm out."         
                                #end "missed a spot?"    
                            
                        elif Line == "watch me":  
                                #"Maybe you could stay and watch?"
                                if StayCount:
                                        if StayCount[0] == RogueX:                                
                                            #Rogue agreed
                                            ch_r "Yeah, I guess I do enjoy the view."                                        
                                        elif StayCount[0] == KittyX:                               
                                            #Kitty agreed
                                            ch_k "I. . . guess I wouldn't mind that. . ."                                            
                                        elif StayCount[0] == EmmaX:                               
                                            #Emma agreed
                                            ch_e "Oh, a show then?"                                        
                                        elif StayCount[0] == LauraX:                               
                                            #Laura agreed
                                            ch_l "Ok, let's see what you got."
                                
                                if RogueX.Loc == bg_current and RogueX not in StayCount: #RogueCount == 1:                                  
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Oh, well, I'm gonna pass on that, [RogueX.Petname]."
                                    else:
                                            ch_r "Yeah, I'm gonna pass on that, [RogueX.Petname]."
                                if KittyX.Loc == bg_current and KittyX not in StayCount: # KittyCount == 1:                                  
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Well, [KittyX.like]I don't need to see that."   
                                            ch_k "See you later, [KittyX.Petname]."
                                    else:
                                            ch_k "[KittyX.Like]I don't need to see that."       
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "You appear to have enough of an audience."
                                            ch_e "I'll be going, [EmmaX.Petname]."
                                    else:
                                            ch_e "I think I'll be fine, [EmmaX.Petname], I'll be going."     
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "She's got you covered."
                                            ch_l "I'm out, [LauraX.Petname]."
                                    else:
                                            ch_l "I'm out."         
                                #end "Watch me"
                                            
                        elif Line == "watch you": 
                                #"But I didn't get to watch."                                    
                                if StayCount:
                                        if StayCount[0] == RogueX:                                
                                            #Rogue agreed
                                            ch_r "Well, I don't mind putting on a show."                                          
                                        elif StayCount[0] == KittyX:                               
                                            #Kitty agreed
                                            ch_k "You want to watch me. . ."
                                            ch_k "Ok."                                                              
                                        elif StayCount[0] == EmmaX:                               
                                            #Emma agreed
                                            ch_e "I suppose I can't blame you for that. . ."                                    
                                        elif StayCount[0] == LauraX:                               
                                            #Laura agreed
                                            ch_l "Huh. Suit yourself."
                                    
                                if RogueX.Loc == bg_current and RogueX not in StayCount: #RogueCount == 1:                                  
                                    #Rogue refused
                                    if StayCount:
                                            ch_r "Really? Well not me."
                                            ch_r "Have fun, [RogueX.Petname]."
                                    else:
                                            ch_r "Keep dreaming, [RogueX.Petname]."
                                if KittyX.Loc == bg_current and KittyX not in StayCount: # KittyCount == 1:                                  
                                    #Kitty refused
                                    if StayCount:
                                            ch_k "Seriously?! Well I'm not into that."   
                                            ch_k "Later, [KittyX.Petname]."
                                    else:
                                            ch_k "[KittyX.Like]no way!"     
                                if EmmaX.Loc == bg_current and EmmaX not in StayCount:
                                    #Emma refused
                                    if StayCount:
                                            ch_e "I wouldn't want to intrude."
                                            ch_e "I'll be going."
                                    else:
                                            ch_e "Hmm, I doubt you could handle it."
                                            ch_e "I'll be going."          
                                if LauraX.Loc == bg_current and LauraX not in StayCount:
                                    #Laura refused
                                    if StayCount:
                                            ch_l "She's got you covered."
                                            ch_l "I'm out, [LauraX.Petname]."
                                    else:
                                            ch_l "I'm out."            
                                #end "Watch you?"
                    
                    if len(StayCount) > 1:
                            #if there are multiple girls   
                            if StayCount[1].GirlLikeCheck(StayCount[0]) > 500:
                                    #if she likes the other girl. . .
                                    if StayCount[1] == RogueX:        
                                        ch_r "I guess I could too."                            
                                    elif StayCount[1] == EmmaX:       
                                        ch_e "I suppose I don't want to be left out of this. . ."
                            else:
                                    if StayCount[1] == RogueX:        
                                        ch_r "Well I guess if she's in, I am too!"             
                                    elif StayCount[1] == EmmaX:       
                                        ch_e "I wouldn't want to leave you alone with. . . this."
                            if StayCount[1] == KittyX:     
                                ch_k "I- yeah, me neither!"                  
                            elif StayCount[1] == LauraX:       
                                ch_l "Fine."    
                    #end "if you asked then a question"                
            $ BO = Occupants[:]   
            while BO:
                    #loops through and adds populates Occupants with locals 
                    if BO[0].Loc == bg_current:
                            if BO[0] in StayCount:  
                                    #If the girl Stays
                                    $ BO[0].OutfitChange("nude")
                                    $ BO[0].Water = 1
                                    $ BO[0].Spunk = []                    
                                    $ BO[0].RecentActions.append("showered")                      
                                    $ BO[0].DailyActions.append("showered")   
                            else:   
                                    #If the girl leaves
                                    call Remove_Girl(BO[0])  
                            while BO[0] in Nearby:
                                    $ Nearby.remove(BO[0])
                    $ BO.remove(BO[0])   
            
#/ / Pre-shower ends / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
#/ / Showering begins / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

    call Seen_First_Peen(0,0,0,1) #You get naked
    
    while len(StayCount) >= 2 and StayCount[1] in Nearby:
            # removes any staying characters from Nearby
            $ Nearby.remove(StayCount[1])
    while StayCount and StayCount[0] in Nearby:
            # removes any staying characters from Nearby
            $ Nearby.remove(StayCount[0])
                
    if Nearby and len(StayCount) < 2:
            # This value carries over from the Entry scene if there are girls who show up late
            $ renpy.random.shuffle(Nearby)
            
            while Nearby and (len(Nearby) + len(StayCount)) > 2:
                        # while Nearby is more than 2-Staying characters
                        $ Nearby.remove(Nearby[0]) #culls it to 1
                        
            if len(Nearby) >= 2:
                "As you finish getting undressed, [Nearby[0].Name] and [Nearby[1].Name] enter the room." 
                $ Nearby[1].Loc = bg_current 
            else:
                "As you finish getting undressed, [Nearby[0].Name] enters the room."   
            $ Nearby[0].Loc = bg_current 
                
            $ BO = Nearby[:]
                    
            #call Present_Check ?
            call Set_The_Scene(Dress=0)
                
            call Seen_First_Peen(0,0,1,1) #You get naked, silent reactions
            
            if RogueX in BO:# in Nearby:  
                    if RogueX.SeenPeen == 1:
                            $ RogueX.FaceChange("surprised",2,Eyes="down")    
                            ch_r "Oh!"
                            $ RogueX.FaceChange("bemused",1,Eyes="side")  
                            ch_r "I am so sorry, I should {i}not{/i} have just barged in like that."
                    else:                    
                            $ RogueX.FaceChange("bemused",1,Eyes="side")  
                            ch_r "I simply {i}must{/i} be more careful. . ."
            if KittyX in BO:  
                    $ KittyX.FaceChange("bemused",2,Eyes="side")
                    if KittyX.SeenPeen == 1:
                            ch_k "Sorry! Sorry! I need to stop just casually phasing into places!"
                    else:                    
                            ch_k "I have {i}got{/i} to knock more. . ."
            if EmmaX in BO:                      
                    if EmmaX.SeenPeen == 1:
                            $ EmmaX.FaceChange("surprised")
                            ch_e "Oh! Dreadfully sorry." 
                            $ EmmaX.FaceChange("sexy",Eyes="down")
                            ch_e "I hope we can meet again under. . . different circumstances."
                    else:              
                            $ EmmaX.FaceChange("sexy",Eyes="down")      
                            ch_e "I really should pay closer attention. . ."
                    if "classcaught" not in EmmaX.History or ((StayCount or len(Nearby) >= 2) and "three" not in EmmaX.History):
                            #if Emma just showed up, but there are other girls around and she's not ok with that
                            "[EmmaX.Name] decides to leave immediately."  
                            call Remove_Girl(EmmaX)
                            $ EmmaX.OutfitChange()
            if LauraX in BO:  
                    if LauraX.SeenPeen == 1:
                            $ LauraX.FaceChange("surprised",Eyes="down")    
                            ch_l "Hey. That's interesting. . ."
                    else:         
                            $ LauraX.FaceChange("normal",Eyes="down")             
                            ch_l ". . ."
                            $ LauraX.FaceChange("normal")    
                            ch_l "I'm supposed to knock, aren't I."
                
            if EmmaX in StayCount and "three" not in EmmaX.History:
                    #if Emma was already here, but there are other girls around and she's not ok with that
                    if len(BO) >= 2:
                            "Seeing the other girls arrive, [EmmaX.Name] quickly excuses herself."      
                    else:
                            "Seeing [BO[0].Name] arrive, [EmmaX.Name] quickly excuses herself."              
                    $ StayCount.remove(EmmaX)  
                    call Remove_Girl(EmmaX)
                    $ EmmaX.OutfitChange() 
                    
            if BO:
                #if there are still girls around to join in. . .
                if ApprovalCheck(BO[0], 1200):
                        $ StayCount.append(BO[0])                     
                if len(BO) >=2 and ApprovalCheck(BO[1], 1200) and len(StayCount) < 2:
                        $ StayCount.append(BO[1]) 
                    
                if len(BO) >=2:
                        if BO[0] not in StayCount and BO[1] not in StayCount:
                                "They both turn right back around."    
                                call Remove_Girl(BO[0])      
                                call Remove_Girl(BO[1])                                      
                                $ BO = []              
                        elif BO[0] not in StayCount:
                                "[BO[0].Name] turns right back around, but [BO[1].Name] stays."  
                                call Remove_Girl(BO[0])                                   
                                $ BO.remove(BO[0])  
                        elif BO[1] not in StayCount:
                                "[BO[1].Name] turns right back around, but [BO[0].Name] stays."    
                                call Remove_Girl(BO[1])                                 
                                $ BO.remove(BO[1])                      
                elif BO[0] not in StayCount:
                                "She turns right back around."  
                                call Remove_Girl(BO[0])                                    
                                $ BO.remove(BO[0])  
                 
                while BO:
                        #loops deals with "Nearby"s joining the party, removes others
                        #If Rogue Stays
                        $ BO[0].OutfitChange("nude")
                        $ BO[0].Water = 1
                        $ BO[0].Spunk = []              
                        $ BO[0].RecentActions.append("showered")                      
                        $ BO[0].DailyActions.append("showered") 
                        if BO[0] == RogueX:
                                    ch_r "I wouldn't mind stickin around though." 
                        elif BO[0] == KittyX: 
                                    ch_k "I {i}could{/i} get in on this."
                        elif BO[0] == EmmaX: 
                                    ch_e "But, I could use some face time." 
                        elif BO[0] == LauraX:
                                    ch_l "Scoot over."                 
                        $ BO.remove(BO[0])   
                    
    #End "girl crashes in"
                                
    $ Round -= 30
    $ Trigger = 0
    
    if StayCount:
                #If at least one stays
                if len(StayCount) > 1 and StayCount[0] == StayCount[1]:
                        $ StayCount.remove(StayCount[0])
                if len(StayCount) > 1:
                        #If both stay
                        call Shift_Focus(StayCount[0], StayCount[1]) 
                        "You take a quick shower with [StayCount[0].Name] and [StayCount[1].Name]."
                else:
                        call Shift_Focus(StayCount[0]) 
                        "You take a quick shower with [StayCount[0].Name]."
                        
                call Shower_Sex
                
                if StayCount[0] == RogueX:                                
                        #Rogue agreed
                        ch_r "That was real nice, [RogueX.Petname]."                                            
                elif StayCount[0] == KittyX:                               
                        #Kitty agreed
                        ch_k "That was. . . nice."                                                       
                elif StayCount[0] == EmmaX:                               
                        #Emma agreed
                        ch_e "That was. . . distracting."                                
                elif StayCount[0] == LauraX:                               
                        #Laura agreed
                        ch_l "Well that was fun."

                if len(StayCount) > 1:
                        #if there are multiple girls      
                        if StayCount[1] == RogueX:                               
                                #Rogue too
                                ch_r "Yeah."                                      
                        elif StayCount[1] == KittyX:                               
                                #Kitty too
                                ch_k "Yeah, I had fun."                            
                        elif StayCount[1] == EmmaX:                               
                                #Emma too
                                ch_e "Indeed."
                        elif StayCount[1] == LauraX:                               
                                #Laura too
                                ch_l "Yup."   
                                                                                       
    else:        
                #solo shower
                $ Line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.", 
                        ". A few people came and went as you did so.", 
                        ". That was refreshing."])  
                "[Line]"    
    #insert random events here
    $ Player.RecentActions.append("showered")
    $ Player.DailyActions.append("showered")
    if "scent" in Player.DailyActions:
            $ Player.DailyActions.remove("scent") 
                   
    call Get_Dressed
    if RogueX.Loc == bg_current:  
            $ RogueX.OutfitChange("towel")
    if KittyX.Loc == bg_current:
            $ KittyX.OutfitChange("towel")
    if EmmaX.Loc == bg_current:
            $ EmmaX.OutfitChange("towel")
    if LauraX.Loc == bg_current:
            $ LauraX.OutfitChange("towel")
    $ Options = []
#    if Round < 5:
#        if Current_Time != "Night":
#                call Wait
#                call Girls_Location
#                call Set_The_Scene
#        else:
#                $ renpy.pop_call()
#                "After the shower, it's getting late, you head back to your room."
#                jump Player_Room
    return
# End Showering / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Shower Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Shower_Sex(Options=0,Line=0):
        #called from showering if sex is on the table. 
        if len(StayCount) > 1 and (ApprovalCheck(StayCount[1], 1800,Check=1) > ApprovalCheck(StayCount[0], 1800,Check=1)):
                $ renpy.random.shuffle(StayCount) #swaps girls if second girl likes you more
        call Shift_Focus(StayCount[0])
                
        $ D20 = renpy.random.randint(1,20)  
        $ D20 += 5 if ApprovalCheck(StayCount[0], 1800) else 0 #bonus if girl really likes you
        
        if "showered" in Player.RecentActions:
                $ D20 = 0
                
        $ StayCount[0].FaceChange("sly")  
        #A set
        if len(StayCount) > 1 and D20 >= 10:
                "As you do so, both girls press their bodies body up against yours."
                $ Line = StayCount[0].Name
                call Close_Launch(StayCount[0],StayCount[1])
        elif D20 >= 5:
                "As you do so, [StayCount[0].Name] presses her body up against you."
                $ Line = "She"
                call Close_Launch(StayCount[0])
        else:
                $ Line = renpy.random.choice(["It was fairly uneventful.", 
                    "A few people came and went as you did so.", 
                    "That was refreshing."]) 
                "[Line]"
                if len(StayCount) > 1: 
                        $ StayCount[0].Statup("Lust", 50, 15)
                        $ StayCount[1].Statup("Lust", 50, 15)
                        $ StayCount[0].Statup("Lust", 90, 10)
                        $ StayCount[1].Statup("Lust", 90, 10)
                        "You got a good look at them washing off, and they didn't seem to mind the view either."
                        $ StayCount[0].GLG(StayCount[1],600,4,1)
                        $ StayCount[1].GLG(StayCount[0],600,4,1)
                        $ StayCount[0].GLG(StayCount[1],800,2,1)
                        $ StayCount[1].GLG(StayCount[0],800,2,1) 
                else: 
                        $ StayCount[0].Statup("Lust", 50, 15)
                        $ StayCount[0].Statup("Lust", 90, 10)
                        "You got a good look at her washing off, and she didn't seem to mind the view either."
                return
            
        if Line:
            if len(StayCount) > 1: 
                    $ StayCount[0].Statup("Lust", 50, 5)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ StayCount[1].Statup("Lust", 50, 5)
                    $ StayCount[1].Statup("Lust", 70, 3)
            else:
                    $ StayCount[0].Statup("Lust", 50, 6)
                    $ StayCount[0].Statup("Lust", 70, 3)
            $ Player.Statup("Focus", 50, 5)
            $ Player.Statup("Focus", 80, 2)
            menu:
                extend ""
                "Continue?":
                        pass
                "Stop her." if len(StayCount) < 2: #if one
                        $Line = 0
                        call QuickReset(StayCount[0])  
                        "You take a step back, pulling away from her."
                        $ StayCount[0].Statup("Love", 80, -1)
                        $ StayCount[0].Statup("Obed", 80, 5)
                        $ StayCount[0].Statup("Inbt", 80, -1)
                        $ StayCount[0].FaceChange("sad")  
                        "She seems a bit disappointed."
                "Stop them." if len(StayCount) > 1: #if both
                        $Line = 0 
                        call QuickReset(StayCount[1])  
                        call QuickReset(StayCount[0])  
                        "You take a step back, pulling away from them."
                        $ StayCount[0].Statup("Love", 80, -1)
                        $ StayCount[0].Statup("Obed", 80, 5)
                        $ StayCount[0].Statup("Inbt", 80, -1)
                        $ StayCount[1].Statup("Obed", 80, 5)
                        $ StayCount[1].Statup("Inbt", 80, -1)
                        $ StayCount[0].FaceChange("sad")  
                        $ StayCount[1].FaceChange("sad") 
                        "They seem a bit disappointed."
        if Line:            
            #B set     
            $ Options = [1]
            if len(StayCount) > 1: 
                    if ApprovalCheck(StayCount[0], 1300) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 800:
                        $ Options.append(2)     #"She reaches over to [StayCount[1]] and begins soaping up her pussy."
                    if ApprovalCheck(StayCount[0], 1200) and StayCount[0].GirlLikeCheck(StayCount[1]) >= 700:
                        $ Options.append(3)     #"She reaches over to [StayCount[1]] and begins soaping up her chest."
                
            if ApprovalCheck(StayCount[0], 1300): 
                $ Options.append(4)     #"She reaches down and takes your cock in her hand, soaping it up."
            if ApprovalCheck(StayCount[0], 1400): 
                $ Options.append(5)     #"She kneels down and wraps her breasts around your cock, soaping it up."
            
            if ApprovalCheck(StayCount[0], 1300): 
                $ Options.append(6)     #"She reaches down and begins fondling her own pussy, building a nice lather." 
            if ApprovalCheck(StayCount[0], 1200): 
                $ Options.append(7)     #"She begins rubbing her own breasts in circles, building a nice lather." 
                
            if not ApprovalCheck(StayCount[0], 1400):
                #only adds these if there's not much in there. 
                if ApprovalCheck(StayCount[0], 1000): 
                    $ Options.append(8)         #"She draws her breasts up and down your arm, the soap bubbles squirting out."
                if ApprovalCheck(StayCount[0], 1100): 
                    $ Options.append(9)         #"She kneels down and rubs her breasts against your leg, soaping it up."
                if ApprovalCheck(StayCount[0], 1000): 
                    $ Options.append(10)        #"She presses against your back, her soapy breasts rubbing back and forth against it."
                if ApprovalCheck(StayCount[0], 1100): 
                    $ Options.append(11)        #"She presses against your chest, her soapy breasts rubbing back and forth against it."
            
            $ renpy.random.shuffle(Options) 
            
            #"Line" will be either the first girl's name, or "She" 
            #lesbian
            if Options[0] == 2:
                    $ StayCount[0].Statup("Lust", 50, 5)
                    $ StayCount[0].Statup("Lust", 70, 2)
                    $ StayCount[1].Statup("Lust", 50, 7)
                    $ StayCount[1].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] reaches over to [StayCount[1].Name] and begins soaping up her chest."
            elif Options[0] == 3:
                    $ StayCount[0].Statup("Lust", 50, 7)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ StayCount[1].Statup("Lust", 50, 8)
                    $ StayCount[1].Statup("Lust", 70, 4)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 5)
                    "[Line] reaches over to [StayCount[1].Name] and begins soaping up her pussy."
            
            #fondling you
            elif Options[0] == 4:
                    if len(StayCount) > 1: 
                            $ StayCount[0].Statup("Lust", 50, 10)
                            $ StayCount[0].Statup("Lust", 70, 7)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 8)
                            $ StayCount[0].Statup("Lust", 70, 5)
                    $ Player.Statup("Focus", 50, 10)
                    $ Player.Statup("Focus", 80, 6)
                    "[Line] reaches down and takes your cock in her hand, soaping it up."
            elif Options[0] == 5:
                    if len(StayCount) > 1: 
                            $ StayCount[0].Statup("Lust", 50, 12)
                            $ StayCount[0].Statup("Lust", 70, 8)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 9)
                            $ StayCount[0].Statup("Lust", 70, 6)
                    $ Player.Statup("Focus", 50, 10)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] kneels down and wraps her breasts around your cock, soaping it up."
                    
            #msturbation
            elif Options[0] == 6:
                    if len(StayCount) > 1: 
                            $ StayCount[0].Statup("Lust", 50, 11)
                            $ StayCount[0].Statup("Lust", 70, 6)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 9)
                            $ StayCount[0].Statup("Lust", 70, 5)
                    $ Player.Statup("Focus", 50, 9)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] reaches down and begins fondling her own pussy, building a nice lather." 
            elif Options[0] == 7:
                    if len(StayCount) > 1: 
                            $ StayCount[0].Statup("Lust", 50, 10)
                            $ StayCount[0].Statup("Lust", 70, 5)
                    else:
                            $ StayCount[0].Statup("Lust", 50, 9)
                            $ StayCount[0].Statup("Lust", 70, 4)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] begins rubbing her own breasts in circles, building a nice lather." 
            
            #gentle tease
            elif Options[0] == 8:
                    $ StayCount[0].Statup("Lust", 50, 6)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 7)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] draws her breasts up and down your arm, the soap bubbles squirting out."
            elif Options[0] == 9:
                    $ StayCount[0].Statup("Lust", 50, 8)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] kneels down and rubs her breasts against your leg, soaping it up."
            elif Options[0] == 10:
                    $ StayCount[0].Statup("Lust", 50, 7)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 6)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] presses against your back, her soapy breasts rubbing back and forth against it."
            elif Options[0] == 11:
                    $ StayCount[0].Statup("Lust", 50, 7)
                    $ StayCount[0].Statup("Lust", 70, 3)
                    $ Player.Statup("Focus", 50, 8)
                    $ Player.Statup("Focus", 80, 4)
                    "[Line] presses against your chest, her soapy breasts rubbing back and forth against it."
            elif Options[0] == 1:
                    $ StayCount[0].Statup("Lust", 50, 5)
                    $ StayCount[0].Statup("Lust", 70, 2)
                    $ Player.Statup("Focus", 50, 6)
                    $ Player.Statup("Focus", 80, 3)
                    "[Line] stares silently at you as she moves her hands along her soapy body. . ."
                    $ Line = 0
             
        if Line and len(StayCount) > 1:
            #C Set, check what the other girl thinks. . .
            $ D20 += 5 if ApprovalCheck(StayCount[1], 1800) else 0
            if StayCount[1].GirlLikeCheck(StayCount[0]) <= 800 and 2 <= Options[0] <=3: 
                $ D20 -= 5
            if StayCount[1].GirlLikeCheck(StayCount[0]) <= 600: 
                $ D20 -= 5
                
            if 2 <= Options[0] <= 3:
                # if it's lesbian stuff. . .
                if ApprovalCheck(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 800:
                        $ StayCount[1].FaceChange("sexy",1)  
                        $ StayCount[0].Statup("Lust", 50, 5)
                        $ StayCount[0].Statup("Lust", 70, 5)
                        $ StayCount[1].Statup("Lust", 50, 12)
                        $ StayCount[1].Statup("Lust", 70, 12)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name] seems really into this, and returns the favor."  
                        $ Player.Statup("Focus", 50, 7)
                        $ Player.Statup("Focus", 80, 3) 
                        $ Line = 4
                elif ApprovalCheck(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700: 
                        $ StayCount[1].FaceChange("sexy",2,Eyes="closed")  
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 10)
                        $ Player.Statup("Focus", 50, 5)
                        $ Player.Statup("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name] seems really into this, and leans into it."
                else:                         
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].FaceChange("sadside",Brows="confused")  
                        "[StayCount[1].Name] doesn't really seem to appreciate this."
                        "She pulls away."
                        $ Line = 3
            else:
                # if it's not lesbian stuff. . .
                if (ApprovalCheck(StayCount[1], 1300) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 700) or ApprovalCheck(StayCount[1], 2000):
                    if Options[0] == 5: #titjob
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 5)
                        $ Player.Statup("Focus", 50, 6)
                        $ Player.Statup("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name] seems really into this, slowly rubbing against you as she watches."  
                    else:
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 5)
                        $ Player.Statup("Focus", 50, 5)
                        $ Player.Statup("Focus", 80, 3)
                        call Close_Launch(StayCount[0],StayCount[1])
                        "[StayCount[1].Name] seems really into this, and joins her on the other side."  
                    $ Line = 4
                elif ((ApprovalCheck(StayCount[1], 1200) and StayCount[1].GirlLikeCheck(StayCount[0]) >= 600)) or ApprovalCheck(StayCount[1], 1600): 
                        $ StayCount[1].FaceChange("sexy",2,Eyes="down")  
                        $ StayCount[1].Statup("Lust", 50, 10)
                        $ StayCount[1].Statup("Lust", 70, 5)
                        "[StayCount[1].Name] seems really into this, and watches her do it."
                else:                       
                        $ StayCount[1].FaceChange("sadside",Brows="confused")  
                        $ StayCount[1].Statup("Lust", 50, 5)
                        "[StayCount[1].Name] doesn't really seem to appreciate this."
                        $ Line = 3
        if Line:
            menu:
                extend ""
                "Continue?":
                    pass
                "Stop her." if len(StayCount) < 2: #if one
                    $Line = 0
                    call QuickReset(StayCount[0])     
                    "You take a step back, pulling away from her."
                    $ StayCount[0].Statup("Love", 80, -2)
                    $ StayCount[0].Statup("Obed", 80, 5)
                    $ StayCount[0].Statup("Inbt", 80, -2)
                    $ StayCount[0].FaceChange("sad")  
                    "She seems a bit disappointed."
                "Stop them." if len(StayCount) > 1: #if both
                    $Line = 0
                    call QuickReset(StayCount[1])  
                    call QuickReset(StayCount[0])  
                    "You take a step back, pulling away from them."
                    $ StayCount[0].FaceChange("sad")  
                    $ StayCount[0].Statup("Love", 80, -2)
                    $ StayCount[0].Statup("Obed", 80, 5)
                    $ StayCount[0].Statup("Inbt", 80, -2)
                    if Line == 3:
                        $ StayCount[1].Statup("Love", 80, 4)
                        $ StayCount[1].Statup("Obed", 80, 5)
                        $ StayCount[1].FaceChange("bemused")  
                        "[StayCount[0].Name] seems a bit disappointed, but [StayCount[1].Name] seems pleased."
                    else:
                        $ StayCount[1].Statup("Love", 80, -1)
                        $ StayCount[1].Statup("Obed", 80, 5)
                        $ StayCount[1].Statup("Inbt", 80, -1)
                        $ StayCount[1].FaceChange("sad")  
                        "They seem a bit disappointed."
                     
        if Line: 
            #D set, wrap-up  
            if len(StayCount) > 1 and Line != 3: #if second didn't disapprove
                    $ StayCount[0].GLG(StayCount[1],600,4,1)
                    $ StayCount[1].GLG(StayCount[0],600,4,1)
                    $ StayCount[0].GLG(StayCount[1],800,3,1)
                    $ StayCount[1].GLG(StayCount[0],800,3,1)
                    $ StayCount[0].GLG(StayCount[1],900,1,1)
                    $ StayCount[1].GLG(StayCount[0],900,1,1)                  
            if 2 <= Options[0] <= 3 and D20 >= 15:
                    #if it's lesbian. . .       
                    $ StayCount[1].GLG(StayCount[0],900,4,1)    
                    $ Player.Statup("Focus", 50, 10)
                    $ Player.Statup("Focus", 80, 5)                 
                    "After a few minutes of this, it looks like [StayCount[1].Name] gets off."
                    call Girl_Cumming(StayCount[1],1)
                    if Line == 4:                                
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            "It looks like [StayCount[0].Name] is reacting positively to it as well. . ."
                            call Girl_Cumming(StayCount[0],1)
                    if len(StayCount) > 1:
                            "The girls take a step back."
                            call QuickReset(StayCount[1]) 
                    else:
                            "[StayCount[0].Name] takes a step back."
                    call QuickReset(StayCount[0])   
                                                        
            elif 4 <= Options[0] <= 5 and D20 >= 10:
                    #if it's her fondling you
                    $ Player.Focus = 15
                    if Options[0] == 5: #if it was titjob
                            $ StayCount[0].Spunk.append("tits")
                        
                    if Line == 4:
                            $ StayCount[0].Statup("Inbt", 90, 7) 
                            $ StayCount[1].Statup("Inbt", 90, 4) 
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            $ StayCount[1].GLG(StayCount[0],900,3,1)                                
                            "After a few minutes of this, the two of them manage to get you off."                                 
                    else:
                            $ StayCount[0].Statup("Inbt", 90, 5) 
                            "After a few minutes of this, she manages to get you off." 
                    "A little more work is needed to clean up the mess." 
                    if Options[0] == 5: #if it was titjob
                            $ StayCount[0].Spunk = []
                    if len(StayCount) > 1:
                            "The girls take a step back."
                            call QuickReset(StayCount[1]) 
                    else:
                            "[StayCount[0].Name] takes a step back."
                    call QuickReset(StayCount[0])   
                    
            elif 6 <= Options[0] <= 7 and D20 >= 15:
                    #if it's her masturbation. . .         
                    $ StayCount[0].Statup("Inbt", 90, 7)   
                    $ Player.Statup("Focus", 50, 15)
                    $ Player.Statup("Focus", 80, 5)             
                    "After a few minutes of this, it looks like [StayCount[0].Name] gets off."
                    call Girl_Cumming(StayCount[0],1)
                    if Line == 4:
                            $ StayCount[1].Statup("Inbt", 90, 6) 
                            $ StayCount[0].GLG(StayCount[1],900,3,1)
                            "It looks like [StayCount[1].Name] is enjoying herself as well. . ."
                            call Girl_Cumming(StayCount[1],1)
                    if len(StayCount) > 1:
                            $ StayCount[1].GLG(StayCount[0],900,3,1)
                            "The girls take a step back."
                            call QuickReset(StayCount[1]) 
                    else:
                            "[StayCount[0].Name] takes a step back."
                    call QuickReset(StayCount[0])   
            else:
                #nobody got off
                if len(StayCount) > 1:
                        call QuickReset(StayCount[1])    
                call QuickReset(StayCount[0])      
                $ Player.Statup("Focus", 50, 15)
                $ Player.Statup("Focus", 80, 5)
                if D20 >= 15:
                    "After a minute or two, it sounds like someone is coming, so you scramble apart."   
                    "Disappointing. . ."
                elif D20 >= 10:
                    "After a minute or two, she seems satisfied with her efforts, and pulls back."
                    if 4 <= Options[0] <= 5:
                            "You're left pretty hard."
                else:
                    "After a minute or so of this, she draws back and finshes washing herself off."
                    if 4 <= Options[0] <= 5:
                            "You're left pretty hard." 
        call Shift_Focus(StayCount[0])  
        return
# End Shower Sex / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# end Shower Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Study Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Study_Room_Entry:  
    $ Player.DrainWord("locked",0,0,1)
    $ Nearby = []     
    $ bg_current = "bg study"     
    call Gym_Clothes
    call Taboo_Level
    call Set_The_Scene(Entry = 1)  
    menu:
            "You're at the door, what do you do?"
            "Knock politely":
                    $ Line = "knock"
                    
            "Enter without knocking":
                 if Current_Time == "Night":
                         "The door is locked. It's not like you could just walk through it."
                         jump Study_Room_Entry
                                                 
            "Use the key to enter" if Current_Time == "Night" and "Xavier" in Keys:
                    "You use your key."
                    $ Line = 0
            
            "Ask Kitty" if Current_Time == "Night" and KittyX in Party:
                    $ Line = "kitty"
                    
            "Leave":
                    "You head back."
                    jump Campus_Map 
     
    if Line == "knock": 
        if Current_Time == "Night":
            "There's no answer, he's probably asleep." 
            jump Study_Room_Entry
        else:           
            ch_x "Yes, enter. . ."
            "You enter the room."
    elif Line == "kitty":
            ch_k "Yeah?"
            while True:
                menu:
                    extend ""
                    "Could you phase through the door and open it for me?":
                            if "Sneakthief" in KittyX.Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in KittyX.RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck(KittyX, 400, "I") or ApprovalCheck(KittyX, 1400):
                                $ KittyX.Statup("Love", 90, 3) 
                                $ KittyX.Statup("Obed", 50, 10) 
                                $ KittyX.Statup("Inbt", 60, 10)  
                                ch_k "Heh, you have a wicked mind. . ."
                                $ KittyX.Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ KittyX.Statup("Love", 90, -3) 
                                $ KittyX.Statup("Obed", 50, 2) 
                                $ KittyX.Statup("Inbt", 60, 2)  
                                ch_k "Um, I don't really feel comfortable doing that. . ."
                                $ KittyX.RecentActions.append("no thief")
                    "Open the door.":
                            if "Sneakthief" in KittyX.Traits:
                                ch_k "No problem. . ."
                                jump Study_Room
                            elif "no thief" in KittyX.RecentActions:
                                ch_k "I told you, no."
                            elif ApprovalCheck(KittyX, 500, "O") or ApprovalCheck(KittyX, 1600):
                                $ KittyX.Statup("Obed", 50, 15) 
                                $ KittyX.Statup("Inbt", 60, 10)  
                                ch_k "Heh, if you say so. . ."
                                $ KittyX.Traits.append("Sneakthief")
                                jump Study_Room
                            else:
                                $ KittyX.Statup("Love", 90, -5) 
                                $ KittyX.Statup("Obed", 50, 2) 
                                $ KittyX.Statup("Inbt", 60, 2)  
                                ch_k "Um, no."
                                $ KittyX.RecentActions.append("no thief")
                    "Never mind. [[Leave]":
                            "You head back."
                            jump Campus_Map 
            jump Study_Room_Entry
    elif Current_Time != "Night":                
            ch_x "You know, [Player.Name], it is not polite to enter a room unannounced."
    $ Cnt = 0                        
                
label Study_Room:
    $ bg_current = "bg study"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10:         
            if Current_Time == "Night":                         
                "It's late, you head back to your room."
                jump Player_Room
            else:
                call Wait                 
                call Girls_Location
    
    call GirlsAngry
    
# Study Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if Current_Time == "Night":
        $ Line = "You are in Xavier's Study, but he isn't in at the moment. What would you like to do?"
    else:
        $ Line = "You are in Xavier's Study. What would you like to do?"
    menu:
        "[Line]"        
        "Chat" if Current_Time == "Night": #fix, open up once sex while in office is fine
                    call Chat
        
        "Plan Omega!" if Current_Time != "Night" and RogueX.Loc == bg_current:
                    if ApprovalCheck(RogueX, 1500, TabM=1, Loc="No") and Player.Lvl >= 5:
                        call Xavier_Plan(RogueX) #Plan_Omega
                    else:
                        ch_r "What?"
        "Plan Kappa!" if Current_Time != "Night" and KittyX.Loc == bg_current:
                    if "Xavier's photo" in Player.Inventory and Player.Lvl >= 5 and ApprovalCheck(KittyX, 1500, TabM=1, Loc="No"):                   
                        call Xavier_Plan(KittyX) #Plan_Kappa
                    else:
                        ch_k "What?"     
        "Plan Psi!" if Current_Time != "Night" and EmmaX.Loc == bg_current:
                    if ApprovalCheck(EmmaX, 1500, TabM=1, Loc="No") and Player.Lvl >= 5:
                        call Xavier_Plan(EmmaX) #Plan_Psi
                    else:
                        ch_e "What?"  
        "Plan Chi!" if Current_Time != "Night" and LauraX.Loc == bg_current:
                    if LauraX.Lvl >= 2 and ApprovalCheck(LauraX, 1500, TabM=1, Loc="No") and ApprovalCheck(LauraX, 750, "I"):   
                        call Xavier_Plan(LauraX) #Plan_Chi
                    else:
                        ch_l "Huh?"                  
        "Explore" if Current_Time == "Night" and "explore" not in Player.RecentActions: 
                    $ Cnt = 0    
                    $ Player.RecentActions.append("explore")
                    jump Study_Room_Explore
            
        "Wait":
                    if Current_Time == "Night":
                            "You probably don't want to be here when Xavier gets in."
                    elif Current_Time == "Evening":
                            ch_x "If you don't mind, I would like to close up for the evening?"
                            "You return to your room."
                            jump Player_Room                    
                    else:           
                            call Wait  
                            call Girls_Location
                            ch_x "Not that I mind the company, but is there something I can do for you?"
                              
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry  
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
                    
    jump Study_Room
    
    
label Study_Room_Explore:
    $ Line = 0
    $ D20 = renpy.random.randint(1, 20)    
    menu:
        "Where would you like to look?"
        "Bookshelf":
            if D20 >= 5 + Cnt:
                    $ Line = "book"
            else:
                    "As you search the bookshelf, you accidentally knock one of the books off."
                    "It hammers against the floor, and a little light blinks on the desk."
        "Left Desk Drawer":
            if KittyX.Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 10 + Cnt:
                    $ Line = "left"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Middle Desk Drawer":
            if KittyX.Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 15 + Cnt:
                    $ Line = "mid"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Right Desk Drawer":
            if KittyX.Loc != bg_current:
                    "You can't seem to get it open, it would be nice to have someone open the catch from the inside."
            elif D20 >= 5 + Cnt:
                    $ Line = "right"
            else:
                    "As you open the drawer, it makes a loud a squeak."
                    "As you look around, you notice a little light starts blinking on the desk."
        "Never mind [[back]": 
                    jump Study_Room
    
    $ D20 = renpy.random.randint(1, 20)
    if not Line:
                "Probably best to get out of here."
                "You slip out and head back to your room."
                jump Player_Room_Entry 
    elif Line == "book":
            if D20 >= 15 and "Well Studied" not in Achievements:            
                "As you check the books on the shelf, you notice that one of them is actually a disguised lockbox."
                if KittyX.Loc == bg_current:
                    menu:
                        "Since [KittyX.Name] is around, have her check inside?"
                        "Check in the box":
                            if ApprovalCheck(KittyX, 700, "I") or ApprovalCheck(KittyX, 1800):
                                if "Well Studied" not in Achievements:
                                        $ KittyX.Statup("Obed", 50, 10) 
                                        $ KittyX.Statup("Inbt", 60, 15)  
                                        ch_k "Sounds like a plan."
                                        "[KittyX.Name] swipes her hand through the box, and pulls out a stack of bills."
                                        "Looks like Xavier was hiding a rainy day fund in here."
                                        $ Player.Cash += 500
                                        "[[$500 acquired.]"
                                        $ Achievements.append("Well Studied")
                                else:
                                        "Looks like this has been thoroughly looted."
                            else:#Kitty doesn't approve 
                                $ KittyX.Statup("Love", 90, -3) 
                                $ KittyX.Statup("Obed", 50, 1) 
                                $ KittyX.Statup("Inbt", 60, 2)  
                                ch_k "I really don't think we should do that."                            
                        "Put it back.":
                            "You place the box back on the shelf."
                else:#[KittyX.Name]'s not there
                            "You can't think of any way to get it open, too bad you aren't a ghost or something."
                            "You place the box back on the shelf."
            elif D20 >= 15:
                "There doesn't seem to be anything more of interest in here."
            else:
                "You search through the books for a few minutes, but don't find anything."
                "It would probably take a more thorough search."            
    elif Line == "left":            
            if "Xavier's photo" not in Player.Inventory: 
                if D20 >= 10:
                        "Buried under a pile of documents, you find a printed out photo."
                        "It appears to be a selfie of Mystique making out with Xavier."
                        "She's reaching down to adjust his . . . oh, {i}that's{/i} interesting."
                        "[[Xavier's photo acquired.]"
                        $ Player.Inventory.append("Xavier's photo")
                        if "kappa" in Player.History: 
                                $ Player.History.remove("kappa")
                else:                 
                        "You search through some documents, but don't find anything."
                        "It would probably take a more thorough search."   
            else:      
                        "There doesn't seem to be anything more of interest in here."
    elif Line == "mid":
            if "All" not in Keys:
                "Under a few trinkets, you find a small keyring."
                "[[Keyring acquired.]"
                if "Xavier" not in Keys:
                        $ Keys.append("Xavier") 
                if RogueX not in Keys:
                        $ Keys.append(RogueX)
                if KittyX not in Keys:
                        $ Keys.append(KittyX)
                if EmmaX not in Keys:
                        $ Keys.append(EmmaX)
                if LauraX not in Keys:
                        $ Keys.append(LauraX)
                if "All" not in Keys:
                        $ Keys.append("All")
            else:
                "There doesn't seem to be anything interesting in here."
    elif Line == "right":
            "There doesn't seem to be anything more of interest in here, maybe later?"
    $ Cnt += 3
    jump Study_Room_Explore
# end Study's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



label Rogue_Room_Entry: 
        $ bg_current = RogueX.Home  
        call Girls_Room_Entry(RogueX) 
        $ bg_current = "bg campus"   
        jump Misplaced
label Kitty_Room_Entry:   
        $ bg_current = KittyX.Home  
        call Girls_Room_Entry(KittyX)
        $ bg_current = "bg campus"   
        jump Misplaced
label Emma_Room_Entry:  
        $ bg_current = EmmaX.Home  
        call Girls_Room_Entry(EmmaX) 
        $ bg_current = "bg campus"   
        jump Misplaced
label Laura_Room_Entry:
        $ bg_current = LauraX.Home  
        call Girls_Room_Entry(LauraX) 
        $ bg_current = "bg campus"   
        jump Misplaced
                            
label Girls_Room_Entry(Chr=0):
        #Set Chr somehow. . .
        if Chr not in TotalGirls:
                return
        $ Player.DrainWord("locked",0,0,1)
        call Shift_Focus(Chr)
        $ bg_current = Chr.Home      
        $ Nearby = []     
        call Gym_Clothes
        call Set_The_Scene(Entry = 1)    
        call Taboo_Level
        $ Player.RecentActions.append("traveling")
        $ D20 = renpy.random.randint(1, 20)
        
        if Chr in Party:
                        if Current_Time == "Night" or (Current_Time == "Evening" and Round <= 10):                         
                            if ApprovalCheck(Chr, 1000, "LI") or ApprovalCheck(Chr, 600, "OI"):     
                                    #It's late but she really likes you
                                    if Chr == RogueX:
                                            ch_r "It's pretty late, [Chr.Petname], but you can come in for a little bit."  
                                    elif Chr == KittyX:
                                            ch_k "It's kinda late, [Chr.Petname], but you can have a minute."    
                                    elif Chr == EmmaX:
                                            ch_e "It's rather late, [Chr.Petname], but I can spare you some time." 
                                    elif Chr == LauraX:
                                            ch_l "It's getting late, but come on in."  
                            elif Chr.Addict >= 50:
                                    if Chr == RogueX:
                                            ch_r "Um, yeah, you'd better come in. . ."    
                                    elif Chr == KittyX:
                                            ch_k "I'd really like to see you. . ."    
                                    elif Chr == EmmaX:
                                            ch_e "Yes. . . I suppose you should. . ."
                                    elif Chr == LauraX:
                                            ch_l "Um, yeah, you'd better come in. . ."  
                            elif ApprovalCheck(Chr, 500, "LI") or ApprovalCheck(Chr, 300, "OI"):      
                                    #she likes you well enough but it's late
                                    if Chr == RogueX:
                                            ch_r "It's a little late [Chr.Petname]. See you tomorrow."
                                    elif Chr == KittyX:
                                            ch_k "It's a little late [Chr.Petname]. Tomorrow?"
                                    elif Chr == EmmaX:
                                            ch_e "It's late [Chr.Petname]. I'll see you tomorrow."
                                    elif Chr == LauraX:
                                            ch_l "See you tomorrow."
                                    $ Chr.RecentActions.append("noentry")                      
                                    $ Chr.DailyActions.append("noentry")  
                                    if Chr in Party:
                                            $ Party.remove(Chr)   
                                    "She heads inside and closes the door behind her."
                                    return
                        else: 
                                    #If Girl is in the party and it's not late in the day 
                                    if Chr == RogueX:  
                                            ch_r "Come on in, [Chr.Petname]."
                                    elif Chr == KittyX:      
                                            ch_k "Come on in!"
                                    elif Chr == EmmaX:    
                                            ch_e "Don't just stand at the door."
                                    elif Chr == LauraX:
                                            ch_l "Come on in."
                        call EventCalls
                        jump expression Chr.Tag + "_Room"   
        #End if Girl in Party
        
         
        if Round >= 10 and Chr.Loc == bg_current and "les" in Chr.RecentActions:
                call Girls_Caught_Lesing(Chr)
                if not _return:
                        jump expression Chr.Tag + "_Room"   
                    
        if bg_current == KittyX.Home and "dress2" in LauraX.History and not Party:
                        #if you helped buy clothes for Laura earlier. . .
                        call Laura_Dressup3
                        $ bg_current = "bg campus"   
                        jump Misplaced
                
        if Round >= 10 and Chr.Loc == bg_current and "gonnafap" in Chr.DailyActions and D20 >= 5: 
                        #girl caught fapping  
                        call Girl_Caught_Mastubating(Chr) 
        else: 
                #not auto-caught fapping
                if Chr in Keys:
                    menu:
                        "You have a key, what do you do?"
                        "Knock politely":
                                $ Line = "knock"
                                
                        "Use the key to enter.":
                                call Set_The_Scene
                            
                if Line != "knock" and Chr in Keys: 
                        if Chr.Loc == bg_current:
                            #if she's home. . .
                            if Round <= 10:        #add "no" condtion here
                                    if  "noentry" in Chr.RecentActions or "angry" in Chr.RecentActions:
                                            $ Chr.FaceChange("angry")
                                            if Chr == RogueX:
                                                    ch_r "Buzz off already."  
                                            elif Chr == KittyX:
                                                    ch_k "GTFO."    
                                            elif Chr == EmmaX:
                                                    ch_e "Out!"    
                                            elif Chr == LauraX:
                                                    ch_l "Get out of my face." 
                                            "[Chr.Name] shoves you back into the hall."
                                            return
                                    if Current_Time == "Night" :    
                                            "She's asleep in bed. You slip out quietly." #fix add options here.                            
                                            return  
                            elif "gonnafap" in Chr.DailyActions and D20 >= 5: 
                                    #girl caught fapping  
                                    call Girl_Caught_Mastubating(Chr) 
                            elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                    #girl caught changing
                                    call Girl_Caught_Changing(Chr)
                                    jump expression Chr.Tag + "_Room"   
                #End "if you enter without knocking"
                    
                else:
                            #You knocked
                            $ Round -= 10 
                            "You knock on [Chr.Name]'s door."        
                            if Chr.Loc != bg_current:
                                        "Looks like she's not home right now."
                                        $ bg_current = "bg campus"   
                                        jump Misplaced
                                
                            if Round <= 10:
                                    if Current_Time == "Night" :
                                        "There's no answer, she's probably asleep." 
                                        $ bg_current = "bg campus"   
                                        jump Misplaced
                        
                            if (D20 >=19 and Chr.Lust >= 50) or (D20 >=15 and Chr.Lust >= 70) or (D20 >=10 and Chr.Lust >= 80):    
                                    #Girl caught fapping
                                    "You hear some soft moans, followed by some shuffling around as items tumble to the ground."
                                    "After several seconds and some more shuffling of clothing, [Chr.Name] comes to the door."
                                    $ Chr.FaceChange("perplexed",2)
                                    call Set_The_Scene  
                                    if Chr == RogueX:
                                            ch_r "Sorry about that [Chr.Petname], I was. . . working out."
                                    elif Chr == KittyX:
                                            ch_k "Oh, hey, [Chr.Petname], I was. . . never mind."
                                    elif Chr == EmmaX:
                                            ch_e "Well, I suppose you could tell I was a bit. . . occupied."
                                    elif Chr == LauraX:
                                            ch_l "Um, hey [Chr.Petname], just working off some stress."
                                    $ Chr.FaceChange("perplexed",1)
                                    $ Tempmod += 10
                            elif D20 >=15 and (Current_Time == "Night" or Current_Time == "Morning"):                          
                                    #Girl caught changing
                                    "You hear the rustling of fabric and some knocking around, but after a few seconds [Chr.Name] comes to the door."
                                    call Set_The_Scene
                                    if Chr == RogueX:
                                            ch_r "Sorry about that [Chr.Petname], I was just getting changed."    
                                    elif Chr == KittyX:
                                            ch_k "Oh, hi [Chr.Petname], I was[KittyX.like]just getting changed."   
                                    elif Chr == EmmaX:
                                            ch_e "Oh, do come in [Chr.Petname], don't mind that I was just getting changed."   
                                    elif Chr == LauraX:
                                            ch_l "Hey [Chr.Petname], I was just getting dressed."  
                            elif "angry" in Chr.RecentActions:
                                    $ Chr.FaceChange("angry")
                                    if Chr == RogueX:
                                            ch_r "I don't want to deal with you right now."
                                    elif Chr == KittyX:
                                            ch_k "Nooope."
                                    elif Chr == EmmaX:
                                            ch_e "I haven't any time for this."
                                    elif Chr == LauraX:
                                            ch_l "Nope."  
                                    $ Trigger = 0
                                    "[Chr.Name] knocks you back into the hall and slams the door."
                                    $ bg_current = "bg campus"   
                                    jump Misplaced
                            else:
                                    call Set_The_Scene
                                    "[Chr.Name] opens the door and leans out."
                                    "You ask if you can come inside."
                #End "if you knocked"
                        
                #if you reach this point then you've asked to enter.               
                if Chr.Loc != bg_current:
                        "Looks like she's not home right now."                
                        if Chr in Keys:
                                menu:
                                    "Go in and wait for her?"
                                    "Yes":
                                            $ Line = 0
                                            jump expression Chr.Tag + "_Room"   
                                    "No":
                                            pass
                        "You head back."
                        $ bg_current = "bg campus"   
                        jump Misplaced 
                elif Current_Time == "Night" and "noentry" in Chr.RecentActions:                
                        if Chr == RogueX:
                                ch_r "Hey, I told you you're not welcome. I'll see you tomorrow."
                        elif Chr == KittyX:
                                ch_k "Scram. I'll see you tomorrow."  
                        elif Chr == EmmaX:
                                ch_e "Later, [Chr.Petname]."  
                        elif Chr == LauraX:
                                ch_l "Not tonight, [Chr.Petname]."
                        $ bg_current = "bg campus"   
                        jump Misplaced 
                elif "noentry" in Chr.RecentActions or "angry" in Chr.RecentActions:
                        $ Chr.FaceChange("angry")
                        if Chr == RogueX:
                                ch_r "Buzz off already."  
                        elif Chr == KittyX:
                                ch_k "GTFO."
                        elif Chr == EmmaX:
                                ch_e "Out."
                        elif Chr == LauraX:
                                ch_l "Fuck off."  
                        $ bg_current = "bg campus"   
                        jump Misplaced 
                elif Current_Time == "Night" and (Chr.Sleep or Chr.SEXP >= 30):                                                   
                        #It's late but she really likes you                    
                        if Chr == RogueX:
                                ch_r "It's pretty late, [Chr.Petname], but it's always nice to see you."    
                        elif Chr == KittyX:
                                ch_k "It's late, [Chr.Petname], but you're so cute."  
                        elif Chr == EmmaX:
                                ch_e "It is getting late, [Chr.Petname]."
                                ch_e "but you are so adorable."           
                        elif Chr == LauraX:
                                ch_l "It's late, but I was hoping you'd stop by."  
                elif Current_Time == "Night" and (ApprovalCheck(Chr, 1000, "LI") or ApprovalCheck(Chr, 600, "OI")):     
                        #It's late but she really likes you
                        if Chr == RogueX:
                                ch_r "It's pretty late, [Chr.Petname], but you can come in for a little bit." 
                        elif Chr == KittyX:
                                ch_k "It's late, [Chr.Petname], but I could hang out a bit."   
                        elif Chr == EmmaX:
                                ch_e "It is getting late, [Chr.Petname], but I could make some time."    
                        elif Chr == LauraX:
                                ch_l "It's late, [Chr.Petname], but you can come in." 
                elif Chr.Addict >= 50:
                        $ Chr.FaceChange("manic")
                        if Chr == RogueX:
                                ch_r "Um, yeah, you'd better come in. . ."
                        elif Chr == KittyX:
                                ch_k "I could use some attention. . ."
                        elif Chr == EmmaX:
                                ch_e "I. . . suppose you should. . ."    
                        elif Chr == LauraX:
                                ch_l "You should come in. . ."  
                elif Current_Time == "Night" and (ApprovalCheck(Chr, 500, "LI") or ApprovalCheck(Chr, 300, "OI")):
                        if Chr == RogueX:
                                ch_r "It's a little late [Chr.Petname]. Maybe tomorrow."
                        elif Chr == KittyX:
                                ch_k "It's late [Chr.Petname]. Tomorrow?"
                        elif Chr == EmmaX:
                                ch_e "It's late [Chr.Petname]. I'll see you tomorrow."
                        elif Chr == LauraX:
                                ch_l "It's late [Chr.Petname]. Come back tomorrow."                    
                        $ Chr.RecentActions.append("noentry")                      
                        $ Chr.DailyActions.append("noentry")   
                        $ bg_current = "bg campus"   
                        jump Misplaced 
                elif ApprovalCheck(Chr, 600, "LI") or ApprovalCheck(Chr, 300, "OI"):                                    
                        #She quite likes you and lets you in   
                        if Chr == RogueX:
                                ch_r "Sure, come on in [RogueX.Petname]."    
                        elif Chr == KittyX:
                                ch_k "Sure, come on in [KittyX.Petname]."       
                        elif Chr == EmmaX: 
                                ch_e "Come in, [EmmaX.Petname]."        
                        elif Chr == LauraX:
                                ch_l "Make yourself at home, I guess."  
                else:                                                                                                           
                        #She doesn't like you
                        if Chr == RogueX:
                                ch_r "I'd rather you didn't come in, thanks."
                        elif Chr == KittyX:
                                ch_k "Nah, you can stay out."
                        elif Chr == EmmaX:
                                ch_e "I don't think that would be appropriate."
                        elif Chr == LauraX:
                                ch_l "Nah."
                        $ Chr.RecentActions.append("noentry")                      
                        $ Chr.DailyActions.append("noentry") 
                        $ bg_current = "bg campus"   
                        jump Misplaced 
        
        # If you get this far, she's allowed you in
        call EventCalls
        if Chr.Loc == Chr.Home and "angry" in Chr.RecentActions:
                # if she's home and pissed, she kicks you out
                $ Line = 0
                $ Trigger = 0
                "[Chr.Name] shoves you back into the hall and slams the door. You head back to your room."
                $ bg_current = "bg player"   
                jump Misplaced
        jump Misplaced

# End Girls room entry / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Rogue's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
label Rogue_Room:
    $ bg_current = "bg rogue"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)    
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls    
    call GirlsAngry    
    
# [RogueX.Name]'s Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if RogueX.Loc == bg_current:
        $ Line = "You are in "+RogueX.Name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+RogueX.Name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":
                    call Study_Session
                    
        "Lock the door" if "locked" not in Player.Traits:
                if RogueX.Loc == bg_current and not ApprovalCheck(RogueX, 1000):
                    ch_r "Hey, could you maybe keep that open, [RogueX.Petname]?"
                else:
                    "You lock the door"
                    $ Player.Traits.append("locked")   
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level  
            
        "Sleep." if Current_Time == "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls    
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry   
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History:   
                            call Girls_Room_Entry(KittyX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call Girls_Room_Entry(EmmaX)  
                "[LauraX.Name]'s Room" if "met" in LauraX.History: 
                            call Girls_Room_Entry(LauraX)   
                "Back":
                            pass      
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in RogueX.RecentActions:
            $ RogueX.FaceChange("angry")
            ch_r "I really think you should leave."
            "[RogueX.Name] pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Rogue_Room
    
# end [RogueX.Name]'s Room Interface //////////////////////////////////////////////////////////////////////


# [KittyX.Name]'s Room Interface //////////////////////////////////////////////////////////////////////

            
label Kitty_Room:
    $ bg_current = "bg kitty"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Round10
                call Girls_Location
                call EventCalls 
    call GirlsAngry        
    
# [KittyX.Name]'s Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if KittyX.Loc == bg_current:
        $ Line = "You are in "+KittyX.Name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+KittyX.Name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":
                    call Study_Session
          
        "Lock the door" if "locked" not in Player.Traits:
                if KittyX.Loc == bg_current and not ApprovalCheck(KittyX, 1000):
                    ch_k "Um, I'd[KittyX.like]rather you didn't lock my door, [KittyX.Petname]?"
                else:
                    "You lock the door"
                    $ Player.Traits.append("locked")     
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level  
                    
        "Sleep." if Current_Time == "Night" and KittyX.Loc == bg_current:
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":
                            call Girls_Room_Entry(RogueX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call Girls_Room_Entry(EmmaX)  
                "[LauraX.Name]'s Room" if "met" in LauraX.History: 
                            call Girls_Room_Entry(LauraX)   
                "Back":
                            pass
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in KittyX.RecentActions:
            $ KittyX.FaceChange("angry")
            ch_k "Go. Now."
            "[KittyX.Name] pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Kitty_Room
    
# end [KittyX.Name]'s Room Interface //////////////////////////////////////////////////////////////////////


# Emma's Room Interface //////////////////////////////////////////////////////////////////////

            
label Emma_Room:
    $ bg_current = "bg emma"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)   
    call QuickEvents
    call Checkout(1)
    if Round <= 10: 
                call Round10
                call Girls_Location
                call EventCalls 
    call GirlsAngry        
    
# Emma's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if EmmaX.Loc == bg_current:
        $ Line = "You are in "+EmmaX.Name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+EmmaX.Name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":                
                    call Study_Session
            
        "Lock the door" if "locked" not in Player.Traits:
                if EmmaX.Loc == bg_current and not ApprovalCheck(EmmaX, 1000):
                    ch_e "Do you really think it's appropriate for you to lock the door to my room?"
                else:
                    "You lock the door"
                    $ Player.Traits.append("locked")     
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level  
                    
        "Sleep." if Current_Time == "Night" and EmmaX.Loc == bg_current:
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                            
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry 
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History:   
                            call Girls_Room_Entry(KittyX)  
                "[LauraX.Name]'s Room" if "met" in LauraX.History: 
                            call Girls_Room_Entry(LauraX)   
                "Back":
                            pass
        "Go to the Showers" if TravelMode:            
                            jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                            call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                            jump Campus_Entry
    
    if "angry" in EmmaX.RecentActions:
            $ EmmaX.FaceChange("angry")
            ch_e "I think you should leave now."
            "[EmmaX.Name] pushes you back into the hall and slams the door. You head back to your room."
            $ Line = 0
            $ Trigger = 0
            jump Player_Room
    jump Emma_Room
    
            
# end Emma's Room Interface //////////////////////////////////////////////////////////////////////


# Laura's Room Interface //////////////////////////////////////////////////////////////////////
            
label Laura_Room:
    $ bg_current = "bg laura"
    $ Player.DrainWord("traveling",1,0)
    call Taboo_Level
    call Set_The_Scene(Quiet=1)
    call QuickEvents
    call Checkout(1)    
    if Round <= 10:
                call Round10
                call Girls_Location
                call EventCalls    
    call GirlsAngry    
    
# Laura's Room Menu Start <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if LauraX.Loc == bg_current:
        $ Line = "You are in "+LauraX.Name+"'s room. What would you like to do?"
    else:
        $ Line = "You are in "+LauraX.Name+"'s room, but she isn't here. What would you like to do?"
    menu:
        "[Line]"
        
        "Chat":
                    call Chat
        
        "Would you like to study?":
                    call Study_Session
         
        "Lock the door" if "locked" not in Player.Traits:
                if LauraX.Loc == bg_current and not ApprovalCheck(LauraX, 1200):
                    ch_l "I don't want to feel caged up like that, [LauraX.Petname]."
                else:
                    "You lock the door"
                    $ Player.Traits.append("locked") 
                    call Taboo_Level
                   
        "Unlock the door" if "locked" in Player.Traits:
                    "You unlock the door"
                    $ Player.Traits.remove("locked")
                    call Taboo_Level  
                    
        "Sleep." if Current_Time == "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls    
                    
        "Wait." if Current_Time != "Night":
                    call Round10
                    call Girls_Location
                    call EventCalls 
                    
        "Return to Your Room" if TravelMode:            
                    jump Player_Room_Entry   
        "Other Girl's Rooms" if TravelMode:
            menu:
                "[RogueX.Name]'s Room":
                            call Girls_Room_Entry(RogueX)  
                "[KittyX.Name]'s Room" if "met" in KittyX.History:   
                            call Girls_Room_Entry(KittyX)  
                "[EmmaX.Name]'s Room" if "met" in EmmaX.History:   
                            call Girls_Room_Entry(EmmaX)  
                "Back":
                            pass      
        "Go to the Showers" if TravelMode:            
                    jump Shower_Room_Entry
                    
        "Leave" if not TravelMode:
                    call Worldmap
        "Leave [[Go to Campus Square]" if TravelMode:
                    jump Campus_Entry
    
    if "angry" in LauraX.RecentActions:
            $ LauraX.FaceChange("angry")
            $ Line = 0
            $ Trigger = 0
            ch_l "Get out before we both regret it."
            "[LauraX.Name] shoves you back into the hall and slams the door. You head back to your room."
            jump Player_Room
    jump Laura_Room
# End Laura's Room Interface / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

