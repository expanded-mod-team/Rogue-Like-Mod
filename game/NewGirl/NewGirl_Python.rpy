init python:
    
    class SetColorNewGirl(object):
        def __init__(self, name = "Mystique"):
            self.red = 255
            self.green = 255
            self.blue = 255
            self.tempred = 255
            self.tempgreen = 255
            self.tempblue = 255
            self.name = name
            
        
        def set_color(self):
            return self.red, self.green, self.blue, 0
            
        def screen_loop(self, outfittype = "Over", outfit = "jacket"):
            self.outfittype = outfittype
            self.outfit = outfit
            renpy.show_screen("recolor_screen_",self.name,self.outfittype, self.outfit) #recolor_screen_()
            self.tempred = self.red
            self.tempgreen = self.green
            self.tempblue = self.blue
            while True:
                result = ui.interact()
                
                if result[0] == "apply":
                    self.red = self.tempred
                    self.green = self.tempgreen
                    self.blue = self.tempblue
                    
                if result[0] == "quit":
                    renpy.hide_screen("recolor_screen_") #recolor_screen_()
                    return

    class Girlnew(object):
        
        def __init__ (self, name = "no name"):
            #self.name = name
            #self.money = money
            #self.girl = {
            self.name = name
            self.Petname = "boy"       #What Mystique calls the player
            self.Petnames = ["boy"]
            self.Pet = "Mystique"           #What you call Mystique
            self.Pets = ["Mystique"]
            self.Rules = 1
            self.GirlName = "Raven"
            self.Loc = "bg Mystique"
            self.Love = 0
            self.Obed = 0
            self.Inbt = 0
            self.Lust = 0
            self.LikeRogue = 0
            self.LikeEmma = 0
            self.LikeKitty = 0
            self.LikeOtherGirl = {}
            self.Addict = 0 #how addicted she is
            self.Addictionrate = 0 #How fast her addiciton rises
            self.Resistance = 0 #how fast her rate falls
            self.Inventory = []    
            self.OCount = 0                #Orgasm counter
            self.Loose = 2
            self.XP = 0
            self.Cheated = 0               #number of times you've cheated on her    
            self.Break = [0,0]                 #minimum time between break-ups/number of total break-ups
            self.StatPoints = 0    
            self.XPgoal = 100
            self.Lvl = 0
            self.Traits = []
            self.Rep = 800
            self.OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
            self.Shame = 0                 #The amount of shame she generates with her current clothing/action
            self.Taboo = 0                 #The taboo level of the location she is at when not with you
            self.Chat = [0,0,0,0,0,0]
            self.Event = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Todo = []
            self.PubeC = 0    
            ## Sprite Variables
            self.Outfit = "regular"
            self.OutfitDay = "regular"
            self.Emote = "normal"
            self.EmoteDefault = "normal"
            self.Girl_Arms = 1               #her arm position
            self.Arms = 0                  #her gloves
            self.Legs = "skirt"
            self.Over = 0
            self.Chest = "top"    
            self.Pierce = 0
            self.Panties = "black panties"
            self.Neck = 0
            self.Hose = 0
            self.Mouth = "normal"
            self.Brows = "normal"
            self.Eyes = "normal"
            self.Hair = "basic"
            self.HairColor = 0
            self.Gag = 0    
            self.Gagx = 0    
            self.Blush = 0
            self.Spunk = []
            self.Pubes = 0
            self.Wet = 0
            self.LegsUp = 0
            self.Water = 0
            self.TitsUp = 1
            self.Upskirt = 0
            self.PantiesDown = 0
            self.Custom = [0,0,0,0,0,0,0,0,0,0]
            self.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
            self.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Custom4 = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Custom5 = [0,0,0,0,0,0,0,0,0,0,0]  
            self.Custom6 = [0,0,0,0,0,0,0,0,0,0,0]    
            self.Custom7 = [0,0,0,0,0,0,0,0,0,0,0]    
            self.Gym = [2,0,0,0,"tights","top","black panties",0,0,0,0] #arms position, 0, 0, over, legs, chest, panties, 
            self.Sleepwear = [0,0,0,0,0,"short top","black panties",0,0,0]
            self.Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
            self.GirlLayer = 101
            self.SpriteLoc = 550                        #Sets Emma to default to the center
            ## Sexual Encounters
            self.History = []
            self.RecentActions = []
            self.DailyActions = []
            self.Action = 3
            self.MaxAction = 4
            self.Caught = 0
            self.Kissed = 0              #How many times they've kissed
            self.Hand = 0
            self.Foot = 0
            self.Slap = 0
            self.Spank = 0
            self.Strip = 0
            self.Tit = 0
            self.Sex = 0
            self.Anal = 0
            self.Hotdog = 0
            self.Mast = 0
            self.Org = 0
            self.FondleB = 0
            self.FondleT = 0
            self.FondleP = 0
            self.FondleA = 0 
            self.DildoP = 0
            self.DildoA = 0
            self.Vib = 0
            self.Vibrator = 0
            self.Plug = 0
            self.Plugged = 0
            self.SuckB = 0
            self.InsertP = 0
            self.InsertA = 0 
            self.LickP = 0    
            self.LickA = 0 
            self.Blow = 0 
            self.Swallow = 0 
            self.CreamP = 0 
            self.CreamA = 0 
            self.Les = 0     
            self.LesWatch = 0  
            self.SexRogue = 0   
            self.SexKitty = 0   
            self.SexEmma = 0  
            self.SexOtherGirl = {} 
            self.SEXP = 0
            self.ShameLevel = 0  
            self.PlayerFav = 0                     #The player's favorite activity with her  
            self.Favorite = 0                      #her favorite activity   
            self.SeenChest = 0
            self.SeenPanties = 0
            self.SeenPussy = 0   
            self.SeenPeen = 0
            self.Sleep = 0
            self.Personality = "normal"
            self.Date = 0 
            self.Forced = 0                                        #This is a toggle for if she's being coerced
            self.ForcedCount = 0 
            self.Glasses = 0 
            self.HeadBand = 0 
            self.Swimsuit = 0 
            self.OnePiece = 0 
            self.Held = 0
            self.Accessory1 = 0 
            self.Accessory2 = 0 
            self.Accessory3 = 0 
            self.Extra = {} 
            self.LooksLike = "Raven" 
            self.Blindfold = 0 
            self.Headband = 0 

            self.Clothes = {
                "Legs" : "skirt",
                "Over" : 0,
                "Chest" : "top",
                "Pierce" : 0,
                "Panties" : "black panties",
                "Neck" : 0,
                "Hose" : 0,
                }

            self.Colors = {
                "Over" : SetColorNewGirl(self.name, "Over", self.Over),
                "Chest" : SetColorNewGirl(self.name, "Chest", self.Chest),
                "Legs" : SetColorNewGirl(self.name, "Legs", self.Legs),
                "Hose" : SetColorNewGirl(self.name, "Hose", self.Hose),
                "Panties" : SetColorNewGirl(self.name, "Panties", self.Panties),
                "Hair" : SetColorNewGirl(self.name, "Hair", self.Hair),
                }
            #} newgirl["Mystique"].Colors["Over"].screen_loop("Over",newgirl["Mystique"].Over)

         

        
    class FieldValue2(BarValue, FieldEquality):
    # """
    #  :doc: value
    #  A bar value that allows the user to adjust the value of a field
    #  on an object.
    #  `object`
    #      The object.
    #  `field`
    #      The field, a string.
    #  `range`
    #      The range to adjust over.
    #  `max_is_zero`
    #      If True, then when the field is zero, the value of the
    #      bar will be range, and all other values will be shifted
    #      down by 1. This works both ways - when the bar is set to
    #      the maximum, the field is set to 0.
    #      This is used internally, for some preferences.
    #  `style`
    #      The styles of the bar created.
    #  `offset`
    #      An offset to add to the value.
    #  `step`
    #      The amount to change the bar by. If None, defaults to 1/10th of
    #      the bar.
    #  """
        offset = 0

        identity_fields = [ 'object' ]
        equality_fields = [ 'range', 'max_is_zero', 'style', 'offset', 'step']

        def __init__(self, object, field, girl, range, max_is_zero=False, style="bar", offset=0, step=None):
            self.object = object
            #self.field = field
            self.variable = field
            self.girl = girl
            self.range = range
            self.max_is_zero = max_is_zero
            self.style = style
            self.offset = offset

            if step is None:
                if isinstance(range, float):
                    step = range / 10.0
                else:
                    step = max(range / 10, 1)

            self.step = step

        def changed(self, value):

            if self.max_is_zero:
                if value == self.range:
                    value = 0
                else:
                    value = value + 1

            value += self.offset

            setattr(newgirl[self.girl], self.variable, value)
            #newgirl["Mystique"].Love = value
            renpy.restart_interaction()

        def get_adjustment(self):

            #value = newgirl["Mystique"].Love
            #getattr(self.object, self.field)
            value = getattr(newgirl[self.girl], self.variable)

            value -= self.offset

            if self.max_is_zero:
                if value == 0:
                    value = self.range
                else:
                    value = value - 1

            return ui.adjustment(
                range=self.range,
                value=value,
                changed=self.changed,
                step=self.step)

        def get_style(self):
            return self.style, "v" + self.style

    def VariableValue2(variable, girl, range, max_is_zero=False, style="bar", offset=0, step=None):
        # """
        #  :doc: value

        #  A bar value that allows the user to adjust the value of a variable
        #  in the default store.

        #  `variable`
        #      A string giving the name of the variable to adjust.
        #  `range`
        #      The range to adjust over.
        #  `max_is_zero`
        #      If True, then when the field is zero, the value of the
        #      bar will be range, and all other values will be shifted
        #      down by 1. This works both ways - when the bar is set to
        #      the maximum, the field is set to 0.

        #      This is used internally, for some preferences.
        #  `style`
        #      The styles of the bar created.
        #  `offset`
        #      An offset to add to the value.
        #  `step`
        #      The amount to change the bar by. If None, defaults to 1/10th of
        #      the bar.
        # """

        return FieldValue2(store, variable, girl, range, max_is_zero=max_is_zero, style=style, offset=offset, step=step)    


    def Girls_Around():
        GirlsAround = []
        if R_Loc == bg_current:
            GirlsAround.append("Rogue")
        if K_Loc == bg_current:
            GirlsAround.append("Kitty")
        if E_Loc == bg_current:
            GirlsAround.append("Emma")
        for xkk in ModdedGirls:
            if newgirl[xkk].Loc == bg_current:
                GirlsAround.append(xkk)
        return GirlsAround

    def OtherGirls_Around(Girl_ = "Rogue"):
        OtherGirlsAround = []
        if R_Loc == bg_current and Girl_ != "Rogue":
            OtherGirlsAround.append("Rogue")
        if K_Loc == bg_current and Girl_ != "Kitty":
            OtherGirlsAround.append("Kitty")
        if E_Loc == bg_current and Girl_ != "Emma":
            OtherGirlsAround.append("Emma")
        for xkk in ModdedGirls:
            if newgirl[xkk].Loc == bg_current and Girl_ != xkk:
                OtherGirlsAround.append(xkk)
        return OtherGirlsAround
        
