﻿# This is the section for sex-related dialog options to be chosen. 
label Primary_SexDialog(GirlA=Primary,TempLine = 0, TempLust = 0, TempLust2 = 0):   #nee Rog*ue_SexDialog(TempLine = 0, TempLust = 0, TempLust2 = 0) 
    #called from Sex_Dialog as call Primary_SexDialog(Primary)
    if Situation == "skip" and Line:
            # if the action was set by a previous trigger, skip this element
            $ Situation = 0
            return
    
    if Trigger == "hand":
            $ Line = GirlA.Name + " continues stroke your cock. "
               
            if not Speed:
                        $ Line = GirlA.Name + " holds your cock in her hand. "
                        if GirlA.Hand > 2:
                                $ Line = Line + "She just seems to be enjoying the feel of it"
                                $ TempLust += 2 if GirlA.Lust < 60 else 0
                        else:
                                $ Line = Line + "She just seems to be looking it over"
                                $ TempLust += 2 if GirlA.Lust < 40 else 0
                                $ TempFocus += -3 if Player.Focus > 50 else 2
                        $ GirlA.Addict -= 1 if D20S > 10 else 2
                        return
            if GirlA in (EmmaX,LauraX):
                        #Laura and Emma have more experience to start
                        if Speed <= 1:                      
                            #slow 
                            $ Line = Line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching", 
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here", 
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])   
                            $ TempFocus += 20 if Player.Focus > 70 else 7
                        else:                              
                            #fast
                            $ Line = Line + renpy.random.choice(["Her movements have become masterful, her slightest touch starts you twitching", 
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here", 
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, you can tell she's had plenty of practice",
                                    "You can't tell where she is at any moment, all you know is that it works"]) 
                            $ TempFocus += 20 if Player.Focus < 60 else 7    
            elif GirlA.Hand > 4:                          
                        # After the 5th time 
                        if Speed <= 1:                      
                            #slow 
                            $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching", 
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"])   
                            $ TempFocus += 20 if Player.Focus > 70 else 5
                        else:                               
                            #fast
                            $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching", 
                                    "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "Her expert strokes will have you boiling over in seconds",
                                    "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                    "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                    "You can't tell where she is at any moment, all you know is that it works"]) 
                            $ TempFocus += 20 if Player.Focus < 40 else 5   
            elif 2 < GirlA.Hand <= 4:                       
                        #third through 5th time
                        if Speed <= 1:                      
                            #slow
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft", 
                                    "She's still learning, but learning fast. Her hands sure are smooth", 
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She gently caresses the shaft, and cups the balls in her other hand, giving them a warm massage"])  
                            $ TempFocus += 15 if Player.Focus > 60 else 5
                        else:                               
                            #fast
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her fingers cause tingles as they caress the shaft", 
                                    "She's still learning, but learning fast. Her hands sure are smooth", 
                                    "Her hands glide smoothly across your cock",
                                    "She has a smooth motion going now, gentle and precise",
                                    "Her lessons are paying off, she's really becoming very talented at this",
                                    "She quickly strokes your cock, with a very deft pressure"]) 
                            $ TempFocus += 15 if Player.Focus < 60 else 7   
            else:                                   
                    #First and second time
                    if Speed <= 1:                      
                        #slow
                        $ Line = Line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock", 
                                "She moves her hands up and down the shaft. She's a little rough at this, but at least she tries", 
                                "She strokes you gently. She isn't quite sure what to make of the balls",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This may take a few tries"])   
                        $ TempFocus += 12 if Player.Focus > 60 else 5         
                    else:                               
                        #fast 
                        $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips out of her hand", 
                                "She rapidly moves her hands up and down the shaft. She's a little rough at this, but at least she tries", 
                                "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                "Her fingers fumble with your shaft a bit",
                                "She squeezes one of your balls too tightly, but stops when you wince",
                                "She has a firm grip, and she's not letting go. This train is out of control"])  
                        $ TempFocus += 10 if Player.Focus > 60 else 2         
                    
            $ TempLust += 2 if GirlA.Lust < 60 else 0
            $ TempLust += 2 if GirlA.Hand > 2 else 0
            $ GirlA.Addict -= 1 if D20S > 10 else 2
            
    #End Handy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////
          
          
    elif Trigger == "titjob":     
            #This can only ever be a primary action. 
            
            if not Speed:
                        if GirlA == KittyX:
                            $ Line = GirlA.Name + " begins to rub her chest against you"
                        elif GirlA.Tit > 2:
                            $ Line = GirlA.Name + " begins to bounce her breasts up and down"
                        else:
                            $ Line = GirlA.Name + " squeezes her breasts together and slowly moves them along your shaft"
                        $ Speed = 1
                        $ TempFocus += 12 if Player.Focus < 60 else 6                      
                        $ TempLust += 6 if GirlA.Lust > 60 else 3 
                        return
            
            if GirlA == EmmaX or (GirlA.Tit > 4 and GirlA.Blow):                                        
                        #5th+ and blown
                        if Speed <= 1:                                              
                            #slow
                            $ Line = renpy.random.choice([GirlA.Name + " rocks her breasts up and down around your cock", 
                                    GirlA.Name + " lightly licks the head as it pops up between her tits", 
                                    GirlA.Name + " has a smooth motion going now, gentle and precise",
                                    GirlA.Name + " pauses to rub her nipples across the shaft",
                                    "In between strokes "+ GirlA.Name + " gently sucks on the head",
                                    GirlA.Name + " drips some spittle down to make sure you're properly lubed",
                                    GirlA.Name + " gently caresses the shaft between her tits"])            
                            
                            $ TempFocus += 15 if Player.Focus < 70 else 5                      
                            $ TempLust += 7 if GirlA.Lust > 60 else 4       
                        else:                                                      
                            #fast
                            $ Line = renpy.random.choice([GirlA.Name + " rapidly rocks her breasts up and down around your cock", 
                                    GirlA.Name + " licks away at the head every time it pops up between her tits", 
                                    GirlA.Name + " has a smooth motion going now, quick by efficient",
                                    GirlA.Name + " dances her nipples across the shaft",
                                    "In as she strokes faster and faster, " + GirlA.Name + " bends down to suck on the head",
                                    GirlA.Name + " covers her tits with drool to keep them well lubed",
                                    GirlA.Name + " rapidly caresses the shaft between her tits"])
                            
                            $ TempFocus += 20 if Player.Focus > 40 else 5                      
                            $ TempLust += 6 if GirlA.Lust > 70 else 4    
                     
                
            elif GirlA.Tit > 1:                                                 
                    #third through 5th time
                    if Speed <= 1:                                              
                        #slow
                        $ Line = renpy.random.choice([GirlA.Name + " juggles her breasts up and down around your cock", 
                                GirlA.Name + " lightly strokes the head as it pops up between her tits", 
                                GirlA.Name + " has a smooth motion going now, gentle and precise",
                                GirlA.Name + " pauses to rub her nipples across the shaft",
                                GirlA.Name + " gently caresses the shaft between her tits"]) 
                        
                        $ TempFocus += 15 if Player.Focus < 60 else 5                      
                        $ TempLust += 6 if GirlA.Lust > 60 else 3                        
                    else:                                                       
                        #fast
                        $ Line = renpy.random.choice([GirlA.Name + " rapidly juggles her breasts up and down around your cock", 
                            GirlA.Name + " lightly brushes the head with her chin as it pops up between her tits", 
                            GirlA.Name + " moves them up and down in a fluid rocking motion",
                            GirlA.Name + " bounces her whole body up and down",
                            GirlA.Name + " rapidly slides the shaft between her tits"])   
                        
                        $ TempFocus += 15 if Player.Focus > 50 else 7                      
                        $ TempLust += 6 if GirlA.Lust > 60 else 4    
                       
            else:                                                           
                    #First and second time
                    if Speed <= 1:                                              
                        #slow
                        $ Line = renpy.random.choice([GirlA.Name + " sort of squishes her breasts back and forth around your cock", 
                            GirlA.Name + " slides the cock up and down between her cleavage", 
                            GirlA.Name + " kind of bounces her tits around your cock",
                            GirlA.Name + " smooshes her cleavage as tight as she can and rubs up and down"])
                        
                        $ TempFocus += 12 if Player.Focus < 60 else 6                      
                        $ TempLust += 6 if GirlA.Lust > 60 else 3    
                                        
                    else:                                                       
                        #fast
                        $ Line = renpy.random.choice([GirlA.Name + " sort of bounces her breasts off your cock", 
                            GirlA.Name + " tries to quickly slide the cock up and down between her cleavage, but it tends to slide out", 
                            GirlA.Name + " slaps her tits against your dick",
                            GirlA.Name + " smooshes her cleavage as tight as she can and rubs up and down quite quickly"])  
                        
                        $ TempFocus += 8 if Player.Focus > 70 else 4                      
                        $ TempLust += 5 if GirlA.Lust > 60 else 3    
              
            if GirlA == KittyX:                
                    $ TempFocus -= 2      
            elif GirlA == EmmaX:                
                    $ TempFocus += 1                
                
            $ GirlA.Addict -= 2
    #End Action Titfuck ///////////////////////////////////////////////////////////////////////////////
           
           
    elif Trigger == "blow":        
            if not Speed:
                    #if Rog*ue is not moving                
                    if "hungry" in GirlA.Traits:
                            $ GirlA.FaceChange("sly")
                            $ Line = GirlA.Name + " stares at your cock. She licks her lips in anticipation"
                            $ TempLust += 3 if GirlA.Lust < 40 else 1                    
                    elif GirlA.Blow > 2:
                            $ GirlA.FaceChange("sly")
                            $ Line = GirlA.Name + " stares at your cock. She seems pretty excited about it"
                            $ TempLust += 2 if GirlA.Lust < 60 else 0                 
                    elif GirlA == EmmaX:
                            $ GirlA.FaceChange("sly")
                            $ Line = GirlA.Name + " stares at your cock. She seems pretty intrigued by it"
                            $ TempLust += 2 if GirlA.Lust < 60 else 0
                    else:
                            $ GirlA.FaceChange("perplexed")
                            $ Line = GirlA.Name + " stares at your cock with trepidation"
                            $ TempLust += 2 if GirlA.Lust < 40 else 0     
                        
                    if GirlA.Blow <= 1 or (GirlA.Obed >= 500 and GirlA.Obed > GirlA.Inbt):
                            $ TempLust += 2 if GirlA.Lust > 60 else 0                 
                            $ Line = Line + ", but she seems to be waiting for some instruction"
                    else:
                            $ Line = Line + ", and then she gets started licking your cock"
                            $ Speed = 1
                    return
                               
            elif Speed < 2: 
                        $ Line = GirlA.Name + " continues to lick your cock. "       
                        #if Rog*ue is the primary but is licking
            else: 
                        $ Line = GirlA.Name + " continues to suck your cock. "        
                        #if Rog*ue is the primary and is heading or sucking
             
            if Speed == 1:                                                                 
                    #Speed 1 (licking)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX):                                                                 
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["Her deft licks are masterful, your cock twitches with each stroke", 
                                    "She gently blows across the head as she covers your cock in smooth licks", 
                                    "How many licks to the center of your cock? No way you're finding out",
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and gentle licks",
                                    "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge dances around it"])  
                            $ TempFocus += 20 if Player.Focus < 70 else 15                   
                            $ TempLust += 2 if GirlA.Lust > 80 else 1
                        
                    elif GirlA.Blow > 1:                                                               
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, her tongue makes your hair stand on end", 
                                    "She's still learning, but learning fast. She seems eager to use her mouth for more than talk", 
                                    "She's settled into a gentle licking pace that washes over you like a warm bath",
                                    "She licks gently up and down the shaft. She's a little rough at this, but at least she tries", 
                                    "Her tongue moves carefully along the shaft",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She licks her way down the shaft, and gently teases the balls"]) 
                            $ TempFocus += 20 if Player.Focus > 60 else 10                      
                            $ TempLust += 2 if GirlA.Lust > 80 else 1    
                        
                    else:                                                                           
                            #First and second time
                            $ Line = Line + renpy.random.choice([GirlA.Name + " makes up for her inexperience with determination, carefully licking your cock", 
                                    "She takes a small lick and grimaces at the taste",
                                    "She tentatively kisses around the head a bit",            
                                    "She nibbles one of your balls, but stops when you wince",
                                    "She licks all over your dick, but she doesn't really have a handle on it"])  
                            $ TempFocus += 15 if Player.Focus > 60 else 5                  
                    $ GirlA.Addict -= 2
                
            elif Speed == 2:                                                                    
                    #Speed 2 (heading)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX):                                                                  
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke", 
                                    "She rapidly bobs up and down on your cock, a frenzy of motion", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the tip into her mouth and her tounge swirls rapidly around it"]) 
                            $ TempFocus += 20 if Player.Focus < 80 else 10                      
                            $ TempLust += 2 if GirlA.Lust > 70 else 1    
                        
                    elif GirlA.Blow > 1:                                                                
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the head", 
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip", 
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way around the head",
                                    "Her mouth envelopes the head, then she quickly draws it in and draws back with a pop"]) 
                            $ TempFocus += 15 if Player.Focus > 80 else 10                      
                            $ TempLust += 1 if GirlA.Lust > 60 else 0    
                        
                    else:                                                                           
                            # First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often pops out of her mouth", 
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries",             
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"]) 
                            $ TempFocus += 9 if Player.Focus > 80 else 3    
                    $ GirlA.Addict -= 2           
                
            elif Speed == 3:                                                                    
                    #Speed 3 (sucking)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX):                                                                  
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke", 
                                    "She smoothly bobs up and down on your cock, a frenzy of motion", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the shaft into her mouth and her tounge swirls rapidly around it"]) 
                            $ TempFocus += 22 if Player.Focus > 40 else 10                      
                            $ TempLust += 3 if GirlA.Lust > 60 else 1    
                        
                    elif GirlA.Blow > 1:                                                               
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft", 
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip", 
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She rapidly licks her way up and down the shaft as her mouth envelopes you",
                                    "Her mouth envelopes the shaft, then she quickly draws it in and draws back with a pop"])
                            $ TempFocus += 15 if Player.Focus > 50 else 5  
                        
                    else:                                                                          
                            #First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for putting it all the way in, and grimaces at the taste", 
                                    "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries", 
                                    "She sucks up and down your cock very quickly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"]) 
                            $ TempFocus += 6 if Player.Focus < 50 else 3 
                    $ GirlA.Addict -= 2 if D20S > 10 else 3
                        
                 
            else:#Speed = 4                                                                    
                    #Speed 4+ (Deep Throat)
                    if GirlA.Blow > 4 or GirlA in (EmmaX,LauraX):                                                                 
                            #After the 5th time
                            $ Line = Line + renpy.random.choice(["She masterfully bobs on your cock, and it twitches with each stroke", 
                                    "She rapidly bobs to the base of your cock, a frenzy of motion", 
                                    "She's becoming something of an expert, making up for years of lost time",
                                    "She gobbles you up all the way to the base, then quickly draws out and plunges back in",
                                    "She's really getting good at this, alternating between deep suction and quick licks across the head",
                                    "She moves very smoothly, bobbing in and out like she's been doing this for years",
                                    "She puts the entire shaft into her mouth and her tounge swirls rapidly around it"])  
                            $ TempFocus += 25 if Player.Focus > 40 else 8                      
                            $ TempLust += 3 if GirlA.Lust > 60 else 2    
                        
                    elif GirlA.Blow > 1:                                                              
                            #After the 2nd time
                            $ Line = Line + renpy.random.choice(["She's begining to figure things out, she bobs carefully up and down the shaft", 
                                    "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip", 
                                    "Her lips envelope you like a warm bath as she bobs in and out",
                                    "She slowly draws you in to the base of your cock, then pulls back at the last second",
                                    "She's really starting to learn some clever tricks to making you feel good",
                                    "She completely envelops the shaft with her throat.",
                                    "Her mouth envelopes the head, then she quickly draws it all the way in and draws back with a pop"])  
                            $ TempFocus += 20 if Player.Focus > 40 else 5                      
                            $ TempLust += -3 if GirlA.Lust < 60 else -1                        
                            $ TempLust += 5 if GirlA.Obed > 500 else 0  
                        
                    else:                                                                            
                            #First and second time
                            $ Line = Line + renpy.random.choice(["She really wasn't prepared for going so deep, and gags a bit", 
                                    "She puts the whole shaft in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries", 
                                    "She draws your cock into her mouth very qucikly, but gets a bit dizzy and has to slow down",
                                    "Her head bobs rapidly, until she goes a bit too deep and starts to gag",
                                    "She lets her teeth get a bit too much action",
                                    "She bobs quickly on your cock, but clamps down a bit too tight for comfort"]) 
                            $ TempFocus += 15 if Player.Focus > 80 else 5                      
                            $ TempLust += -5 if GirlA.Lust < 60 else -2                       
                            $ TempLust += 7 if GirlA.Obed > 500 else 0  
                    $ GirlA.Addict -= 3
           
    # end GirlA.Blowjob                                 //////////////////////////////////////////////////////////////////////////////
        
    elif Trigger == "sex": 
            #Trigger4 not available
        
            if not Speed:
                    #if Rog*ue is not moving   
                    $ Line = "She seems to be waiting for you to do something. . "
                    return
                        
            elif Speed < 2: 
                    $ Line = "You continue to pound "+ GirlA.Name + ". "        
                    #if Rog*ue is the primary but is licking
            else: 
                    $ Line = "You continue to slowly drive into " + GirlA.Name + ". "       
                    #if Rog*ue is the primary and is heading or sucking
            
            if GirlA.Sex > 4 or GirlA in (EmmaX,LauraX):
                if Speed > 1:                       
                        # After the 5th time fast
                        $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                            "You thrust into her and she squeaks a bit",
                            "You quickly grind back and forth inside her",
                            "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                            "You pound away at her",    
                            "She grinds furiously back and forth along your cock"])
                        $ TempFocus += 18 if Player.Focus > 50 else 12                   
                        $ TempLust += 16 if GirlA.Lust > 70 else 10                    
                else:                      
                        # After the 5th time slow
                        $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                            "You thrust into her and she coos a bit",
                            "You slowly grind back and forth inside her",
                            "You alternate between long and slow thrusts, and the occasional quick one",
                            "You slowly slide back and forth near the entrance",    
                            "She slides slowly back and forth along your cock, teasing you"])
                        $ TempFocus += 14 if Player.Focus < 60 else 12                   
                        $ TempLust += 12 if 40 > GirlA.Lust > 90 else 10                        
                        
            elif GirlA.Sex > 1:
                if Speed > 1:            
                    #third through 5th time fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust into her and she squeaks a bit",
                        "You quickly grind back and forth inside her",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You pound away at her",    
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += 12 if Player.Focus > 50 else 9                   
                    $ TempLust += 14 if GirlA.Lust > 80 else 10
                else:          
                    #third through 5th time slow
                    $ Line = Line + renpy.random.choice(["she bumps slowly against your cock", 
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",    
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 12 if Player.Focus < 70 else 7                   
                    $ TempLust += 10 if 50 > GirlA.Lust > 90 else 8
                    
            else:
                if Speed > 1:           
                    # First and second time fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust into her and she squeeks in pain",
                        "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                        "You pound away at her",    
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                    $ TempFocus += 10 if Player.Focus > 60 else 9                   
                    $ TempLust += 10 if GirlA.Lust > 80 else 6
                else:           
                    # First and second time slow
                    $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                        "You thrust into her and she squeaks a bit",
                        "You slowly grind back and forth inside her",
                        "You alternate between long and slow thrusts, and the occasional quick one",
                        "You slowly slide back and forth near the entrance",    
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += 10 if Player.Focus < 70 else 9                   
                    $ TempLust += 8 if 60 > GirlA.Lust > 90 else 6
                    
            $ GirlA.Addict -= 2
            
    # end GirlA.Sex                                 ////////////////////////////////////////////////////////////////////////////// 
            
    elif Trigger == "hotdog": 
            #Trigger4 not available
            #TempLust2 in this action is how much lower body clothing she has on, it gets cleared at the end.
            $ TempLust2 = 2
            if GirlA.Panties and not GirlA.PantiesDown: 
                    #if panties are in the way
                    $ TempLust2 -= 1
            if GirlA.HoseNum() >= 6:
                    #if complete hose
                    $ TempLust2 -= 1        
            if GirlA.Legs and not GirlA.Upskirt: 
                    #If pants/skirt is up
                    $ TempLust2 -= 2 if TempLust2 <= 2 else TempLust2
                
            if not Speed:
                $ Line = "She seems to be waiting for you to do something. . "
                return
            elif Speed < 2: 
                    $ Line = "You continue to hotdog " + GirlA.Name + ". "       
            else: 
                    $ Line = "You continue to grind against " + GirlA.Name + "." 
                    
            if GirlA.Hotdog >= 2:
                if Speed > 1:      
                    # After the 2ndtime fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust against her and she squeaks a bit",
                        "You quickly grind back and forth along her crack",
                        "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                        "You grind away at her",    
                        "She grinds furiously back and forth along your cock"])
                    $ TempFocus += (TempLust2 + 8) if Player.Focus < 60 else (TempLust2 + 4)
                    $ TempLust += (TempLust2 + 8) if 50 > GirlA.Lust > 80 else (TempLust2 + 2)
                    
                elif Speed:        
                    #2nd time slow
                    $ Line = Line + renpy.random.choice(["She grinds slowly against your cock", 
                        "You thrust against her and she coos a bit",
                        "You slowly rub the tip across her pussy",
                        "You alternate between long and slow thrusts, and the occasional rapid ones",
                        "You slowly slide back and forth near her rim",    
                        "She slides slowly back and forth along your cock, teasing you"])                    
                    $ TempFocus += (TempLust2 + 8) if Player.Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 7) if 30 > GirlA.Lust > 70 else (TempLust2 + 3)
                    
            else: 
                #If you haven't done hotdog before       
                if Speed > 1:     
                    #fast
                    $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                        "You thrust into her and she squeeks in surprise",
                        "You quickly grind back and forth against her but she doesn't seem to have the rhythm down",
                        "She bounces rapidly against your cock, occasionally sliding out and having to stick it back in",
                        "You pound away at her",    
                        "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])                    
                    $ TempFocus += (TempLust2 + 5) if Player.Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 4) if 50 > GirlA.Lust > 80 else (TempLust2 + 2)
                    
                elif Speed:        
                    #slow
                    $ Line = Line + renpy.random.choice(["She grinds slowly against your cock", 
                        "You thrust into her crack and she squeaks a bit",
                        "You slowly grind back and forth across her rear",            
                        "You slowly slide back and forth near her rim",    
                        "She slides slowly back and forth along your cock"])
                    $ TempFocus += (TempLust2 + 5) if Player.Focus < 60 else (TempLust2 + 3)
                    $ TempLust += (TempLust2 + 5) if 50 > GirlA.Lust > 70 else (TempLust2 + 2)
            
            if TempLust2:
                $ GirlA.Addict -= 1  
                $ TempLust2 = 0
        
    # end GirlA.Hotdog                                 //////////////////////////////////////////////////////////////////////////////
            
         
    elif Trigger == "anal": 
            #Trigger4 not available
        
            if not Speed:
                $ Line = "She seems to be waiting for you to do something. . "
                return
                
            elif Speed < 2: 
                    $ Line = "You continue to pound into " + GirlA.Name + "'s ass. "       
            else: 
                    $ Line = "You continue to push into " + GirlA.Name + "'s ass. " 
                    
                 
            if GirlA.Anal >= 5:
                    if Speed > 1:
                            #Fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",    
                                "She grinds furiously back and forth along your cock"])
                            $ TempFocus += 18 if Player.Focus > 60 else 12                   
                            $ TempLust += 14 if GirlA.Lust > 80 else 9
                        
                    else:       
                            #Slow
                            $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                                "You thrust into her and she coos a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",    
                                "She slides slowly back and forth along your cock, teasing you"])
                            $ TempFocus += 12 if Player.Focus > 60 else 9                   
                            $ TempLust += 12 if 50 < GirlA.Lust < 90 else 8
                              
            elif GirlA.Loose:           
                    #You've done some anal stuff before       
                    if Speed > 1:            
                            #third through 5th time fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You quickly grind back and forth inside her",
                                "You alternate between shallow rapid thrusts, and the occasional deep, slow one",
                                "You pound away at her",    
                                "She grinds furiously back and forth along your cock"])                            
                            $ TempFocus += 12 if Player.Focus > 60 else 8                   
                            $ TempLust += 12 if GirlA.Lust > 80 else 6
                        
                    elif Speed:           
                            #third through 5th time
                            $ Line = Line + renpy.random.choice(["She bumps slowly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You alternate between long and slow thrusts, and the occasional quick one",
                                "You slowly slide back and forth near the rim",    
                                "She slides slowly back and forth along your cock"])
                            $ TempFocus += 13 if Player.Focus > 60 else 8                   
                            $ TempLust += 8 if 70 > GirlA.Lust > 90 else 4
            
            else:
                    #If you haven't done anal things before       
                    if Speed > 1:          
                            #fast
                            $ Line = Line + renpy.random.choice(["She bounces rapidly against your cock but seems to be in pain", 
                                "You thrust into her and she squeeks in pain",
                                "You quickly grind back and forth inside her but she doesn't seem to have the rhythm down",
                                "She bounces rapidly against your cock, occasionally popping out and having to stick it back in",
                                "You pound away at her",    
                                "She moves rapidly back and forth along your cock, but seems a bit uncomfortable"])
                            $ TempFocus += 10 if Player.Focus > 60 else 8                   
                            $ TempLust += 2 if GirlA.Lust > 80 else -3
                        
                    elif Speed:           
                            #heading
                            $ Line = Line + renpy.random.choice(["She grits her teeth and slides slowly against your cock", 
                                "You thrust into her and she squeaks a bit",
                                "You slowly grind back and forth inside her",
                                "You slowly slide back and forth near the rim",    
                                "She slides slowly back and forth along your cock"])  
                            $ TempFocus += 10 if Player.Focus > 60 else 6                   
                            $ TempLust += 4 if GirlA.Lust > 60 else -1
            
            if GirlA.Loose > 1:                                                        
                #If she's extra loose
                $ TempLust += 1
                
            $ TempLust = 0 if (GirlA.Lust - TempLust) < 0 else TempLust
            
    # end GirlA.Anal                                 //////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "fondle breasts":   
                    $ Line = "You continue to fondle " + GirlA.Name + ". "    
                    if not GirlA.Uptop and GirlA.Over and GirlA.Chest: 
                                #Full top
                                $ Line = Line + renpy.random.choice(["You reach under her layers of clothing and massage her breasts", 
                                    "You pass your hands gently over her warm breasts", 
                                    "Her firm nipples catch on the fabric of her top as you grasp her warm flesh",
                                    "She gasps as you grasp her under her top"])
                                $ TempFocus += 2 if Player.Focus < 40 else 1  
                                $ TempLust += 4 if GirlA.Lust > 50 else 2
                    elif not GirlA.Uptop and GirlA.Over:        
                                #Just overtop
                                $ Line = Line + renpy.random.choice(["You reach under her top and massage her breasts", 
                                    "You pass your hands gently over her warm breasts", 
                                    "Her nipples catch on the fabric of her top as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Over])
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ TempLust += 4 if GirlA.Lust > 50 else 2   
                    elif not GirlA.Uptop and GirlA.Chest:      
                                #just bra
                                $ Line = Line + renpy.random.choice(["You reach under her " + GirlA.Chest + " and massage her breasts", 
                                    "You pass your hands gently over her warm breasts", 
                                    "Her nipples catch on the fabric of her " + GirlA.Chest + " as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you grasp her under her " + GirlA.Chest])
                                $ TempFocus += 3 if Player.Focus < 60 else 2    
                                $ TempLust += 5 if GirlA.Lust > 50 else 2    
                    elif GirlA.Pierce: 
                                #pierced
                                $ Line = Line + renpy.random.choice(["You reach out and massage her glorious breasts", 
                                    "You pass your hands gently over her warm breasts, and blow across her pierced nipples", 
                                    "Her piercings catch lightly on your fingers as you grasp her warm flesh, you can see the nipples stiffen",
                                    "She gasps as you lightly thumb across her pierced nipples"])
                                $ TempFocus += 4 if Player.Focus < 70 else 2 
                                $ TempLust += 6 if GirlA.Lust > 40 else 4  
                    else: #topless
                                $ Line = Line + renpy.random.choice(["You reach out and massage her glorious breasts", 
                                    "You pass your hands gently over her warm breasts, and blow across her nipples", 
                                    "Her nipples catch lightly on your fingers as you grasp her warm flesh, you can see them stiffen",
                                    "She gasps as you lightly thumb her rigid nipples"])
                                $ TempFocus += 4 if Player.Focus < 60 else 2 
                                $ TempLust += 6 if GirlA.Lust > 50 else 3  
                    if D20S > 18:
                            if GirlA == KittyX:
                                    $ Line = "You continue to fondle " + GirlA.Name + ". They fit comfortably into your palms." 
                            elif GirlA == EmmaX:
                                    $ Line = "You continue to fondle " + GirlA.Name + ". You can barely wrap your hands around them." 
                    $ GirlA.Addict -= 2
                  
    # end Fondle breasts                                 //////////////////////////////////////////////////////////////////////////////
    elif Trigger == "suck breasts":  
                    $ Line = "You continue to suck on " + GirlA.Name + "'s breasts. "    
                    if not GirlA.Uptop and GirlA.Over and GirlA.Chest: 
                                #Full top
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the layered tops",
                                        "You  place a nipple between your lips, and give it a quick tug through the " + GirlA.Over,
                                        "She gasps as you gently nibble her rigid nipples poking through her tops"])      
                                $ TempFocus += 2 if Player.Focus < 50 else 1  
                                $ TempLust += 2 if GirlA.Lust < 30 else 1
                    elif not GirlA.Uptop and GirlA.Over:        
                                #Just overtop
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You gently nibble at her nipples as you suck on them through the " + GirlA.Over,
                                        "You tease her nipples with your tongue through the fabric",
                                        "You slowly lick her nipples through her moist top", 
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her top"])    
                                $ TempFocus += 2 if Player.Focus < 50 else 1
                                $ TempLust += 5 if GirlA.Lust > 50 else 3
                    elif not GirlA.Uptop and GirlA.Chest:      
                                #just bra
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                        "You tease her nipples with your tongue through her " + GirlA.Chest,
                                        "You slowly lick her nipples through her moist " + GirlA.Chest, 
                                        "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                        "She gasps as you lightly lick her rigid nipples, poking through her " + GirlA.Chest])   
                                $ TempFocus += 4 if Player.Focus < 60 else 3    
                                $ TempLust += 5 if GirlA.Lust > 50 else 2    
                    elif GirlA.Pierce: 
                                #pierced
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her piercings with your tongue",
                                    "You slowly lick around, and then blow across her nipples", 
                                    "You gently place a pierced nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if Player.Focus < 70 else 4 
                                $ TempLust += 10 if GirlA.Lust > 40 else 7
                                $ GirlA.Addict -= 2
                    else: #topless
                                $ Line = renpy.random.choice(["You bend down and motor-boat her breasts",
                                    "You gently nibble at her nipples as you suck on them",
                                    "You tease her nipples with your tongue",
                                    "You slowly lick around, and then blow across her nipples", 
                                    "You gently place a nipple between your lips, and draw it out until it releases with a *pop*",
                                    "She gasps as you lightly lick her rigid nipples"])
                                $ TempFocus += 5 if Player.Focus < 60 else 3 
                                $ TempLust += 10 if GirlA.Lust > 50 else 7  
                                $ GirlA.Addict -= 2
           
    # end Suck breasts                                 //////////////////////////////////////////////////////////////////////////////
        
    elif Trigger == "fondle thighs":  #Trigger4 not available
                    $ Line = "You continue to massage " + GirlA.Name + "'s thighs. "   
                    
                    if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                #she's wearing pants of some sort. . .
                                $ Line = renpy.random.choice(["Her legs twitch a bit in her pants as you caress them", 
                                        "She gasps as you stroke her warm thighs through the pants",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her . . ."])                              
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 1 if GirlA.Lust < 50 else 0
                    elif GirlA.PantsNum() == 5 and GirlA.HoseNum() >= 5: 
                                # skirt with full hose  
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs", 
                                        "You lift her skirt a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her lightly covered thighs",
                                        "You slide a hand up her inner thigh, to just below her . . "])
                                $ TempFocus += 2 if Player.Focus < 40 else 0  
                                $ TempLust += 2 if GirlA.Lust < 40 else 0                                
                                $ GirlA.Addict -= 1 if D20S > 10 else 0                            
                    elif GirlA.PantsNum() == 5 and GirlA.Hose: 
                                #skirt with stockings         
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs", 
                                        "You lift her skirt a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose"])
                                $ TempFocus += 2 if Player.Focus < 50 else 0  
                                $ TempLust += 2 if GirlA.Lust < 50 else 0                               
                                $ GirlA.Addict -= 1 if D20S > 10 else 0                            
                    elif GirlA.PantsNum() == 5:  
                                #skirt and no hose
                                $ Line = renpy.random.choice(["You reach under skirt and stroke her thighs", 
                                        "You lift her skirt a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath her skirt",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just her skirt"])
                                $ TempFocus += 2 if Player.Focus < 50 else 0  
                                $ TempLust += 2 if GirlA.Lust < 50 else 0                               
                                $ GirlA.Addict -= 2 if D20S > 10 else 1                                
                    elif GirlA.HoseNum() >= 5: 
                                # just hose
                                $ Line = renpy.random.choice(["You reach out and stroke her lightly covered thighs", 
                                        "You lift her leg a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, the smooth faberic creasing",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 40 else 0  
                                $ TempLust += 2 if GirlA.Lust < 40 else 0                               
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    elif GirlA.Hose: 
                                #just stockings
                                $ Line = renpy.random.choice(["You reach out and stroke her thighs", 
                                        "You lift her leg a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You slide a hand up her inner thigh, to just above the hose",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 50 else 0  
                                $ TempLust += 2 if GirlA.Lust < 50 else 0                               
                                $ GirlA.Addict -= 1 if D20S > 10 else 0
                    else: #nude legs
                                $ Line = renpy.random.choice(["You reach out and stroke her thighs", 
                                        "You lift her leg a bit and feel her firm thighs", 
                                        "Her legs twitch a bit beneath your hands",
                                        "She gasps as you stroke her warm thighs",
                                        "You draw your hand from her knee to mid-thigh, and she gasps a little",
                                        "You slide a hand up her inner thigh, to just below her. . "])
                                $ TempFocus += 2 if Player.Focus < 50 else 0  
                                $ TempLust += 2 if GirlA.Lust < 50 else 0                               
                                $ GirlA.Addict -= 2 if D20S > 10 else 1
        
    # end fondle thighs                               //////////////////////////////////////////////////////////////////////////////
     
     
    elif Trigger == "fondle pussy":
                    if Speed == 2 and D20S <= 10:
                            $ Line = renpy.random.choice(["You continue to finger " + GirlA.Name + "'s pussy. ", 
                                                    "You continue to finger bang " + GirlA.Name + "'s pussy. ",
                                                    "You continue to finger blast " + GirlA.Name + "'s pussy. "])
                                            
                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            #pants
                                            $ Line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her pussy underneath", 
                                                    "You push her panties aside, and slide a finger between her lips", 
                                                    "You slide a finger into her pussy and stroke the top", 
                                                    "You pull her pants out a bit and she gasps as you slide two fingers between her lips", 
                                                    "You rub her clit with your palm as you dive into her pussy with your middle finger"]) 
                            elif GirlA.PantsNum() == 5:
                                    if GirlA.Panties and not GirlA.PantiesDown: 
                                            #Just panties
                                            $ Line = renpy.random.choice(["You push her skirt and " + GirlA.Panties + " aside, and slide a finger between her lips", 
                                                    "You slide a finger under her " + GirlA.Panties + " and stroke the top or her pussy", 
                                                    "You lift her skirt a bit and she gasps as you pull her " + GirlA.Panties + " aside and slide two fingers between her lips", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                            $ Line = renpy.random.choice(["You push her skirt aside, and slide a finger between her lips", 
                                                    "You slide a finger into her pussy and stroke the top", 
                                                    "You lift her skirt a bit and she gasps as you slide two fingers between her lips", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"]) 
                                            $ TempFocus += 2 
                                            $ TempLust += 2                            
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown: 
                                        # just shorts on
                                        $ Line = renpy.random.choice(["You slide a hand down her shorts, and slide your fingers into her pussy underneath", 
                                                "You push her shorts up, and slide a finger between her lips", 
                                                "You slide a finger along her pussy and stroke to the top", 
                                                "You pull her shorts out a bit and she gasps as you slide two fingers between her lips",                                                 
                                                "You rub her clit with your palm as you dive into her pussy with your middle finger"])  
                            elif GirlA.Panties and not GirlA.PantiesDown: 
                                        #Just panties
                                        $ Line = renpy.random.choice(["You push her panties aside, and slide a finger between her lips", 
                                                "You slide a finger along her pussy and stroke to the top", 
                                                "You lift her panties a bit and she gasps as you slide two fingers between her lips"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and slide a finger between her lips", 
                                                "You slide a finger along her pussy and stroke to the top", 
                                                "You lift her lips a bit and she gasps as you slide two fingers between them", 
                                                "You rub her clit with your thumb as you dive into her pussy with your middle finger"]) 
                                        $ TempFocus += 2 
                                        $ TempLust += 2
                                
                            $ TempFocus += 4 if Player.Focus < 50 else 3  
                            $ TempLust += 6 if GirlA.Lust > 40 else 3
                            $ GirlA.Addict -= 2  
                                
                    else: #if not fingerblasting or not high rolls
                            $ Line = renpy.random.choice(["You continue to stroke " + GirlA.Name + "'s pussy. ", 
                                                    "You continue to rub " + GirlA.Name + "'s pussy. ",
                                                    "You continue to caress " + GirlA.Name + "'s pussy. "])
                                            
                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            #pants on
                                            $ Line = renpy.random.choice(["You reach out and brush your hands across her pussy through the pants", 
                                                    "You slide a hand down her pants, and brush your hands across her pussy underneath", 
                                                    "You put your hand against her mound and grind against it", 
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the pants",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                                
                            elif GirlA.PantsNum() == 5:
                                    if GirlA.Panties == "shorts" and not GirlA.PantiesDown: 
                                            #shorts on
                                            $ Line = renpy.random.choice(["You reach under skirt and ran your hands over the thin shorts covering her", 
                                                    "You slide a hand up the leg of her shorts, and brush your hands across her pussy underneath", 
                                                    "You put your hand against her mound and grind against it", 
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                    "As you dig your thumb into her, she gasps and raises up a bit",
                                                    "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"]) 
                                    elif GirlA.Panties and not GirlA.PantiesDown: #Just panties
                                            $ Line = renpy.random.choice(["You reach under skirt and brush across her panties", 
                                                    "You lift her skirt a bit and grind against her panties", 
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and stroke her lips", 
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her",
                                                    "She gasps as you rub her pussy through her panties",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])  
                                    elif GirlA.HoseNum() >= 5: 
                                            #just hose
                                            $ Line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric", 
                                                    "You grab her hose and pull them taut, elliciting a small gasp",
                                                    "You put your hand against her mound and grind against it", 
                                                    "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material", 
                                                    "Her legs twitch a bit as you press your thumb against her",
                                                    "She gasps as you reach under her hose and lightly stroke her ass",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                    else: #skirt, but nothing else
                                            $ Line = renpy.random.choice(["You reach under skirt and brush across her bare lips", 
                                                    "You lift her skirt a bit and grind against her warm mound", 
                                                    "You lift her skirt a bit and she gasps as you stroke her moist lips", 
                                                    "Her legs twitch a bit beneath her skirt as you press your thumb against her"
                                                    "She gasps as you rub her bare pussy",
                                                    "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                            if D20S <= 10:
                                                $ TempFocus += 3 if Player.Focus < 50 else 1  
                                                $ TempLust += 4 if GirlA.Lust > 40 else 2
                                                $ GirlA.Addict -= 2  
                                            else: #If it touches skin
                                                $ TempFocus += 1 
                                                $ TempLust += 1
                            
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown:
                                        # just shorts on
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her pussy through the shorts", 
                                                "You slide a hand down her shorts, and brush your hands across her pussy underneath", 
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the thin shorts",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif GirlA.Panties and not GirlA.PantiesDown: 
                                        #Just panties
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her panties", 
                                                "You grab her panties and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material", 
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her panties and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            elif GirlA.HoseNum() >= 5: 
                                        #just hose
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her cleft through the thin fabric", 
                                                "You grab her hose and pull them taut, elliciting a small gasp",
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips through the thin material", 
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her hose and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across her bare lips", 
                                                "You put your hand against her mound and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her lips", 
                                                "Her legs twitch a bit as you press your thumb against her",
                                                "She gasps as you reach under her and lightly stroke her ass",
                                                "You slide a hand up her inner thigh, she moans a little as you reach the point where they meet"])
                                        if D20S <= 10:
                                            $ TempFocus += 3 if Player.Focus < 50 else 1  
                                            $ TempLust += 4 if GirlA.Lust > 40 else 2
                                            $ GirlA.Addict -= 2  
                                        else: #If it touches skin
                                            $ TempFocus += 1 
                                            $ TempLust += 1
                                
                            if D20S > 10:#If it touches skin
                                $ TempFocus += 3 if Player.Focus < 50 else 1  
                                $ TempLust += 4 if GirlA.Lust > 40 else 2
                                $ GirlA.Addict -= 2  
                            else: 
                                $ TempFocus += 2 if Player.Focus < 50 else 1  
                                $ TempLust += 2 if GirlA.Lust > 40 else 1
                            if GirlA.Pierce and D20S <= 3:
                                    "You tug on her piercing with your thumb, then let it snap back"
                                
        
    # end fondle pussy                               /////////////////////////////////////////////////////////////////////////////
    
    
    elif Trigger == "lick pussy":
                            $ Line = renpy.random.choice(["You continue to lick " + GirlA.Name + "'s pussy. ", 
                                                    "You continue to suck " + GirlA.Name + "'s pussy. ",
                                                    "You continue to tongue " + GirlA.Name + "'s pussy. "])
                                            
                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            $ Line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her, even through the thick material",
                                                    "She gasps as you press on her clit through the thick fabric",
                                                    "You rub her clit with your nose as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the surface of her pants", 
                                                    "With a little nibble, you tug at the denim", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"]) 
                                            $ TempFocus += 1 if Player.Focus < 70 else 0  
                                            $ TempLust += 3 if GirlA.Lust > 60 else 2
                            else:                    
                                if GirlA.PantsNum() == 5:
                                        if GirlA.Panties == "shorts" and not GirlA.PantiesDown: 
                                                #shorts on
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her shorts",                 
                                                        "You bend down and lick the edges of her lips through the shorts",                 
                                                        "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin shorts", 
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        elif GirlA.Panties and not GirlA.PantiesDown:
                                                #Just panties
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her panties",                 
                                                        "You bend down and stroke the edges of her panties with your tongue",                 
                                                        "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin panties", 
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        elif GirlA.HoseNum() >= 5: 
                                                #just hose
                                               $ Line = renpy.random.choice(["You push her skirt up and lick at her pussy through her hose",                 
                                                        "You bend down and stroke the edges of her lips through the hose",                 
                                                        "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit through the thin fabric",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick the juice from her thin hose", 
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                        else: #skirt, but nothing else
                                                $ Line = renpy.random.choice(["You push her skirt aside and stroke her lips with your tongue", 
                                                        "You slide your tongue into her pussy and flick the roof with deft strokes", 
                                                        "You spread the lips back and she gasps as you slide your tongue between them", 
                                                        "You can feel her twitching as you grind your tongue against her clit",
                                                        "She gasps as you suck on her clit",
                                                        "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                        "You put your hand against her mound and lick around her lips", 
                                                        "With a little nibble, you tug on her lower lips",
                                                        "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                        "She gasps as you reach under her warm lips and lightly stroke her ass"])            
                                                if D20S <= 10:
                                                    $ TempFocus += 3 if Player.Focus < 70 else 1  
                                                    $ TempLust += 4 if GirlA.Lust > 60 else 2
                                                    $ GirlA.Addict -= 3  
                                                else: #If it touches skin
                                                    $ TempFocus += 1 
                                                    $ TempLust += 1
                                
                                #no skirt or pants
                                elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown: 
                                            # just shorts on
                                            $ Line = renpy.random.choice(["You bend down and lick the edges of her lips through her shorts",                 
                                                    "You spread the lips back beneath her shorts, and she gasps as you slide your tongue across them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin shorts", 
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])       
                                elif GirlA.Panties and not GirlA.PantiesDown: 
                                            #Just panties
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",                 
                                                    "You spread the lips back beneath her panties, and she gasps as you slide your tongue across them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin panties", 
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                elif GirlA.HoseNum() >= 5:
                                            #just hose
                                            $ Line = renpy.random.choice(["You bend down and stroke her lips with your tongue",                 
                                                    "You spread the lips back beneath her hose, and she gasps as you slide your tongue across them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit through the thin fabric",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick the juice from her thin hose", 
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                else: #nothing
                                            $ Line = renpy.random.choice(["You bend down and stroke her lips with your tongue", 
                                                    "You slide your tongue into her pussy and flick the roof with deft strokes", 
                                                    "You spread the lips back and she gasps as you slide your tongue between them", 
                                                    "You can feel her twitching as you grind your tongue against her clit",
                                                    "She gasps as you suck on her clit",
                                                    "You rub her clit with your thumb as you dive into her pussy with your tongue",
                                                    "You put your hand against her mound and lick around her lips", 
                                                    "With a little nibble, you tug on her lower lips",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])
                                            if D20S <= 10: 
                                                $ TempFocus += 3 if Player.Focus < 70 else 1  
                                                $ TempLust += 4 if GirlA.Lust > 60 else 2
                                                $ GirlA.Addict -= 3  
                                            else: #If it touches skin
                                                $ TempFocus += 1 
                                                $ TempLust += 1
                                    
                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 4 if Player.Focus < 70 else 1  
                                    $ TempLust += 10 if GirlA.Lust > 60 else 5
                                    $ GirlA.Addict -= 3  
                                else: 
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 5 if GirlA.Lust > 60 else 3
                                if GirlA.Pierce and D20S <= 3:
                                        "You tug on her piercing with your teeth, then let it snap back"
                                
    # end lick pussy                               /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "fondle ass":                  
                        $ Line = renpy.random.choice(["You continue to fondle " + GirlA.Name + "'s ass. ", 
                                                "You continue to feel up " + GirlA.Name + "'s ass. ",
                                                "You continue to grope " + GirlA.Name + "'s ass. "])
                                        
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                        $ Line = renpy.random.choice(["You reach out and brush your hands across the back of her pants", 
                                                "You slide a hand down her pants, and firmly cup her ass", 
                                                "You put your hand against her rear and grind against it", 
                                                "You reach into her gap and she gasps as you slide your hand across and stroke her warm mound", 
                                                "As you dig your thumb into her, she gasps and raises up a bit",
                                                "She gasps as you reach under her and lightly stroke her ass through the pants",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])  
                                            
                        elif GirlA.PantsNum() == 5:
                                # skirt
                                if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                        #shorts on
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her shorts", 
                                                "You lift her skirt a bit and grind against her shorts", 
                                                "You lift her skirt a bit and she gasps as you pull her shorts aside and stroke across her butt", 
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her shorts",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                elif GirlA.Panties and not GirlA.PantiesDown: 
                                        #Just panties
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her panties", 
                                                "You lift her skirt a bit and grind against her panties", 
                                                "You lift her skirt a bit and she gasps as you pull her panties aside and stroke across her butt", 
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her panties",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                elif GirlA.HoseNum() >= 5: 
                                        #just hose
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her hose", 
                                                "You lift her skirt a bit and grind against her hose", 
                                                "You lift her skirt a bit and she gasps as you pull her hose aside and stroke across her butt", 
                                                "Her legs twitch a bit beneath her skirt as you give her cheeks a firm squeeze",
                                                "She gasps as you stroke her asshole through her hose",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                else: #skirt, but nothing else
                                        $ Line = renpy.random.choice(["You reach under skirt and brush across her bare ass", 
                                                "You lift her skirt a bit and grind against her warm cheeks", 
                                                "You lift her skirt a bit and she gasps as you stroke asshole", 
                                                "Her legs twitch a bit beneath her skirt as you press your thumb against her firm rear",
                                                "She gasps as you rub her bare hole",
                                                "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"]) 
                                        if D20S <= 10:
                                            $ TempFocus += 2 if Player.Focus < 50 else 1  
                                            $ TempLust += 3 if GirlA.Lust > 40 else 2
                                            $ GirlA.Addict -= 1  
                                        else: #If it touches skin
                                            $ TempFocus += 1 
                                            $ TempLust += 1
                        
                        #no skirt or pants
                        elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown: 
                                    # just shorts on
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her lightly covered cheeks", 
                                            "You grab her shorts and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material", 
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her shorts and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])                                      
                        elif GirlA.Panties and not GirlA.PantiesDown: 
                                    # panties   
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks", 
                                            "You grab her panties and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material", 
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her panties and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])  
                        elif GirlA.HoseNum() >= 5: 
                                    #just hose
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her barely covered cheeks", 
                                            "You grab her hose and pull them taut, elliciting a small gasp",
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her hole through the thin material", 
                                            "Her legs twitch a bit as you grind her puckered hole",
                                            "She gasps as you reach under her hose and lightly stroke her warm flesh",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])  
                        else: #nothing
                                    $ Line = renpy.random.choice(["You reach out and brush your hands across her bare ass", 
                                            "You put your hand against her firm rear and grind against it", 
                                            "You reach into her gap and she gasps as you slide your hand across and stroke her puckered hole", 
                                            "Her legs twitch a bit as you press your thumb against her",
                                            "She gasps as you reach under her and lightly stroke her ass",
                                            "You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks"])   
                                    if D20S <= 10:
                                        $ TempFocus += 2 if Player.Focus < 50 else 1  
                                        $ TempLust += 3 if GirlA.Lust > 40 else 2
                                        $ GirlA.Addict -= 1  
                                    else: #If it touches skin
                                        $ TempFocus += 1 
                                        $ TempLust += 1
                            
                        if D20S > 10:#If it touches skin
                            $ TempFocus += 2 if Player.Focus < 50 else 1  
                            $ TempLust += 3 if GirlA.Lust > 40 else 2
                            $ GirlA.Addict -= 1  
                        else: 
                            $ TempFocus += 2 if Player.Focus < 50 else 1  
                            $ TempLust += 2 if GirlA.Lust > 40 else 1
                                
    # end fondle ass                               /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "insert ass":
                            $ Line = renpy.random.choice(["You continue to finger " + GirlA.Name + "'s asshole. ", 
                                                    "You continue to finger bang " + GirlA.Name + "'s asshole. ",
                                                    "You continue to finger " + GirlA.Name + "'s rim. "])
                                            
                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                            $ Line = renpy.random.choice(["You slide a hand down her pants, and slide your fingers into her anus", 
                                                    "You push her panties aside, and slide a finger between her cheeks", 
                                                    "You slide a finger into her tight anus", 
                                                    "You pull her pants out a bit and she gasps as you slide a finger up her hole", 
                                                    "You gasps as you rub her asshole with your fingers"]) 
                            elif GirlA.PantsNum() == 5:
                                    if GirlA.Panties == "shorts" and not GirlA.PantiesDown: 
                                            #shorts on
                                            $ Line = renpy.random.choice(["You push her skirt and shorts up, and slide a finger into her anus", 
                                                    "You slide a finger into her tight anus", 
                                                    "You lift her skirt a bit and she gasps as you pull her shorts up and slide a finger into her anus", 
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"])
                                    elif GirlA.Panties and not GirlA.PantiesDown: 
                                            #Just panties
                                           $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide a finger into her anus", 
                                                    "You slide a finger into her tight anus", 
                                                    "You lift her skirt a bit and she gasps as you pull her panties aside and slide a finger into her anus", 
                                                    "You rub her clit with your thumb as you dive into her pussy with your middle finger"])
                                    else: #skirt, but nothing else
                                             $ Line = renpy.random.choice(["You push her skirt aside, and slide a finger into her anus", 
                                                    "You slide a finger into her tight anus", 
                                                    "You lift her skirt a bit and she gasps as you slide a finger into her anus", 
                                                    "You rub her pussy with your thumb as you dive into her anus with your middle finger"]) 
                            #no skirt or pants
                            elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown: 
                                    # just shorts on
                                    $ Line = renpy.random.choice(["You slide a hand down her shorts, and slide a finger into her anus", 
                                                "You push her shorts up, and slide a finger between her lips", 
                                                "You slide a finger into her tight anus", 
                                                "You pull her shorts out a bit and she gasps as you slide a finger into her anus",                                                 
                                                "You rub her pussy with your palm as you dive into her anus with your middle finger"])  
                            elif GirlA.Panties and not GirlA.PantiesDown: 
                                        #Just panties
                                        $ Line = renpy.random.choice(["You push her panties aside, and slide a finger into her anus", 
                                                "You slide a finger into her tight anus", 
                                                "You lift her panties a bit and she gasps as you and slide a finger into her anus"])
                            else: #nothing
                                        $ Line = renpy.random.choice(["You reach out and slide a finger into her anus", 
                                                "You slide a finger into her tight anus", 
                                                "You lift her lips a bit and she gasps as you  slide a finger into her anus",  
                                                "You rub her pussy with your thumb as you dive into her anus with your middle finger"]) 
                                                                
                            $ TempFocus += 2 if Player.Focus < 50 else 1  
                            $ TempLust += 6 if GirlA.Lust > 70 else 3
                            if not GirlA.Loose:
                                    $ TempLust -= 3
                            elif GirlA.Loose < 2:
                                    $ TempLust += 1   
                                    
                            $ GirlA.Addict -= 2  
                                        
    # end insert ass                              /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "lick ass":
                            $ Line = renpy.random.choice(["You continue to lick " + GirlA.Name + "'s ass. ", 
                                                    "You continue to suck " + GirlA.Name + "'s ass. ",
                                                    "You continue to tongue " + GirlA.Name + "'s ass. "])
                                            
                            if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                                $ Line = renpy.random.choice(["You can feel her twitching as you grind your tongue against her anus, even through the thick material",
                                                        "She gasps as you press on her asshole through the thick fabric",
                                                        "You put your hand against her mound and lick the surface of her pants", 
                                                        "With a little nibble, you tug at the denim"])  
                                                $ TempFocus += 1 if Player.Focus < 70 else 0  
                                                $ TempLust += 1 if GirlA.Lust < 60 else 0
                            else:                    
                                if GirlA.PantsNum() == 5:
                                        if GirlA.Panties == "shorts" and not GirlA.PantiesDown:
                                                #shorts on
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her shorts",                 
                                                        "You bend down and stroke the edges of her shorts with your tongue",                 
                                                        "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it", 
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])  
                                        elif GirlA.Panties and not GirlA.PantiesDown: 
                                                #Just panties
                                                $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her panties",                 
                                                        "You bend down and stroke the edges of her panties with your tongue",                 
                                                        "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it", 
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])  
                                        elif GirlA.HoseNum() >= 5: 
                                                #just hose
                                               $ Line = renpy.random.choice(["You push her skirt up and lick at her asshole through her hose",                 
                                                        "You bend down and stroke the edges of her hose with your tongue",                 
                                                        "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it", 
                                                        "You can feel her twitching as you grind your tongue against her anus",
                                                        "She gasps as you suck on her asshole through the thin fabric",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "With a little nibble, you tug back the fabric",
                                                        "You slowly lick into her gap and she gasps as you press the rim aside"])  
                                        else: #skirt
                                                $ Line = renpy.random.choice(["You push her skirt aside and stroke her asshole with your tongue", 
                                                        "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                        "You can feel her twitching as you grind your tongue against her asshole",
                                                        "She gasps as you suck on her anus",
                                                        "You rub her pussy with your thumb as you dive into her asshole with your tongue",
                                                        "You put your hand against her mound and lick around her rim", 
                                                        "You slowly lick into her gap and she gasps as you press the rim apart"])         
                                                if D20S <= 10:
                                                    $ TempFocus += 2 if Player.Focus < 70 else 0  
                                                    $ TempLust += 3 if GirlA.Lust > 60 else 1
                                                    $ GirlA.Addict -= 3  
                                                else: #If it touches skin
                                                    $ TempFocus += 1 
                                                    $ TempLust += 1
                                
                                #no skirt or pants
                                elif (GirlA.PantsNum() == 6 or (GirlA == RogueX and GirlA.Panties == "shorts")) and not GirlA.PantiesDown: 
                                            # just shorts on
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her shorts with your tongue",                 
                                                    "You spread the cheeks back beneath her shorts, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"])   
                                elif GirlA.Panties and not GirlA.PantiesDown: 
                                            #Just panties
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her panties with your tongue",                 
                                                    "You spread the cheeks back beneath her panties, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"]) 
                                elif GirlA.HoseNum() >= 5: 
                                            #just hose
                                            $ Line = renpy.random.choice(["You bend down and stroke the edges of her hose with your tongue",                 
                                                    "You spread the cheeks back beneath her hose, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her anus",
                                                    "She gasps as you suck on her anus through the thin fabric",
                                                    "You rub her pussy with your thumb as you dive into her anus with your tongue",
                                                    "With a little nibble, you tug back the fabric",
                                                    "You slowly lick into her gap and she gasps as you press the rim apart"]) 
                                else: #nothing
                                            $ Line = renpy.random.choice(["You bend down and stroke her rim with your tongue", 
                                                    "You slide your tongue into her asshole and flick the roof with deft strokes", 
                                                    "You spread the cheeks back, and she gasps as you slide your tongue into it",
                                                    "You can feel her twitching as you grind your tongue against her rim",
                                                    "She gasps as you suck on her hole",
                                                    "You rub her clit with your thumb as you dive into her asshole with your tongue",
                                                    "You knead her cheeks and lick around her rim", 
                                                    "With a little nibble, you toss her salad",
                                                    "You slowly lick into her gap and she gasps as you press the walls aside", 
                                                    "She gasps as you reach under her warm lips and lightly stroke her ass"])  
                                            if D20S <= 10: 
                                                $ TempFocus += 2 if Player.Focus < 70 else 0  
                                                $ TempLust += 3 if GirlA.Lust > 60 else 1
                                                $ GirlA.Addict -= 3  
                                            else: #If it touches skin
                                                $ TempFocus += 1 
                                                $ TempLust += 1
                                    
                                if D20S > 10: #If it touches skin
                                    $ TempFocus += 3 if Player.Focus < 70 else 0  
                                    $ TempLust += 9 if GirlA.Lust > 60 else 4
                                    $ GirlA.Addict -= 3  
                                else: 
                                    $ TempFocus += 1 if Player.Focus < 50 else 0  
                                    $ TempLust += 4 if GirlA.Lust > 60 else 2
                
                            $ TempLust += 2 if GirlA.Loose > 1 else 0 #Bonus lust if she's anal experienced
                                   
    # end lick ass                               /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "dildo pussy":                            
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her pants", 
                                        "You slap the dildo lightly against her mound"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 10:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her tights", 
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 5:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her hose", 
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        else:
                                if GirlA.PantsNum() == 5 and GirlA.Panties:            
                                    $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her pussy", 
                                            "You slide the toy deep into her pussy", 
                                            "She gasps as you rotate the dildo within her tight pussy",
                                            "You rub her clit with your thumb as you dive into her puss with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.PantsNum() == 5:            
                                    $ Line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole", 
                                            "You slide the toy deep into her pussy",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight puss", 
                                            "She gasps as you rotate the dildo within her slit",
                                            "You rub her clit with your thumb as you dive into her pussy with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.Panties and not GirlA.PantiesDown:            
                                    $ Line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight pussy", 
                                            "You slide the dildo into her moist slit and stroke it rapidly", 
                                            "You lift her panties a bit and she gasps as you slide the dildo between her lower lips", 
                                            "She gasps as you rub her tight pussy with the toy",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight slit through the thin material"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                else:            
                                    $ Line = renpy.random.choice(["You reach out and slide the dildo along her mound", 
                                            "You slide the toy into her pussy and stroke it slowly", 
                                            "You pull her lips apart and she gasps as you slide the dildo between them", 
                                            "You can feel her twitching as you press your thumb against her clit",
                                            "She gasps as you rub her clit with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her pussy with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her wet pussy"])            
                                    $ TempFocus += 3 if Player.Focus < 50 else 1  
                                    $ TempLust += 10 if GirlA.Lust > 70 else 8
    # end dildo pussy                              /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "dildo anal":
                        if GirlA.PantsNum() > 6 and not GirlA.Upskirt:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her pants", 
                                        "You slap the dildo lightly against her ass"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 10:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her tights", 
                                        "You slap the dildo lightly at the outside of her tights"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        elif GirlA.HoseNum() >= 5:
                                $ Line = renpy.random.choice(["You rub the dildo against the outside of her hose", 
                                        "You slap the dildo lightly at the outside of her hose"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 1
                        else:
                                if GirlA.PantsNum() == 5 and GirlA.Panties:            
                                    $ Line = renpy.random.choice(["You push her skirt and panties aside, and slide the dildo into her ass", 
                                            "You slide the toy deep into her ass", 
                                            "She gasps as you rotate the dildo within her tight asshole",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.PantsNum() == 5:            
                                    $ Line = renpy.random.choice(["You push her skirt aside, and slide the dildo into her tight hole", 
                                            "You slide the toy deep into her ass",
                                            "You lift her skirt a bit and she gasps as you slide the dildo firmly into her tight anus", 
                                            "She gasps as you rotate the dildo within her ass",
                                            "You rub her clit with your thumb as you dive into her ass with the rubber phallus"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                elif GirlA.Panties and not GirlA.PantiesDown:            
                                    $ Line = renpy.random.choice(["You push her panties aside, and slide the dildo into her tight ass", 
                                            "You slide the dildo into her ass and stroke it rapidly", 
                                            "You lift her panties a bit and she gasps as you slide the dildo between her cheeks", 
                                            "She gasps as you rub her tight asshole with the toy",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the dildo in and press against her tight anus through the thin material"])
                                    $ TempFocus += 2 if Player.Focus < 50 else 1  
                                    $ TempLust += 8 if GirlA.Lust > 70 else 5
                                else:            
                                    $ Line = renpy.random.choice(["You reach out and slide the dildo between her cheeks", 
                                            "You slide the toy into her asshole and stroke it against the sides", 
                                            "You pull her cheeks apart and she gasps as you slide the dildo between them", 
                                            "You can feel her twitching as you press your thumb against her anus",
                                            "She gasps as you rub her anus with the hard rubber",
                                            "You rub her clit with your thumb as you dive into her asshole with the dildo",
                                            "You reach into her gap and she gasps as you slide the toy across and press it into her firm anus"])            
                                    $ TempFocus += 3 if Player.Focus < 50 else 1  
                                    $ TempLust += 10 if GirlA.Lust > 70 else 6
                                if not GirlA.Loose:
                                        $ TempLust -= 3
                                elif GirlA.Loose < 2:
                                        $ TempLust += 1   
    # end dildo ass                              /////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "masturbation":
                call Girl_Self_Lines(GirlA) #Rog*ue_Self_Lines  
                if "unseen" not in GirlA.RecentActions:
                    if Trigger2 == "jackin" or "cockout" in Player.RecentActions:
                            $ TempLust += 2
#                $ TempLust = 0
                
    # end Masturbation                               /////////////////////////////////////////////////////////////////////////////
    elif Trigger == "lesbian":
                call SexDialog_Threeway(GirlA,"lesbian",GirlB=Partner) #Rog*ue_SexDialog_Threeway("lesbian")      
    
    elif Trigger == "foot":
                        $ Line = GirlA.Name + " continues stroke your cock with her feet. "
                           
                        if not Speed:
                                    if GirlA.Foot > 2:
                                            $ Line = Line + "She just seems to be enjoying the feel of it"
                                            $ TempLust += 2 if GirlA.Lust < 60 else 0
                                    else:
                                            $ Line = Line + "She just seems to be looking it over"
                                            $ TempLust += 2 if GirlA.Lust < 40 else 0
                                            $ TempFocus += -3 if Player.Focus > 50 else 2
                                        
                                    $ GirlA.Addict -= 1 if D20S > 10 else 2
                                    return
                        
                        if GirlA.Foot > 4:                          # After the 5th time 
                                    if Speed <= 1:                      #slow 
                                        $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching",
                                                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"])   
                                        
                                        $ TempFocus += 20 if Player.Focus > 70 else 5
                                              
                                    else:                               #fast
                                        $ Line = Line + renpy.random.choice(["Her movements have become almost masterful, her slightest touch starts you twitching", 
                                                "Her expert strokes will have you boiling over in seconds",
                                                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head",
                                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                                "You can't tell where she is at any moment, all you know is that it works"]) 
                                        
                                        $ TempFocus += 20 if Player.Focus < 40 else 5        
                                
                        elif GirlA.Foot >= 3:                       #third through 5th time
                                    if Speed <= 1:                      #slow
                                        $ Line = Line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft", 
                                                "She's still learning, but learning fast", 
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She gently caresses the shaft, and brushes the balls in her other foot, giving them a light massage"])  
                                        
                                        $ TempFocus += 15 if Player.Focus > 60 else 5
                                        
                                    else:                               #fast
                                        $ Line = Line + renpy.random.choice(["She's begining to figure things out, her toes cause tingles as they caress the shaft", 
                                                "She's still learning, but learning fast", 
                                                "Her feet glide smoothly across your cock",
                                                "She has a smooth motion going now, gentle and precise",
                                                "Her lessons are paying off, she's really becoming very talented at this",
                                                "She quickly strokes your cock, with a very deft pressure"]) 
                                        
                                        $ TempFocus += 15 if Player.Focus < 60 else 7         
                            
                        else:                                   #First and second time
                                if Speed <= 1:                      #slow
                                    $ Line = Line + renpy.random.choice(["She makes up for her inexperience with determination, carefully stroking your cock", 
                                            "She moves her feet up and down the shaft. She's a little rough at this, but at least she tries", 
                                            "She strokes you gently. She isn't quite sure what to do with the balls",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This may take a few tries"])     
                                    
                                    $ TempFocus += 10 if Player.Focus > 60 else 5         
                                else:                               #fast 
                                    $ Line = Line + renpy.random.choice(["She really wasn't prepared for speeding up, and your cock often slips between her feet", 
                                            "She rapidly moves her feet up and down the shaft. She's a little rough at this, but at least she tries", 
                                            "She strokes you a bit too quickly, the friction is a bit uncomfortable",
                                            "Her toes fumble with your shaft a bit",
                                            "She nudges one of your balls too tightly, but stops when you wince",
                                            "She has a firm grip, and she's not letting go. This train is out of control"])  
                                    
                                    $ TempFocus += 8 if Player.Focus > 60 else 2         
                                
                        $ TempLust += 2 if GirlA.Lust < 60 else 0
                        $ TempLust += 3 if GirlA.Foot > 2 else 0
                        $ GirlA.Addict -= 1
            
    #End Footy dialog ////////////////////////////////////////////////////////////////////////////////////////////////////////
    
    elif Trigger == "kiss you":  
                        $ GirlA.Addict -= 3 
                        if GirlA.Kissed > 10 and GirlA.Love >= 700:#Loving
                                $ Line = renpy.random.choice(["She hungrily presses her lips against yours", 
                                        "She confidently presses her lips against yours", 
                                        "Her lips part as you hold her close",    
                                        "You nibble her neck as she groans in pleasure",
                                        "You squeeze her tightly as your tongues jostle",
                                        "Her tongue dances around yours",
                                        "She nibbles your ear as her hands slide across your back",
                                        "Your hands slide down her body as your lips press hers"])
                                $ TempFocus += 1 if Player.Focus < 50 else 0  
                                $ TempFocus += 1 if Player.Focus < 90 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 0
                                $ TempLust += 1 if GirlA.Lust < 90 else 0
                        elif GirlA.Kissed > 5 or GirlA == EmmaX:#reasonably experienced        
                                $ Line = renpy.random.choice(["She confidently presses her lips against yours", 
                                        "You softly kiss her plump lips", 
                                        "Her lips part as you hold her close",    
                                        "You nibble her neck as she coos in pleasure",
                                        "You squeeze her tightly as your lips connect",
                                        "Her tongue flickers out to meet yours",
                                        "Your hands slide down her body as your lips brush hers"])
                                $ TempFocus += 1 if Player.Focus < 70 else 0  
                                $ TempLust += 3 if GirlA.Lust < 50 else 0
                                $ TempLust += 1 if GirlA.Lust < 90 else 0
                        else:#basic kissing
                                $ Line = renpy.random.choice(["She tentatively presses her lips against yours", 
                                        "You softly kiss her plump lips", 
                                        "Her lips part slightly as you hold her close",
                                        "You squeeze her tightly as your lips connect",
                                        "Your hands slide down her body as your lips brush hers"]) 
                                $ TempFocus += 1 if Player.Focus < 70 else 0  
                                $ TempLust += 2 if GirlA.Lust < 30 else 0
                                $ TempLust += 1 if GirlA.Lust < 70 else 0
                                
    # end kissing                              /////////////////////////////////////////////////////////////////////////////
    else: #no Trigger was set, somehow
        "No trigger was set, or it was '[Trigger]'. Please tell Oni what happend up to this point."
        $ Line = "Huh."
       
    $ Line = Line + "."                        
    # Wrap-up
    $ PrimaryLust += TempLust
    $ SecondaryLust += TempLust2 + 2
        
    return
    
    
#end Primary_SexDialog Trigger1  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 



# Offhand function  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Offhand_Dialog(Girl=Primary, TempLine=0):
    #This is the dialog for what you're doing with your other hand while a primary action takes place
    #called by Sex_Dialog, if Trigger2 and D20S <= 15: call Offhand_Dialog                        
    if Girl not in TotalGirls:
            return
    if not Trigger2: #If there are no offhand options set, return
            return    
    
    $ D20X = renpy.random.randint(1,20)
    
    if Trigger2 == "kiss you":
                $ Line = renpy.random.choice([" Your lips gently slide across hers.", 
                        " Her lips part as you hold her close.",    
                        " You nibble her neck as she groans in pleasure.",
                        " You squeeze her tightly as your tongues jostle.",
                        " Her tongue dances around yours.",
                        " She nibbles your ear as her hands slide across your back.",
                        " Your hands slide down her body as your lips press hers.",
                        " You kiss her passionately.", 
                        " Your tongues swirl around each other's."])
                if Girl.Love >= 300:
                        $ Girl.Statup("Love", 75, 1)
                $ PrimaryLust += 2 if Girl.Lust < 50 else 1
        
    elif Trigger2 == "fondle breasts":
                if Girl == EmmaX and D20X >= 15:
                    $ Line = " You reach out and massage her enormous breasts."
                    $ PrimaryLust += 1           
                    $ TempFocus += 1 
                elif Girl == KittyX and D20X >= 15:
                    $ Line = " You reach out and massage her pert breasts."
                elif D20X >= 15:
                    $ Line = " You reach out and massage her glorious breasts."
                else:
                    $ Line = renpy.random.choice([" You reach out and massage her breasts.", 
                            " You pass your hands gently over her warm breasts.", 
                            " Her nipples catch lightly on your fingers as you grasp her warm flesh, you can feel them stiffen.",
                            " She gasps as you lightly thumb her rigid nipples."])
                $ PrimaryLust += 3           
                $ TempFocus += 2 if Player.Focus < 90 else 0 
        
    elif Trigger2 == "suck breasts":
            if Girl.ChestNum() > 1 or Girl.OverNum() > 1:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You tease her nipples with your tongue through her top.",
                    " You slowly lick her nipples through her moist top.", 
                    " you gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples, poking through her top."])            
            else:
                $ Line = renpy.random.choice([" You bend down and motor-boat her breasts.",
                    " You gently nibble at her nipples as you suck on them.",
                    " You tease her nipples with your tongue.",
                    " You slowly lick around, and then blow across her nipples.", 
                    " You gently place a nipple between your lips, and draw it out until it releases with a *pop*.",
                    " She gasps as you lightly lick her rigid nipples."])
            $ PrimaryLust += 4 if 60 < Girl.Lust < 80 else 2  
            $ TempFocus += 3 if Player.Focus < 90 else 0 
        
    elif Trigger2 == "fondle pussy":
            if Girl.Pubes and D20X >= 15:
                $ Line = " You draw your hand along her furry bush, dripping with her excitement."
            elif D20X >= 15:
                $ Line = " You draw your hand along her smooth mount, slick with her excitement."
            else:
                $ Line = renpy.random.choice([" You put your hand against her mound and grind against it.", 
                        " You reach into her gap and she gasps as you slide your hand across and stroke her lips.", 
                        " Her legs twitch a bit as you press your thumb against her.",
                        " You slide a singer along her lower lips, and she lets out a small shudder.",
                        " You reach between her legs and she gasps as you stroke along her crevice.", 
                        " You slide a hand up her inner thigh, she moans a little as you reach the point where they meet."])
            $ PrimaryLust += 4 if 60 < Girl.Lust < 90 else 2        
            $ TempFocus += 4 if Player.Focus < 90 else 0 
        
    elif Trigger2 == "lick pussy":
            if Girl.PantsNum() <= 5 and Girl.PantiesNum() <= 1:                 
                if Girl.Pubes and D20X >= 15:
                    $ Line = " You press you nose into her furry bush, dripping with her excitement."
                elif D20X >= 15:
                    $ Line = " You press you nose against her smooth mount, slick with her excitement."
                else:
                    $ Line = renpy.random.choice([" You slide your tongue into her pussy and flick the roof with deft strokes.", 
                        " You spread the lips back and she gasps as you slide your tongue between them.", 
                        " You can feel her twitching as you grind your tongue against her clit.",
                        " She gasps as you suck on her clit.",
                        " You rub her clit with your thumb as you dive into her pussy with your tongue.",
                        " With a little nibble, you tug on her lower lips.",
                        " You slowly lick into her gap and she gasps as you press the walls aside."])
            else:
                $ Line = renpy.random.choice([" You spread the lips back beneath the thin fabric, and she gasps as you slide your tongue across them.", 
                    " She gasps as you suck on her clit through the fabric.",
                    " You rub her clit with your thumb as you press against her pussy with your tongue.",
                    " You put your hand against her mound and lick the juice that's collected.", 
                    " With a little nibble, you tug back the fabric.",
                    " You slowly lick into her gap and she gasps as you press the walls aside."])
            $ PrimaryLust += 5 if Girl.Lust > 50 else 2       
            $ TempFocus += 4 if Player.Focus < 90 else 0 
            
    elif Trigger2 == "fondle ass":
            $ Line = renpy.random.choice([" You reach out and brush your hands across her ass.", 
                    " You put your hand against her firm rear and grind against it.", 
                    " You reach between her legs and she gasps as you stroke along her crevice.", 
                    " Her legs twitch a bit as you press your thumb against her.",
                    " She gasps as you reach under her and lightly stroke her ass.",
                    " You slide a hand up her inner thigh, she moans a little as it slides betweek her cheeks."])
            $ PrimaryLust += 2 if Girl.Lust < 50 else 1
            $ TempFocus += 1 if Player.Focus < 50 else 0  
            $ TempFocus += 1 if Player.Focus < 80 else 0   
        
    elif Trigger2 == "insert ass":
            $ Line = renpy.random.choice([" You reach out and slide a finger into her ass.", 
                    " You slide a finger into her asshole and stroke the roof of it.", 
                    " You can feel her twitching as you press your thumb against her clit.",
                    " She gasps as you rub her asshole with your fingers.",
                    " You rub her pussy with your thumb as you dive into her asshole with your middle finger.",
                    " You reach into her gap and she gasps as you slide your hand across and press against her hole.", 
                    " She gasps as you reach under her warm lips and lightly stroke her ass."])       
            $ PrimaryLust += 3 if Girl.Lust > 70 and Girl.Loose else 1
            $ TempFocus += 2 if Player.Focus < 90 else 0 
        
    elif Trigger2 == "jackin":
            if Trigger == "masturbation":
                    $ Line = " You stroke your cock as you watch her go."
            elif Trigger == "lesbian":
                    $ Line = " You stroke your cock as you watch them."
            elif Trigger == "hand":
                    $ Line = renpy.random.choice([" You also give it a little rub.", 
                            " As she does so, you polish the knob a bit.", 
                            " You help.",
                            " Your hand bumps into hers occasionally."])     
            elif Trigger == "blow":
                    if Speed >= 3:
                        $ Line = "."
                    else:
                        $ Line = renpy.random.choice([" You also give it a little rub.", 
                            " As she does so, you work the shaft a bit.", 
                            " Your fingers brush her lips.",
                            " Her lips brush your hand occasionally."])    
            else:
                    $ Line = renpy.random.choice([" With your other hand, you stroke your shaft.", 
                            " You stroke your cock with your other hand.", 
                            " As you do, you stoke yourself."])   
            if "unseen" not in Girl.RecentActions:
                $ PrimaryLust += 3 if 20 < Girl.Lust < 70 else 2
                $ TempFocus += 1 if Player.Focus < 70 else 0            
            $ TempFocus += 5
    return
    #End Offhand check
    
label Offhand_Set(Situation = Situation, TempTrigger = Trigger2,Chr=0):
    #called by various sex activities to set Trigger 2, which is the player's secondary action related to the primary girl 
    #if the Situation is "shift focus," it means that the player is attempting to make his secondary action into his primary one. 
    if not Chr:
            $ Chr = Ch_Focus
    if Situation == "shift focus":        
            if TempTrigger:   
                $ Trigger2 = 0
                if TempTrigger == "fondle breasts":
                        "You shift your attention to her breasts."
                        jump expression Chr.Tag + "_FB_Prep"
                elif TempTrigger == "suck breasts":
                        "You shift your attention to her breasts."
                        jump expression Chr.Tag + "_SB_Prep"
                elif TempTrigger == "fondle pussy":
                        "You shift your attention to her pussy."
                        jump expression Chr.Tag + "_FP_Prep"
                elif TempTrigger == "lick pussy":
                        "You shift your attention to her pussy."
                        jump expression Chr.Tag + "_LP_Prep"
                elif TempTrigger == "fondle ass":
                        "You shift your attention to her ass."
                        jump expression Chr.Tag + "_FA_Prep"
                elif TempTrigger == "insert ass":
                        "You shift your attention to her ass."
                        jump expression Chr.Tag + "_IA_Prep"
                else: #If Trigger2 is "kiss you"
                        "You go back to kissing her deeply."
                        jump KissPrep                
            else: #if there's no Trigger2
                "You aren't doing anything else to shift to."     
            return
    # End "shift" situation    
        
    if Trigger:
        $ Situation = "auto"                 
        menu:  
            "Also kiss her." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    "You lean in and start kissing her."
                    $ Trigger2 = "kiss you"
                    
            "Also fondle her breasts." if Trigger in ("kiss you","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle breasts"
                    call expression Chr.Tag + "_Fondle_Breasts"
                    
            "Also suck her breasts." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "sex", "anal", "hotdog", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "suck breasts"
                    call expression Chr.Tag + "_Suck_Breasts"
                    
            "Also fondle her pussy." if Trigger in ("kiss you","fondle breasts","fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle pussy"
                    call expression Chr.Tag + "_Fondle_Pussy"
                    
            "Also fondle her ass." if Trigger in ("kiss you","fondle breasts","fondle pussy", "fondle thighs", "insert ass", "suck breasts", "lick pussy", "lick ass", "sex", "anal", "hotdog", "foot", "dildo pussy", "dildo anal"):
                    $ Trigger2 = "fondle ass"
                    call expression Chr.Tag + "_Fondle_Ass"
                    
            "Also finger her ass." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "suck breasts", "lick pussy", "lick ass", "sex", "hotdog", "foot", "dildo pussy"):
                    $ Trigger2 = "insert ass"
                    call expression Chr.Tag + "_Insert_Ass"
                    
            "Also jack it." if Trigger in ("fondle breasts","fondle pussy", "fondle thighs", "fondle ass", "insert ass", "suck breasts", "lick pussy", "lick ass", "dildo pussy", "dildo anal"):
                    call Jackin(Chr)
                    
            "Nevermind":
                pass
    else: #if a Trigger is not found. . .
        "There's some kind of bug here, let Oni know." 
        
    $ Situation = 0
    return

    
# end Offhand function  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Girl Self Lines  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Girl_Self_Lines(GirlA = Primary, Mode = "T3", Action = Trigger3, TempLustX = 0): 
    # The Mode can be T3 for Trigger 3 for a masturbation option, or T5/Trigger5 if it's setting a Threeway action. 
    # call Girl_Self_Lines(GirlA,"T5",Trigger5)  X Rogu*e_Self_Lines("T5",Trigger5) 
    # This sets a Action if there isn't one, or sets an intitial line
    # Primary if called from main sex dialog, secondary if called from Threesome 
    
    $ Line = 0
    if not Action or D20S >= 15: 
            #if there is no appropriate trigger set or if RNG says to pick a new one. . .
            if Trigger != "masturbation" and "passive" in GirlA.Traits:
                    # This bypasses self-set if Rog*ue is told not to take initiative
                    $ Line = 0
                    return            
            call Girl_Self_Set(GirlA,Mode,Action) #Rog*ue_Self_Set(Mode, Action)
            
            if Mode == "T3": 
                    #Sets Action based on the result
                    $ Action = Trigger3
            else:
                    #if Mode == "T5"
                    $ Action = Trigger5  
            if not Action: 
                    return
            elif Action == "hand" and not Line: 
                        $ Line = "Also, " + GirlA.Name + " continues stroke your cock. "
            elif not Line:        
                        $ Line = "Also, " + GirlA.Name + " continues to masturbate. "      
    elif Action == "hand": 
                        $ Line = GirlA.Name + " continues stroke your cock. "
    else:        
                        $ Line = renpy.random.choice([GirlA.Name + " continues to masturbate. ", 
                                GirlA.Name + "'s hands move across her body. ",
                                GirlA.Name + " continues to feel herself. ",
                                GirlA.Name + " can't keep still. "]) 
            
    if Action == "hand": 
                        $ Line = Line + renpy.random.choice(["She lightly strokes the shaft, fingers sliding along the vein", 
                                "She grasps the shaft firmly, and slowly slides along its length", 
                                "She's becoming something of a handjob expert",
                                "Her expert strokes will have you boiling over in seconds",
                                "She strokes the shaft vigorously, lightly touching the tip",
                                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years",
                                "Her hand slides slowly down your shaft"]) 
                        $ TempFocus += 10 if Player.Focus > 60 else 4
                        $ TempFocus += 2 if GirlA.Hand > 2 else 0
                                
                        $ TempLustX += 2 if GirlA.Lust < 60 else 1
                        $ TempLustX += 2 if GirlA.Hand > 2 else 0
                        $ GirlA.Addict -= 1            
    else:
        if GirlA.Lust >= 80:   
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her mound, firmly stroking her clit", 
                                "She inserts two fingers into her dripping pussy and rapidly pistons them",
                                "She gasps as her fingers bury themselves deeply inside her",
                                "She gives a little squeal as she pinches her clit between her fingers",           
                                "She fingers move quickly across her mound, constantly sliding across her clit",
                                "She fingers move rapidly up and down her inner thighs and belly, building towards their center",
                                "She spreads her lower lips and furiously strokes the inner lining",
                                "She alternately dives her fingers into herself, and licks the juices off of them",
                                "She slides two fingers firmly in and out of her tight gap as she massages the clit with her palm",
                                "She rapidly circles her fingers against her erect clit",
                                "She quickly slides a finger up and down the crease of her pussy", 
                                "She lets out a moan as her fingers brush against her erect clit"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it", 
                                "She hungrily slams the dildo into her tight pussy, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping pussy",               
                                "She quickly slides the phallus up and down her crease"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand rapidly moves across her ass, firmly stroking her tight hole", 
                                "She inserts a finger deep into her grasping hole and rapidly pistons it",
                                "She gasps as she buries a finger deeply into her tight anus",
                                "She gives a little squeal as she pinches her clit between her fingers",           
                                "Her fingers move quickly across her ass, constantly sliding across her rim",
                                "Her fingers move rapidly up and down her inner thighs and ass, building towards their center",
                                "She spreads her cheeks and furiously strokes the puckered rim",
                                "She slides two fingers firmly in and out of her tight hole",
                                "She rapidly circles her fingers against the sensitive rim",
                                "She lets out a moan as her fingers brush against her quivering hole"])
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her ass, firmly rubbing into it", 
                                "She hungrily slams the dildo into her tight hole, and pistons it in and out",
                                "She shoves the dildo firmly in and out of her grasping asshole",               
                                "She quickly slides the phallus up and down the crease of her ass"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "She slides the buzzing egg into her dripping pussy and tugs it in and out",    
                                "She presses the vibrator firmly against her clit and a shiver runs through her",                
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She  spreads her lower lips and runs the device along the inner lining",
                                "She presses the toy deep into her and the vibrations send a shock through her body"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She passionately rubs her breasts, desperately tugging at her nipples",
                                "Her hands squeeze at her breasts, massaging them firmly with both hands",                 
                                "She hungrily cups her breasts and moves them in rapid circles",
                                "Her hands move constantly across her chest, alternately pulling at her nipples or just grazing her skin",
                                "She firmly pinches her nipples and gives them steady tugs",
                                "She passionately rubs her breasts, desperately tugging at her nipples"])     
        #End GirlA.Lust >= 80
        elif GirlA.Lust >= 50:   
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her mound, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly across her delta, occasionally grazing her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She gently slides a finger up and down the crease of her pussy", 
                                "She lets out a gasp as her fingers brush against her erect clit"])
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She moves the dildo in circles across her mound, firmly rubbing into it",  
                                "She traces the rubber phallus slowly down her body, barely grazing her mound",  
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",                
                                "She gently slides the phallus up and down the crease of her pussy", 
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand moves in circles across her ass, firmly rubbing into it", 
                                "Her hands move along her sides, carefully caressing them",                
                                "Her fingers move smoothly along her crack, occasionally grazing her asshole",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the tight hole within",
                                "She gently slides a finger up and down the crease of ass", 
                                "She lets out a gasp as her fingers brush against her puckered hole"]) 
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple",                  
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "Her hands firmly caress her breasts, massaging them in circular motions",
                                "Her hands move along her breasts, carefully caressing them",
                                "She gasps as her finger brushes against an erect nipple"])
        #End GirlA.Lust >= 50
        else: #if GirlA.Lust < 50:      
                if Action == "fondle pussy":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely grazing her mound", 
                                "Her fingers move lightly across her pubic region, subtly avoiding her lips",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "Her hands move along her sides, carefully caressing them"])  
                elif Action == "dildo pussy":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her mound",                 
                                "Her dildo slides lightly across her pubic region, subtly avoiding her lips",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "fondle ass":
                        $ Line = Line + renpy.random.choice(["Her hand traces slowly down her body, barely passing smoothly across her hips", 
                                "Her fingers move lightly across her crack, subtly avoiding her rosebud",
                                "Her fingers move up and down her inner thighs, slowly building towards their center",
                                "Her hands move along her sides, carefully caressing them"])              
                elif Action == "dildo anal":
                        $ Line = Line + renpy.random.choice(["She traces the rubber phallus slowly down her body, barely grazing her ass",                 
                                "Her dildo slides lightly across her crack, subtly avoiding the hole",
                                "Her dildo is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her cheeks and caresses the rim beneath",
                                "She drags the dildo slowly along her sides, carefully caressing them"])
                elif Action == "vibrator pussy":
                        $ Line = Line + renpy.random.choice(["She traces the buzzing ball slowly down her body, barely grazing her mound",                 
                                "Her vibrator slides lightly across her pubic region, subtly avoiding her lips",
                                "Her whirring toy is dragged up and down her inner thighs, slowly building towards their center",
                                "She slowly spreads her lower lips and caresses the inner lining",
                                "She drags the vibrator slowly along her sides, carefully caressing them"])
                else: # Action == "fondle breasts"
                        $ Line = Line + renpy.random.choice(["She gently rubs her breasts, dragging a finger across her nipple", 
                                "She gently cups her breasts and moves them in slow circles",
                                "She moves her hands from her breasts to rub her neck",
                                "She lightly pinches one of her nipples",
                                "She gasps as her finger brushes against an erect nipple"])   
                #End GirlA.Lust 0-60
        #End Girl's Action masturbation dialog        
                        
            
        # Girl's Self-stat boosts  
        $ TempLustX += 4 if GirlA.Lust > 80 else 0        
        $ TempLustX += 5 if GirlA.Lust < 40 else 3                      #Bonus if she is relatively low lust
        $ TempLustX += 5 if Trigger == "masturbation" and GirlA != Partner else 0            #Bonus if masturbation is her primary action
        
        if Partner != GirlA: 
            #If this is a primary, Trigger3 action
            $ TempLust = TempLustX
        else: 
            #If this is a Secondary, Trigger5 action
            $ TempLust2 = TempLustX
             
        $ TempFocus += 4 if Player.Focus < 50 else 3 
    #End Action all dialog     
    
    return