## Blinking eyes start      
    def eyewarp(x):     
        return x**1.33      
    eye_open = ImageDissolve("eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)      
    eye_shut = ImageDissolve("eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)   

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x
            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]
            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):
        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)
    Shake = renpy.curry(_Shake)

    def Mod_ApprovalCheck(Chr = "Rogue", T = 1000, Type = "LOI", Spread = 150, TmpM = 1, TabM = 0, C = 1, Bonus = 0, Loc = 0, Check = 0):  
        # $ Count = ApprovalCheck(125, Chr="Rogue")
        # T is the value being checked against, Type is the LOI condition in play, Spread is the difference between basic approval and high approval
        # TmpM is Tempmod multiplier, TabM is the taboo modifier, C is cologne modifiers, Bonus is a random bonus applied, and Loc is the girl's location

        if Chr == "Kitty":                                     
                #sets the data based on Kitty's data
                L = K_Love
                O = K_Obed
                I = K_Inbt
                Loc = K_Loc if not Loc else Loc
        elif Chr == "Emma":                                      
                #sets the data based on Emma's data
                L = E_Love
                O = E_Obed
                I = E_Inbt
                Loc = E_Loc if not Loc else Loc
        elif Chr == "Rogue":                                 
                #sets the data based on Rogue's data
                L = R_Love
                O = R_Obed
                I = R_Inbt
                Loc = R_Loc if not Loc else Loc
        elif Chr in ModdedGirls:                                 
                #sets the data based on Rogue's data
                L = newgirl[Chr].Love
                O = newgirl[Chr].Obed
                I = newgirl[Chr].Inbt
                Loc = newgirl[Chr].Loc if not Loc else Loc
        
        if Loc == bg_current:
                #Bumps stats based on colognes
                if "mandrill" in P_Traits and C:                      
                        if L <= 500:
                            L += 500
                        else:
                            L = 1000
                elif "purple" in P_Traits and C:
                        if O <= 500:
                            O += 500
                        else:
                            O = 1000
                elif "corruption" in P_Traits and C:
                        if I <= 500:
                            I += 500
                        else:
                            I = 1000
       
        
        if Type == "LOI":
                LocalTaboo = Taboo * 10
                LocalTempmod = Tempmod * 10
                
        elif Type == "LO":                      #40 -> 240
                #culls unwanted parameters.
                #These bits multiply everything from the 0-300 range to the 0-3000 range  
                I = 0
                LocalTaboo = Taboo * 6                              
                LocalTempmod = Tempmod * 6
        elif Type == "OI":
                L = 0
                LocalTaboo = Taboo * 6
                LocalTempmod = Tempmod * 6
        elif Type == "LI":
                O = 0
                LocalTaboo = Taboo * 6      
                LocalTempmod = Tempmod * 6
                
        elif Type == "L":                       #40 -> 120
                O = 0
                I = 0
                LocalTaboo = Taboo * 3
                LocalTempmod = Tempmod * 3
        elif Type == "O":
                L = 0
                I = 0
                LocalTaboo = Taboo * 3
                LocalTempmod = Tempmod * 3
        elif Type == "I":
                O = 0
                L = 0
                LocalTaboo = Taboo * 3      
                LocalTempmod = Tempmod * 3
                
        else:            
                LocalTaboo = Taboo * 10         #40 -> 400
                LocalTempmod = Tempmod * 10
        
        TabM = 0 if TabM <= 0 else TabM #test this, makes sure TabM is positive

        if Check:
                #this returns the actual value of the tested stat.
                Check = (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo))
                return Check  
        
        if (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + (2 * Spread)):                           
                #She passes and loves it
                return 3    
        elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= (T + Spread):                                  
                #She passes
                return 2
        elif (L + O + I + Bonus + (TmpM * LocalTempmod) - (TabM * LocalTaboo)) >= T:                         
                #She doesn't really want to, but can be convinced
                return 1
        else:                                                                                                   #She's out
                return 0
        
    def Mod_Statupdate(Name, Flavor, Type, Check=100, Value=1, Greater=0):
        
        if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                Check = Check * 10                  #bumps this stat into the 1000s
        
        if Greater:                             #this checks if it's greater or less than the intended value
                if Type >= Check:
                    Type += Value                   #If it passes the check, add Value to it 
                else:
                    Value = 0                       #If not, don't add Value and set Value to 0
        else:
                if Type <= Check:
                    Type += Value  
                else:
                    Value = 0
                
        if Value:                                       #If there is any change to the stat
                        
            if Type > 1000:                              #If the value would overflow the stat, on Rogue
                if Name == "Rogue" and R_Chat[4]:
                        global R_Love
                        global R_Obed                    
                        global R_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if R_Chat[4] == 1:
                                    R_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif R_Chat[4] == 2:
                                    R_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if R_Chat[4] == 3:
                                    R_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif R_Chat[4] == 4:
                                    R_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if R_Chat[4] == 5:
                                    R_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif R_Chat[4] == 6:
                                    R_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        R_Love = 1000 if R_Love > 1000 else R_Love  #fix, check this works, not sure.
                        R_Obed = 1000 if R_Obed > 1000 else R_Obed
                        R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt
                #End Rogue content
                        
                elif Name == "Kitty" and K_Chat[4]:
                        global K_Love
                        global K_Obed                    
                        global K_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if K_Chat[4] == 1:
                                    K_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif K_Chat[4] == 2:
                                    K_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if K_Chat[4] == 3:
                                    K_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif K_Chat[4] == 4:
                                    K_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if K_Chat[4] == 5:
                                    K_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif K_Chat[4] == 6:
                                    K_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        K_Love = 1000 if K_Love > 1000 else K_Love  #fix, check this works, not sure.
                        K_Obed = 1000 if K_Obed > 1000 else K_Obed
                        K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt
                #End Kitty content
                
                elif Name == "Emma" and E_Chat[4]:
                        global E_Love
                        global E_Obed                    
                        global E_Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if E_Chat[4] == 1:
                                    E_Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif E_Chat[4] == 2:
                                    E_Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if E_Chat[4] == 3:
                                    E_Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif E_Chat[4] == 4:
                                    E_Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if E_Chat[4] == 5:
                                    E_Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif E_Chat[4] == 6:
                                    E_Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        E_Love = 1000 if E_Love > 1000 else E_Love  #fix, check this works, not sure.
                        E_Obed = 1000 if E_Obed > 1000 else E_Obed
                        E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt
                #End Emma content

                elif Name in ModdedGirls and newgirl[Name].Chat[4]:
                        #global newgirl["Mystique"].Love
                        #global newgirl["Mystique"].Obed                    
                        #global newgirl["Mystique"].Inbt
                        
                        Value = Type - 1000
                        if Flavor == "Love":                    
                                if newgirl[Name].Chat[4] == 1:
                                    newgirl[Name].Obed += Value    #[Love to Obedience]
                                    Flavor = "Obed"
                                elif newgirl[Name].Chat[4] == 2:
                                    newgirl[Name].Inbt += Value   #[Love to Inhibition] 
                                    Flavor = "Inbt"
                        elif Flavor == "Obed":             
                                if newgirl[Name].Chat[4] == 3:
                                    newgirl[Name].Inbt += Value    #[Obedience to Inhibition]
                                    Flavor = "Inbt"
                                elif newgirl[Name].Chat[4] == 4:
                                    newgirl[Name].Love += Value    #[Obedience to Love] 
                                    Flavor = "Love"  
                        elif Flavor == "Inbt":            
                                if newgirl[Name].Chat[4] == 5:
                                    newgirl[Name].Obed += Value    #[Inhibition to Obedience]
                                    Flavor = "Obed"
                                elif newgirl[Name].Chat[4] == 6:
                                    newgirl[Name].Love += Value    #[Inhibition to Love]
                                    Flavor = "Love"
                        newgirl[Name].Love = 1000 if newgirl[Name].Love > 1000 else newgirl[Name].Love  #fix, check this works, not sure.
                        newgirl[Name].Obed = 1000 if newgirl[Name].Obed > 1000 else newgirl[Name].Obed
                        newgirl[Name].Inbt = 1000 if newgirl[Name].Inbt > 1000 else newgirl[Name].Inbt
                #End Mystique content
                
                Type = 1000
                
                
                    
            
            if Flavor == "Love":                        #Sets reporting text color based on Flavor
                    Color = "#c11b17"
            elif Flavor == "Obed":
                    Color = "#2554c7"
            elif Flavor == "Inbt":
                    Color = "#FFF380"
            elif Flavor == "Lust":
                    Color = "#FAAFBE"
            else:
                    Color = "#FFFFFF"
            
            if Name == "Rogue":
                    XPOS = R_SpriteLoc
            elif Name == "Kitty":
                    XPOS = K_SpriteLoc
            elif Name == "Emma":
                    XPOS = E_SpriteLoc
            elif Name in ModdedGirls:
                    XPOS = newgirl[Name].SpriteLoc
            else:
                    XPOS = 0.75
                
            CallHolder(Value, Color, XPOS)
                            
        if Type < 0:                                    #If Type ends up less than zero, set it to zero
            Type = 0
            
        return Type
    # def GetOutfitStringMystique(first = "images/MystiqueSprite/Rogue_panties_", second = "test", third = ".png"):
    #     if second:
    #         string = first + second + third
    #         if not renpy.loadable(string):
    #             string = Null()
    #     else:
    #         string = Null()
    #     return string
image blackblink:   
    Solid("#000")   
image whiteblink:   
    Solid("#FFF")   
    
label BlinkEyes:      
    scene blackblink    
    ## Closed   
    scene whiteblink    
    with eye_open   
    ## Open     
    scene blackblink    
    with eye_shut   
    ## Closed   
    return      
## Blinking eyes end        