# end Self_Lines / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Girl_Self_Set / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Self_Set(GirlA=Primary, Mode = "T3", Action = Trigger3, Length=0, Count2=0, Options =[]): #nee Rog*ue_Self_Set(Mode = "T3", Action = Trigger3, Length=0, Count2=0, Options =[]): 
    #If T3/Trigger3 is sent, this is for Primary role, offhand behavior
    #If T5/Trigger5 is sent, this is for Secondary role, threesome masturbation behavior
    if Mode == "T3" and Trigger != "masturbation":
                # This cuts it out if she's submissive or not horny enough to get busy
                if "sub" in GirlA.Traits:
                    return
                    
                #if she's inexperienced or shy, skip this   
                if GirlA.SEXP >= 50 or ApprovalCheck(GirlA, 500, "I"):                    
                    if GirlA.Lust <= 30:
                        return
                elif GirlA.SEXP >= 25 or ApprovalCheck(GirlA, 300, "I"):
                    if GirlA.Lust <= 50:
                        return
                else:
                        return
    
    if Mode == "T3" and Trigger == "masturbation":
                #sets base options as masturbatory
                $ Options = ["fondle pussy", "fondle breasts", "fondle ass"]
                if "dildo" in GirlA.Inventory:
                        $ Options.append("dildo pussy")  
                        if GirlA.Loose:
                            $ Options.append("dildo anal")                  
                if "vibrator" in GirlA.Inventory:            
                        $ Options.append("vibrator pussy") 
            
    else:
                if GirlA.Hand >= 5 and Mode != "T5" and Trigger in ("fondle pussy", "fondle breasts", "fondle thighs", "kiss you", "fondle ass", "suck breasts"):
                        #if this is about the primary girl, and she's done handys, and you're feeling her up, she might feel you up
                        $ Options.append("hand")
                    
                if Trigger not in ("sex", "fondle pussy", "lick pussy", "dildo pussy"):
                        #if you aren't touching her pussy, she might
                        if "dildo" in GirlA.Inventory:
                                $ Options.append("dildo pussy")    
                        $ Options.append("fondle pussy") 
                
                if Trigger not in ("anal", "fondle ass", "insert ass", "lick ass", "dildo anal") and GirlA.Loose:
                        #if you aren't messing with her ass, she might
                        if "dildo" in GirlA.Inventory:
                                $ Options.append("dildo anal")
                        $ Options.append("fondle ass") 
                
                if "vibrator" in GirlA.Inventory:
                        $ Options.append("vibrator pussy")
                
                if Trigger not in ("fondle breasts", "suck breasts"):
                        #if you aren't dealing with her breasts. . .
                        $ Options.append("fondle breasts") 
                
                if GirlA.Obed < GirlA.Inbt:
                        #adds more options if she is not submissive
                        if "fondle pussy" not in Options:
                                $ Options.append("fondle pussy")                            
                        if "fondle ass" not in Options:
                                $ Options.append("fondle ass")                            
                        if "fondle breasts" not in Options:
                                $ Options.append("fondle breasts")
    # End filling options
    
    $ Length = len(Options)-1
    $ D20 = renpy.random.randint(1, 20)    
    if D20 >=18:
            $ Count2 = 0
    elif D20 >= 15:
            $ Count2 = 1
    elif D20 >= 12:
            $ Count2 = 2
    elif D20 >= 10:
            $ Count2 = 3
    else:        
            $ Count2 = renpy.random.randint(0, Length)
            
    $ Count2 = Length if Count2 > Length else Count2
    if Action != Options[Count2]: 
            #If the action has changed, play change dialog
            $ Action = Options[Count2] #Sets Action to the selected Option
            if Action == "hand": 
                    $ Line = GirlA.Name + " slides her hand down and firmly grabs your dick. "   
                    $ Approval = 3
            elif Action == "fondle pussy":
                    $ Line = GirlA.Name + "'s hand slides down and begins to stroke her pussy. "
            elif Action == "dildo pussy":
                    $ Line = GirlA.Name + " pulls out her dildo and draws it toward her pussy. " 
            elif Action == "fondle ass":
                    $ Line = GirlA.Name + "'s hand slides behind her body, reaching toward her ass. " 
            elif Action == "dildo anal":
                    $ Line = GirlA.Name + " pulls out her dildo and reaches it behind her. "
            elif Action == "vibrator pussy":
                    $ Line = GirlA.Name + " pulls out her vibrator and strokes it across her body. "      
            else: # Action == "fondle breasts"
                    $ Line = GirlA.Name + "'s hands slide up her body and begin to kneed her breasts. "
    elif Action == "hand": 
            $ Line = "Also, " + GirlA.Name + " continues stroke your cock. "
    else:        
            $ Line = "Also, " + GirlA.Name + " continues to masturbate. "
            
    if Mode == "T3": #Sets Action based on the result
        $ Trigger3 = Action
    else:
        $ Trigger5 = Action                            
            
    return

# end self-set / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Threeway Dialog / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label SexDialog_Threeway(GirlA = Secondary, Mode = 0, Action = 0, GirlB = Primary, TempLine = 0, TempLust = 0, TempLust2 = 0, TempFocus = 0): #nee Rog*ue_SexDialog_Threeway(Mode = 0, Action = 0, 
    # This is the dialog checked for Trigger 4, activated when GirlA is the second girl in a scene, or for Lesbian activities.
    # if Mode is "lesbian" then it means she's doing a girl/girl sequence, and activating secondary dialogs.
    # By default, GirlB will be the primary and this sequence will build text for what the secondary girl does.
    # In "lesbian" mode, GirlB will be the secondary girl, and this sequence will build text for what the primary will do to her.
    # Lesbian Trigger1 dialog calls "call SexDialog_Threeway(RogueX,"lesbian")" #nee "call Rog*ue_SexDialog_Threeway("lesbian")"
    
    call Threeway_Set(GirlA,Mode=Mode,GirlB=GirlB) #nee Rog*ue_Threeway_Set(Mode=Mode)   #Picks a new activty on a 7-9 roll or when not set, otherwise returns
    
    if Mode == "lesbian":
            $ Action = Trigger3
            $ GirlB = Secondary  
    else:
            $ Action = Trigger4
            
    if Line:        
            #if it picked something, it should have set a line and returned
            return  
    elif not Action:
            $ Action = "watch"
            
    if Action == "hand":
                    if D20S <= 8 and (Trigger == "blow" or Trigger == "hand"): #This is a random bonus dialog
                        if Trigger == "blow": #If Kitty is blowing you                                    
                            $ Line = renpy.random.choice([GirlA.Name + "'s fingers brush against " + GirlB.Name + "'s lips as they work",
                                    GirlA.Name + " and " + GirlB.Name + " pause for a second to briefly kiss", 
                                    GirlA.Name + " takes a turn to suck on the head before passing it back",
                                    GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"]) 
                        elif Trigger == "hand":  #If Kitty is handying you
                            $ Line = renpy.random.choice([GirlA.Name + "'s fingers brush against " + GirlB.Name + "'s as they work",
                                    GirlA.Name + " strokes " + GirlB.Name + "'s palm as she works", 
                                    GirlA.Name + " takes a turn to stroke a few times before passing it back",
                                    GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"])   
                    else:                
                        if Trigger == "hand": #if another girl is also handy
                                $ Line = GirlA.Name + " also continues to stroke your cock"
                        else: #if the other girl is doing something else
                                $ Line = GirlA.Name + " continues stroke your cock" 
                                
                        $ Line = Line + renpy.random.choice([", lightly stroking the shaft, fingers sliding along the vein", 
                                ", grasping the shaft firmly, and slowly sliding along its length", 
                                ", making up for years of lost time",
                                ", her expert strokes will have you boiling over in seconds",
                                ", stroking the shaft vigorously, lightly touching the tip",
                                ", moving very smoothly, stroking casually",
                                ", hand sliding slowly down your shaft"]) 
                    $ TempFocus += 3 if Player.Focus > 70 else 2
                          
                    $ TempLust += 2 if GirlA.Lust < 60 else 0
                    $ TempLust += 2 if GirlA.Hand > 2 else 0
                    $ GirlA.Addict -= 1 if D20S > 10 else 2
                    
    # end GirlA.Hand Threeway                                //////////////////////////////////////////////////////////////////////////////
                             
    elif Action == "blow":
                    if Speed > 2 and Trigger == "blow":
                        $ Line = "Since " + GirlB.Name + " is working so hard, " + GirlA.Name + " settles for the occasional nibble or lick."
                        $ TempFocus += 5 if Player.Focus > 60 else 3                      
                        $ TempLust += 2 if GirlA.Lust > 80 else 1    
                    else:
                        if D20S <= 8 and (Trigger == "blow" or Trigger == "hand"): #This is a random bonus dialog
                            if Trigger == "blow": #If Kitty is blowing you
                                $ Line = renpy.random.choice([GirlA.Name + "'s tongue brushes against " + GirlB.Name + "'s as they work",
                                        GirlA.Name + " and " + GirlB.Name + " pause for a second to briefly kiss", 
                                        GirlA.Name + " takes a turn to suck on the head before passing it back",
                                        GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"]) 
                            elif Trigger == "hand": #If Kitty is handying you
                                $ Line = renpy.random.choice([GirlA.Name + "'s tongue brushes against " + GirlB.Name + "'s hand as they work",
                                        GirlA.Name + " licks " + GirlB.Name + "'s palm as she works", 
                                        GirlA.Name + " takes a turn to stroke a few times before passing it back",
                                        GirlA.Name + " and " + GirlB.Name + " get into an alternating rhythm"])  
                            $ TempLust2 += 1 if GirlB.GirlLikeCheck(GirlA) >= 800 else 0                
                        else:
                            if Trigger == "blow": #if another girl is also blowing
                                    $ Line = GirlA.Name + " also continues to lick your cock"
                            else: #if the other girl is doing something else
                                    $ Line = "Also, " + GirlA.Name + " continues lick your cock"     
                            
                            $ Line = Line + renpy.random.choice([", settling into a gentle licking pace along the base",
                                    ", licking gently up and down the shaft", 
                                    ", her tongue moves carefully along the shaft",
                                    ", really starting to learn some clever tricks to making you feel good",
                                    ", licking her way down the shaft, and gently teasing the balls"]) 
                        
                        $ TempFocus += 20 if Player.Focus > 60 else 10                      
                        $ TempLust += 2 if GirlA.Lust > 80 else 1    
                              
                        $ GirlA.Addict -= 2
    # end GirlA.Blowjob Threeway                                //////////////////////////////////////////////////////////////////////////////
            
    elif Action == "fondle breasts":    
                        if Trigger2 == "fondle breasts" and Trigger != "lesbian": #if you're also fondling them,
                            $ Line = GirlA.Name + " also continues to fondle " + GirlB.Name + "'s breasts" 
                        else:
                            $ Line = GirlA.Name + " continues to fondle " + GirlB.Name + "'s breasts" 
                            
                        $ Line = Line + renpy.random.choice([", giving little tugs to her nipples", 
                                        ", cupping them firmly with both hands",                 
                                        ", gently moving them in slowly increasing circles",
                                        ", then moves her hands from her breasts to rub her neck",
                                        ", firmly pinching her nipples and giving them a tug",
                                        ", passing repeatedly against her rigid nipples"])  
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1 
    # end Fondle breasts Threeway                                //////////////////////////////////////////////////////////////////////////////
    
    
    elif Action == "suck breasts":  
                        if Trigger2 == "fondle breasts" and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to suck " + GirlB.Name + "'s breasts" 
                        else:
                                $ Line = GirlA.Name + " continues to suck " + GirlB.Name + "'s breasts" 
                            
                        $ Line = Line + renpy.random.choice([", giving little tugs to her nipple", 
                                        ", cupping them firmly with both hands",               
                                        ", then moves her hands down along her side",
                                        ", licking slowly up her chest",
                                        ", firmly nibbling her nipples and giving them a tug",
                                        ", nibbling repeatedly at her rigid nipples"])  
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 4 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1                      
    # end Suck breasts Threeway                                //////////////////////////////////////////////////////////////////////////////
        
     
    elif Action == "fondle pussy":
                        if (Trigger == "fondle pussy" or Trigger2 == "fondle pussy") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to fondle " + GirlB.Name + "'s pussy" 
                                $ Templine = renpy.random.choice([", stroking across her clit",   
                                        ", the two of you taking turns in your motions",              
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing against it vigorously",
                                        ", stroking into it vigorously",
                                        ", pressing firmly into it",
                                        ", sliding firmly into it",
                                        ", moving inside it with slow undulating motions",
                                        ", moving with slow undulating motions"])  
                        else:    
                                $ Line = GirlA.Name + " continues to fondle " + GirlB.Name + "'s pussy" 
                                $ Templine = renpy.random.choice([", running fingers gently up her cleft", 
                                        ", stroking across her clit",                 
                                        ", taking a little taste of the warm juices on her finger",
                                        ", rubbing against it vigorously",
                                        "a",
                                        "b",
                                        "c",
                                        ", moving with slow undulating motions"])  
                            
                                #a, b, and c can change depending on other circumstances at the time. 
                                if Templine == "a":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brush against your cock as it goes in" 
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", your tongue slides past her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brush against the dildo as it goes in" 
                                    else:
                                            $ Templine = ", stroking into it vigorously"
                                elif Templine == "b":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brushing up against your balls as you sink in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", you briefly suck on one of her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ Templine = ", sliding firmly into it"
                                elif Templine == "c":
                                    if Trigger == "sex" or Trigger == "anal":
                                            $ Templine = ", her fingers brush against your cock as it goes in"
                                    elif Trigger == "lick pussy":
                                            $ Templine = ", your tongue slides along her fingers"
                                    elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                            $ Templine = ", her fingers brushing up against the dildo as it slides by"
                                    else:
                                            $ Templine = ", moving inside it with slow undulating motions"
                                #End if the other girl is not fondling
                        $ Line = Line + Templine
                            
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 3
                        $ TempFocus += 1  
        
    # end fondle pussy Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    
    elif Action == "lick pussy":
                        if (Trigger == "lick pussy" or Trigger2 == "lick  pussy") and Trigger != "lesbian": #if you're also fondling them,
                            $ Line = GirlA.Name + " also continues to lick " + GirlB.Name + "'s pussy" 
                        else:    
                            $ Line = GirlA.Name + " continues to lick " + GirlB.Name + "'s pussy" 
                            
                        $ Templine = renpy.random.choice([", running her tongue gently up her cleft", 
                                    ", stroking across her clit",                 
                                    ", taking a little taste of the warm juices flowing out",
                                    ", lapping against it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])  
                        
                        #a, b, and c can change depending on other circumstances at the time. 
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in" 
                                elif Trigger == "lick pussy":
                                        $ Templine = ", her tongue brushing against yours as you work"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides along your fingers" 
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue brushes along the dildo as it goes in" 
                                else:
                                        $ Templine = ", lapping into it vigorously"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her longue lapping against your balls as you sink in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", you briefly kiss as you take turns"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick pussy":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "fondle pussy" or Trigger2 == "fondle pussy":
                                        $ Templine = ", her tongue slides past your fingers" 
                                elif Trigger == "dildo pussy" or Trigger2 == "dildo pussy":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"
                           
                        $ Line = Line + Templine
                                                    
                        $ TempLust += 3 if ApprovalCheck(GirlA, 600, "I") else 1  # GirlA's lust
                        $ TempLust2 += 7 if GirlB.GirlLikeCheck(GirlA) >= 800 else 4
                        $ TempFocus += 3  
        
    # end lick pussy Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "fondle ass":
                        if Trigger2 == "fondle ass" and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to fondle " + GirlB.Name + "'s ass" 
                                $ Line = Line + renpy.random.choice([", stroking across her rear",   
                                        ", the two of you taking turns in your motions",              
                                        ", her fingers brushing against yours as you work",
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"])  
                        else:
                                $ Line = GirlA.Name + " continues to fondle " + GirlB.Name + "'s ass" 
                                $ Line = Line + renpy.random.choice([", running fingers gently up her cleft", 
                                        ", stroking across her rear",                 
                                        ", rubbing it vigorously",
                                        ", squeezing it vigorously",
                                        ", pressing firmly into it",
                                        ", kneeding it with slow undulating motions",
                                        ", moving with slow undulating motions"]) 
                                                    
                        $ TempLust += 1 if ApprovalCheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ TempLust2 += 3 if GirlB.GirlLikeCheck(GirlA) >= 800 else 1
                        $ TempFocus += 1  
    # end fondle ass Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    
    elif Action == "insert ass":
                        if (Trigger == "insert ass" or Trigger2 == "insert ass") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to stroke " + GirlB.Name + "'s ass" 
                        else:    
                                $ Line = GirlA.Name + " continues to stroke " + GirlB.Name + "'s ass" 
                            
                        $ Templine = renpy.random.choice([", stroking across her rim",  
                                    ", stroking across her hole",                 
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])  
                        
                        #a, b, and c can change depending on other circumstances at the time. 
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brush against your cock as it goes in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her fingers circling yours" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers brush against the dildo as it goes in" 
                                else:
                                        $ Templine = ", running fingers gently up her cleft"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brushing up against your balls as you sink in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", the two of you taking turns in your motions"     
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers run along the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her fingers brush against your cock as it goes in"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her fingers intertwine yours" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her fingers brush against the dildo as it goes in" 
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"
                           
                        $ Line = Line + Templine
                        
                        if not GirlB.Loose:
                                        $ TempLust2 -= 3
                        $ TempLust += 2 if ApprovalCheck(GirlA, 700, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 3
                        $ TempFocus += 1  
        
    # end insert ass Threeway                             /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "lick ass":
                        if (Trigger == "lick ass" or Trigger2 == "lick ass") and Trigger != "lesbian": #if you're also fondling them,
                                $ Line = GirlA.Name + " also continues to lick " + GirlB.Name + "'s ass" 
                        else:    
                                $ Line = GirlA.Name + " continues to lick " + GirlB.Name + "'s ass" 
                            
                        $ Templine = renpy.random.choice([", tonguing across her rim", 
                                    ", stroking across her hole",
                                    ", circling it vigorously",
                                    "a",
                                    "b",
                                    "c",
                                    ", moving with slow undulating motions"])  
                        
                        #a, b, and c can change depending on other circumstances at the time. 
                        if Templine == "a":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in" 
                                elif Trigger == "lick ass":
                                        $ Templine = ", her tongue brushing against yours as you work"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides along your fingers" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue brushes along the dildo as it goes in" 
                                else:
                                        $ Templine = ", lapping into it vigorously"
                        elif Templine == "b":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her longue lapping against your balls as you sink in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", you briefly kiss as you take turns"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides past your fingers"
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", sliding firmly into it"
                        elif Templine == "c":
                                if Trigger == "sex" or Trigger == "anal":
                                        $ Templine = ", her tongue brushes against your cock as it goes in"
                                elif Trigger == "lick ass":
                                        $ Templine = ", the two of you taking turns in your motions"
                                elif Trigger == "insert ass" or Trigger2 == "insert ass":
                                        $ Templine = ", her tongue slides past your fingers" 
                                elif Trigger == "dildo anal" or Trigger2 == "dildo anal":
                                        $ Templine = ", her tongue runs up against the dildo as it slides by"
                                else:
                                        $ Templine = ", moving inside it with slow undulating motions"
                           
                        $ Line = Line + Templine 
                            
                        $ TempLust += 3 if ApprovalCheck(GirlA, 800, "I") else 1  # GirlA's lust
                        $ TempLust2 += 4 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 3  
        
    # end lick ass Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "masturbation":            
                        call Girl_Self_Lines(GirlA,"T5",Trigger5)  #nee Rog*ue_Self_Lines
                        $ TempLust = 0
                
    # end Masturbation Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action in ("kiss you", "kiss girl", "kiss both"):
                        if Trigger == "blow" and GirlA.Blow > 5 and Trigger4 == "kiss girl":
                                    $ Line = GirlA.Name + " also continues to kiss " + GirlB.Name
                                    $ Line = Line + renpy.random.choice([", occasionally taking a lick of your cock as well", 
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", taking the occasional lick down your shaft",
                                            ", nudging her aside to kiss the head of your cock"])
                        elif Trigger == "blow" and Trigger4 == "kiss girl":
                                    $ Line = GirlA.Name + " also continues to kiss " + GirlB.Name
                                    $ Line = Line + renpy.random.choice([", occasionally bumping into your cock as well", 
                                            ", licking along her cheek",
                                            ", nudging you out of her mouth to get a deep kiss in",
                                            ", trailing kisses down her neck"])
                        else: #they're just kissing
                                    if Action == "kiss girl" or Mode == "lesbian":
                                        if Trigger == "lesbian" and Partner != GirlA:
                                                $ Line = GirlA.Name + " continues to make out with " + GirlB.Name
                                        else:                                            
                                                $ Line = GirlA.Name + " also continues to make out with " + GirlB.Name
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air", 
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])
                                    elif Action == "kiss you":
                                        $ Line = GirlA.Name + " also continues to make out with you" 
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air", 
                                                ", licking along your cheek",
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", occasionally nibbling at your ears",
                                                ", trailing kisses down your neck"])
                                    else: #Action == "kiss both":
                                        $ Line = GirlA.Name + " also continues to make out with both of you"
                                        $ Line = Line + renpy.random.choice([", occasionally coming up for air", 
                                                ", licking along your cheek",
                                                ", occasionally nibbling your lip as well", 
                                                ", nudging you aside to get a deep kiss in",
                                                ", all three of your tongues swirling",
                                                ", nudging her aside to give you a deep kiss"
                                                ", grabbing your face in both hands",
                                                ", your tongues swirl around each other",
                                                ", licking along her cheek",
                                                ", grabbing her face in both hands",
                                                ", their tongues swirl around each other",
                                                ", occasionally nibbling at her ears",
                                                ", trailing kisses down her neck"])                                                
                        $ TempLust += 1 if ApprovalCheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 800 else 0
                        $ TempLust2 += 2 if GirlB.GirlLikeCheck(GirlA) >= 800 else 1 
                        $ TempFocus += 1  
    # end Kissing Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    elif Action == "watch":
                        $ Line = GirlA.Name + " continues to watch the two of you" 
                        $ Line = Line + renpy.random.choice([", shifting uncomfortably", 
                                        ", readjusting her clothes",                 
                                        ", glancing at the door",               
                                        ", taking in " + GirlB.Name + "'s body",
                                        ", transfixed by the action"]) 
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 600 else 0  # GirlA's lust
                        $ TempLust += 2 if GirlA.GirlLikeCheck(GirlB) >= 800 else 1  # GirlA's lust
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 500, "I") else 0
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 700, "I") else 0                        
                        $ TempFocus += 1  
    # end watching Threeway                              /////////////////////////////////////////////////////////////////////////////
    
    else:
        "Nothing triggered. 1:[Trigger], 2:[Trigger2], 3:[Trigger3], 4:[Trigger4], 5:[Trigger5]" #diagnostic
    
    # Wrap-up
    $ TempLust2 += 2
    if Mode == "lesbian":        
            $ PrimaryLust += (TempLust * 3)
            $ SecondaryLust += (TempLust2 * 3)
    else:
            $ SecondaryLust += TempLust
            $ PrimaryLust += TempLust2
        
    $ Player.Focus += TempFocus
    return
    
    
#end SexDialog_Threeway  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Start Threesome activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Three_Change(LeadGirl = Primary, SecondGirl = Partner, D20S=0, PrimaryLust=0, SecondaryLust=0):
        #this is called when the player wants to change over a threeway behavior, and revolves around the partner girl
        # if changes what the Partner does to the lead girl
        # for Threeway secondary activity: #nee Rogue_Threeway_Set("preset", 0, Trigger4, "ActiveGirl")  
        # call Three_Change(Primary,Partner)
        # call Threeway_Set(KittyX,"preset",0,Trigger4,RogueX)         
        if LeadGirl not in TotalGirls:
                return
        if Partner == LeadGirl:
                "Let Oni know that both roles are set to [Girl.Name]."
                return             
        menu Three_Change_Menu:
            ch_p "Hey [Partner.Name]. . ." 
            "about [LeadGirl.Name]. . .": #about the primary girl. . .
                menu:
                    ch_p "about [LeadGirl.Name]. . ."
                    "why don't you kiss her?" if Trigger5 != "kiss girl" and Trigger5 != "kiss both":
                                    call Threeway_Set(SecondGirl,"kiss girl", 0, Trigger4, LeadGirl)                            
                    "why don't you grab her tits?" if Trigger4 != "fondle breasts":
                                    call Threeway_Set(SecondGirl,"fondle breasts",0, Trigger4, LeadGirl)                    
                    "why don't you suck her breasts?" if Trigger4 != "suck breasts":
                                    call Threeway_Set(SecondGirl,"suck breasts",0, Trigger4, LeadGirl)                            
                    "why don't you finger her?" if Trigger4 != "fondle pussy":
                                    call Threeway_Set(SecondGirl,"fondle pussy",0, Trigger4, LeadGirl)                            
                    "why don't you go down on her?" if Trigger4 != "lick pussy":
                                    call Threeway_Set(SecondGirl,"lick pussy", 0, Trigger4, LeadGirl)                            
                    "why don't you grab her ass?" if Trigger4 != "fondle ass":
                                    call Threeway_Set(SecondGirl,"fondle ass", 0, Trigger4, LeadGirl)                            
                    "why don't you lick her ass?" if Trigger4 != "lick ass":
                                    call Threeway_Set(SecondGirl,"lick ass", 0, Trigger4, LeadGirl)
                    "wait, I meant. . .":
                                    jump Three_Change_Menu
                    
            "about me. . .":
                menu:
                    ch_p "about me. . ."
                    "why don't you kiss me?" if Trigger5 != "kiss you" and Trigger5 != "kiss both":
                                    call Threeway_Set(SecondGirl,"kiss you", 0, Trigger4, LeadGirl)                            
                    "maybe take me in hand?" if Trigger4 != "hand":
                                    call Threeway_Set(SecondGirl,"hand", 0, Trigger4, LeadGirl)                            
                    "maybe give me a lick?" if Trigger4 != "blow":
                                    call Threeway_Set(SecondGirl,"blow", 0, Trigger4, LeadGirl)                           
                    "why don't you give me a show?" if Trigger4 != "masturbation":
                                    call Threeway_Set(SecondGirl,"masturbation", 0, Trigger4, LeadGirl)
                    "wait, I meant. . .":
                                    jump Three_Change_Menu
            "never mind.":
                pass
        return
        
# End Threesome activity change  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Threeway-set  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Threeway_Set(GirlA=Secondary,Preset = 0, Mode = 0, Action = Trigger4, GirlB = Primary, State = "watcher", TempLust = 0, TempLust2 = 0, TempFocus = 0): #nee Rog*ue_Threeway_Set(Preset = 0, Mode = 0,
            # Action defaults to Trigger4, the action of the seondary girl and GirlB to the lead girl in the scene
            # In lesbian mode, Action becomes Trigger3, the secondary action of the primary girl, and GirlB is the secondary girl
            # If Set gets passed a preset, it chooses that preset, otherwise it chooses one randomly
            # for Lesbian: call Threeway_Set(Primary,"suck breasts", "lesbian", Trigger3,Secondary)
            # for Threeway: call Threeway_Set(SecondGirl,"fondle breasts",0, Trigger4, LeadGirl)  
            # ThreeCount is a value that gets set to a few digits lower then the current Round
            # The girl will not arbitrarily change motions until after this value has been passed.
            
            $ D20 = renpy.random.randint(1, 20)
            if not Preset: 
                    #if no preset is offered
                    if Mode == "lesbian": #called from Les_Change()
                            #If it's in lesbian mode, there is already a trigger set, and the roll is good, continue
                            if Trigger3 == "kiss girl" and GirlA.Lust <= 20 and GirlA.Org < 1:
                                    # If kissing at low lust, keep doing it
                                    return
                            elif Trigger3 and ThreeCount <= Round:
                                    # If a Trigger3 is already set and it's under the count, return
                                    return
                    elif Trigger4 and D20 < 15 and Trigger4 != "watch": 
                                    #If there is a trigger, it's not set to "watch," and the roll is good, continue
                                    return
                    elif Trigger4 and ThreeCount <= Round:
                                    # if there's not a Preset, and it's only been X turns since the last change, return.
                                    return
            $ Options = ["watch", "masturbation", "masturbation", "masturbation"]
                        
            if Trigger == "lesbian":
                    # if this was sent from a Lesbian action. . .
                    $ State = "lesbian"
                    if GirlA == GirlB and GirlA != Partner:
                            $ GirlB = Partner
                    elif GirlA == GirlB and GirlA != Primary:
                            $ GirlB = Primary
                    if GirlA == GirlB:
                            "Tell Oni that in Threeway_Set, A:[GirlA.Tag] and B:[GirlB.Tag]"
                            "[Girl.Gibberish]"
                    $ Options = ["kiss girl","kiss girl"]        
                    if Preset in ("hand","blow","kiss you","kiss both"):
                            #if you send it presets that you want the other girl to touch you. . .
                            $ State = "threeway"   
                    elif Preset:
                            pass
                    elif GirlA.GirlLikeCheck(GirlB) >= 600 and ApprovalCheck(GirlA, 500, "I"):
                            #if she likes the other girl, and is unihibited. . .
                            pass
                    else:
                            #this returns if she doesn't like the other girl enough to do anything more.
                            if Action != "kiss girl":                                
                                    $ Line = GirlA.Name + " gives " + GirlB.Name + " a passionate kiss"
                                    $ Action = "kiss girl" 
                                    $ Trigger3 = "kiss girl" 
                                    if "lesbian" not in GirlA.RecentActions:
                                            $ GirlA.Les += 1
                                            $ GirlA.RecentActions.append("lesbian")    
                            return
            elif not ApprovalCheck(GirlA, 500, "I"): 
                    # If GirlA is too timid to do anything, stick to neutral options
                    pass            
            elif GirlA.GirlLikeCheck(GirlB) >= 600 and ApprovalCheck(GirlA, (1500-(10*GirlA.Les)-(10*(GirlA.GirlLikeCheck(GirlB)-60)))): 
                    #If she likes both of you a lot, threeway
                    $ State = "threeway"
            elif ApprovalCheck(GirlA, 1000): 
                    #If she likes you well enough, Hetero
                    $ State = "hetero"            
            elif GirlA.GirlLikeCheck(GirlB) >= 700: 
                    #if she doesn't like you but likes the other girl, lesbian
                    $ State = "lesbian"
                    
            if State == "lesbian" or State == "threeway":  
                #if she's into girls, add girl-touching options
                $ Options.extend(("fondle breasts","suck breasts","fondle pussy","fondle ass","kiss girl")) 
                
                if ApprovalCheck(GirlA, 800, "I") or GirlA.GirlLikeCheck(GirlB) >= 800:
                    $ Options.append("lick pussy")
                if ApprovalCheck(GirlA, 900, "I") and GirlA.GirlLikeCheck(GirlB) >= 900:
                    $ Options.append("lick ass") 
#                if "dildo" in GirlA.Inventory: #add later once these systems are done
#                    $ Options.append("dildo pussy") 
#                    if GirlA.Loose:
#                        $ Options.append("dildo ass") 
#                if "vibrator" in GirlA.Inventory:
#                    $ Options.append("vibrator") 
                    
            if State == "hetero" or State == "threeway":
                #if she's into you, add you-touching options
                if Trigger == "anal":
                    $ Options.extend(("hand","kiss you","kiss you"))   
                else:
                    $ Options.extend(("hand","blow","kiss you"))                 
            $ renpy.random.shuffle(Options)
            
            if Preset:
                if Preset in Options:
                        #if the suggested action is in the possible actions. . .
                        $ Options[0] = Preset
                        if GirlA == RogueX: 
                                ch_r "Ok, that seems fine. . ."
                        elif GirlA == KittyX:     
                                ch_k "Oh, ok. . ."              
                        elif GirlA == EmmaX:  
                                ch_e "Oh, very well. . ."               
                        elif GirlA == LauraX: 
                                ch_l "Ok, that seems legit. . ."
                elif ApprovalCheck(GirlA, 750, "I") or ApprovalCheck(GirlA, 1500):
                        #if the suggestion is not in the options, but she's game anyway
                        $ Options[0] = Preset 
                        if GirlA == RogueX: 
                                ch_r "I guess I could. . ."  
                        elif GirlA == KittyX:     
                                ch_k "If that's what you want, I could give it a try. . ."      
                        elif GirlA == EmmaX:    
                                ch_e "I suppose it's worth a try. . ."             
                        elif GirlA == LauraX: 
                                ch_l "Worth a shot. . ."  
                else:
                        #she refuses
                        if GirlA == RogueX: 
                                ch_r "I don't really feel like doing that one. . ."
                        elif GirlA == KittyX:       
                                ch_k "That doesn't seem as fun. . ."        
                        elif GirlA == EmmaX:    
                                ch_e "That doesn't really seem appropriate. . ."             
                        elif GirlA == LauraX: 
                                ch_l "Nah, not my style. . ."
            #Sets opening lines. . .
            if Options[0] == Action:                          
                    #If it's the same result, just hop back
                    return
            elif Mode == "lesbian":
                    $ Line = GirlA.Name + " shifts her position"
            elif not Trigger4 or Trigger4 == "masturbation":    
                    #If this is the first action,
                    $ Line = GirlA.Name + " moves closer"            
            else:                                              
                    #If this is a new action
                    $ Line = GirlA.Name + " shifts her position"
                    
                    
            if Options[0] == "masturbation":
                        $ Action = "masturbation"  
                        call Girl_Self_Lines(GirlA,"T5",Trigger5)  #nee Rog*ue_Self_Lines
            elif Options[0] == "hand":
                        call Seen_First_Peen(GirlA,GirlB,React=1)
                        $ Line = Line + " before she slides her hand down and firmly grabs your dick"
                        $ Action = "hand"
                        if GirlA == RogueX:
                                show Rogue_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        elif GirlA == KittyX:
                                show Kitty_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        elif GirlA == EmmaX:
                                show Emma_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        elif GirlA == LauraX:
                                show Laura_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        $ Approval = 4                        
                        $ TempFocus += 3 if Player.Focus > 70 else 2                              
                        $ TempLust += 2 if GirlA.Lust < 60 else 0
                        $ TempLust += 2 if GirlA.Hand > 2 else 0
                        $ GirlA.Addict -= 1 if D20 > 10 else 2
            elif Options[0] == "blow":
                        call Seen_First_Peen(GirlA,GirlB,React=1)
                        $ Line = Line + " before she slides down and begins to slowly lick your cock"
                        if GirlA == RogueX:
                                show Rogue_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        elif GirlA == KittyX:
                                show Kitty_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        elif GirlA == EmmaX:
                                show Emma_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        elif GirlA == LauraX:
                                show Laura_Sprite zorder GirlA.Layer:
                                        ease 1 ypos 200 
                        $ Action = "blow"     
                        $ Approval = 4
                        
                        $ TempFocus += 20 if Player.Focus > 60 else 10                      
                        $ TempLust += 2 if GirlA.Lust > 80 else 1  
                        $ GirlA.Addict -= 2
            #the above three do not apply to lesbian actions.
                        
            elif Options[0] == "fondle breasts":
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slides her hands along " + GirlB.Name + "'s breasts" 
                        $ Action = "fondle breasts"   
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian") 
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian") 
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 4 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1 
            elif Options[0] == "suck breasts":
#                        call RThreewayBreasts_Launch #Launches position change
                        $ Line = Line + " and slurps " + GirlB.Name + "'s nipple into her mouth" 
                        $ Action = "suck breasts"    
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian") 
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian") 
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 2
                        $ TempFocus += 1  
            elif Options[0] == "fondle pussy":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her finger along " + GirlB.Name + "'s pussy" 
                        $ Action = "fondle pussy"  
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian") 
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")                  
                        $ TempLust += 2 if ApprovalCheck(GirlA, 500, "I") else 1  # GirlA's lust
                        $ TempLust2 += 5 if GirlB.GirlLikeCheck(GirlA) >= 800 else 3
                        $ TempFocus += 2  
            elif Options[0] == "lick pussy":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and runs her tongue along " + GirlB.Name + "'s pussy" 
                        $ Action = "lick pussy"  
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian") 
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian") 
                        $ TempLust += 3 if ApprovalCheck(GirlA, 600, "I") else 1  # GirlA's lust
                        $ TempLust2 += 8 if GirlB.GirlLikeCheck(GirlA) >= 800 else 5
                        $ TempFocus += 3  
            elif Options[0] == "fondle ass": 
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and gives " + GirlB.Name + "'s ass a firm squeeze" 
                        $ Action = "fondle ass" 
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian") 
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")                
                        $ TempLust += 1 if ApprovalCheck(GirlA, 400, "I") else 0  # GirlA's lust
                        $ TempLust2 += 3 if GirlB.GirlLikeCheck(GirlA) >= 600 else 2
                        $ TempFocus += 1  
            elif Options[0] == "lick ass":
#                        call RThreewayPussy_Launch #Launches position change
                        $ Line = Line + " and starts to lick around " + GirlB.Name + "'s ass" 
                        $ Action = "lick ass"  
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian") 
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian") 
                        $ TempLust += 3 if ApprovalCheck(GirlA, 800, "I") else 1  # GirlA's lust
                        $ TempLust2 += 6 if GirlB.GirlLikeCheck(GirlA) >= 800 else 4
                        $ TempFocus += 2  
                        
            elif Options[0] == "kiss girl" or Mode == "lesbian":                               
                        $ Line = Line + " and gives " + GirlB.Name + " a passionate kiss"
                        $ Action = "kiss girl"
                        if Mode != "lesbian" and "kiss you" in Options:
                                if Trigger == "kiss you":
                                        $ Action = "kiss both"                        
                                elif Trigger3 == "kiss you":
                                        $ Action = "kiss both"           
                                elif Trigger4 == "kiss you":
                                        $ Action = "kiss both" 
                        $ TempFocus += 1  
            elif Options[0] == "kiss you":   
                        $ Line = Line + " and gives you a passionate kiss"
                        $ Action = "kiss you"  
                        if "kiss girl" in Options: 
                                if Trigger == "kiss you":
                                        $ Action = "kiss both"                         
                                elif Trigger3 == "kiss you":
                                        $ Action = "kiss both"           
                                elif Trigger4 == "kiss you":
                                        $ Action = "kiss both" 
                        $ TempLust += 1 
                        $ TempFocus += 1 
                        
#            elif Options[0] == "dildo pussy":  
#            elif Options[0] == "dildo ass":        
#            elif Options[0] == "vibrator":    

            else:
                        $ Line = GirlA.Name + " is just watching the two of you intently"
                        $ Action = "watch"
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 600 else 0  # GirlA's lust
                        $ TempLust += 2 if GirlA.GirlLikeCheck(GirlB) >= 800 else 1  # GirlA's lust
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 500, "I") else 0
                        $ TempLust2 += 1 if ApprovalCheck(GirlB, 700, "I") else 0
                        $ TempFocus += 1 
            
            if Action == "kiss girl" or Action == "kiss both":
                        #If there's a semi-lesbian make-out. . .
                        if "lesbian" not in GirlA.RecentActions:
                                $ GirlA.Les += 1
                                $ GirlA.RecentActions.append("lesbian")  
                        if "lesbian" not in GirlB.RecentActions:
                                $ GirlB.Les += 1
                                $ GirlB.RecentActions.append("lesbian")            
                        $ TempLust += 1 if ApprovalCheck(GirlA, 500, "I") else 0  # GirlA's lust
                        $ TempLust += 1 if GirlA.GirlLikeCheck(GirlB) >= 800 else 0
                        $ TempLust2 += 2 if GirlB.GirlLikeCheck(GirlA) >= 800 else 1
                        $ TempFocus += 1 
                                
            # Wrap-up
            if Preset:
                    $ ThreeCount = Round - 2
            else: 
                    #this sets a delay before the values change again on their own
                    $ ThreeCount = Round - 1
            $ TempLust2 += 2       
            if Mode == "lesbian":
                    #Sets Primary Girl's secondary action
                    $ Trigger3 = Action                
                    $ PrimaryLust += (TempLust * 3)
                    $ SecondaryLust += (TempLust2 * 3)
            elif Mode == "start":                
                    #Sets Rog*ue's action and Lust if this is a starting action
                    $ Trigger4 = Action
                    $ GirlA.Lust += TempLust2
            else:
                    #Sets Secondary girl's action
                    $ Trigger4 = Action
                    $ SecondaryLust += TempLust
                    $ PrimaryLust += TempLust2
            if Preset:
                    #if this was done at your direction, apply lusts
                    $ GirlA.Lust += TempLust
                    $ GirlB.Lust += TempLust2
            $ Player.Focus += TempFocus

            return

# end Threeway-set / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



#Start Dirty Talk / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Dirty_Talk(Girl = Primary, D20=0, TempCheck=0, TempLine=0, TempTrigger=Trigger4, ActiveGirl=0): 
    # TempCheck is the triggering variable, which shifts depending on whether the girl is leading or not. 
    # Temptrigger is what the other girl is doing.
    # ActiveGirl is the girl being referenced
            
    if Trigger == "strip" or not Trigger:
            #if nothing that involves dirty talk. . .
            return
            
    $ D20 = renpy.random.randint(1, 4)
    # 1 is nobody, 2 and 3 is primary, 4 is secondary
    
    if D20 == 1:
            return
    elif D20 == 4 and Partner:
        $ Girl = Partner
    else:
        $ Girl = Primary
            
    if (Primary == Girl and D20 in (2,3)) or (Secondary == Girl and Trigger4 and D20 == 4):
            #If the primary is Girl and 1-10 or Girl is the Partner and 11-15 
            if Primary == Girl:
                        #if Girl is primary, Tempcheck is the Trigger variable
                        $ TempCheck = Trigger                
                        $ ActiveGirl = Secondary
                        $ TempTrigger = Trigger3
            else:
                        #if Girl is secondary, Tempcheck is the Trigger4 variable
                        $ TempCheck = Trigger4
                        $ ActiveGirl = Primary
                        $ TempTrigger = Trigger4  
                 
    $ D20 = renpy.random.randint(1, 20)
            
    if "vocal" not in Girl.Traits:
            #if she's non-vocal, she will remain silent
            if Girl.Lust >= 60:
                pass
            else:
                return
    elif D20 >= 15:
            #drops it down to the generic grunts if roll over 15
            pass
                    
    elif Girl == RogueX:
            # if the Girl is Rogue. . .
            if Trigger == "lesbian" or (Secondary == RogueX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused  
                    
                    if "unseen" not in RogueX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Hmm, enjoying the show, "+RogueX.Petname+"?" #you watching
                    elif D20 <= 10:
                            pass
                    elif TempTrigger == "fondle breasts":                            
                            $ TempLine = "Your titties feel so nice, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":                            
                            $ TempLine = "Your titties taste so good, "+ActiveGirl.Name+"." #suck breasts
                    elif TempTrigger == "fondle pussy":                            
                            $ TempLine = "You're sucking me in, "+ActiveGirl.Name+"." #fondle pussy
                    elif TempTrigger == "lick pussy":                            
                            $ TempLine = "You taste so good, "+ActiveGirl.Name+"." #lick pussy
                            
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Touch'n ya is so amazing, " + ActiveGirl.Name + ".",
                                    "Your body feels so amazing. . .",
                                    "Mmmm. . .right there.",
                                    "Ya like that, " + ActiveGirl.Name + "?"
                                    ])    
                            
            elif TempCheck == "masturbation":  
                    if "unseen" not in RogueX.RecentActions:
                            #if she knows you're watching  
                            if D20 <= 3: 
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Could I get some of that, " + RogueX.Petname + "?",
                                                "Why don'tcha bring that over here, " + RogueX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Why so shy, " + RogueX.Petname + "?",
                                                "I'm showing mine, where's yours?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
                                                "I want ya so bad, " + RogueX.Petname + ".",
                                                "Come on over here, " + RogueX.Petname + ". Take me however ya want.",
                                                "Hmm, enjoying the show, "+RogueX.Petname+"?",    
                                                "I love the look you get on your face, " + RogueX.Petname + "."
                                                ])
                    #else: D20 >=15, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.
                       
                    if D20 <= 10:
                            pass
                    elif RogueX.SEXP <= 20 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "Touching ya is so amazing, " + RogueX.Petname + ".",
                                    "Every time you touch me. . . it's like, I can't even put it into words.",
                                    "Mmmm. . .right there.",
                                    "Am I doing that right?",
                                    "Ya like that, " + RogueX.Petname + "?"
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "Seems like you like my hand, huh, " + RogueX.Petname + "?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "You taste so nice, " + RogueX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",                                    
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + RogueX.Petname + ".",
                                    "I can feel you get harder in there. . ."              
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                        if D20 <= 3 and TempCheck == "anal" and RogueX.Loose <= 1:
                            $ TempLine = "It. . .hurts. But it kinda feels good, too." #anal
                        else:
                            $ TempLine = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Ung, so deep. . .",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "I can feel you get harder inside me. . ."
                                        ])
                        
                    if not TempLine:
                        #if nothing else is selected, or if D20 < 10
                        if Primary == RogueX:
                                $ TempLine = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.Petname + ".",
                                        "Your touch is so amazin, " + RogueX.Petname + ".",
                                        "Oooh, right there. . .",
                                        "More, gimme more!",
                                        "I'm all yours, " + RogueX.Petname + ". Take me however ya want.",
                                        "I love it when ya do that, " + RogueX.Petname + ".",
                                        "I love the look you get on your face, " + RogueX.Petname + "."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "I want ya so bad, " + RogueX.Petname + ".",
                                        "Could I get some of that, " + RogueX.Petname + "?",
                                        "Think ya could maybe share that, " + ActiveGirl.Name + "?",
                                        "Come on over here, " + RogueX.Petname + ". Take me however ya want.",
                                        "So that's what you look like from this angle.",
                                        "I love the look you get on your face, " + RogueX.Petname + ".",
                                        "That's right, give it to her.",
                                        "You're really getting into it, " + ActiveGirl.Name + "."
                                        ])
    #end Rogue        
    elif Girl == KittyX:
            # if the Girl is Kitty. . .
            if Trigger == "lesbian" or (Secondary == KittyX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused 
                    
                    if "unseen" not in KittyX.RecentActions and D20 <= 7:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Hmm, like what you see, "+KittyX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts":                            
                        if ActiveGirl == EmmaX:
                            $ TempLine = "I'm so jelly here Emma." #fondle breasts
                        else:
                            $ TempLine = "I love these tits, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":                           
                        if ActiveGirl == EmmaX:                 
                            $ TempLine = "These tits are {i}amazing,{/i} Emma." #fondle breasts
                        else:       
                            $ TempLine = "Hmm, you taste so good, "+ActiveGirl.Name+"." #suck breasts
                    elif TempTrigger == "fondle pussy":                            
                            $ TempLine = "So wet, "+ActiveGirl.Name+"." #fondle pussy
                    elif TempTrigger == "lick pussy":                 
                        if ActiveGirl == RogueX and RogueX.Pubes:
                            $ TempLine = "I love your little stripe, Rogue." #lick pussy                            
                        else:
                            $ TempLine = "You're drowning me here, "+ActiveGirl.Name+"." #lick pussy
                            
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "You're so amazing, " + ActiveGirl.Name + ".",
                                    "You know how to push" + KittyX.like + "every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's" + KittyX.like + "{i}so{/i} good.",
                                    "You taste so good. . ."
                                    ])     
            
            elif TempCheck == "masturbation":  
                    if "unseen" not in KittyX.RecentActions:
                            #if she knows you're watching  
                            if D20 <= 3: 
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Hmm, I'd like some of that, " + KittyX.Petname + "?",
                                                "Could I get a taste, " + KittyX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Feeling shy, " + KittyX.Petname + "?",
                                                "How 'bout a little tat for tit?"
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
                                                "I really want you, " + KittyX.Petname + ".",
                                                "Come'ere, " + KittyX.Petname + ". Gimme a taste.",
                                                "Hmm, like the show, "+KittyX.Petname+"?",    
                                                "You look so cute over there, " + KittyX.Petname + "."
                                                ])
                    #else: D20 >=17, drops to generic options
            else:
                #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.
                       
                    if D20 <= 10:
                            pass
                    elif KittyX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're so amazing, " + KittyX.Petname + ".",
                                    "You know how to push, like, every one of my buttons. . .",
                                    "Heh. . .{i}somebody{/i} seems to like that.",
                                    "That's, like, {i}so{/i} good."
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I love the way it"+KittyX.like+"feels in my hands.",
                                    "Seems like you like my hand, huh, " + RogueX.Petname + "?",
                                    "I can feel you get harder in my hand. . .",
                                    ])
                    elif TempCheck == "blow":
                        if D20 <= 3:
                            ch_k "I hope you don't think I'm[KittyX.like]a slut for saying this. . ."                                
                            $ TempLine = "but I love how you taste, " + KittyX.Petname + "."
                        else:        
                            $ TempLine = renpy.random.choice([
                                        "So warm. . .",
                                        "You taste so good, " + KittyX.Petname + ".",
                                        "You're getting harder in my mouth. . .",
                                        "Mmhmhm. . .",
                                        "-gulp-. . .",                                    
                                        ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + KittyX.Petname + ".",
                                    "I can feel you get harder in there. . ."              
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                        if D20 <= 3 and TempCheck == "anal" and KittyX.Loose <= 1:
                            $ TempLine = "Please. . .go slow, 'kay?  You feel so {i}big{/i}."                             
                        else:
                            $ TempLine = renpy.random.choice([
                                        "Your cock is so warm. . .",
                                        "Ohhh. . .that's sooo good.",
                                        "Mmm, you feel so huge. . .",
                                        "Ung, so deep. . .",
                                        "Oooohh. . .just like {i}that{/i}.",
                                        "Keep it up, keep it up. . .",
                                        "Oh, don't stop. . .",
                                        "Did you just get harder?"
                                        ])
                        
                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == KittyX:
                                $ TempLine = renpy.random.choice([
                                            "This is {i}so{/i} hot, " + KittyX.Petname + ".",
                                            "I think I just"+KittyX.like+"discovered one of your other mutant powers, " + KittyX.Petname + ".",
                                            "I like it."+KittyX.Like+"a {i}lot{/i}.",
                                            "Oooh, that's it. . .",
                                            "More, gimme more!",
                                            "That look's so cute, " +KittyX.Petname + "!",
                                            "I've never wanted a guy like I want you, " + KittyX.Petname + "."
                                            ])
                        else:
                                $ TempLine = renpy.random.choice([
                                            "Don't take all the fun, " + ActiveGirl.Name + ".",
                                            "I could use some attention over here, " + KittyX.Petname + ".",
                                            "I got something over here for you, " + KittyX.Petname + ".",
                                            "You're looking pretty good from over here.",                         
                                            "Looks like he likes the way you do that.",
                                            "Make sure you save some for {i}me{/i}!",
                                            "You two look {i}so{/i} sexy doing that.",
                                            "I can't believe you can take all of him like that!",
                                            "That looks like fun, " + ActiveGirl.Name + "."
                                            ])
    #end Primary Kitty  
    elif Girl == EmmaX:
            # if the Girl is Emma. . .
            if Trigger == "lesbian" or (Secondary == EmmaX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused  
                    
                    if "unseen" not in EmmaX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Are you enjoying the performance, "+EmmaX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts" or TempTrigger == "suck breasts":                            
                            if ActiveGirl == KittyX:
                                $ TempLine = "Oh my, these breasts are adorable!" #fondle breasts
                            else: 
                                $ TempLine = "These really are wonderfully. . . pert." #fondle breasts
                    elif TempTrigger == "fondle pussy":                                                     
                                $ TempLine = "Such pressure, "+ActiveGirl.Name+"." #fondle pussy   
                    elif TempTrigger == "lick pussy":                            
                            if ActiveGirl == LauraX:
                                $ TempLine = "Oh yes, that is a Howlett." #lick pussy
                            else:                    
                                $ TempLine = "What an exotic flavor, " + ActiveGirl.Name + "." #lick pussy
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Incredible, " + ActiveGirl.Name + ".",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional, darling.",
                                    "Delicious. . ."
                                    ])   
                            
            elif TempCheck == "masturbation":  
                    if "unseen" not in EmmaX.RecentActions:
                            #if she knows you're watching  
                            if D20 <= 3: 
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Oh, I could use some of that, " + EmmaX.Petname + "?",
                                                "Why don't you join me over here, " + EmmaX.Petname + "?"
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "Feeling shy, " + EmmaX.Petname + "?",
                                                "I feel like you aren't enjoying the show."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
                                                "I need you over here, " + EmmaX.Petname + ".",
                                                "Come here, " + EmmaX.Petname + ". Take me.",
                                                "I hope you're enjoying the show, "+EmmaX.Petname+".",    
                                                "I do love the look on your face, " + EmmaX.Petname + "."
                                                ])
                    #else: D20 >=15, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.
                       
                    if D20 <= 10:
                            pass
                    elif EmmaX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're incredible, " + EmmaX.Petname + ".",
                                    "You're surprisingly skilled at this. . .",
                                    "Well, that certainly got a positive response.",
                                    "Exceptional work, darling.",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so very warm. . .",
                                    "I trust you're enjoying the massage?",
                                    "I take it you're enjoying yourself, " + EmmaX.Petname + "?",
                                    "I can feel you grow harder. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "So delicious. . .",
                                    "I must say, I enjoy the flavor, " + EmmaX.Petname + ".",
                                    "I can feel you get harder in my mouth. . .",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",                                    
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + EmmaX.Petname + ".",
                                    "Don't get lost in there now . .",
                                    "I can feel you get harder in there. . ."              
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Mmmm, give me more like that. . .", 
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Oh, don't stop. . .",
                                    "I can feel you get harder inside me. . ."
                                    ])
                        
                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == EmmaX:
                                $ TempLine = renpy.random.choice([
                                        "I'm overwhelmed, " + EmmaX.Petname + ".",
                                        "Well now we have another skill to develop, " + EmmaX.Petname + ".",                                        
                                        "Oooh, that's lovely. . .",
                                        "More, I want more!",
                                        "You're simply adorable, " + EmmaX.Petname + ".",
                                        "Ooh, you'll {i}have{/i} to do that one again. . .",
                                        "You certainly do leave an impression, " + EmmaX.Petname + "."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Oh " + EmmaX.Petname + "? Don't keep me waiting.",
                                        "Oh " + ActiveGirl.Name + "? Could you share some of that?",
                                        "Come on over here, " + EmmaX.Petname + ", ravish me.",
                                        "You certainly do put on a show.",
                                        "You're simply adorable, " + EmmaX.Petname + ".",
                                        "Nngh, give it to her.",
                                        "You seem to be enjoying yourself, " + ActiveGirl.Name + "."
                                        ])
            #End Emma's dirty talk lines  
    #end Primary Emma  
    elif Girl == LauraX:
            # if the Girl is Laura. . .
            if ApprovalCheck(LauraX, 1500):
                $ D20 -= 5
            elif ApprovalCheck(LauraX, 1200):
                $ D20 -= 3
            if D20 >= 10:
                    #drops it down to the generic grunts
                    pass
            elif Trigger == "lesbian" or (Secondary == LauraX and TempTrigger not in ("hand","blow","masturbation")):
                    #if this is a lesbian action, or if the threesome action is girl-focused  
                    
                    if "unseen" not in LauraX.RecentActions and D20 <= 5:
                            #if they know you're watching, there is a 3/10 or 2/5 chance
                            $ TempLine = "Looking good, "+LauraX.Petname+"?" #you watching
                    elif TempTrigger == "fondle breasts":                            
                            if ActiveGirl == EmmaX: 
                                $ TempLine = "These things are huge." #fondle breasts
                            else:
                                $ TempLine = "Your titties feel so nice, "+ActiveGirl.Name+"." #fondle breasts
                    elif TempTrigger == "suck breasts":                            
                            $ TempLine = "Hmm, tasty." #suck breasts
                    elif TempTrigger == "fondle pussy":                                                     
                                $ TempLine = "Cozy in there." #fondle pussy   
                    elif TempTrigger == "lick pussy":             
                            if ActiveGirl == RogueX:
                                $ TempLine = "Spicy." #lick pussy
                            elif ActiveGirl == KittyX:
                                $ TempLine = "Hmm, sweet." #lick pussy               
                            elif ActiveGirl == EmmaX:
                                $ TempLine = "So many different flavors." #lick pussy
                    if not TempLine:
                            #if nothing else is selected, or if D20: 1-3, or if D20: 14-15
                            $ TempLine = renpy.random.choice([
                                    "Good job, " + ActiveGirl.Name + ".",
                                    "You know what you're doing. . .",
                                    "Oooh, I liked that one.",
                                    "Great work.",
                                    "Tasty. . ."
                                    ])   
                            
            elif TempCheck == "masturbation":  
                    if "unseen" not in LauraX.RecentActions:
                            #if she knows you're watching  
                            if D20 <= 3: 
                                # it's under a 3 roll
                                if "cockout" in Player.RecentActions:
                                    # Your cock's out
                                    $ TempLine = renpy.random.choice([
                                                "Hey, don't let that go to waste.",
                                                "Come here, " + LauraX.Petname + "."
                                                ])
                                else:
                                    # Your cock's not out
                                    $ TempLine = renpy.random.choice([
                                                "You aren't shy, are you " + LauraX.Petname + "?",
                                                "Pants, lose'em."
                                                ])
                            else:
                                    # It's over a 3 roll
                                    $ TempLine = renpy.random.choice([
                                                "Get over here, " + LauraX.Petname + ".",
                                                "Not enjoying the show, "+LauraX.Petname+"?",    
                                                "Heh, the look on your face, " + LauraX.Petname + "."
                                                ])
                    #else: D20 >=10, drops to generic options
            else:
                    #if neither lesbian nor masturbation
                    # Tempcheck will be trigger if primary or trigger4 if secondary
                    #this will not be masturbation, or girl-focused.
                       
                    if D20 <= 5:
                            pass
                    elif LauraX.SEXP <= 30 or TempCheck == "kiss you":
                            #If she's relatively inexperienced
                            $ TempLine = renpy.random.choice([
                                    "You're good at this, " + LauraX.Petname + ".",
                                    "Huh, you seem to know what you're doing. . .",
                                    "Oh, hey down there.",
                                    "Hmm, like that.",
                                    ])
                    elif TempCheck == "hand":
                        $ TempLine = renpy.random.choice([
                                    "Hmm, your dick's so warm. . .",
                                    "This working for you?",
                                    "Seems like you're having fun, " + LauraX.Petname + "?",
                                    "You seem to be getting harder. . .",
                                    ])
                    elif TempCheck == "blow":
                        $ TempLine = renpy.random.choice([
                                    "Mmm, delicious. . .",
                                    "That's an interesting taste, " + LauraX.Petname + ".",
                                    "Did you just get harder? . .",
                                    "-Slurp.-",
                                    "Mmhmhm. . .",
                                    "-gulp-. . .",                                    
                                    ])
                    elif TempCheck == "titjob":
                        $ TempLine = renpy.random.choice([
                                    "Your cock is so warm. . .",
                                    "I can feel you between my breasts, " + LauraX.Petname + ".",
                                    "I can feel you get harder in there. . ."              
                                    ])
                    elif TempCheck == "sex" or TempCheck == "anal":
                            $ TempLine = renpy.random.choice([
                                    "Mmmm, yeah, gimme more like that. . .", 
                                    "Nngh, how filling. . .",
                                    "Ung, so deep. . .",
                                    "Keep it up, keep it up. . .",
                                    "Ngh, don't stop. . .",
                                    "That's right, harder, faster. . ."
                                    ])
                        
                    if not TempLine:
                        #if nothing else is selected, or if D20 > 10
                        if Primary == LauraX:
                                $ TempLine = renpy.random.choice([
                                        "Wow, " + LauraX.Petname + ".",
                                        "That's great, " + LauraX.Petname + ".",                                        
                                        "Oooh, that's nice. . .",
                                        "More!",
                                        "You're great, " + LauraX.Petname + ".",
                                        "Ok, that was a good one. . ."
                                        ])
                        else:
                                $ TempLine = renpy.random.choice([
                                        "Hey, " + LauraX.Petname + "? Don't keep me waiting.",
                                        "Hey, " + ActiveGirl.Name + "? Share, uh?",
                                        "Get over here, " + LauraX.Petname + ".",
                                        "Well you certainly put on a show.",
                                        "You're looking hot, " + LauraX.Petname + ".",
                                        "You're looking hot, " + ActiveGirl.Name + ".",
                                        "Nngh, yeah, stick it to her.",
                                        "Well you seem to be having fun, " + ActiveGirl.Name + "."
                                        ])
    #end Primary Laura  
    
    if not TempLine:
            #if nothing else was chosen. . .
            if not ActiveGirl or Trigger4 == "masturbation":
                    $ TempLine = Girl.Petname
            else:
                    $ TempLine = ActiveGirl.Name
            $ TempLine = renpy.random.choice([
                    "Mmmh. . .",
                    "Ung. . .",
                    "Ooooh. . .",
                    "Oooh, " + TempLine + ", yes. . ."
                    ])   
    
    if Girl == RogueX:                  #does this need to be global?
            ch_r "[TempLine]"
    elif Girl == KittyX:
            ch_k "[TempLine]"
    elif Girl == EmmaX:
            ch_e "[TempLine]"
    elif Girl == LauraX:
            ch_l "[TempLine]"
    return
    
#End Dirty Talk / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Sex Basic Dialogs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Sex_Basic_Dialog(Girl=0,Type=0):
        # call Sex_Basic_Dialog(Girl,"done")
        #called from during sex scenes if a girl is getting tired. . .
        if Girl not in TotalGirls:
                return
        if Girl == RogueX:
                if Type == 10:
                        ch_r "You might want to wrap this up, it's getting late."  
                elif Type == 5:
                        ch_r "Seriously, it'll be time to stop soon."  
                elif Type == "done":
                        ch_r "Ok, [Girl.Petname], that's enough of that for now."
                elif Type == "tired":
                        ch_r "I'm actually getting a little tired, so maybe we could wrap this up?" 
                elif Type == "sitch":
                        ch_r "Mmm, so what else did you have in mind?"
        elif Girl == KittyX:
                if Type == 10:
                        ch_k "It's[KittyX.like]getting kinda late." 
                elif Type == 5:
                        ch_k "We should wrap this up."   
                elif Type == "done":
                        ch_k "Time to take a little break, for now."
                elif Type == "tired":
                        ch_k "I kinda need a break, so if we could wrap this up?"  
                elif Type == "sitch":
                        ch_k "Mmm, so what else did you have in mind?"
        elif Girl == EmmaX:
                if Type == 10:
                        ch_e "It's getting late. . ."  
                elif Type == 5:
                        ch_e "We should take a break soon."     
                elif Type == "done":
                        ch_e "We need to stop for a moment, let me catch my breath."
                elif Type == "tired":
                        ch_e "I could use a break, are you about finished here?" 
                elif Type == "sitch": 
                        ch_e "Ok then, what were you thinking?"
        elif Girl == LauraX:
                if Type == 10:
                        ch_l "It's getting late, we should wrap this up."  
                elif Type == 5:
                        ch_l "Tic tock, [Girl.Petname]."   
                elif Type == "done":
                        ch_l "Ok, [Girl.Petname], breaktime."
                elif Type == "tired":
                        ch_l "Maybe we could finish this up for now?" 
                elif Type == "sitch":    
                        ch_l "Ok then, what next?"                    
        return
# End Sex Basic Dialogs / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
      
