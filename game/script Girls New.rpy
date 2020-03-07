init python:
    class PlayerClass(object):         
        def __init__(self):
                self.Name = "Zero"        
                self.Semen = 2                  #available semen
                self.Semen_Max = 3              #amount it maxes out at
                self.Focus = 0                  #progress towards orgasm
                self.FocusX = 0                 #is the player trying not to orgasm
                self.XP = 0
                self.StatPoints = 0    
                self.XPgoal = 100
                self.Lvl = 1
                self.Rep = 600
                self.RecentActions = []
                self.DailyActions = []
                self.Traits = []
                self.History = []
                self.Harem = []                 #this is a list of all girls the player is currently dating
                self.Male = 1        
            # Player Inventory Variables 
                self.Income = 12                #how much you make each day
                self.Cash = 20
                self.Inventory = []
                #default Inventory_Count = 0    #check to see if this works on screens, if so, delete it
            # Player Sprite
                self.Sprite = 0
                self.Color = "green"
                self.Cock = "out"
                self.Spunk = 0
                self.Wet = 0
                
        def AddWord(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):
                #applies variables to appropriate character stats
                # $ Player.AddWord(1,"angry",0,0,0)
                #if Only, then only apply it if it's not already there
                if (Recent and not Only) or (Recent and Recent not in self.RecentActions):
                        self.RecentActions.append(Recent)
                if (Daily and not Only) or (Daily and Daily not in self.DailyActions):
                        self.DailyActions.append(Daily)
                if (Trait and not Only) or (Trait and Trait not in self.Traits):
                        self.Traits.append(Trait)
                if (History and not Only) or (History and History not in self.History):
                        self.History.append(History)                    
                return
            
        def DrainWord(self, Word = "word", Recent = 1, Daily = 1, Traits=0):
                # to remove words from the daily/recent lists , ie call DrainWord("Rogue","sex",1,0)
                # $ Player.DrainWord("angry",0,1)                  
                if Recent and Word in self.RecentActions:
                    while Word in self.RecentActions:
                            self.RecentActions.remove(Word) 
                if Daily and Word in self.DailyActions:
                    while Word in self.DailyActions:
                            self.DailyActions.remove(Word)  
                if Traits and Word in self.Traits:
                    while Word in self.Traits:
                            self.Traits.remove(Word)       
                return  
                    
        def Statup(self, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Overflow=0, BStat=0, XPOS = 0.75): 
                # $ Player.Statup("Focus", 90, 5)                
                Type = getattr(self,Flavor)                                
                if Greater:                             
                        #this checks if it's greater or less than the intended value
                        #if it fails, the value is zeroed out, cancelling the rest
                        if Type >= Check:
                            #If it passes the check, add Value to it 
                            Type += Value                   
                        else:
                            #If not, don't add Value and set Value to 0
                            Value = 0                      
                else:
                        if Type <= Check:
                            Type += Value  
                        else:
                            Value = 0
                       
                if Value:  
                        Color = "#FFFFFF"
                        # show pop-up 
                        CallHolder(Value, Color, XPOS)
                #end "if value is positive"                            
                Type = 100 if Type > 100 else Type                         
                setattr(self,Flavor,Type)                            
                return
        #End Statup
    #End Player Class contents, Player = PlayerClass() / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    
    class GirlClass(object):      
        def __init__(self,Name="no name",Love=0,Obed=0,Inbt=0,Lust=0):
                self.Name = Name        #changable by player, used in dialog
                self.Tag = Name         #Permanent label, used in code
                self.Names = [Name]     #this is a list of primary names you're allowed to use
                self.Love = Love
                self.Obed = Obed
                self.Inbt = Inbt
                self.Lust = Lust
                self.Thirst = 0         #how much she wants sex
                self.Addict = 0         #how much she needs a fix, goes 0-100
                self.Addictionrate = 0  #how fast her Addict rises, goes from 0-10
                self.Resistance = 0     #how much her Addiciton drops naturally 0-3
                self.Taboo = 0
                self.XP = 0
                self.StatPoints = 0    
                self.XPgoal = 100
                self.Lvl = 1
                self.SpriteLoc = StageCenter
                self.Layer = 50         #the layer her sprite appears on
                self.Action = 3         #times the girl can do something this turn
                self.MaxAction = 3      #max times the girl can do something per turn
                self.Rep = 600
                self.RecentActions = []
                self.DailyActions = []
                self.Traits = []
                self.History = []  
                self.Date = 0                           #how many dates you've been on
                self.Chat = [0,0,0,0,0,0]               #whether certain dialogs occurred
                self.Event = [0,0,0,0,0,0,0,0,0,0,0]    #whether certain relationship milestones happened 
                self.Petname = "Zero"
                self.Petnames = ["Zero"]
                self.Pet = "Girl"
                self.Pets = ["Girl"]
                self.Break = [0,0]      #minimum time between break-ups/number of total break-ups
                self.Forced = 0         #are they being coerced
                self.ForcedCount = 0    #countdown for how long they stay mad
                self.Loc = "hold"       #Where she is right now
                self.Home = 0           #where she lives
                # Clothing parts
                self.Outfit = "casual1"         #current outfit
                self.OutfitDay = "casual1"      #outfit she picked for the day
                self.SeenPeen = 0
                self.SeenChest = 0
                self.SeenPussy = 0
                self.SeenPanties = 0
                self.Upskirt = 0
                self.Uptop = 0
                self.PantiesDown = 0
                self.Wet = 0
                self.Water = 0                
                self.Spunk = []
                self.Pierce = 0     
                self.Pubes = 1                
                self.ArmPose = 1
                self.Blush = 0
                self.Eyes = "normal"
                self.Mouth = "normal"
                self.Brows = "normal"
                self.Emote = "normal"
                self.Held = 0                           #object held in hand                
                self.Arms = 0
                self.Legs = 0
                self.Over = 0
                self.Neck = 0
                self.Chest = 0
                self.Panties = 0  
                self.Acc = 0     
                self.Hair = 1      
                self.Hose = 0
                self.Shame = 0
                self.Inventory = []
                # Clothing sets
                # toggle(0),arms/gloves(1),pants(2),jacket(3),necklace(4),bra(5),panties(6),boots(7),hair(8),hose(9)
                self.Casual1 = [0,0,0,0,0,0,0,0,0,0,0]
                self.Casual2 = [0,0,0,0,0,0,0,0,0,0,0]
                self.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                self.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                self.Custom3 = [0,0,0,0,0,0,0,0,0,0,0] 
                self.TempClothes = [0,0,0,0,0,0,0,0,0,0,0]  
                self.Gym = [0,0,0,0,0,0,0,0,0,0,0]
                self.Sleepwear = [0,0,0,0,0,0,0,0,0,0,0]
                self.Swim = [0,0,0,0,0,0,0,0,0,0,0] 
                self.Gag = 0
                self.Todo = []                  #todo list, piercing, pubes, etc.
                self.PubeC = 0                  #countdown for when pubes grow back
                self.Schedule = [["MM","MA","ME","MN"],
                                ["TM","TA","TE","TN"],
                                ["WM","WA","WE","WN"],
                                ["ThM","ThA","ThE","ThN"],
                                ["FM","FA","FE","FN"],
                                ["SaM","SaA","SaE","SaN"],
                                ["SuM","SuA","SuE","SuN"],
                                ] #Schedule[0-6][0-4] = Schedule[Day][Time]
                self.Clothing = [0,0,0,0,0,0,0,0,0,0]                      #schedules when she wears what
                #                                                          #(0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private
                self.Org = 0                    #lifetime orgasms
                self.OCount = 0                 #orgasms per encounter
                self.Caught = 0
                self.Kissed = 0                 #How many times they've kissed
                self.Sleep = 0                  #How many times they've slept over
                self.Hand = 0
                self.Foot = 0
                self.Slap = 0
                self.Strip = 0
                self.Tit = 0
                self.Sex = 0
                self.Anal = 0
                self.Loose = 0
                self.Hotdog = 0
                self.Mast = 0
                self.Massage = 0
                self.FondleB = 0
                self.FondleT = 0
                self.FondleP = 0
                self.FondleA = 0
                self.DildoP = 0
                self.DildoA = 0
                self.Vib = 0
                self.Plug = 0
                self.SuckB = 0
                self.InsertP = 0
                self.InsertA = 0
                self.LickP = 0    
                self.LickA = 0
                self.Blow = 0
                self.Swallow = 0
                self.CreamP = 0
                self.CreamA = 0
                self.Les = 0                                    #how many times she's done les stuff
                self.LesWatch = 0                               #how many times you've watched her lesing
                self.SEXP = 0
                self.MassageChart = [0,0,0,0,0,0,0,0,0,0]
                self.PlayerFav = 0                              #you favorite activity with her    
                self.Favorite = 0                               #her favorite activity    
                
                
                if self.Tag == "Rogue":
                        self.Casual1 = [2,"gloves","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0]
                        self.Casual2 = [2,"gloves","pants","pink top",0,"buttoned tank","black panties",0,0,0,0]
                        self.Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,10]
                        self.Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,20]
                        self.Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0] 
                        # turn "evo_green" to Casual1
                        # turn "evo_pink" to Casual2
                        # change "Schedule" stat to "Clothing" stat?
                        self.Home = "bg rogue"                         
                        self.Hair = "evo"  
                        self.LikeKitty = 600
                        self.LikeEmma = 500                      
                        self.LikeLaura = 500
                        self.Schedule = [["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                        ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                        ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                        ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                        ] #Schedule[0-6][0-4] = Schedule[Day][Time]
                        self.SexKitty = 0
                        self.SexEmma = 0
                        self.SexLaura = 0                   
                        self.History = ["met"]
                        self.MassageChart = ["shoulders","arms","arms","hands","hands","back","hips","back","breasts","breasts"]
                elif self.Tag == "Kitty": 
                        self.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0]
                        self.Casual2 = [2,0,"black jeans","red shirt","star necklace","bra","green panties",0,0,0,0]
                        self.Gym = [0,0,"shorts",0,0,"sports bra","green panties",0,0,0,10]
                        self.Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0,20]
                        self.Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0] 
                        self.Home = "bg kitty"                         
                        self.Hair = "evo"  
                        self.LikeRogue = 600
                        self.LikeEmma = 500                      
                        self.LikeLaura = 500
                        self.like = ", like, "
                        self.Like = "Like, "
                        self.Schedule = [["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg classroom","bg pool","bg kitty","bg kitty"],
                                        ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg classroom","bg pool","bg kitty","bg kitty"],
                                        ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                        ] #Schedule[0-6][0-4] = Schedule[Day][Time]
                        self.SexRogue = 0
                        self.SexEmma = 0
                        self.SexLaura = 0
                        self.MassageChart = ["shoulders","back","hips","thighs","calves","feet","feet","hips","ass","pussy"]
                elif self.Tag == "Emma":   
                        self.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0]
                        self.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,5]
                        self.Gym = [0,0,0,0,0,"sports bra","sports panties",0,0,0,10]
                        self.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0,25]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
                        self.Home = "bg emma"                         
                        self.Hair = "wavy"  
                        self.Pubes = 0  
                        self.LikeRogue = 500 
                        self.LikeKitty = 500                     
                        self.LikeLaura = 500   
                        self.Schedule = [["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                        ["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                        ["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg pool","bg pool","bg emma","bg emma"],
                                        ["bg pool","bg pool","bg emma","bg emma"],
                                        ] #Schedule[0-6][0-4] = Schedule[Day][Time]
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexLaura = 0
                        self.Loose = 2
                        self.MassageChart = ["shoulders","neck","neck","back","hips","ass","ass","back","breasts","breasts"]
                        
                elif self.Tag == "Laura":     
                        self.Casual1 = [2,"wrists","leather pants",0,0,"leather bra","leather panties",0,0,0,0]
                        self.Casual2 = [2,0,"skirt","jacket",0,"leather bra","leather panties",0,0,0,0]
                        self.Gym = [2,"wrists","leather pants",0,0,"leather bra","leather panties",0,0,0,0]
                        self.Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0,20]
                        self.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]    
                        self.Home = "bg laura"                         
                        self.Hair = "long"              
                        self.LikeRogue = 500
                        self.LikeKitty = 500
                        self.LikeEmma = 500   
                        self.ScentTimer = 0 #this timer gives you X seconds of watching Laura before she notices you there
                        self.Claws = 0
                        self.Schedule = [["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                        ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                        ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg pool","bg laura","bg dangerroom","bg laura"],
                                        ["bg pool","bg laura","bg dangerroom","bg laura"],
                                        ] #Schedule[0-6][0-4] = Schedule[Day][Time]
                        self.SexRogue = 0
                        self.SexKitty = 0
                        self.SexEmma = 0
                        self.Loose = 2                        
                        self.MassageChart = ["shoulders","back","arms","hips","thighs","calves","ass","ass","pussy","pussy"]
                        
                elif self.Tag == "Jean": 
                        # JeanX = GirlClass("Jean",0,0,1000,10) #love to up to 300 by end of intro, Inbt falls to 800
                        self.StatStore = 0 #this stores Love stat above 500 and distributes it later. 
                        
                self.OutfitChange(Changed=1) #assigns their default outfit, hopefully
                
        def Introduction(self):
                #things to add when girl is introduced
                if self == RogueX: #if self.Name == "Rogue":?
                        self.Petname = "Sugar"
                        self.Petnames = ["Sugar",Player.Name]
                        self.Pet = "Rogue"
                        self.Pets = ["Rogue"]
                elif self == KittyX:
                        self.Petname = Player.Name[:1]
                        self.Petnames = ["sweetie",Player.Name[:1],Player.Name]
                        self.Pet = "Kitty"
                        self.Pets = ["Kitty"]
                elif self == EmmaX:
                        self.Names = ["Ms. Frost"]
                        self.Name = "Ms. Frost"
                        self.Petname = "young man"
                        self.Petnames = ["young man",Player.Name]
                        self.Pet = EmmaX.Name
                        self.Pets = ["Emma","Ms. Frost"]               
                elif self == LauraX:
                        self.Petname = "guy"
                        self.Petnames = ["guy",Player.Name]
                        self.Pet = LauraX.Name
                        self.Pets = ["Laura","X-23"]  
                elif self.Tag == "Jean": 
                        pass
                        
                self.OutfitChange(6,Changed=1) #assigns their default outfit, hopefully
                #make sure to convert all "addict kitty" tags to "addict Kitty".
                global TotalGirls
                if self not in TotalGirls:
                        TotalGirls.append(self)                 #These are the girls you have met at all      
                #global ActiveGirls
                #ActiveGirls.append(self)                #These are the girls that you have not dismissed from rotation, now applied when character introduced  
                Shop_Inventory.extend(["DL","G","A"])     #adds these three items to the store for each girl added
                PersonalRooms.append(self.Home)
                         
        def SluttyClothes(self):
                # called to check if loosened morals will lead to looser default outfits.
                # $ RogueX.SluttyClothes
                if self == RogueX:
                            if "stockings and garterbelt" in self.Inventory:
                                    self.Casual1[9] = "stockings and garterbelt"
                            elif self.Inbt >= 300: #ApprovalCheck("Rogue", 300, "I"):                        
                                    self.Casual1[9] = "stockings"
                            else:
                                    self.Casual1[9] = "tights"    
                                
                            if self.Gym[0] == 0 and self.Gym[5] and self.Inbt >= 300:   
                                    #removed hoodie if she's no longer shy
                                    self.Gym[3] == 0 
                                                                
                            if self.Swim[0] == 0 and self.Swim[5] and self.Inbt >= 300:   
                                    #removed hoodie if she's no longer shy
                                    self.Swim[3] == 0 
                elif self == KittyX:
                            if self.Swim[2] == "blue skirt" and self.Swim[6] and self.Inbt > 500:
                                    #removes blue skirt if she gets comfortable with it. 
                                    self.Swim[2] = 0
                elif self == LauraX:
                            if self.Inbt >= 400 and self.Casual2[5] == "leather bra":
                                    self.Casual2[5] = "corset"
                            if self.Inbt >= 600 and "lace panties" in self.Inventory:
                                    self.Casual2[6] = "lace panties"                            
                            if self.Inbt >= 600 and "stockings and garterbelt" in self.Inventory:
                                    self.Casual2[9] = "stockings and garterbelt"    
                return
                                           
        def AddWord(self,Only=0,Recent=0,Daily=0,Trait=0,History=0):
                #applies variables to appropriate character stats
                # $ RogueX.AddWord(1,"angry",0,0,0)
                #if Only, then only apply it if it's not already there
                if (Recent and not Only) or (Recent and Recent not in self.RecentActions):
                        self.RecentActions.append(Recent)
                if (Daily and not Only) or (Daily and Daily not in self.DailyActions):
                        self.DailyActions.append(Daily)
                if (Trait and not Only) or (Trait and Trait not in self.Traits):
                        self.Traits.append(Trait)
                if (History and not Only) or (History and History not in self.History):
                        self.History.append(History)                    
                return
            
        def DrainWord(self, Word = "word", Recent = 1, Daily = 1, Traits=0):
                # to remove words from the daily/recent lists , ie call DrainWord("Rogue","sex",1,0)
                # $ RogueX.DrainWord("angry",0,1)  
                if Recent and Word in self.RecentActions:
                    while Word in self.RecentActions:
                            self.RecentActions.remove(Word) 
                if Daily and Word in self.DailyActions:
                    while Word in self.DailyActions:
                            self.DailyActions.remove(Word)  
                if Traits and Word in self.Traits:
                    while Word in self.Traits:
                            self.Traits.remove(Word)     
                return  
        
        def Statup(self, Flavor=0, Check=100, Value=1, Greater=0, Type=0, Alt=[[],0,0], Overflow=0, BStat=0, XPOS = 0.75): 
                # $ RogueX.Statup("Love", 90, 5)
                #figure out a way to send a matrix variable for altering the results based on character Alt=[[RogueX,KittyX],500,-10]
                if self not in TotalGirls: #should remove "character don't exist" errors
                        return
                
                if self in Alt[0]:
                                #if there is an alternate character option. . .
                                Check = Alt[1] if Alt[1] else Check
                                Value = Alt[2] if Alt[2] else Value
                                
                if Flavor == "Love" or Flavor == "Obed" or Flavor == "Inbt":
                        #bumps this stat into the 1000s
                        Check = Check * 10    
                                  
                Type = getattr(self,Flavor)
                
                Overflow = self.Chat[4]
                XPOS = self.SpriteLoc
                
                if Greater:                             
                        #this checks if it's greater or less than the intended value
                        #if it fails, the value is zeroed out, cancelling the rest
                        if Type >= Check:
                            #If it passes the check, add Value to it 
                            Type += Value                   
                        else:
                            #If not, don't add Value and set Value to 0
                            Value = 0                      
                else:
                        if Type <= Check:
                            Type += Value  
                        else:
                            Value = 0
                                        
                if Value:                                       
                    #If there is any change to the stat  
                    #Sets reporting text color based on Flavor     
                                        
                    if self.Tag == "Jean":
                            if Flavor == "Obed" and Type <= 800 and Check < 800:
                                    # if her Obedience is under 800 and the check is for less than 800, 
                                    # reduces half the gains. This slows low obed farming options
                                    Value = int(Value/2)
                                    Type -= Value
                            elif Flavor == "Love" and Type >= 500 and self.Obed < 900:
                                    #if the character is Jean, her Love stat will not raise above 500,
                                    #unless her Obedience is over 900. It does get stored up, however,
                                    #and doled out at a later date. 
                                    Value = Type - 500                                      #sets value to the overflow
                                    self.Love = 500 if self.Love >= 500 else self.Love      #caps Love at 500
                                    self.StatStore += Value                                 #stores overflow amount for later
                                    if Check > 900:
                                        Flavor = "Obed"                                     #sets the flavor to obed
                                        Type = self.Obed + 1                                #establishes the new change as Obed+1
                                        Value = 1                                           #sets value change as 1
                            
                    if Flavor == "Love":                        
                            Color = "#c11b17"
                    elif Flavor == "Obed":
                            Color = "#2554c7"
                    elif Flavor == "Inbt":
                            Color = "#FFF380"
                    elif Flavor == "Lust":
                            Color = "#FAAFBE"
                    
                    if Type > 1000 and Flavor != "Lust": 
                        if self.Loc == bg_current:
                                CallHolder((-(Type-1000-Value)), Color, XPOS)                         
                        if not self.Chat[4]:
                            #if no overflow mechanic is prepared. . .
                            Value = 0
                        else:
                            #if the value overflows, play one value meter, then. . .
                            Value = Type - 1000
                            # change the Flavor to the new thing if there is a swap happening
                            setattr(self,Flavor,1000)
                            if Flavor == "Love":    
                                    if self.Chat[4] == 1:       #[Love to Obedience]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 2:     #[Love to Inhibition] 
                                        Flavor = "Inbt"
                                    else: 
                                        Value = 0                                          
                            elif Flavor == "Obed":    
                                    if self.Chat[4] == 3:       #[Obedience to Inhibition]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 4:    
                                        Flavor = "Love"   #[Obedience to Love] 
                                    else: 
                                        Value = 0  
                            elif Flavor == "Inbt":    
                                    if self.Chat[4] == 5:       #[Inhibition to Obedience]
                                        Flavor = "Obed"
                                    elif self.Chat[4] == 6:    
                                        Flavor = "Love"    #[Inhibition to Love]
                                    else: 
                                        Value = 0  
                                       
                            if Flavor == "Love":                        
                                    #Sets reporting text color based on Flavor
                                    Color = "#c11b17"
                            elif Flavor == "Obed":
                                    Color = "#2554c7"
                            elif Flavor == "Inbt":
                                    Color = "#FFF380"
                            else:
                                    Color = "#FFFFFF"
                    #end Type change element
                                                 
                    if Value and self.Loc == bg_current:               
                        # show pop-up 
                        CallHolder(Value, Color, XPOS)
                        
                    if Flavor == "Lust" and Type >= 100 and not Trigger:
                                #calls orgasm if Lust goes over 100, breaks routine
                                renpy.call("Girl_Cumming",self,1)
                                Value = 0
                                return                        
                        
                #end "if value is positive"
                            
                Type = 1000 if Type > 1000 else Type
                         
                setattr(self,Flavor,Type)                            
                return
        #End Statup
                        
        def FaceChange(self, Emote = 5, B = 5, M = 0, Mouth = 0, Eyes = 0, Brows = 0):
                # $ RogueX.FaceChange("sadside",1,Mouth="smile")
                # Emote is the chosen emote, B is the lush state, 
                # M is whether the character is in a  manic state   
                Emote = self.Emote if Emote == 5 else Emote
                B = self.Blush if B == 5 else B
                
                if (self.Forced or "angry" in self.RecentActions) and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                        Emote = "angry"   
                elif self.ForcedCount > 0 and Emote in ("normal", "bemused", "sexy", "sly", "smile", "startled"):
                        Emote = "sad" 
                        
                if Emote == "normal":
                        self.Mouth = "normal"
                        self.Brows = "normal"
                        self.Eyes = "normal"
                elif Emote == "angry":
                        if self == LauraX:
                                self.Mouth = "kiss"
                        else:
                                self.Mouth = "sad"
                        self.Brows = "angry"
                        self.Eyes = "sexy"
                elif Emote == "bemused":
                        if self == EmmaX:
                                self.Mouth = "normal"
                        else:
                                self.Mouth = "lipbite"
                        self.Brows = "sad"
                        self.Eyes = "squint"
                elif Emote == "closed":
                        if self == RogueX:
                                self.Mouth = "lipbite"
                        else:
                                self.Mouth = "normal"
                        self.Brows = "sad"
                        self.Eyes = "closed"  
                elif Emote == "confused":
                        self.Mouth = "kiss"
                        self.Brows = "confused"
                        if self == LauraX or self == EmmaX:
                                self.Eyes = "squint"
                        else:
                                self.Eyes = "surprised"                        
                elif Emote == "kiss":
                        self.Mouth = "kiss"
                        if self == LauraX or self == EmmaX:
                                self.Brows = "sad"
                        else:
                                self.Brows = "normal"
                        self.Eyes = "closed"                   
                elif Emote == "sad":
                        self.Mouth = "sad"
                        self.Brows = "sad"
                        self.Eyes = "sexy"
                elif Emote == "sadside":
                        self.Mouth = "sad"
                        self.Brows = "sad"
                        self.Eyes = "side"
                elif Emote == "sexy":
                        self.Mouth = "lipbite"
                        if self == EmmaX:
                                self.Brows = "normal"
                                self.Eyes = "squint"
                        elif self == LauraX:
                                self.Brows = "sad"
                                self.Eyes = "squint"
                        else:
                                self.Brows = "normal"
                                self.Eyes = "sexy"  
                elif Emote == "sly":   
                        self.Brows = "normal"
                        self.Eyes = "squint"  
                        if self == RogueX:
                                self.Mouth = "grimace"                
                        if self == LauraX:
                                if LauraX.Love >= 700:
                                    self.Mouth = "smile"
                                else:
                                    self.Mouth = "smirk" 
                                self.Brows = "confused"
                        elif self == KittyX:
                                self.Mouth = "smile"
                        elif self == EmmaX:
                                self.Mouth = "smirk"                      
                elif Emote == "smile":
                        if self == LauraX and LauraX.Love < 700:
                                self.Mouth = "smirk"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "normal"
                        self.Eyes = "normal"
                elif Emote == "surprised":                    
                        if self == RogueX or self == KittyX:
                                self.Mouth = "surprised"
                        else:
                                self.Mouth = "kiss"
                        self.Brows = "surprised"
                        self.Eyes = "surprised"
                elif Emote == "oh":
                        self.Mouth = "kiss"
                        self.Brows = "surprised"
                        self.Eyes = "surprised"
                elif Emote == "startled":                    
                        if self == RogueX or self == KittyX:
                                self.Mouth = "grimace"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "surprised"
                        self.Eyes = "surprised"
                elif Emote == "down":
                        if self == RogueX or self == KittyX:
                                self.Mouth = "surprised"
                        else:
                                self.Mouth = "sad"
                        self.Brows = "sad"
                        self.Eyes = "down" 
                elif Emote == "perplexed":
                        if self == RogueX:
                                self.Mouth = "sad"
                                self.Brows = "confused"
                        else:
                                self.Mouth = "smile"
                                self.Brows = "sad"
                        if self == LauraX:
                                self.Eyes = "surprised"
                        else:
                                self.Eyes = "normal" 
                elif Emote == "sucking":
                        self.Mouth = "sucking"
                        if self == EmmaX:
                                self.Brows = "surprised"
                        elif self == LauraX:
                                self.Brows = "sad"
                        else:
                                self.Brows = "normal"
                        self.Eyes = "closed" 
                elif Emote == "tongue":
                        self.Mouth = "tongue"
                        self.Brows = "sad"
                        if self == LauraX:
                                self.Eyes = "stunned"
                        else:
                                self.Eyes = "sexy"
                elif Emote == "manic":
                        if self == RogueX:
                                self.Mouth = "grimace"
                        elif self == LauraX:
                                self.Mouth = "lipbite"
                        else:
                                self.Mouth = "smile"
                        self.Brows = "sad"
                        self.Eyes = "manic"
                        self.Blush = 1     
                    
                if M:
                        self.Eyes = "manic"        
                if B > 1:
                        self.Blush = 2
                elif B:
                        self.Blush = 1
                else:
                        self.Blush = 0
                        
                if Mouth:
                        self.Mouth = Mouth
                if Eyes:
                        self.Eyes = Eyes
                if Brows:
                        self.Brows = Brows                
                return
        # End Face Change / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /  
        
        def DefaultFaces(self):
                #This sets a default face for the girl
                #was "call Faces"
                # $ RogueX.DefaultFaces()
                if self.Lust >= 50 and ApprovalCheck(self, 1200):
                        self.Emote = "sexy"           
                elif self.Addict > 75:
                        self.Emote = "manic"
                elif self.Love >= self.Obed and self.Love >= 500:
                        self.Emote = "smile"      
                elif self.Inbt >= self.Obed and self.Inbt >= 500:
                        self.Emote = "smile"      
                elif self.Addict > 50:
                        self.Emote = "manic"
                elif (self.Love + self.Obed) < 300:
                        self.Emote = "angry"
                else:
                        self.Emote = "normal"
                return
        
        def LustFace(self,Extreme=0,Kissing=0):        
                if self.Thirst >= 80:
                        self.Lust += 2
                elif self.Thirst >= 50:
                        self.Lust += 1
                    
                if self.Lust >= 40:        
                        self.Blush = 1
                    
                if self.Lust >= 80:
                        self.Wet = 2 
                elif self.Lust >= 50:
                        self.Wet = 1
                
                if Trigger3 == "kiss both" or Trigger3 == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1
                elif Trigger4 == "kiss both" or Trigger3 == "kiss girl":
                        #if the girls are kissing or all three are
                        Kissing = 1   
                elif Partner != self:
                        #If the called girl is kissing and is primary
                        if Trigger == "kiss you" or Trigger2 == "kiss you":  
                            Kissing = 1
                elif Trigger4 == "kiss you":   
                        #If the called girl is kissing you in a threesome action
                        Kissing = 1
                        
                if Kissing:
                        self.Eyes = "closed"
                        if self.Kissed >= 10 and self.Inbt >= 300:
                            self.Mouth = "sucking"
                        elif self.Kissed > 1 and self.Addict >= 50:            
                            self.Mouth = "sucking"
                        else:
                            self.Mouth = "kiss"
                else:    
                        #If called girl is not kissing someone
                        if self.Lust >= 90:
                                self.Eyes = "closed"
                                self.Brows = "sad"
                                self.Mouth = "surprised"
                        elif self.Lust >= 70 or Extreme:
                                self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.Lust >= 50:
                                self.Eyes = "sexy"
                                self.Brows = "sad"
                                self.Mouth = "lipbite"
                        elif self.Lust >= 30:
                                self.Eyes = "sexy"
                                self.Brows = "normal"
                                self.Mouth = "kiss"
                        else:
                                self.Eyes = "sexy"
                                self.Brows = "normal"
                                self.Mouth = "normal"    
                
                if Partner == self and Trigger4 in ("lick pussy", "lick ass", "blow", "suck breasts"):         
                                self.Mouth = "tongue"   
                elif Trigger3 in ("lick pussy", "lick ass", "suck breasts"):         
                                self.Mouth = "tongue"  
                                
                if self.OCount >= 10:   
                        #If you've fucked her senseless
                        self.Eyes = "stunned"
                        self.Mouth = "tongue"   
                        
                if not self.Loose:     
                        #if anal hurts. . .
                        if Partner != self and (Trigger == "anal" or Trigger == "dildo anal" or Trigger3 == "dildo anal"):  
                            self.Eyes = "closed"
                            self.Brows = "angry"
                    
                if "unseen" in self.RecentActions:
                        self.Eyes = "closed"
                if Partner and self != Partner:
                        Partner.LustFace()
                return
        
        # End Lust Face / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
            
        def OutfitChange(self, OutfitTemp = 0, Spunk = 0, Undressed = 0, Changed = 1,HolderOutfit=[]):
                # $ RogueX.OutfitChange("casual1") 
                # OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed
                #OutfitTemp = self.Outfit if not OutfitTemp else OutfitTemp
                if self not in TotalGirls: #should remove "character don't exist" errors
                        return
                        
                OutfitTemp = OutfitTemp if OutfitTemp else self.Outfit
                
                if OutfitTemp == 5: 
                        #this sets it to default if using AnyOutfit
                        OutfitTemp = self.Outfit
                elif OutfitTemp == 6: 
                        #this sets it to daily default if using AnyOutfit
                        OutfitTemp = self.OutfitDay
                        self.Outfit = self.OutfitDay
                        
#                elif 7 <= OutfitTemp <= 20:
#                        # if Outfittemp is between 7 and 20                        
#                        if OutfitTemp == 7: 
#                                self.Over = TempOver
#                        elif OutfitTemp == 8: 
#                                self.Chest = TempChest
#                        elif OutfitTemp == 9: 
#                                self.Legs = TempLegs
#                        elif OutfitTemp == 10: 
#                                self.Panties = TempPanties
#                        elif OutfitTemp == 11: 
#                                self.Upskirt = TempUpskirt
#                        elif OutfitTemp == 12: 
#                                self.Uptop = TempUptop
#                        elif OutfitTemp == 13: 
#                                self.Hose = TempHose
#                        return
                #Redundant, just change these traits to directly changing the stats instead
                    
                if self.Loc == bg_current and renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
                        #Skips this check if it's a sleepover
                        return
                
                if OutfitTemp != self.Outfit:
                        #if her new outfit is not what she was wearing before,
                        #don't flag the undressed mechanic
                        Changed = 1
                if self in Party and OutfitTemp == self.OutfitDay:
                        #this ignores her daily outfit if she's in a party
                        OutfitTemp = self.Outfit
                if self.Loc not in ("bg showerroom","bg pool") or (OutfitTemp != "nude" and OutfitTemp != "towel"):
                        #Dries her off
                        self.Water = 0
                if self.Spunk:
                        #Removes spunk if told to do so. 
                        if "painted" not in self.DailyActions or "cleaned" not in self.DailyActions:        
                            del self.Spunk[:]  
                 
                #Resets "half-dressed" states
                if self.Upskirt or self.Uptop or self.PantiesDown:
                        Undressed = 1
                
                self.Upskirt = 0
                self.Uptop = 0
                self.PantiesDown = 0
                                       
                if OutfitTemp == "casual1":
                        HolderOutfit = self.Casual1[:] #fills Holder with the values of the sent uni. . .      
                elif OutfitTemp == "casual2":
                        HolderOutfit = self.Casual2[:] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "nude":
                        HolderOutfit = [0,0,0,0,0,0,0,0,0,0,50] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "towel":
                        HolderOutfit = [0,0,0,"towel",0,0,0,0,0,0,35] #fills Holder with the values of the sent uni. . .  
                elif OutfitTemp == "custom1":
                        HolderOutfit = self.Custom1[:] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "custom2":
                        HolderOutfit = self.Custom2[:] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "custom3":
                        HolderOutfit = self.Custom3[:] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "temporary":
                        HolderOutfit = self.TempClothes[:] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "sleep":  
                        HolderOutfit = self.Sleepwear[:] #fills Holder with the values of the sent uni. . .      
                elif OutfitTemp == "gym":
                        HolderOutfit = self.Gym[:] #fills Holder with the values of the sent uni. . .   
                elif OutfitTemp == "swimwear":
                        if not self.Swim[0]:
                                if "bikini top" not in self.Inventory or "bikini bottoms" not in self.Inventory:
                                        #if she doesn't own her swimsuit components. . .
                                        if "swim" not in self.DailyActions:
                                                if self == RogueX:
                                                    ch_r("I don't really have any swimsuit I could wear. . .", interact=True)
                                                elif self == KittyX:
                                                    ch_k("I wish I had something cute to wear, but I don't. . .", interact=True)
                                                elif self == EmmaX:
                                                    ch_e("I really don't own the proper attire. . .", interact=True)
                                                elif self == LauraX:
                                                    ch_l("Don't have a suit. . .", interact=True)
                                        return 0                                   
                                elif self == KittyX and "blue skirt" not in self.Inventory and self.Inbt <= 400:                                        
                                        if "swim" not in self.DailyActions:
                                                    ch_k("I don't know, I do have a suit, but it's a little daring. . .", interact=True)
                                                    ch_k("If only I had a little skirt or something. . .", interact=True)
                                                    return 0
                                else:
                                    self.Swim[0] = 1
                        HolderOutfit = self.Swim[:] #fills Holder with the values of the sent uni. . .   
                #end Holder setting. . .
                while len(HolderOutfit) < 11:
                    HolderOutfit.append(0)                    
                
                if not self.Legs and HolderOutfit[2]:            
                    Undressed = 1
                elif not self.Over and HolderOutfit[3]:          
                    Undressed = 1
                elif not self.Chest and HolderOutfit[5]:          
                    Undressed = 1
                elif not self.Panties and HolderOutfit[6] and "pantyless" not in self.DailyActions:          
                    Undressed = 1
                elif not self.Hose and HolderOutfit[9]:          
                    Undressed = 1
        
                self.Arms = HolderOutfit[1]
                self.Legs = HolderOutfit[2]
                self.Over = HolderOutfit[3]
                self.Neck = HolderOutfit[4]
                self.Chest = HolderOutfit[5]
                self.Panties = HolderOutfit[6]
                self.Acc = HolderOutfit[7]
                self.Hair = HolderOutfit[8] if HolderOutfit[8] else self.Hair 
                self.Hose = HolderOutfit[9]        
                self.Shame = HolderOutfit[10]
                         
                if self.Panties and self.Panties != "shorts" and "pantyless" in self.DailyActions:       
                        # This checks the pantyless state from flirting 
                        if OutfitTemp != "sleep" and OutfitTemp != "gym":
                                self.Panties = 0        
        #                renpy.call(OutfitShame,self,0,1)
                        #make sure that this element accurately checks to decide whether she would wear this outfit with or without panties.
                        
                if not Changed and OutfitTemp == self.Outfit and self.Loc == bg_current:
                        #If she was partially dressed then it says she gets dressed
                        if Undressed == 2:
                                renpy.say(None,self.Name+" throws on a towel.", interact=True)
                        elif Undressed:
                                renpy.say(None,self.Name+" throws her clothes back on.", interact=True)
                if Undressed:
                    return 2
                return 1
                #End Outfits
        
        # End Outfits / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        
        def Set_Temp_Outfit(self):
                    # This takes whatever the girl is wearing, and sets it as the temporary outfit
                    # $ RogueX.Set_Temp_Outfit()
                    self.TempClothes[1] = self.Arms  
                    self.TempClothes[2] = self.Legs 
                    self.TempClothes[3] = self.Over
                    self.TempClothes[4] = self.Neck 
                    self.TempClothes[5] = self.Chest 
                    self.TempClothes[6] = self.Panties
                    self.TempClothes[7] = self.Acc
                    self.TempClothes[8] = self.Hair
                    self.TempClothes[9] = self.Hose
                    self.TempClothes[0] = 1 
                    self.Outfit = "temporary"
                    self.OutfitDay = "temporary"  
                    return
            
        def ChestNum(self): 
                    #This function determines how much Bra are on, 5 for decent, less for less. 
                    if self.Uptop and self.Chest:
                        return 1
                    if self == RogueX:  
                            if self.Chest == "tank":
                                return 5
                    if self == LauraX:
                            if self.Chest == "leather bra":
                                return 5         
                            elif self.Chest == "wolvie top":
                                return 3        
                            elif self.Chest == "lace corset":
                                return 2 
                    if self.Chest == "lace bra":
                        return 2
                    elif self.Chest == "corset":
                        return 5   
                    elif self.Chest:
                        return 4             
                    #if it falls though. . .
                    return 0 
        
        def OverNum(self): 
                    #This function determines how much Over are on, 5 for decent, less for less.
                    if self.Uptop and self.Over:
                        return 1
                    if self == RogueX:                    
                            if self.Over == "mesh top":
                                return 2
                    if self == KittyX:                    
                            if self.Over == "pink top":
                                return 4             
                    if self.Over == "towel":
                        return 3    
                    elif self.Over == "jacket":
                        return 4                            
                    elif self.Over == "nighty":
                        return 3  
                    elif self.Over:
                        return 5       
                    #if it falls though. . .
                    return 0 
                    
        def PantsNum(self): 
                    #This function determines how much pants are on, 10 for pants, 6 for shorts, 5 for skirt, <5 for non-covering.
                    if self.Upskirt and self.Legs:
                                return 1
                    if self == RogueX and self.Panties == "shorts":
                                return 6
                    elif self == KittyX:
                            if self.Legs == "black jeans":
                                return 10            
                            elif self.Legs == "capris":
                                return 10                 
                            elif self.Legs == "shorts":
                                return 6       
                            elif self.Legs == "blue skirt":
                                return 4 #5?
                    elif self == LauraX:
                            if self.Legs == "leather pants":
                                return 10    
                            elif self.Legs == "mesh pants":
                                return 2  
                    if self.Legs == "skirt":
                                return 5
                    elif self.Legs == "yoga pants":
                                return 8       
                    elif self.Legs == "pants":
                                return 10
                        
                    #if it falls though. . .
                    return 0 
        
        def PantiesNum(self): 
                    #This function determines how much panties are on, 5 for decent, less for less.
                    if self.PantiesDown and self.Panties:
                        return 1
                    if self.Panties == "lace panties":
                        return 2    
                    elif self.Panties == "sports panties":
                        return 8   
                    elif self.Panties == "bikini bottoms":
                        return 7     
                    elif self.Panties:
                        return 5
                    return 0 
                    
        def HoseNum(self): 
                    #This function determines how seethrough her hose is, 5 for "visible," 10 for "solid"
                    if self.Hose and (self.PantiesDown or self.Upskirt):
                        return 1
                    if self.Hose == "stockings":
                        return 1
                    elif self.Hose == "pantyhose":
                        return 6
                    elif self.Hose == "tights":
                        return 10
                    elif self.Hose == "stockings and gaterbelt":
                        return 4
                    elif self.Hose == "ripped pantyhose":
                        return 4
                    elif self.Hose == "ripped tights":
                        return 4   
                    #if it falls though. . .        
                    return 0 
           
        def ClothingCheck(self, C = 0): 
                    C = 0
                    #This function counts how many items of clothing she has on and returns that number.
                    if self.Over:
                        C += 1
                    if self.Chest:
                        C += 1
                    if self.Legs:
                        C += 1
                    if self.HoseNum() >= 5: #double check this one. . .
                        C += 1
                    if self.Panties:
                        C += 1
                    return C 
                    
        def SeenCheck(self, Check=0, C = 0): 
                    C = 0
                    #This function returns 1-2 if she is partiallly naked and this is the first the player's seen of it.
                    # "Check" is 1 if it's intended to see whether she has been seen at all.
                    # "Check" is 2 if it's intended to see whether she has been seen topless.
                    # "Check" is 3 if it's intended to see whether she has been seen bottomless.
                    if not self.SeenChest:
                        if (not self.Over and not self.Chest) or self.Uptop or Check == 1 or Check == 2:
                                    C += 1
                    if not self.SeenPussy:
                        if Check == 1 or Check == 3:
                                    C += 1
                        elif not self.Legs or self.Upskirt: 
                            #if no pants or pants down
                            if self.PantiesDown or (self.HoseNum() < 5 and not self.Panties): 
                                    # if no panties and loose hose or they're down
                                    C += 1                  
                    return C 
        # End Clothing Checks / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        
        
        # Girl interactions / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        def GirlLikeCheck(self,Chr=0):  
                # RogueX.GirlLikeCheck(KittyX) will return RogueX.LikeKitty, ie 600
                return getattr(self,"Like"+Chr.Tag)
                
        def GirlLikeUp(self,Chr=0,Value=0,Like=0):  
                # RogueX.GirlLikeUp(Kitty,5) will return RogueX.LikeKitty += 5
                Like = getattr(self,"Like"+Chr.Tag) #Like = RogueX.LikeKitty
                if Like + Value > 1000:
                        setattr(self,"Like"+Chr.Tag, 1000)
                elif Like + Value < 0:
                        setattr(self,"Like"+Chr.Tag, 0)
                else:
                        setattr(self,"Like"+Chr.Tag, Value + Like) #RogueX.LikeKitty = RogueX.LikeKitty + Value
                return 
                
        def GLG(self, ChrB = 0, Check=200, Modifier = 1, Auto = 0, Jealousy = 0, Ok = 0, Likes=0):
                # self is the subject girl, ChrB is the object girl,
                # Modifier is sent as the amount of offense this might cause,
                # Jealousy is the temp value for how mad the girl will get
                # Likes stores the XLikesY stat temporarily
                # Auto quickly raises lust and like by a sent amount
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.
                
                # was call GirlLikesGirl(Party[0],Party[1],700,5,1)
                # now $ RogueX.GLG(Party[1],700,5,1)
                if self not in TotalGirls or ChrB not in TotalGirls: #should remove "character don't exist" errors
                        return  
                Jealousy = 0
                Likes = self.GirlLikeCheck(ChrB)
                #stores this value temporarily
                
                if Likes <= Check: 
                        #if the checked girl likes the second girl less than the checked value. . .                        
                        if Auto:
                                #if set to auto, just raises the Like stat by the modifier value.
                                setattr(self,"Like"+ChrB.Tag,Likes+Modifier) #updates Like modifier
                                self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5th modifier
                                return
                        
                        # checks if they have agreed to share or not
                        if "dating" in self.Traits or self in Player.Harem:                            
                                #if "dating" in RogueX.Traits or RogueX in Player.Harem:
                                if ChrB not in Player.Harem and "poly " + ChrB.Tag not in self.Traits:
                                        # if KittyX not in Player.Harem and "poly Kitty" not in RogueX.Traits:
                                        Jealousy = 100
                elif Auto: #this is a quick return, 
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5th modifier
                            return        
                                  
                #Establishes how jealous lead is likely to get
                Jealousy += (self.Love - 600) if self.Love > 600 else 0
                        #How much her Love stat is over 600, +0-400
                Jealousy += self.SEXP if self.Inbt <= 500 else 0  
                        #plus her SexP rating if she has low inhibitions, +0-200
                Jealousy -= (self.Obed - 250) if self.Obed > 250 else 0
                        #minus how much her Obed stat is over 250, -0-750
                        # = result of up to 700 if high love, dating, and low obedience
 
                Jealousy = 0 if Jealousy < 1 else Jealousy                    
                    #Balances it to no less than zero                    
                Modifier += 1 if not Jealousy and Likes >= 500 else 0   
                    #+ modifier if she doesn't hate Kitty but has no jealousy left
                            
                                
                if Likes >= 900:          
                            #If she really likes the girl, then she is turned on, likes both of you more. 
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/2))) #raises Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 2                
                elif Likes >= 800:        
                        #If she mostly likes the girl, and is not super jealous, she likes you both more. 
                        if Jealousy <= 300:
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/2))) #raises Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/2 modifier
                            Ok = 2
                        else:
                            Likes -= Modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 1                        
                elif Likes >= 600:        
                        #If she's friends with the girl, only low jealousy is positive
                        if Jealousy <= 100:
                            Likes += Modifier
                            self.Statup("Love", 80, (int(Modifier/4))) #raises Love by 1/4 modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/2 modifier
                            Ok = 2
                        elif Jealousy <= 300:
                            Likes -= Modifier
                            self.Statup("Lust", 200, (int(Modifier/2))) #raises Lust by 1/5 modifier
                            Ok = 1
                        else:                            
                            Likes -= (Modifier + (int(Jealousy/50)))
                            self.Statup("Love", 90, (-(int(Modifier)))) #lowers Love by 1/2 modifier
                            self.Statup("Lust", 200, (int(Modifier/5))) #raises Lust by 1/5 modifier
                            Ok = 2
                elif Likes >= 400:       
                        #If she is neutral to the girl, it's all negative                 
                        if Jealousy <= 100:
                            Likes -= Modifier
                            Ok = 1
                        else:
                            Likes -= (Modifier + (int(Jealousy/100)))
                        self.Statup("Lust", 200, (int(Modifier/10))) #raises Lust by 1/10 modifier
                else:                           
                        #If she hates the girl, it's all very negative
                        Likes -= (Modifier + (int(Jealousy/50)))
                        self.Statup("Lust", 200, (int(Modifier/10))) #raises Lust by 1/5 modifier
                self.Statup("Inbt", 60, (int(Modifier/10))) #raises Inbt by 1/10 modifier
                          
                # restores "likes" to target character. 
                
                setattr(self,"Like"+ChrB.Tag,Likes+Modifier) #updates Like modifier
                                        
                return Ok
                # returns 2 if very into it, 1 if ok with it, 0 if not cool with it.
        # End Girl Like girl stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
        
        
        def NameCheck(self, Cnt = 0):
                #Checks how she reacts to you using her petname
                #Cnt and Ugh are internal count variable
                # $ RogueX.NameCheck() #nee 
                if self.Pet == self.Name:
                        return 0   
                if self.Taboo:
                        # +4 if Taboo 40, +2 if Taboo 20
                        Cnt = int(self.Taboo/10) 
                        
                #easy options
                if self.Pet in ("girl","boo","bae","baby","sweetie"):
                    if ApprovalCheck(self, 500, "L", TabM=1,Alt=[[LauraX],600]):       
                        self.Statup("Love", 80, 1)
                    else:
                        self.Statup("Love", 50, -1)
                        return 1                         
                elif self.Pet == "sexy" or self.Pet == "lover":
                    if ApprovalCheck(self, 900, TabM=1,Alt=[[LauraX],1100]):    
                        self.Statup("Love", 80, 2)
                        self.Statup("Obed", 80, 1)
                        self.Statup("Inbt", 70, 1) 
                    else:                                                            
                        self.Statup("Love", 50, (-1-Cnt))
                        self.Statup("Obed", 50, 1)
                        self.Statup("Inbt", 20, -1)
                        return 1                       
                #tougher options
                elif self.Pet == "slave":                      
                        if ApprovalCheck(self, 800, "O", TabM=3,Alt=[[EmmaX],900]):
                            self.Statup("Lust", 90, (3+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 30, 1)
                            self.Statup("Inbt", 70, 1)     
                        elif ApprovalCheck(self, 500, "O", TabM=3,Alt=[[EmmaX],600]):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, -1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)        
                        else:                         
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 50, -1)
                            return 1               
                elif self.Pet == "pet":
                        if ApprovalCheck(self, 1500, TabM=2,Alt=[[LauraX],800]):
                            self.Statup("Lust", 90, (3+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 30, 1)
                            self.Statup("Inbt", 70, 1)     
                        elif ApprovalCheck(self, 1200, TabM=2,Alt=[[LauraX],650]): 
                            self.Statup("Lust", 60, 1)
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)        
                        else:
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 50, -1)
                            return 1                       
                elif self.Pet == "slut":
                        if ApprovalCheck(self, 500, "O", TabM=2) or ApprovalCheck(self, 500, "I", TabM=2,Alt=[[LauraX],400]): 
                            self.Statup("Lust", 90, (4+Cnt))
                            self.Statup("Obed", 95, (2+Cnt))
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 300, "O", TabM=2) or ApprovalCheck(self, 300, "I", TabM=2,Alt=[[LauraX],200]):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, (2+Cnt))
                            self.Statup("Inbt", 70, 1)        
                        else:     
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1                       
                elif self.Pet == "whore":
                        if ApprovalCheck(self, 600, "O", TabM=2,Alt=[[EmmaX],700]) or ApprovalCheck(self, 600, "I", TabM=2,Alt=[[LauraX],400]): 
                            self.Statup("Lust", 90, 4)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 50, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 400, "O", TabM=2,Alt=[[EmmaX],500]) or ApprovalCheck(self, 400, "I", TabM=2):
                            self.Statup("Lust", 90, 1)
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Obed", 80, 2)
                            self.Statup("Inbt", 70, 1)
                        else:  
                            self.Statup("Love", 200, (-3-Cnt))
                            self.Statup("Love", 50, (-2-Cnt), 1)
                            self.Statup("Obed", 50, 1)            
                            self.Statup("Inbt", 21, 1, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1                       
                elif self.Pet == "sugartits":
                        if ApprovalCheck(self, 1500, TabM=1,Alt=[[EmmaX],1300]):  
                            self.Statup("Obed", 80, 1)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 70, 1,Alt=[[EmmaX],70,2])            
                            self.Statup("Inbt", 30, 2,Alt=[[KittyX],60,3])
                        else:                                                                       
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1                       
                elif self.Pet == "sex friend":    
                        if ApprovalCheck(self, 750, "O", TabM=1) or ApprovalCheck(self, 600, "I", TabM=1):  
                            self.Statup("Lust", 90, 3)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 80, 1)
                        elif ApprovalCheck(self, 600, "O", TabM=1) or ApprovalCheck(self, 400, "I", TabM=1): 
                            self.Statup("Lust", 90, 2)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                            self.Blush = 1
                        else:  
                            self.Statup("Love", 200, -Cnt)
                            self.Statup("Love", 50, (-1-Cnt), 1)
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1                       
                elif self.Pet == "fuckbuddy":
                        if ApprovalCheck(self, 700, "O", TabM=2) or ApprovalCheck(self, 700, "I", TabM=1): 
                            self.Statup("Lust", 90, 3)
                            self.Statup("Obed", 95, 2)
                            self.Statup("Inbt", 40, 2)
                            self.Statup("Inbt", 85, 1)
                        elif ApprovalCheck(self, 600, "O", TabM=2) or ApprovalCheck(self, 500, "I", TabM=1): 
                            self.Statup("Lust", 90, 2)
                            self.Statup("Love", 200, (-1-Cnt))
                            self.Statup("Obed", 80, 1)
                            self.Statup("Inbt", 70, 1)
                            self.Blush = 1
                        else:            
                            self.Statup("Love", 200, -Cnt)
                            self.Statup("Love", 60, (-2-Cnt), 1)
                            self.Statup("Obed", 60, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1                       
                elif self.Pet == "baby girl" or self.Pet == "mommy":
                        if ApprovalCheck(self, 1200, TabM=1): 
                            self.Statup("Obed", 80, 1)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 70, 1)            
                            self.Statup("Inbt", 30, 2)
                        else:                                                                       
                            self.Statup("Love", 200, (-2-Cnt))
                            self.Statup("Love", 50, (-1-Cnt))
                            self.Statup("Obed", 50, 1)
                            self.Statup("Inbt", 20, -1)
                            return 1
                #Rogue
                elif self.Pet == "chere":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Kitty
                elif self.Pet == "kitten":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Emma
                elif self.Pet == "darling":
                        if ApprovalCheck(self, 600, "L", TabM=1):
                            self.Statup("Love", 80, 2)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                #Laura        
                elif self.Pet == "Wolvie":
                        if ApprovalCheck(self, 500, "I", TabM=1):
                            self.Statup("Love", 80, 1)
                        else:
                            self.Statup("Love", 50, -1)
                            return 1
                elif self.Pet == "X-23":   
                        if ApprovalCheck(self, 800, "O"):
                            self.Statup("Lust", 90, 3) 
                            self.Statup("Love", 90, -1)  
                            self.Statup("Obed", 95, 2)                                   
                        elif ApprovalCheck(self, 700, "L") and not ApprovalCheck(self, 500, "O"):
                            self.Statup("Love", 200, -2)
                            self.Statup("Love", 50, -1, 1)
                            self.Statup("Obed", 30, 2)
                            self.Statup("Obed", 50, 2)
                            self.Statup("Inbt", 50, -1)
                            return 1
                return 0
        # End Petname Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
                                
#End Girls Class / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Girl Stats and Details / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
# Start Emotion editor / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label EmotionEditor(Chr=0):
        # call EmotionEditor(RogueX)
        while True:
            menu:
                "Emotions1: Normal Angry Smiling Sexy Surprised Bemused Manic.":        
                    menu:
                        "Normal":
                            $ Chr.Emote = "normal"
                        "Angry":
                            $ Chr.Emote = "angry"
                        "Smiling":
                            $ Chr.Emote = "smile"
                        "Sexy":
                            $ Chr.Emote = "sexy"
                        "Suprised":
                            $ Chr.Emote = "surprised"
                        "Bemused":
                            $ Chr.Emote = "bemused"
                        "Manic":
                            $ Chr.Emote = "manic"
                            
                "Emotions2: Sad Sucking Kiss Tongue Confused Closed Down.":  
                    menu:
                        "Sad":
                            $ Chr.Emote = "sad"
                        "Sucking":
                            $ Chr.Emote = "sucking"
                        "kiss":
                            $ Chr.Emote = "kiss"
                        "Tongue":
                            $ Chr.Emote = "tongue"
                        "confused":
                            $ Chr.Emote = "confused"
                        "Closed":
                            $ Chr.Emote = "closed"
                        "Down":
                            $ Chr.Emote = "down"
                            
                "Emotions3: Sadside Startled Perplexed Sly":  
                    menu:
                        "Sadside":
                            $ Chr.Emote = "sadside"
                        "Startled":
                            $ Chr.Emote = "startled"
                        "Perplexed":
                            $ Chr.Emote = "perplexed"
                        "Sly":
                            $ Chr.Emote = "sly"
                    #$ Chr.FaceChange
                "Toggle Mouth Spunk":
                    if "mouth" in Chr.Spunk:
                        $ Chr.Spunk.remove("mouth")
                    else:
                        $ Chr.Spunk.append("mouth")
                "Toggle hand Spunk":
                    if "hand" in Chr.Spunk:
                        $ Chr.Spunk.remove("hand")
                    else:
                        $ Chr.Spunk.append("hand")
                        
                "Toggle Facial Spunk":
                    if "facial" in Chr.Spunk and "hair" not in Chr.Spunk:
                        $ Chr.Spunk.append("hair")
                    elif "facial" in Chr.Spunk:
                        $ Chr.Spunk.remove("facial")                
                        $ Chr.Spunk.remove("hair")
                    else:
                        $ Chr.Spunk.append("facial")
                    
                "Blush":
                    if Chr.Blush == 2:
                        $ Chr.Blush = 0
                    elif Chr.Blush:
                        $ Chr.Blush = 2
                    else:
                        $ Chr.Blush = 1  
                "Exit.":
                    return
            $ Chr.FaceChange() #applies change
        #end Emotion Editor

label WardrobeEditor(Chr=0):
    while True:
        menu Wardrobe_Menu:      
            "View" if True:
                while True:
                    menu:
                        "Default":
                            call expression Chr.Tag + "_Pos_Reset"
                        "Face":
                            call expression Chr.Tag + "_Kissing_Launch" pass (0)
                        "Body":
                            call expression Chr.Tag + "_Pussy_Launch" pass (0)
                        "BJ":
                            if not renpy.showing(Chr.Tag+"_BJ_Animation"):
                                call expression Chr.Tag + "_BJ_Launch"
                            else:
                                call expression Chr.Tag + "_BJ_Reset"
                        "HJ":
                            if not renpy.showing(Chr.Tag+"_HJ_Animation"):
                                call expression Chr.Tag + "_HJ_Launch"
                            else:
                                call expression Chr.Tag + "_HJ_Reset"
                        "TJ":
                            if not renpy.showing(Chr.Tag+"_TJ_Animation"):
                                call expression Chr.Tag + "_TJ_Launch"
                            else:
                                call expression Chr.Tag + "_TJ_Reset"
                        "Doggy" if Chr == RogueX:
                            if not renpy.showing(Chr.Tag+"_Doggy"):
                                call expression Chr.Tag + "_Doggy_Launch"
                            else:
                                call expression Chr.Tag + "_Doggy_Reset"
                        "Sexpose" if Chr != RogueX:
                            if not renpy.showing(Chr.Tag+"_SexSprite"):
                                call expression Chr.Tag + "_Sex_Launch"
                            else:
                                call expression Chr.Tag + "_Sex_Reset"
                        "Back":
                            pass
            # Outfits
            "First casual outfit":
                $ Chr.Outfit = "casual1"
                $ Chr.OutfitChange() 
            "Second casual outfit":
                $ Chr.Outfit = "casual2"
                $ Chr.OutfitChange() 
            "Nude":
                $ Chr.Outfit = "nude"
                $ Chr.OutfitChange() 
            "Over":              
                while True:
                    menu:
                        # Overshirts    
                        "Remove [Chr.Over]" if Chr.Over:
                            $ Chr.Over = 0
                        "Add mesh top" if Chr == RogueX:
                            $ Chr.Over = "mesh top"
                            $ Chr.Neck = "spiked collar"
                            $ Chr.Arms = "gloves"
                            if Chr.Chest == "buttoned tank":
                                $ Chr.Chest = "tank"     
                        "Add pink top" if Chr == RogueX:
                            $ Chr.Over = "pink top"  
                            $ Chr.Arms = "gloves"
                        "Add nighty":
                            $ Chr.Over = "nighty"   
                            $ Chr.Arms = 0
                        "Add towel":
                            $ Chr.Over = "towel"   
                            $ Chr.Arms = 0
                        "Toggle up-top":
                            if Chr.Uptop:
                                $ Chr.Uptop = 0
                            else:
                                $ Chr.Uptop = 1   
                        "Back":
                            jump Wardrobe_Menu                
            "Tops":            
                while True:
                    menu:
                        # Tops    
                        "Remove [Chr.Chest]" if Chr.Chest:
                            $ Chr.Chest = 0
                        "Add tank top" if Chr == RogueX:
                            $ Chr.Chest = "tank"
                        "Add sports bra":
                            $ Chr.Chest = "sports bra"
                        "Add buttoned tank top" if Chr == RogueX:
                            $ Chr.Chest = "buttoned tank"
                        "Add lace bra":
                            $ Chr.Chest = "lace bra"
                        "Add bra":
                            $ Chr.Chest = "bra"     
                        "Add bikini":
                            $ Chr.Chest = "bikini top"       
                        "Toggle up-top":
                            if Chr.Uptop:
                                $ Chr.Uptop = 0
                            else:
                                $ Chr.Uptop = 1                         
                        "Toggle Piercings":
                            if Chr.Pierce == "ring":
                                $ Chr.Pierce = "barbell"
                            elif Chr.Pierce == "barbell":
                                $ Chr.Pierce = 0
                            else:
                                $ Chr.Pierce = "ring"
                        "Back":
                            jump Wardrobe_Menu  
            
            "Legs":            
                while True:
                    menu:
                        # Legs   
                        "Remove legs" if Chr.Legs:     
                            $ Chr.Legs = 0
                        "Add Skirt":  
                            $ Chr.Legs = "skirt"
                            $ Chr.Upskirt = 0
                        "Add pants":
                            $ Chr.Legs = "pants"
                            $ Chr.Hose = 0
                        "Toggle upskirt":
                            if Chr.Upskirt:
                                $ Chr.Upskirt = 0
                            else:
                                $ Chr.Upskirt = 1
                        "Back":
                            jump Wardrobe_Menu  
            
            "Underwear":            
                while True:
                    menu:
                        # Underwear
                        "Hose":
                            menu:
                                "Add hose":     
                                    $ Chr.Hose = "stockings"  
                                "Add garter":     
                                    $ Chr.Hose = "garterbelt"  
                                "Add stockings and garter":     
                                    $ Chr.Hose = "stockings and garterbelt"  
                                "Add pantyhose":     
                                    $ Chr.Hose = "pantyhose"   
                                "Add tights":     
                                    $ Chr.Hose = "tights"   
                                "Add ripped hose":     
                                    $ Chr.Hose = "ripped pantyhose"   
                                "Add ripped tights":     
                                    $ Chr.Hose = "ripped tights"   
                                "Add tights":     
                                    $ Chr.Hose = "tights"    
                                "Remove hose" if Chr.Hose:     
                                    $ Chr.Hose = 0  
                        "Remove panties" if Chr.Panties:     
                            $ Chr.Panties = 0     
                        "Add black panties":
                            $ Chr.Panties = "black panties"
                        "Add bikini":
                            $ Chr.Panties = "bikini bottoms"
                        "Add shorts":
                            $ Chr.Panties = "shorts"
                        "Add green panties":
                            $ Chr.Panties = "green panties"  
                        "Add lace panties":
                            $ Chr.Panties = "lace panties"    
                        "pull down-up panties":
                            if Chr.PantiesDown:
                                $ Chr.PantiesDown = 0
                            else:
                                $ Chr.PantiesDown = 1
                        "Back":
                            jump Wardrobe_Menu  
            "Misc":
                while True:
                    menu: 
                        "Emotions":
                            call EmotionEditor(Rogue)
                        "Toggle Arms":
                            if Chr.ArmPose == 1:
                                $ Chr.ArmPose = 2
                            else:
                                $ Chr.ArmPose = 1
                        "Toggle Wetness":
                            if not Chr.Wet:
                                $ Chr.Wet = 1
                            elif Chr.Wet == 1:
                                $ Chr.Wet = 2
                            else:
                                $ Chr.Wet  = 0
                        "Toggle wet look":
                            if not Chr.Water:
                                $ Chr.Water = 1
                            elif Chr.Water == 1:
                                $ Chr.Water = 3
                            else:
                                $ Chr.Water  = 0
                        "Toggle pubes":
                            if not Chr.Pubes:
                                $ Chr.Pubes = 1
                            else:
                                $ Chr.Pubes = 0
                        "Toggle held":
                            if not Chr.Held:
                                $ Chr.Held  = "phone"
                            elif Chr.Held == "phone":
                                $ Chr.Held  = "dildo"
                            elif Chr.Held == "dildo":
                                $ Chr.Held  = "vibrator"
                            elif Chr.Held == "vibrator":
                                $ Chr.Held  = "panties"
                            else:
                                $ Chr.Held  = 0    
                        "Add Gloves" if not Chr.Arms:
                            $ Chr.Arms = "gloves"
                        "Remove Gloves" if Chr.Arms:
                            $ Chr.Arms = 0
                        "Back":
                            jump Wardrobe_Menu   
            "Nothing":
                return
return

# Start StatHacks / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label StatHacks(Chr=0,Cnt=0): 
    while True:
            menu:
                "[Chr.Name]: Love: [Chr.Love], Obedience: [Chr.Obed], Inhibition:[Chr.Inbt], Lust: [Chr.Lust] Taboo: [Taboo], Location: [Chr.Loc]"
                "Activities":
                    menu:
                        "Recent Actions":
                            "[Chr.RecentActions]"
                        "Daily Actions":
                            "[Chr.DailyActions]"
                        "Traits":
                            "[Chr.Traits]"
                        "History":
                            "[Chr.History]"
                "Gwen's face" if False:
                    call Gwen_FaceEditor
                "Raise Love":
                    $ Chr.Love += 100
                "Lower Love":
                    $ Chr.Love -= 100
                "Raise Obedience":
                    $ Chr.Obed += 100
                "Lower Obedience":
                    $ Chr.Obed -= 100
                "Raise Inhibitions":
                    $ Chr.Inbt += 100
                "Lower Inhibitions":
                    $ Chr.Inbt -= 100
                "Taboo toggle":
                    $ Taboo = 40 if Taboo != 40 else 0
                    "[Taboo]"
                "Small":
                    $ Cnt = 1
                    while Cnt:
                        menu:
                            "Raise Love":
                                $ Chr.Love += 10
                            "Lower Love":
                                $ Chr.Love -= 10
                            "Raise Obedience":
                                $ Chr.Obed += 10
                            "Lower Obedience":
                                $ Chr.Obed -= 10
                            "Raise Inhibitions":
                                $ Chr.Inbt += 10
                            "Lower Inhibitions":
                                $ Chr.Inbt -= 10
                            "Back":
                                $ Cnt = 0                 
                "Other":
                    menu:        
                        "Raise Lust":
                            $ Chr.Lust += 10
                        "Lower Lust":
                            $ Chr.Lust -= 10
                        "Raise Addiction":
                            $ Chr.Addict += 10
                        "Lower Addiction":
                            $ Chr.Addict -= 10
                        "Back":
                            pass
                "Wardrobe":
                    call WardrobeEditor(Chr)
                    
                "Return":
                    call Checkout
                    return
    

label Cheat_Menu(Girl=0):
        if Girl not in TotalGirls:
                $ Girl = Ch_Focus
        menu:
            "Level-Up":
                $ Girl.Hand += 5
                $ Girl.Blow += 5
                $ Girl.Swallow += 5
                $ Girl.Hand += 5
                $ Girl.Slap += 5
                $ Girl.Tit += 5
                $ Girl.Sex += 5
                $ Girl.Anal += 5
                $ Girl.Hotdog += 5
                $ Girl.Mast += 5
                $ Girl.Org += 5
                $ Girl.FondleB += 5
                $ Girl.FondleT += 5
                $ Girl.FondleP += 5
                $ Girl.FondleA += 5
                $ Girl.DildoP += 5
                $ Girl.DildoA += 5
                $ Girl.Plug += 5
                $ Girl.SuckB += 5
                $ Girl.InsertP += 5
                $ Girl.InsertA += 5
                $ Girl.LickP += 5    
                $ Girl.LickA += 5
                $ Girl.Blow += 5
                $ Girl.Swallow += 5
                $ Girl.CreamP += 5
                $ Girl.CreamA += 5
                $ Girl.SeenChest = 1
                $ Girl.SeenPanties = 1
                $ Girl.SeenPussy = 1
                "Hand [Girl.Hand], Blow [Girl.Blow], Swallow [Girl.Swallow]"
            "Level Reset":
                $ Girl.Hand = 0
                $ Girl.Blow = 0
                $ Girl.Swallow = 0
                "Hand [Girl.Hand], Blow [Girl.Blow], Swallow [Girl.Swallow]"
            "Toggle Taboo":
                if not Taboo:
                    $ Taboo = 40
                else:
                    $ Taboo = 0
            "Maxed":
                    $ Girl.Love = 1000
                    $ Girl.Inbt = 1000
                    $ Girl.Obed = 1000
                    $ Girl.Lust = 50
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 0 #How faster her addiciton rises
                    $ Girl.Kissed = 1 #How many times they've kissed
                    $ Girl.Swallow = 0
            "50\%":
                    $ Girl.Love = 500
                    $ Girl.Inbt = 500
                    $ Girl.Obed = 500
                    $ Girl.Lust = 65
                    $ Girl.Addict = 0 #how addicted she is
                    $ Girl.Addictionrate = 10 #How faster her addiciton rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "25\%":
                    $ Girl.Love = 250
                    $ Girl.Inbt = 250
                    $ Girl.Obed = 250
                    $ Girl.Lust = 85
                    $ Girl.Addict = 10 #how addicted she is
                    $ Girl.Addictionrate = 50 #How faster her addiciton rises
                    $ Girl.Kissed = 10 #How many times they've kissed
                    $ Girl.Swallow = 0
            "Juice up":
                    $ Player.Semen += 5
                    $ Girl.Action = 10
            "Cold Shower":
                    $ Player.Focus = 0
            "Exit":
                return
        jump Cheat_Menu
# End StatHacks / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /      


label Clothing_Schedule_Check(Girl=0,Changed=0,Value=0,Count=0):
        #this clears out clothing items that are out of date. 
        #call Clothing_Schedule_Check("Rogue",3,1)    
        
        # Girl is the checked girl, "changed" is the outfit to compare against
        # Value defaults to 0, but if set, it will only check if the value is not 2.
        # (0-6) = Mon-Sun, (7) Datewear, (8) Teach, (9) Private (skips this one)
        # R_Schedule = [0,0,0,0,0,0,0,0,0,0]  
        # Custom1=3,Cusotm2=5,Custom3=6,Gym=4,Sleep=7,Swim=10
        while Count < 9:  
            if Girl.Clothing[Count] == Changed:
                    if Value:
                        #if the Outfit is custom1, and the outfit is SFW, then leave it alone.
                        if Girl.Clothing[Count] == 3 and Girl.Custom1[0] == 2:
                                pass
                        elif Girl.Clothing[Count] == 5 and Girl.Custom2[0] == 2:
                                pass
                        elif Girl.Clothing[Count] == 6 and Girl.Custom3[0] == 2:
                                pass
                        elif Girl.Clothing[Count] == 4 and Girl.Gym[0] != 1:
                                pass
                        else:
                            $ Girl.Clothing[Count] = 0
                    else:
                            $ Girl.Clothing[Count] = 0   
            $ Count += 1
        return
    
# Start Emergency clothing reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Emergency_Clothing_Reset:
        "This resets all customized clothing to their defaults."
        menu:
            "Do you want to continue?"
            "Yes":
                    $ RogueX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ RogueX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0] 
                    $ RogueX.Casual1 = [2,"gloves","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0]
                    $ RogueX.Casual2 = [2,"gloves","pants","pink top","spiked collar","buttoned tank","black panties",0,0,0,0]
                    $ RogueX.Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ RogueX.Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0,0]
                    
                    $ RogueX.Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0] 
                    $ RogueX.Clothing = [0,0,0,0,0,0,0,0,0,0]   #chooses when she wears what
                    
                    $ KittyX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ KittyX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]   
                    $ KittyX.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0]
                    $ KittyX.Casual2 = [2,0,"black jeans","red shirt",0,"bra","green panties",0,0,0,0]
                    $ KittyX.Gym = [2,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
                    $ KittyX.Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0,0]
                    $ KittyX.Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0] 
                    $ KittyX.Clothing = [0,0,0,0,0,0,0,0,0,0] 
                    
                    $ EmmaX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ EmmaX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
                    $ EmmaX.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0]
                    $ EmmaX.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,0]
                    $ EmmaX.Gym = [2,0,0,0,0,"sports bra","sports panties",0,0,0,0]
                    $ EmmaX.Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0,0]
                    $ EmmaX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
                    $ EmmaX.Clothing = [0,0,0,0,0,0,0,0,0,0] 
                    
                    $ LauraX.Custom1 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ LauraX.Custom3 = [0,0,0,0,0,0,0,0,0,0,0]    
                    $ LauraX.Casual1 = [2,"wrists","leather pants",0,0,"leather bra","leather panties",0,0,0,0]
                    $ LauraX.Casual2 = [2,0,"skirt",0,"jacket","corset","leather panties",0,0,0,0]
                    $ LauraX.Gym = [2,"wrists","leather pants",0,0,"leather bra","leather panties",0,0,0,0]
                    $ LauraX.Sleepwear = [0,0,0,0,0,"leather bra","leather panties",0,0,0,0]
                    $ LauraX.Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
                    $ LauraX.Clothing = [0,0,0,0,0,0,0,0,0,0] 
                    "Done."
                    "You will now need to set their custom outfits again."
            "No":
                pass
        return
# End Emergency clothing reset / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
# End Girl Stats and Details / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


label AnyLine(Girl=0,Templine=". . ."):
        #This calls a line from any girl you reference 
        # call AnyLine(Girl,Line)
        if Girl not in TotalGirls: #should remove "character don't exist" errors
                $ Girl = Ch_Focus
                
        $ global PassLine
        $ PassLine = Templine
        if Girl == RogueX:
                ch_r "[PassLine]"
        elif Girl == KittyX:
                ch_k "[PassLine]"
        elif Girl == EmmaX:
                ch_e "[PassLine]"
        elif Girl == LauraX:
                ch_l "[PassLine]"
        return               
    
label GirlsAngry(Girls = 0,BO=[]):
        # Causes girls to storm off if you've pissed them off. 
        $ Tempmod = 0
        $ BO = TotalGirls[:]                
        while BO:
                if BO[0].Loc == bg_current and "angry" in BO[0].RecentActions:
                        if bg_current == BO[0].Home:  
                                if BO[0] == RogueX:
                                        ch_r "You should get out, I'm fix'in ta throw down."
                                elif BO[0] == KittyX:
                                        ch_k "You should get out of here, I can't even look at you right now."
                                elif BO[0] == EmmaX:
                                        ch_e "You should leave, or do you want to test me?"
                                elif BO[0] == LauraX:
                                        ch_l "You should leave."
                                "You head back to your room."
                                $ Party = []
                                $ renpy.pop_call()
                                jump Player_Room_Entry
                        else:        
                                $ BO[0].Loc = BO[0].Home           
                        if BO[0] in Party:
                                $ Party.remove(BO[0]) 
                        if Girls:
                            ". . . and so does [BO[0].Name]."
                        else:
                            "[BO[0].Name] storms off."
                        $ Girls += 1
                        if BO[0] == RogueX:
                                hide Rogue_Sprite with easeoutleft
                        if BO[0] == KittyX:
                                hide Kitty_Sprite with easeoutleft
                        if BO[0] == EmmaX:
                                hide Emma_Sprite with easeoutleft
                        if BO[0] == LauraX:
                                hide Laura_Sprite with easeoutleft
                $ BO.remove(BO[0])
        return    
        
    
# Start Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label LastNamer(Wordcount = 0, Splitname = 0, Lastname = 0):
        # Wordcount = number of words
        $ Wordcount = Player.Name.count(" ")
        
        # Splitname turns the name into a list, ie [Charles, Francis, Xavier]
        $ Splitname = Player.Name.split()
        
        # Lastname picks the last word in that set
        $ Lastname = "Mr. " + Splitname[Wordcount]
        return Lastname
    
# End Last Namer / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

# Start Drain All / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label DrainAll(Word=0,Recent=1,Daily=1,Traits=0):
        # called to remove words from all girls in the game. 
        # call DrainAll("arriving")
        $ BO = TotalGirls[:]
        while BO:
            $ BO[0].DrainWord(Word,Recent,Daily,Traits)
            $ BO.remove(BO[0])
        return
        

# Start Clothes Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

 
# Start Clothes Scheduling / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Clothes_Schedule(Girl=0,Cnt = 0):
        #Sets clothing for different days, if Cnt is 3 it's all days, 2 is TuThu, 1 is only weekends
        #Schedule 0-6= mon-fri, Schedule 7 is dates, 9 is private  
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
    
        if Girl == RogueX:   
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_r "So, you'd like to choose what I wear for the week? Ok, shoot."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_r "I guess I could set aside a few schooldays for you."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_r "We can talk about what I wear outside of classes."
                        $ Cnt = 1
                else:
                        ch_r "You know, I don't really need fashion advice from you."
                        return   
        elif Girl == KittyX:        
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_k "Let me know what you like."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_k "I could let you pick a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_k "We could talk about weekends, maybe. . ."
                        $ Cnt = 1
                else:
                        ch_k "I think I'll[Girl.like]figure out my own outfits."
                        return
        elif Girl == EmmaX:   
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_e "I'm open to suggestions."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_e "I could let you choose a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_e "Perhaps when I'm off the clock. . ."
                        $ Cnt = 1
                else:
                        ch_e "I'd prefer to handle my own wardrobe."
                        return  
        elif Girl == LauraX:         
                if ApprovalCheck(Girl, 1500, "LO"):
                        ch_l "Fine, you pick, whatever."
                        $ Cnt = 3
                elif ApprovalCheck(Girl, 1200, "LO"):
                        ch_l "I don't know, you could pick a few days. . ."
                        $ Cnt = 2
                elif ApprovalCheck(Girl, 1000, "LO"):
                        ch_l "Maybe on weekends. . ."
                        $ Cnt = 1
                else:
                        ch_l "Nah, I got it covered."
                        return
        while True:    
            menu:
                    extend ""
                    "Every Day":
                        "This sets her outfit for every day of the week in one go."
                        "This overwrites the default schedule, and any scheduling you've already made."
                        "Any choices you make later will overwrite this choice."
                        menu:
                            "Pick an outfit to wear":                                
                                call Clothes_ScheduleB
                                if Cnt > 1:
                                        $ Girl.Clothing[0] = _return
                                if Cnt > 2:
                                        $ Girl.Clothing[1] = _return
                                if Cnt > 1:
                                        $ Girl.Clothing[2] = _return
                                if Cnt > 2:
                                        $ Girl.Clothing[3] = _return
                                if Cnt > 1:
                                        $ Girl.Clothing[4] = _return
                                $ Girl.Clothing[5] = _return
                                $ Girl.Clothing[6] = _return
                            "Never mind.":
                                pass
                    "Weekdays":
                        menu:
                            "On Monday you should wear. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[0] = _return
                            "On Monday you should wear. . . (locked)" if Cnt <= 1:
                                pass
                                
                            "On Tuesday you should wear. . ." if Cnt > 2:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[1] = _return        
                            "On Tuesday you should wear. . . (locked)" if Cnt <= 2:
                                pass
                                
                            "On Wednesday you should wear. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[2] = _return
                            "On Wednesday you should wear. . . (locked)" if Cnt <= 1:
                                pass        
                                
                            "On Thursday you should wear. . ." if Cnt > 2:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[3] = _return
                            "On Thursday you should wear. . . (locked)" if Cnt <= 2:
                                pass
                                
                            "On Friday you should wear. . ." if Cnt > 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[4] = _return
                            "On Friday you should wear. . . (locked)" if Cnt <= 1:
                                pass
                            "Back":
                                pass 
                    "Other":
                        menu:
                            "On Saturday you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On Saturday you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[5] = _return
                                
                            "On Sunday you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On Sunday you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[6] = _return
                                
                            "In our rooms you should wear. . . (locked)" if Cnt < 1:
                                pass  
                            "In our rooms you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB(Girl,99)
                                $ Girl.Clothing[9] = _return   
                                
                            "On dates you should wear. . . (locked)" if Cnt < 1:
                                pass
                            "On dates you should wear. . ." if Cnt >= 1:
                                call Clothes_ScheduleB
                                $ Girl.Clothing[7] = _return  
                            "Back":
                                pass 
                                
                    "About Gym clothes":
                        menu:
                            ch_p "You asked me before about your gym clothes?"
                            "Don't ask before changing into gym clothes" if "no ask gym" not in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.append("no ask gym")
                            "Ask me before changing into gym clothes" if "no ask gym" in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.remove("no ask gym")    
                            "Never Mind":
                                pass                              
                                
                    "Private outfit" if Girl.Clothing[9]:
                                #if comfy is in LauraX.Traits, she won't ask before changing
                                ch_p "You know that outfit you wear in private?"
                                call AnyLine(Girl,"Yeah?")
                                menu:
                                    extend ""
                                    "Just put them on without asking me about it." if "comfy" not in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.append("comfy")
                                    "Ask before changing into that." if "comfy" in Girl.Traits:
                                        call AnyLine(Girl,"Sure.")
                                        $ Girl.Traits.remove("comfy")
                                    "Never Mind":
                                        pass       
                            
                    "Never mind [[Done]":
                        return        
        jump Clothes_Schedule
        
label Clothes_ScheduleB(Girl=0,Count = 0):
        #This is called by Clothes_Schedule when setting her outfit for a given day
        #If Count by the end, yes, if not count, no. If count is 99 then it's an auto-yes  
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        menu:
            "Your green outfit." if Girl == RogueX:
                $ Count = 1
            "That pink outfit, with the jeans." if Girl == RogueX:
                $ Count = 2
                
            "That pink outfit, with the jeans." if Girl == KittyX:
                $ Count = 1
            "Your red shirt outfit." if Girl == KittyX:
                $ Count = 2
            
            "That leather combat look." if Girl == EmmaX:
                $ Count = 1
            "Your jacket and skirt." if Girl == EmmaX:
                $ Count = 2
                
            "That teacher outfit." if Girl == LauraX:
                $ Count = 1
            "Your superhero outfit." if Girl == LauraX:
                $ Count = 2
                
            "That outfit we put together [[custom]":                    
                        if Girl == RogueX:
                                ch_r "Which one again?"
                        elif Girl == KittyX:     
                                ch_k "[Girl.Like]which?"           
                        elif Girl == EmmaX:  
                                ch_e "Which were you thinking?"               
                        elif Girl == LauraX:
                                ch_l "Which one?"
                        menu:
                            extend ""
                            "The first one. (locked)" if not Girl.Custom1[0]:
                                        pass
                            "The first one." if Girl.Custom1[0]:
                                        if Girl.Custom1[0] == 2 or Count == 99:
                                            $ Count = 3
                                        else:
                                            $ Line = "no"
                            "The second one. (locked)" if not Girl.Custom2[0]:
                                        pass
                            "The second one." if Girl.Custom2[0]:
                                        if Girl.Custom2[0] == 2 or Count == 99:
                                            $ Count = 5
                                        else:
                                            $ Line = "no"
                            "The third one. (locked)" if not Girl.Custom3[0]:
                                        pass
                            "The third one." if Girl.Custom3[0]:
                                        if Girl.Custom3[0] == 2 or Count == 99:
                                            $ Count = 6
                                        else:
                                            $ Line = "no"
                            "Never mind":
                                        pass
                        if Line == "no":
                                if Girl == RogueX:
                                        ch_r "I told you I'm not wearing that outside, [Girl.Petname]."
                                elif Girl == KittyX:    
                                        ch_k "I said I'm not[Girl.like]wearing that one out."            
                                elif Girl == EmmaX:         
                                    ch_e "I said I'm not wearing that one in public."        
                                elif Girl == LauraX:
                                        ch_l "I told you I wouldn't wear that out."
                                $ Line = 0
                            
            "Your gym clothes.":
                if Count == 90:
                    ch_e "Not in class, [Girl.Petname]."
                    $ Count = 0
                else:
                    $ Count = 4
            "Your sleepwear.":
                if Count != 99:                        
                    if Girl == RogueX:
                            ch_r "I don't know about that, [Girl.Petname]."
                    elif Girl == KittyX:  
                            ch_k "That's not really appropriate, [Girl.Petname]."              
                    elif Girl == EmmaX:            
                            ch_e "I don't think that would be appropriate, [Girl.Petname]."     
                    elif Girl == LauraX:
                            ch_l "That's kinda skimpy, [Girl.Petname]."
                    $ Count = 0
                else:
                    $ Count = 7
            "Whatever you like.":
                pass
             
        if Girl == RogueX:                
                if Count:
                        ch_r "Ok, sure, I'll wear that."
                else:
                        ch_r "I'll just wear whatever then."
        elif Girl == KittyX:    
                if Count:
                        ch_k "Ok, sure, I'll wear that."
                else:
                        ch_k "I'll just wear whatever then."            
        elif Girl == EmmaX:        
                if Count:
                        ch_e "Very well."
                else:
                        ch_e "I'll wear something else instead."         
        elif Girl == LauraX:  
                if Count:
                        ch_l "Ok, sure."
                else:
                        ch_l "I'll figure something else out."
        return Count    
#End Clothes Scheduling Check / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label AltClothes(Girl=0,Outfit=8):
        #1 = "casual1", 2 = "casual2"
        #3 = "custom1", 5 = "custom2", 6 = "custom3", 7 = "sleep", 4 = "gym", 10 = "swimwear"
        #This selects her outfit when teaching if 8
        #This selects her private outfit if 9  
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        if Girl.Clothing[Outfit] == 1 or not Girl.Clothing[Outfit]:
                    $ Girl.Outfit = "casual1"
        elif Girl.Clothing[Outfit] == 2:
                    $ Girl.Outfit = "casual2"
        elif Girl.Clothing[Outfit] == 3:
                    $ Girl.Outfit = "custom1"
        elif Girl.Clothing[Outfit] == 5:
                    $ Girl.Outfit = "custom2"
        elif Girl.Clothing[Outfit] == 6:
                    $ Girl.Outfit = "custom3"
        elif Girl.Clothing[Outfit] == 7:
                    $ Girl.Outfit = "sleep"
        elif Girl.Clothing[Outfit] == 4:
                    $ Girl.Outfit = "gym"
        elif Girl.Clothing[Outfit] == 10:
                    $ Girl.Outfit = "swimwear"
        return
  
label Private_Outfit(Girl=0):
        #sets Girl's private outfit in private  
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        if Girl.Break[0] or "angry" in Girl.DailyActions:
                return
        if Girl.Outfit == "temporary":
                #if you manually set a different option, keep it
                return
        if "comfy" in Girl.RecentActions or "comfy" in Girl.Traits or Girl.Outfit == Girl.Clothing[9]:
                call AltClothes(Girl,9)
                $ Girl.OutfitChange(Changed=1)
        elif "no comfy" in Girl.RecentActions:
                pass        
        elif (2 * Girl.Inbt) >= (Girl.Love + Girl.Obed +100):
                # if her inhibition is much higher than her obedience to you. . .             
                if Girl == RogueX:
                        ch_r "Be right there [Girl.Petname]. . ."
                        ch_r "I'm slippin' inta somethin' more comfortable. . ."
                elif Girl == KittyX:                            
                        ch_k "Gimme a sec. . ."
                        ch_k "I'm throwing on something a bit more. . . fun."
                elif Girl == EmmaX:               
                        ch_e "I'll be just a moment. . ."
                        ch_e "I'll just slip into something more comfortable. . ."          
                elif Girl == LauraX:
                        ch_l "One minute. . ."
                        ch_l "I'm getting a bit more comfortable."
                call AltClothes(Girl,9)
                $ Girl.OutfitChange(Changed=1)
                $ Girl.RecentActions.append("comfy")
        else:
                if Girl == RogueX:
                        ch_r "Be right there [Girl.Petname]. . ."
                        menu: 
                            ch_r "Should I throw on somethin' more comfortable?"
                            "Sure.":
                                    ch_r "Love to. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_r "Suit yourself."       
                                    $ Girl.RecentActions.append("no comfy")          
                elif Girl == KittyX:   
                        ch_k "Gimme a sec. . ."
                        menu: 
                            ch_k "Want me to wear something more fun?"
                            "Sure.":
                                    ch_k "Hehe. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_k "Oh, ok."       
                                    $ Girl.RecentActions.append("no comfy")   
                elif Girl == EmmaX:      
                        ch_e "I'll be just a moment. . ."
                        menu: 
                            ch_e "Would you like me to change into something more comfortable?"
                            "Sure.":
                                    ch_e "Lovely. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_e "Very well."       
                                    $ Girl.RecentActions.append("no comfy")              
                elif Girl == LauraX:
                        ch_l "One minute. . ."
                        menu: 
                            ch_l "I could throw on something a bit more fun. . ."
                            "Sure.":
                                    ch_l "Cool. . ."
                                    call AltClothes(Girl,9)
                                    $ Girl.OutfitChange(Changed=1)
                                    $ Girl.RecentActions.append("comfy")
                            "No thanks.":
                                    ch_l "Oh, ok."       
                                    $ Girl.RecentActions.append("no comfy")               
        return       
    
label Custom_Out(Girl=0,Custom = 3, Shame = 0, Agree = 1):
        #If Custom1 = 3, if custom2 = 5, if custom3 = 6    
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        $ Girl.FaceChange("sexy", 1)
        if Custom == 5:
                    $ Shame = Girl.Custom2[10] 
        elif Custom == 6:
                    $ Shame = Girl.Custom3[10] 
        else: #if custom 1:
                    $ Shame = Girl.Custom1[10] 
                    
        if "exhibitionist" in Girl.Traits:                  
                    if Girl == RogueX:
                            ch_r "Ooo, momma likes." 
                    elif Girl == KittyX:     
                            ch_k "Hmm, I'm getting excited. . ."             
                    elif Girl == EmmaX:   
                            ch_e "Hmm, I'm getting excited. . ."                
                    elif Girl == LauraX:
                            ch_l "Mmmmmm. . ."                         
                    if Custom == 5 and Girl.Custom2[0] == 2:
                        $ Girl.Outfit = "custom2"                    
                        $ Girl.Shame = Shame
                    elif Custom == 6 and Girl.Custom3[0] == 2:
                        $ Girl.Outfit = "custom3"                    
                        $ Girl.Shame = Shame
                    else: #if custom 1:
                        $ Girl.Outfit = "custom1"                    
                        $ Girl.Shame = Shame           
                    return    
        
        if Custom == 5 and Girl.Custom2[0] == 2:
                    $ Girl.Outfit = "custom2"   
        elif Custom == 6 and Girl.Custom3[0] == 2:
                    $ Girl.Outfit = "custom3"   
        elif Girl.Custom1[0] == 2: #if custom 1:
                    $ Girl.Outfit = "custom1"   
        else: #no
                    $ Agree = 0
         
        if Girl == RogueX:
                if Agree: 
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame       
                        if Shame >= 50:
                            ch_r "You realize I'm pretty much naked here, right?"
                        elif Shame >= 25:
                            ch_r "This is pretty shameless. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_r "I don't know, I guess I could try it. . ."
                        else:
                            ch_r "Sure, [Girl.Petname], that one's nice."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_r "Come on, I'd be totally nude!"
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_r "You're lucky I show {i}you{/i} this."
                        else:
                            $ Girl.FaceChange("bemused", 1)
                            ch_r "It's kind of daring for me, sorry."  
        elif Girl == KittyX:    
                if Agree: 
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame          
                        if Shame >= 50:
                            ch_k "This is. . . kinda slutty. . ."
                        elif Shame >= 25:
                            ch_k "I'm not really comfortable with this one. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_k "I'll give it a shot. . ."
                        else:
                            ch_k "Yeah, I like that one too."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_k "You have GOT to be kidding me here."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_k "This is just between us."
                        else:
                            $ Girl.FaceChange("bemused", 1)  
                            ch_k "I can't wear this out!" 
        elif Girl == EmmaX:       
                if Agree: 
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame          
                        if Shame >= 50:
                            ch_e "This is rather. . . slutty. . ."
                        elif Shame >= 25:
                            ch_e "I'm a bit uncomfortable with this one. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_e "I'll try it. . ."
                        else:
                            ch_e "Yeah, I like that one too."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "You have GOT to be kidding me here."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "This is just between us."
                        else:
                            $ Girl.FaceChange("bemused", 1) 
                            ch_e "I can't wear this out!"  
        elif Girl == LauraX:   
                if Agree: 
                        #she's decided to wear this out.
                        $ Girl.Shame = Shame          
                        if Shame >= 50:
                            ch_l "This is. . . really brave. . ."
                        elif Shame >= 25:
                            ch_l "This one's pretty skimpy. . ."
                        elif Shame >= 15:
                            $ Girl.FaceChange("bemused", 1)
                            ch_l "Yeah, ok. . ."
                        else:
                            ch_l "Yup."
                else:
                        #She's decided not to wear this out
                        if Shame >= 50:
                            $ Girl.FaceChange("angry", 1)
                            ch_l "Perv."
                        elif Shame >= 25:
                            $ Girl.FaceChange("angry", 1)
                            ch_l "Yeah, not in public."
                        else:
                            $ Girl.FaceChange("bemused", 1)   
                            ch_l "Nah."   
        return
# End Custom Out / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start Outfit Shame / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label OutfitShame(Girl=0, Custom = 3, Check = 0, Count = 0, Tempshame = 50, Agree = 1):
        #Custom determines which custom outfit is being checked against.    
        #If Custom1 = 3, if custom2 = 5, if custom3 = 6, if gym = 4, if sleepwear 7, if private = 9, if swimsuit = 10
        #if not a check, then it is only applied if it's in a taboo area
        # Tempshame is a throwaway value, 0-50, Agree is whether she will wear it out, 2 if yes, 1 if only around you. 
        # call OutfitShame(RogueX,20)
        $ Girl = Ch_Focus if not Girl else Girl
        #call Shift_Focus(Girl)  #removed because this gets called passively
        
        if not Check and not Girl.Taboo and Custom != 20:
                #if this is not a custom check and you're in a safe space,
                if Girl.Clothing[9]:
                        #if there is a "private outfit" set, ask to change.
                        call Private_Outfit
                return
                        
        #If she's wearing a bra of some kind
        if Custom == 20 and Girl.Uptop: 
            $ Count = 0
        elif Girl.Chest == "tank" or Girl.Chest == "leather bra":                                              
            $ Count = 20
        elif Girl.Chest == "buttoned tank" or Girl.Chest == "corset":
            $ Count = 15
        elif Girl.Chest == "sports bra" or Girl.Chest == "cami":
            $ Count = 15
        elif Girl.Chest == "bikini top":
            $ Count = 15
        elif Girl.Chest == "bra" or Girl.Chest == "wolvie top":
            $ Count = 10    
        else:     #Girl.Chest == 0 or lace bra:
            if Girl.Chest == "lace bra" or Girl.Chest == "lace corset":
                $ Count = 5
            if Girl.Pierce:
                $ Count = -5
            else:
                $ Count = 0
                
        #If she's wearing an overshirt
        if Custom == 20 and Girl.Uptop: 
            $ Count = 0
        elif Girl.Over == "red shirt":                                             
            $ Count += 20
        elif Girl.Over == "pink top":                                             
            $ Count += 15
        elif Girl.Over == "hoodie" or Girl.Over == "jacket":      
            $ Count += 15
        elif Girl.Over == "mesh top" or (Girl == EmmaX and Girl.Over == "towel"):      
            $ Count += 5
        elif Girl.Over == "towel":      
            $ Count += 10
        #else: nothing    
                        
        $ Girl.FaceChange("sexy", 0)
        if Custom == 9 or Custom == 7:
            pass
        elif Count >= 20:
            $ Count = 20
            if Check:
                if Girl == RogueX:
                        ch_r "Oh, I think this top combination works." 
                elif Girl == KittyX:
                        ch_k "This is[Girl.like]totally a cute top."                    
                elif Girl == EmmaX:
                        ch_e "This is a fashionable top."                    
                elif Girl == LauraX:
                        ch_l "This top works."
        elif not Check:
            pass            
        elif Girl == RogueX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):  
                        ch_r "This top is pretty sexy. . ."        
                elif Count >= 10:
                        ch_r "This top might be a bit daring to wear outside."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                        ch_r "Not leaving much to the imagination. . ."        
                elif Count >= 5:        
                        $ Girl.FaceChange("startled", 1)
                        ch_r "I really think this is a bit scandelous to wear out. . ."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):  
                        ch_r "Oooh, I'm getting turned on already. . ."        
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_r "This is just for in private, right. . ."
        elif Girl == KittyX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):  
                        ch_k "Kinda hot top."        
                elif Count >= 10:
                        ch_k "I wouldn't[Girl.like]feel comfortable in this top."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                        ch_k "This top is is[Girl.like]kinda breezy. . ."        
                elif Count >= 5:        
                        $ Girl.FaceChange("startled", 1)
                        ch_k "This top is[Girl.like]way too slutty."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):  
                        ch_k "Is it hot in here? Whew. . ."        
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_k "I wouldn't wear this out, but maybe indoors."
        elif Girl == EmmaX:
                if Count >= 10: 
                        if ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0):  
                                ch_e "A bit daring. . ."        
                        else:
                                ch_e "I'm not sure about this top."
                elif Count >= 5:
                        if ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0):  
                                ch_e "I typically cover a {i}bit{/i} more than this."        
                        else:        
                                $ Girl.FaceChange("startled", 1)
                                ch_e "This is a bit more cleavage than even I'm comforable with."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):  
                        ch_e "Aren't my assets a bit. . . exposed here?"        
                else:
                        $ Girl.FaceChange("bemused", 1)
                        ch_e "This is considerably more cleavage than even I'm comforable with."
        elif Girl == LauraX:
                if Count >= 10 and (ApprovalCheck(Girl, 1200, TabM=0) or ApprovalCheck(Girl, 500, "I", TabM=0)):  
                    ch_l "This top works."     
                elif Count >= 10:
                    ch_l "The top's not really a good look."
                elif Count >= 5 and (ApprovalCheck(Girl, 2300, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                    ch_l "I don't know, the top's a little light."
                elif Count >= 5:        
                    $ Girl.FaceChange("startled", 1)
                    ch_l "I can't really wear this top out."
                elif (ApprovalCheck(Girl, 2700, TabM=0) or ApprovalCheck(Girl, 950, "I", TabM=0)):  
                    ch_l ". . ."        
                else:
                    $ Girl.FaceChange("bemused", 1)
                    ch_l "I wouldn't go out with my tits out."
        #end top check dialog
         
        $ Tempshame -= Count                  #Set Outfit shame for the upper half    
        $ Count = 0         
        
        if Girl.Legs and Girl.Panties: #If wearing both legs and panties   
                    $ Count = 30        
        else: #If she's missing something on her legs   
                    if Girl.PantsNum() > 5:                  
                        #If wearing pants commando
                        $ Count = 25
                    elif Girl.PantsNum() == 5:                           
                        #If wearing a skirt commando
                        $ Count = 20
                    elif Girl.Panties == "shorts":             
                        #If wearing shorts
                        $ Count = 25  
                    elif Girl.PantiesNum() >= 6:    
                        #If wearing only bikini bottoms
                        $ Count = 15
                    elif Girl.PantiesNum() >= 5:      
                        #If wearing only panties
                        $ Count = 10
                    elif Girl.Panties == "lace panties":     
                        #If wearing only lace panties
                        $ Count = 5
                    elif Girl.Panties:                        
                        #If wearing only any other panties
                        $ Count = 7
                    #else: 0
                    
                    if Girl.HoseNum() >= 10:             
                        #Factors in tights and hose
                        $ Count = 25 if Count < 25 else Count
                        
                    if Girl.Over == "towel" and Count:         
                        #If wearing a Towel and anything else
                        $ Count = 25
                    elif Girl.Over == "towel":                 
                        #If just wearing a Towel
                        $ Count = 15        
        
                    if Girl.Legs == "blue skirt":
                        $ Count += 10   
                    if Girl.Legs == "mesh pants":
                        $ Count += 5
        if not Check:
                    #If this isn't a custom check, skip this dialog stuff
                    pass      
        elif Custom == 9 or Custom == 7:
                    pass
        elif Girl == RogueX:
                if Count >= 20:
                            if Girl.PantsNum() > 6:
                                ch_r "Oh, I think these pants will work fine."
                            elif Girl.PantsNum() == 5:
                                ch_r "Oh, I think this skirt will work fine."
                            elif Girl.HoseNum() >= 10:
                                ch_r "Oh, these [Girl.Hose] will work."
                            elif Girl.Panties == "shorts":
                                ch_r "Oh, I think these shorts will work fine."  
                            elif Girl.Over == "towel":
                                ch_r "The towel's an odd choice. . ."
                            else:
                                ch_r "Kinda breezy across my nethers, [Girl.Petname]. . ."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_r "I kinda like going commando."           
                            elif not Girl.Panties:
                                ch_r "Don't know about going commando though."                    
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                    ch_r "These don't really leave much to the imagination. . ."        
                elif Count >= 10:
                    $ Girl.FaceChange("angry", 1)
                    ch_r "I'm warning you, I'm not running around in my panties. . ."                
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                    ch_r "Hmm, Breezy. . ."        
                else:
                    ch_r "So long as we stay inside. . ."
        elif Girl == KittyX:
                if Count >= 20:
                            if Girl.PantsNum() >= 5:
                                ch_k "and these pants look cute on me."
                            elif Girl.Legs == "shorts":
                                ch_k "and these are cute shorts."  
                            elif Girl.HoseNum() >= 10:
                                ch_k "I guess these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_k "The towel's an odd choice. . ."
                            else:
                                ch_k "This is kinda breezy."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_k "I like going without panties."           
                            elif not Girl.Panties:
                                ch_k "It's a little uncomfortable without panties."                            
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_k "I'm not sure about the coverage down here. . ."        
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_k "I'm barely covered down here. . ."                
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                        ch_k "kinda chilly. . ."        
                else:
                        ch_k "if it's just[Girl.like]you and me. . ."
        elif Girl == EmmaX:
                if Count >= 20:
                            if Girl.PantsNum() > 5:
                                ch_e "and these pants always did suit me."
                            elif Girl.PantsNum() >= 5:
                                ch_e "and this skirt always did suit me."
                            elif Girl.HoseNum() >= 10:
                                ch_e "I guess these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_e "I'm unsure about wearing a towel out, [Girl.Petname]. . ."
                            else:
                                ch_e "I probably could wear something more downstairs, [Girl.Petname]. . ."
                            if not Girl.Panties:
                                if ApprovalCheck(Girl, 500, "I", TabM=0):
                                    ch_e "I do enjoy going without panties."
                                else:
                                    ch_e "I don't know about going without panties in this situation."                           
                elif Count >= 10:
                    if ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0):
                            ch_e "I hope you don't expect me to wear this out. . ."        
                    else:
                            $ Girl.FaceChange("angry", 1)
                            ch_e "I don't know about wearing this outside. . ."                
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                            ch_e "This really tests my limits."        
                else:
                            ch_e "I'll need to put something else on to leave the room though."
        elif Girl == LauraX:
                if Count >= 20:
                            if Girl.PantsNum() >= 5:
                                ch_l "and these pants work."
                            elif Girl.HoseNum() >= 10:
                                ch_l "and these [Girl.Hose] will work fine."
                            elif Girl.Over == "towel":
                                ch_l "The towel's an odd choice. . ."
                            else:
                                ch_l "but there's a draft."
                            if not Girl.Panties and ApprovalCheck(Girl, 500, "I", TabM=0):
                                ch_l "Commando's cool."           
                            elif not Girl.Panties:
                                ch_l "I might accidentally flash some people like this though."
                elif Count >= 10 and (ApprovalCheck(Girl, 2000, TabM=0) or ApprovalCheck(Girl, 700, "I", TabM=0)):
                        ch_l "I don't think I'm fully covered. . ."        
                elif Count >= 10:
                        $ Girl.FaceChange("angry", 1)
                        ch_l "I'm not covered like this. . ."                
                elif (ApprovalCheck(Girl, 2500, TabM=0) or ApprovalCheck(Girl, 800, "I", TabM=0)):  
                        ch_l "It's pretty minimal. . ."        
                else:
                        ch_l "I wouldn't show off my cooch either. . ."
        # End Panties check dialog
                        
        $ Tempshame -= Count                  #Set Outfit shame for the lower half
        
        if Check:
                #if this is a custom outfit check                    
                if Check == 2:
                    ch_p "So can I see it then?"
                elif Custom == 4:
                    ch_p "So would you work out in that?"
                elif Custom == 7:
                    ch_p "So would you sleep in that?"
                else:
                    ch_p "So would you wear that outside?"  
                    
                $ Girl.FaceChange("sexy", 0)
                if Girl.PantsNum() > 2:  
                    pass        #if she's wearing pants
                elif Girl.PantiesNum() > 2 and (Girl.SeenPanties or ApprovalCheck(Girl, 900, TabM=0)):
                    pass        #no pants, but panties
                elif Girl.SeenPussy or ApprovalCheck(Girl, 1200, TabM=0):
                    pass        #no panties, but she's fine with that
                else:
                    $ Agree = 0 #not fine with it
                    
                if not Agree:
                    pass
                elif Girl.OverNum() > 2:    
                    pass        #if she's wearing a top
                elif Girl.ChestNum() > 2 and (Girl.SeenChest or ApprovalCheck(Girl, 900, TabM=0)):
                    pass        #no top, but bra
                elif Girl.SeenChest or ApprovalCheck(Girl, 1200, TabM=0):
                    pass        #no bra, but she's fine with that
                else:
                    $ Agree = 0 #not fine with it
                
                if Check == 2 and Agree:
                            #if checking to see if she'll drop the dressing screen. . .                                
                            $ Girl.Shame = Tempshame
                            $ Girl.FaceChange("sly")
                            if Girl == RogueX: 
                                    ch_r "This ain't a bad look, I guess. . ."
                            elif Girl == KittyX:   
                                    ch_k "I suppose you've put together a cute little outfit. . ."
                            elif Girl == EmmaX:    
                                    ch_e "I suppose I could pull this off. . ."  
                            elif Girl == LauraX:
                                    ch_l "Huh, this'll work. . ."                                
                            hide DressScreen
                            return 1   
                if not Agree:
                            #she isn't even comfortable with you seeing it
                            $ Girl.FaceChange("bemused", 2,Eyes="side")
                            if Girl == RogueX: 
                                    ch_r "I don't really feel comfortable in this. . ."
                            elif Girl == KittyX:   
                                    ch_k "I don't think I'd be comfortable with you seeing me like this. . ."
                            elif Girl == EmmaX:     
                                    ch_e "I wouldn't want to blind you. . ." 
                            elif Girl == LauraX:
                                    ch_l "You'll have to earn it."
                            menu:
                                extend ""
                                "Ok then, you can put your normal clothes back on.":
                                            $ Girl.OutfitChange(Changed=1)  
                                            hide DressScreen
                                "Ok, we can keep tweaking it.":
                                            pass
                            $ Girl.FaceChange("smile", 1)
                            if Girl == RogueX: 
                                    ch_r "Thanks, [Girl.Petname]."
                            elif Girl == KittyX:   
                                    ch_k "Thanks."    
                            elif Girl == EmmaX:    
                                    ch_e "Appreciated."  
                            elif Girl == LauraX:
                                    ch_l "Thanks."                                    
                            return
                if Girl == RogueX:
                        if Girl.Taboo >= 40: 
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_r "It's a little late to worry about that, right?" 
                        elif "exhibitionist" in Girl.Traits:        
                                ch_r "Hmm. . . yeah, I'd love to. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Custom == 7: 
                                #Sleepwear
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                        ch_r "A bit scandelous, but yeah."
                                elif Tempshame >= 15:
                                        ch_r "Yeah, you're worth it."
                                else:
                                        ch_r "Sure, it's cute."                            
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_r "Yeah, I think I like this style, I'd wear this."
                        elif Tempshame <= 15:
                            if ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0):        
                                ch_r "It's pretty skimpy, but I can make it work."
                            else:
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "I think this looks is a bit daring to wear."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:  
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "Sure, I can swim in this. . ."
                        elif Tempshame <= 25:
                            if ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0):
                                ch_r "Kinky, but I can rock this."
                            else:
                                $ Girl.FaceChange("angry", 1)
                                ch_r "I'm definitely not going out in this."
                                $ Agree = 0
                        elif ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0):
                                $ Girl.FaceChange("bemused", 1)
                                ch_r "I can't believe it. . . but yeah."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_r "You have got to be kidding."
                                $ Agree = 0
                elif Girl == KittyX:                                     
                        if Girl.Taboo >= 40: #Girl.Loc != "bg player" and Girl.Loc != "bg kitty": 
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_k "Kinda late to ask, right?" 
                        elif "exhibitionist" in Girl.Traits and Tempshame <= 20:        
                                ch_k "I'm getting wet just thinking about it. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_k "Sure, it's a cute look!"
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):        
                                ch_k "It's pretty hot, right?"
                        elif Custom == 7:
                                #if it's sleepwear      
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_k "This is[Girl.like]pretty exposed, but ok."  
                                elif Tempshame >= 15:
                                    ch_k "It's kinda naughty, I like it."  
                                else:
                                    ch_k "Yeah, these are fine."                        
                        elif Tempshame <= 15:  
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "It's kinda slutty to wear out."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:  
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "This is a cute swimsuit. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_k "So sexy, but I can handle it."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_k "{i}Way{/i} too sexy for outside."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_k "OMG, I can't believe I'm doing this."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_k "I - can't - even."
                                $ Agree = 0
                elif Girl == EmmaX:
                        if Girl.Taboo >= 40:
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                "She glances around."
                                ch_e "Is that a trick question?" 
                        elif "exhibitionist" in Girl.Traits and Tempshame <= 20:        
                                ch_e "The thought of it gets me moist. . ."
                                $ Girl.Statup("Lust", 80, 10)
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_e "Yes, it's a fine choice."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):        
                                ch_e "Rather daring, how could I resist?"
                        elif Custom == 7:
                                #if it's sleepwear      
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_e "You understand I only wear this sort of thing in private."  
                                else:
                                    ch_e "It is a comfortable outfit."   
                        elif Tempshame <= 15:  
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "Rather too daring, don't you think?."
                                $ Agree = 0                            
                        elif Tempshame >= 15 and "public" not in Girl.History:                 
                                ch_e "I doubt I could get away with this in public, [Girl.Petname]."
                                $ Agree = 0                        
                        elif Custom == 10 and Tempshame <= 20:  
                            #if it's a swimsuit. . .
                            $ Girl.FaceChange("bemused", 1)
                            ch_e "Fine, this is decent swimwear. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_e "This is particularly inappropriate. . . in the best ways."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_e "I don't believe even I could pull off this look, [Girl.Petname]."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_e "This look certainly pushes the boundaries."
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_e "Even I can't pull this off."
                                $ Agree = 0
                elif Girl == LauraX:
                        if Girl.Taboo >= 40: 
                                $ Girl.FaceChange("confused",1)
                                $ Girl.Mouth = "smile"
                                ch_l "Well a bit late for that, I guess." 
                        elif "exhibitionist" in Girl.Traits and Tempshame <= 20: 
                                $ Girl.Statup("Lust", 80, 10) 
                                $ Girl.FaceChange("sexy", 2)      
                                ch_l ". . ."
                                $ Girl.FaceChange("sexy", 1)      
                        elif Tempshame <= 5:
                                $ Girl.FaceChange("smile")
                                ch_l "I don't see why not."
                        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1700, TabM=0, C = 0) or ApprovalCheck(Girl, 400, "I", TabM=0, C = 0)):        
                                ch_l "It looks good, right?"
                        elif Custom == 7:
                                #if it's sleepwear      
                                $ Girl.FaceChange("bemused", 1)
                                if Tempshame >= 30:
                                    ch_l "Sure, perv."   
                                elif Tempshame >= 15:
                                    ch_l "Sure, why not."  
                                else:
                                    ch_l "Yeah, I guess."                       
                        elif Tempshame <= 15:  
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "I can't move freely in this without showing off the goods."
                                $ Agree = 0
                        elif Custom == 10 and Tempshame <= 20:  
                                #if it's a swimsuit. . .
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Yeah, I can swim in this. . ."
                        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2300, TabM=0, C = 0) or ApprovalCheck(Girl, 700, "I", TabM=0, C = 0)):
                                ch_l "I can handle this."
                        elif Tempshame <= 25:
                                $ Girl.FaceChange("angry", 1)
                                ch_l "Nah, too slutty."
                                $ Agree = 0
                        elif (ApprovalCheck(Girl, 2500, TabM=0, C = 0) or ApprovalCheck(Girl, 800, "I", TabM=0, C = 0)):
                                $ Girl.FaceChange("bemused", 1)
                                ch_l "Pretty daring, eh?"
                        else:
                                $ Girl.FaceChange("angry", 1)
                                ch_l "As if."
                                $ Agree = 0
                #End check dialog
                    
                #$ Girl.OutfitShame[Custom] = Tempshame 
                if Custom == 5:
                        $ Girl.Custom2[1] = Girl.Arms  
                        $ Girl.Custom2[2] = Girl.Legs 
                        $ Girl.Custom2[3] = Girl.Over
                        $ Girl.Custom2[4] = Girl.Neck
                        $ Girl.Custom2[5] = Girl.Chest 
                        $ Girl.Custom2[6] = Girl.Panties
                        $ Girl.Custom2[8] = Girl.Hair
                        $ Girl.Custom2[9] = Girl.Hose
                        $ Girl.Custom2[10] = Tempshame
                        $ Girl.Custom2[0] = 2 if Agree else 1   
                        call Clothing_Schedule_Check(Girl,5,1) #checks to make sure it's still SFW     
                elif Custom == 6:
                        $ Girl.Custom3[1] = Girl.Arms  
                        $ Girl.Custom3[2] = Girl.Legs 
                        $ Girl.Custom3[3] = Girl.Over
                        $ Girl.Custom3[4] = Girl.Neck
                        $ Girl.Custom3[5] = Girl.Chest 
                        $ Girl.Custom3[6] = Girl.Panties
                        $ Girl.Custom3[8] = Girl.Hair
                        $ Girl.Custom3[9] = Girl.Hose
                        $ Girl.Custom3[10] = Tempshame
                        $ Girl.Custom3[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,6,1)   
                elif Custom == 4 and Agree:
                        $ Girl.Gym[1] = Girl.Arms  
                        $ Girl.Gym[2] = Girl.Legs 
                        $ Girl.Gym[3] = Girl.Over
                        $ Girl.Gym[4] = Girl.Neck
                        $ Girl.Gym[5] = Girl.Chest 
                        $ Girl.Gym[6] = Girl.Panties
                        $ Girl.Gym[8] = Girl.Hair
                        $ Girl.Gym[9] = Girl.Hose
                        $ Girl.Gym[10] = Tempshame
                        $ Girl.Gym[0] = 2     
                        call Clothing_Schedule_Check(Girl,4,1)   
                elif Custom == 7:
                        $ Girl.Sleepwear[1] = Girl.Arms  
                        $ Girl.Sleepwear[2] = Girl.Legs 
                        $ Girl.Sleepwear[3] = Girl.Over
                        $ Girl.Sleepwear[4] = Girl.Neck 
                        $ Girl.Sleepwear[5] = Girl.Chest 
                        $ Girl.Sleepwear[6] = Girl.Panties
                        $ Girl.Sleepwear[8] = Girl.Hair
                        $ Girl.Sleepwear[9] = Girl.Hose                        
                        $ Girl.Sleepwear[10] = Tempshame
                        $ Girl.Sleepwear[0] = 2 if Agree else 1    
                elif Custom == 10 and Agree:            
                        $ Girl.Swim[1] = Girl.Arms  
                        $ Girl.Swim[2] = Girl.Legs 
                        $ Girl.Swim[3] = Girl.Over
                        $ Girl.Swim[4] = Girl.Neck 
                        $ Girl.Swim[5] = Girl.Chest 
                        $ Girl.Swim[6] = Girl.Panties
                        $ Girl.Swim[8] = Girl.Hair
                        $ Girl.Swim[9] = Girl.Hose
                        $ Girl.Swim[10] = Tempshame
                        $ Girl.Swim[0] = 2
                else: #Typically Custom == 3
                        $ Girl.Custom1[1] = Girl.Arms  
                        $ Girl.Custom1[2] = Girl.Legs 
                        $ Girl.Custom1[3] = Girl.Over
                        $ Girl.Custom1[4] = Girl.Neck
                        $ Girl.Custom1[5] = Girl.Chest 
                        $ Girl.Custom1[6] = Girl.Panties
                        $ Girl.Custom1[8] = Girl.Hair
                        $ Girl.Custom1[9] = Girl.Hose
                        $ Girl.Custom1[10] = Tempshame
                        $ Girl.Custom1[0] = 2 if Agree else 1
                        call Clothing_Schedule_Check(Girl,3,1)   
        elif Girl.Taboo <= 20:
                # halves shame level if she's comfortable
                $ Tempshame /= 2
            
        $ Girl.Shame = Tempshame
             
        if Custom == 20:
                # This returns the scene if it's a check Shame adjustment
                return
            
        if Check:
                pass
        elif "exhibitionist" in Girl.Traits and Tempshame <= 20: 
                #If she's an exhibitionist
                pass
        elif Tempshame <= 5:
                #If the outfit is very tame
                pass
        elif Girl.Over == "towel" and Girl.Loc == "bg showerroom": 
                #If she's in a towel but it's appropriate
                pass
        elif Tempshame <= 15 and (ApprovalCheck(Girl, 1500) or ApprovalCheck(Girl, 500, "I")):
                #If the outfit is hot but she's ok     
                pass
        elif Tempshame <= 20 and (Girl.Loc == "bg dangerroom" or Girl.Loc == "bg pool"): 
                #If the outfit is light but she's in the gym or pool
                pass
        elif Tempshame <= 20 and (ApprovalCheck(Girl, 1800) or ApprovalCheck(Girl, 650, "I")):
                #If the outfit is sexy but she's cool with that
                pass
        elif Tempshame <= 25 and (ApprovalCheck(Girl, 2000) or ApprovalCheck(Girl, 700, "I")):
                #If the outfit is sexy but she's cool with that
                pass
        elif (ApprovalCheck(Girl, 2500) or ApprovalCheck(Girl, 800, "I")):
                #If the outfit is very scandelous but she's ok with that      
                pass
        elif Girl.Loc == "bg dangerroom" and Girl.Outfit == "gym":                
                $ Girl.OutfitChange("gym",Changed = 1)
        elif not Girl.Taboo:
                pass
        else:
                if Girl.Loc == bg_current:                                
                        if Girl == RogueX:
                                ch_r "I'll be right back, I've got to change out of this."  
                        elif Girl == KittyX:
                                ch_k "One sec, I gotta change real quick."
                        elif Girl == EmmaX:      
                                ch_e "I'm afraid I'll have to change, one moment."  
                        elif Girl == LauraX:
                                ch_l "One sec, I gotta change real quick."
                if Girl.Loc == "bg dangerroom":
                        $ Girl.Outfit =  "gym"
                elif Girl.Loc == "bg pool" and Girl.Swim[0]:
                        $ Girl.Outfit =  "swimwear"                        
                else:
                        $ Girl.Outfit = renpy.random.choice(["casual1", "casual2"])
                $ Girl.Water = 0
                $ Girl.OutfitChange(Changed=1)                     
                if Girl == RogueX:
                        ch_r "That wasn't really \"outdoor ready\"." 
                elif Girl == KittyX:
                        ch_k "I wouldn't want to be seen like that."
                elif Girl == EmmaX:      
                        ch_e "Sorry for the wait." 
                elif Girl == LauraX:                    
                        ch_l "That wasn't really \"outdoors\" wear."  
        return   
#End Custom clothes check. / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Girl Undressing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Girl_Undress(Girl=0,Region = "ask",CountStore=0): 
        #Called mostly from sex act menus when you want a girl to strip down
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        $ CountStore = Tempmod    
        if Partner == Girl:
                $ Tempmod = 0
        call Shift_Focus(Girl)           
                        
        if Region == "auto":
                if Girl.Upskirt and Girl.PantiesDown:
                    return
                if Girl.PantsNum() > 5 and Tempmod < 20:
                    $ Tempmod = 20
                if Girl.Lust >= 90:
                    $ Tempmod += 10      
                elif Girl.Lust >= 80:
                    $ Tempmod += 5     
                $ Situation = "auto"
                call Bottoms_Off(Girl,0)
        
        if Region == "ask":
            menu:
                "Which parts?"
                "Her top" if Girl.Over or Girl.Chest or Girl.Arms:    
                        $ Region = "top"     
                "Her bottoms" if Girl.Legs or Girl.Panties or Girl.Hose:
                        $ Region = "bottom"           
                "A little of both. . ." if Girl.Over or Girl.Chest or Girl.Legs or Girl.Panties or Girl.Hose: 
                        $ Region = "both"    
                "Never mind":
                    pass
        
        if Region == "top":
            if Girl.Over or Girl.Chest:    
                call Top_Off(Girl,0)  
        elif Region == "bottom":
            if Girl.Legs or Girl.Panties or Girl.Hose:
                call Bottoms_Off(Girl,0)    
        elif Region == "both":        
                if Girl.Over or Girl.Chest:    
                        call Top_Off(Girl,0) 
                
                if Partner == Girl:
                        $ Tempmod = 0
                else:
                        $ Tempmod = CountStore 
                
                if "angry" in Girl.RecentActions: 
                        pass            
                elif not Girl.Legs and not Girl.Panties and not Girl.Hose:
                        pass                
                elif "no topless" in Girl.RecentActions:
                        if Girl == RogueX:
                                ch_r "You might want to rethink your next question."
                        elif Girl == KittyX:
                                ch_k "Don't push it. . ."
                        elif Girl == EmmaX:      
                                ch_e "Care to push your luck?"
                        elif Girl == LauraX: 
                                ch_l "Know when to fold'em, [Girl.Petname]."
                        menu:
                            extend ""
                            "And now the bottoms?":
                                call Bottoms_Off(Girl,0) 
                            "You're probably right, sorry.":
                                pass
                else:
                        ch_p "And now the bottoms?"
                        call Bottoms_Off(Girl,0) 
                        
        $ Tempmod = CountStore
        return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Top_Off(Girl=0,Intro = 1, Line = 0, Cnt = 0):                                                    
        # Will she take her top off? Modifiers  
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        if not Girl.Over and not Girl.Chest:                              
                # If she's already topless. Just skip back.
                $ Tempmod = 0
                return
            
        if "angry" in Girl.RecentActions:  
                if Girl == RogueX:
                        ch_r "I'm just too annoyed to deal with this right now."
                elif Girl == KittyX:
                        ch_k "No titties for you."
                elif Girl == EmmaX:      
                        ch_e "I'm in no mood, [Girl.Petname]."
                elif Girl == LauraX: 
                        ch_l "Don't push it, [Girl.Petname]."
                return
        
        if Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo:                             
                #You've seen her tits.
                $ Tempmod += 20
        if "exhibitionist" in Girl.Traits:
                $ Tempmod += (4*Taboo)
        if "dating" in Girl.Traits or "sex friend" in Girl.Petnames and not Taboo:
                $ Tempmod += 10
        elif "ex" in Girl.Traits:
                $ Tempmod -= 40 
        if "no topless" in Girl.RecentActions: 
                $ Tempmod -= 10
                
       
        if Intro and not Girl.Uptop:
                if Girl.Over:
                        ch_p "This might be easier without your [Girl.Over] on."
                elif Girl.Chest:
                        ch_p "This might be easier without your [Girl.Chest] on."                   
        

        $ Approval = ApprovalCheck(Girl, 1100, TabM = 4) # 110, 125, 140, 300 taboo, -20 if already seen
        
        if Situation == "auto" and  (Girl.Over or Girl.Chest) and not Girl.Uptop:   
                $ Line = 0
                if ApprovalCheck(Girl, 1250, TabM = 1) or (Girl.SeenChest and ApprovalCheck(Girl, 500) and not Taboo):
                        #if she'd go topless
                        $ Girl.Statup("Inbt", 70, 1)
                        $ Girl.Uptop = 1
                        $ Line = Girl.Over if Girl.Over else Girl.Chest
                        if Girl == KittyX:
                                "[Girl.Name] sighs in frustration, and her [Line] drops to the ground."
                        else:
                                "[Girl.Name] sighs in frustration, and pulls her [Line] up over her breasts."
                        if Girl == RogueX:
                                ch_r "I just wasn't getting much out of it that way." 
                        elif Girl == KittyX:
                                ch_k "I[Girl.like]wasn't feeling it that way."  
                        elif Girl == EmmaX:      
                                ch_e "Sometimes only direct contact will do."   
                        elif Girl == LauraX: 
                                ch_l "That wasn't working out."  
                        if Taboo:
                            $ Girl.Statup("Inbt", 90, (int(Taboo/20)))   
                        call expression Girl.Tag + "_First_Topless" pass (1)
                elif Girl.Over and Girl.Chest and ApprovalCheck(Girl, 800, TabM = 1):
                        #if she won't go topless, but has a bra on. . .
                        $ Girl.Statup("Inbt", 40, 1)
                        $ Line = Girl.Over
                        $ Girl.Over = 0
                        if Girl == KittyX:
                                "[Girl.Name] sighs in frustration, and her [Line] drops to the ground."
                        else:
                                "[Girl.Name] sighs in frustration, and pulls her [Line] over her head, throwing it aside."
                        if Girl == RogueX:
                                ch_r "I just wasn't getting much out of it that way."  
                        elif Girl == KittyX:
                                ch_k "I[Girl.like]wasn't feeling it that way."  
                        elif Girl == EmmaX:      
                                ch_e "I just wasn't getting much out of it that way."  
                        elif Girl == LauraX:   
                                ch_l "That wasn't working out."  
                        
                        
                $ Line = 0
                return    
        
        if Approval >= 2: #(Girl.Love + Girl.Obed + Girl.Inbt + (2*Tempmod) - (4*Taboo)) >= 1250:                             
            # Does she assume top off?            
            if "no topless" in Girl.DailyActions:
                    if Girl == RogueX:
                            ch_r "Ok, fine, top off."
                    elif Girl == KittyX:
                            ch_k "Okay, okay!"
                    elif Girl == EmmaX:      
                            ch_e "{i}Fine,{/i} if that will shut you up."
                    elif Girl == LauraX: 
                            ch_l "{i}Fine,{/i} but don't think I'm getting soft on you."
            $ Girl.FaceChange("sexy", 1)
            if Girl.Forced:
                    $ Girl.FaceChange("sad", 1)
                    $ Girl.Statup("Love", 20, -2, 1)
                    $ Girl.Statup("Love", 70, -3, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1)
            $ Girl.Statup("Inbt", 50, 3)  
            $ Cnt = 1
            while (Girl.Chest or Girl.Over) and Cnt:
                if Girl == RogueX:
                        ch_r "So, [Girl.Petname]. Did you want me to take my top off?"  
                elif Girl == KittyX:
                        ch_k "So[Girl.like]how much did you want me to take off?"  
                elif Girl == EmmaX:      
                        ch_e "What was it you were interested in, [Girl.Petname]?" 
                elif Girl == LauraX:  
                        ch_l "What did you want to see, [Girl.Petname]?"  
                menu:                                                                                 
                    #Menu All off?
                    extend ""
                    "Lose the [Girl.Over]." if Girl.Over:                 
                            $ Girl.FaceChange("bemused", 1)                    
                            $ Line = Girl.Over
                            $ Girl.Over = 0
                            if Girl == KittyX:
                                    "[Girl.Name] shrugs and her [Line] falls through to the ground."
                            else:
                                    "[Girl.Name] pulls her [Line] off and tosses it aside."
                    "Why don't you lose the [Girl.Neck]?" if Girl.Neck:
                            $ Line = Girl.Neck
                            $ Girl.Neck = 0
                            "[Girl.Name] pulls her [Line] off."                    
                    "Just lose the [Girl.Chest]." if Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)                    
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0         
                            if Girl == KittyX:
                                    "[Girl.Name] reaches through her top and pulls her [Line] free, dropping it to the ground."
                            else:        
                                    "[Girl.Name] slowly removes her [Line] from under the [Girl.Over]."   
                    "Lose the [Girl.Chest]." if not Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = Girl.Chest
                            $ Girl.Chest = 0        
                            if Girl == KittyX:
                                    "[Girl.Name] shrugs and her [Line] falls through to the ground."
                            else:         
                                    "[Girl.Name] throws off her [Line]."   
                    "Just pull it up." if (Girl.Over or Girl.Chest) and not Girl.Uptop:
                            $ Girl.FaceChange("bemused", 1)
                            $ Girl.Uptop = 1
                            if Girl == EmmaX:
                                    "[Girl.Name] smiles and pulls out her tits. . ."   
                            elif Girl.Over and Girl.Chest:
                                    "[Girl.Name] smiles and lifts up her tops. . ."   
                            else:
                                    "[Girl.Name] smiles and lifts up her top. . ."   
                    "Lose both tops." if Girl.Over and Girl.Chest:
                            $ Girl.FaceChange("bemused", 1)
                            if Girl == KittyX:
                                    $ Girl.Over = 0  
                                    $ Girl.Chest = 0     
                                    "[Girl.Name] shrugs and her tops fall through her body to the ground."
                            else:                            
                                    $ Line = Girl.Over
                                    $ Girl.Over = 0                        
                                    "[Girl.Name] tosses the [Line] over her head. . ."   
                                    $ Line = Girl.Chest
                                    $ Girl.Chest = 0 
                                    ". . .and then the [Line] as well."        
                    "Lose the [Girl.Arms]. . ." if Girl.Arms:
                            $ Girl.FaceChange("sexy")
                            $ Line = Girl.Arms
                            $ Girl.Arms = 0          
                            "She pulls off her [Line]."
                    "That's enough. [[exit]":               
                            $ Girl.FaceChange("bemused", 1)
                            call AnyLine(Girl,"All right, "+Girl.Petname+".")   
                            $ Cnt = 0
            if Girl.ChestNum() < 3 and Girl.OverNum() < 3:
                    #if her top's are off. . .
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    call expression Girl.Tag + "_First_Topless"  
            $ Girl.Statup("Lust", 80, 3)        
            $ Girl.RecentActions.append("ask topless")                      
            $ Girl.DailyActions.append("ask topless") 
            $ Tempmod = 0        
            return
            
        #Else, Doesn't automatically want to lose the top//////////////////////////////////  
                     
        $ Girl.FaceChange("bemused", 1)     
        if Girl == RogueX:
                if Intro == "massage" and not Approval:
                    ch_r "I'm ok with a massage, but my top stays on."
                elif "no topless" in Girl.RecentActions: 
                    $ Girl.FaceChange("angry")
                    ch_r "I just told you no, [Girl.Petname]."    
                elif Approval and not Girl.SeenChest:
                    ch_r "I'd like to leave something to the imagination. . ."    
                elif not Girl.SeenChest:
                    ch_r "I'm not ready to show you those yet. . ."   
                elif "no topless" in Girl.DailyActions: 
                    ch_r "I wasn't into it earlier, [Girl.Petname], what's changed?"           
                elif "ask topless" in Girl.RecentActions: 
                    ch_r "Changed your mind, [Girl.Petname]?"       
                elif Taboo:
                    ch_r "It's a bit exposed here. . ."          
                elif Approval:
                    ch_r "Well, you've seen them before, but. . ."
                else:
                    ch_r "Not right now."
        elif Girl == KittyX:
                if Intro == "massage" and not Approval:
                    ch_k "A massage is fine, but I'm keeping my top on, ok?"
                elif "no topless" in Girl.RecentActions: 
                    $ KittyX.FaceChange("angry")
                    ch_k "I[Girl.like]already told you, no way!"    
                elif Approval and not Girl.SeenChest:
                    ch_k "I'm[Girl.like]not really comfortable with that."    
                elif not Girl.SeenChest:
                    ch_k "I'd[Girl.like]really rather not, ok?"   
                elif "no topless" in Girl.DailyActions: 
                    ch_k "Do you[Girl.like]think something's changed since earlier?"           
                elif "ask topless" in Girl.RecentActions: 
                    ch_k "Did you[Girl.like]want something else off?"       
                elif Taboo:
                    ch_k "I'm[Girl.like]not that comfortable out here. . ."          
                elif Approval:
                    ch_k "Maybe not?"
                else:
                    ch_k "Nu-uh."
        elif Girl == EmmaX: 
                if Intro == "massage" and not Approval:
                    ch_e "I welcome a massage, but I'm staying fully dressed."
                elif "no topless" in EmmaX.RecentActions: 
                    $ EmmaX.FaceChange("angry")
                    ch_e "Learn from previous mistakes, [Girl.Petname]."    
                elif Approval and not Girl.SeenChest:
                    ch_e "I don't know if that would be appropriate."    
                elif not Girl.SeenChest:
                    ch_e "I don't think you're ready for that."   
                elif "no topless" in Girl.DailyActions: 
                    ch_e "Are you still that obsessed?"           
                elif "ask topless" in Girl.RecentActions: 
                    ch_e "You want more?"       
                elif Taboo:
                    ch_e "[Girl.Petname], not around prying eyes."          
                elif Approval:
                    ch_e "Are you sure you're prepared?"
                else:
                    ch_e "No."
        elif Girl == LauraX: 
                if Intro == "massage" and not Approval:
                    ch_l "I could use a massage, but I'm keeping my clothes on."
                elif "no topless" in Girl.RecentActions: 
                    $ LauraX.FaceChange("angry")
                    ch_l "Don't push it, [Girl.Petname]."    
                elif Approval and not Girl.SeenChest:
                    ch_l "I don't know, man."    
                elif not Girl.SeenChest:
                    ch_l "I really don't think so."   
                elif "no topless" in Girl.DailyActions: 
                    ch_l "Dude, relax."           
                elif "ask topless" in Girl.RecentActions: 
                    ch_l "Again?"       
                elif Taboo:
                    ch_l "[Girl.Petname], not around here, alright?"          
                elif Approval:
                    ch_l "Are you sure?"
                else:
                    ch_l "No."
                        
        menu:
            extend ""
            "Sorry, sorry." if "no topless" in Girl.RecentActions:  
                $ Girl.FaceChange("bemused", 1)   
                if Girl == RogueX:
                        ch_r "Ok, just. . . give it a rest, huh?"
                elif Girl == KittyX:
                        ch_k "It's cool, I get it, but[Girl.like]chill out, huh?"
                elif Girl == EmmaX:      
                        ch_e "I can't blame you for your persistance, but learn from your errors."
                elif Girl == LauraX: 
                        ch_l "Right, I get it, stay thirsty."
                
            "Ok, that's fine." if "no topless" not in Girl.RecentActions: 
                if "ask topless" not in Girl.DailyActions:
                        $ Girl.Statup("Lust", 80, 3)
                        $ Girl.Statup("Love", 70, 1)
                        $ Girl.Statup("Love", 90, 1)
                        $ Girl.Statup("Inbt", 50, 3)
                if Girl.Forced:
                        $ Girl.Mouth = "grimace"
                        if Girl == RogueX:
                                ch_r "I really appreciate that."
                        elif Girl == KittyX:
                                ch_k "That's[Girl.like]really cool of you."
                        elif Girl == EmmaX:      
                                ch_e "How. . . generous of you."
                        elif Girl == LauraX: 
                                ch_l "Ok."
                        if "ask topless" not in Girl.DailyActions:
                            $ Girl.Statup("Love", 20, 2)
                            $ Girl.Statup("Love", 70, 2)
                            $ Girl.Statup("Inbt", 60, 1)
                                                                                                             
            "How about just the [Girl.Over]?" if Girl.Over:                                                
                # asked to go shirtless. 
                if ApprovalCheck(Girl, 800, TabM = 2) and Girl.Chest: #80, 160 taboo 
                        $ Girl.FaceChange("sexy") 
                        if Girl == RogueX:
                                ch_r "Well, that's no big deal I guess. . ." 
                        elif Girl == KittyX:
                                ch_k "Um, I guess I could. . ."    
                        elif Girl == EmmaX:      
                                ch_e "Well, I suppose that would be fine. . ."  
                        elif Girl == LauraX:       
                                ch_l "I mean. . . I guess. . ."   
                        $ Girl.FaceChange("bemused", 1)                
                        $ Line = Girl.Over
                        $ Girl.Over = 0    
                        if Girl == KittyX:
                                "[Girl.Name] shrugs and her [Line] falls through to the ground."
                        else:         
                                "[Girl.Name] tosses the [Line] over her head."   
                        $ Girl.Statup("Obed", 50, 1)
                        $ Girl.Statup("Inbt", 30, 2)
                elif not Girl.Chest:
                        $ Girl.Eyes = "surprised"
                        $ Girl.Blush = 2
                        if Girl == RogueX:
                                ch_r "I'm not exactly decent under this, you know." 
                        elif Girl == KittyX:
                                ch_k "I'd[Girl.like]be {i}totally{/i} exposed here." 
                        elif Girl == EmmaX:      
                                ch_e "I don't think you're prepared for what's under there." 
                        elif Girl == LauraX: 
                                ch_l "I don't really have anything on under here." 
                        $ Girl.Statup("Inbt", 30, 1)
                        menu:
                            extend ""
                            "Ok, you can leave it on.":
                                    $ Girl.Mouth = "smile"
                                    $ Girl.Statup("Love", 70, 2)
                                    if Girl == RogueX:
                                            ch_r "Great!"  
                                    elif Girl == KittyX:
                                            ch_k "Thanks!"
                                    elif Girl == EmmaX:  
                                            ch_e "Good."       
                                    elif Girl == LauraX:   
                                            ch_l "Right."   
                                    
                            "That doesn't bother me any.":
                                if ApprovalCheck(Girl, 500, "I", TabM=3) or ApprovalCheck(Girl, 1000, "LI", TabM=3):
                                    $ Girl.FaceChange("bemused", 1)
                                    if Girl == RogueX:
                                            ch_r "Ooh, at least you know what you like"  
                                    elif Girl == KittyX:
                                            ch_k "Why am I not surprised?"     
                                    elif Girl == EmmaX:      
                                            ch_e "Well, I suppose it couldn't hurt to try."
                                    elif Girl == LauraX:         
                                            ch_l "Maybe it should. . ."   
                                    $ Girl.Statup("Obed", 20, 2)                                                         
                                    $ Girl.Statup("Obed", 60, 1)
                                    $ Girl.FaceChange("sexy")   
                                    $ Line = Girl.Over
                                    $ Girl.Over = 0
                                    if Girl == KittyX:
                                            "[Girl.Name] shrugs and her [Line] falls through to the ground."
                                    else:         
                                            "[Girl.Name] tosses the [Line] over her head."                            
                                    $ Girl.Over = 0
                                    $ Girl.Statup("Inbt", 30, 2)  
                                    $ Girl.Statup("Inbt", 60, 1)
                                    call expression Girl.Tag + "_First_Topless"   
                                else:   
                                    $ Girl.FaceChange("bemused")
                                    call Top_Off_Refused(Girl)  
                                
                            "I know, take it off.":
                                call ToplessorNothing(Girl)
                        $ Girl.Blush = 1        
                else:   
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)  
                                     
            "Come on, Please? [[take it all off]":                                                                      
                # asked to go topless. 110, 270 Taboo           
                if Approval and ApprovalCheck(Girl, 600, "L", TabM=1):                 
                        $ Girl.Statup("Obed", 40, 2)
                        $ Girl.FaceChange("sexy")   
                        if Girl == RogueX:
                                if "no topless" in Girl.RecentActions:  
                                    ch_r "You're pretty persistent, [Girl.Petname]. I guess this time it'll be rewarded. . ."
                                else:
                                    ch_r "Heh, I suppose I can hardly refuse ya when you use the magic words . . ." 
                        elif Girl == KittyX:
                                if "no topless" in Girl.RecentActions:     
                                    ch_k "You just don't know when to quit. . . but you got lucky this time. . ."
                                else:
                                    ch_k "You[Girl.like]know how to ask nicely . . ."
                        elif Girl == EmmaX:      
                                if "no topless" in EmmaX.RecentActions:     
                                    ch_e "Fine, I can't take your constant begging."
                                else:
                                    ch_e "Well, I suppose if you ask nicely . . ."
                        elif Girl == LauraX: 
                                    ch_l "Fine, you thirsty weirdo."
                        $ Girl.Uptop = 1                    
                        if Girl == KittyX:
                                "[Girl.Name] shrugs and her tits drop out from her top."
                        else:         
                                "[Girl.Name] just pulls her top up over her tits."
                        $ Girl.Arms = 0          
                        $ Girl.Statup("Inbt", 30, 2)  
                        $ Girl.Statup("Inbt", 60, 1)
                        call expression Girl.Tag + "_First_Topless"     
                elif "no topless" in Girl.RecentActions:
                        $ Girl.FaceChange("angry")
                        if Girl == RogueX:
                                ch_r "Nuh uh, [Girl.Petname]."
                        elif Girl == KittyX:
                                ch_k "Noooope!"
                        elif Girl == EmmaX:   
                                ch_e "Again, no."   
                        elif Girl == LauraX: 
                                ch_l "Still no."
                        $ Girl.Statup("Love", 80, -5)   
                        $ Girl.RecentActions.append("angry")   
                        $ Girl.DailyActions.append("angry")
                else:   
                        $ Girl.FaceChange("sexy")
                        call Top_Off_Refused(Girl)
               
            "Lose the [Girl.Arms], at least. . ." if Girl.Arms:
                    $ Girl.FaceChange("sexy")
                    call AnyLine(Girl,"Oh, all right.")
                    $ Line = Girl.Arms
                    $ Girl.Arms = 0          
                    "She pulls off her [Line]."
            "No, topless or nothing.":                                                              
                    #demanded topless 60, 260 taboo 
                    call ToplessorNothing(Girl)
                
            "Never mind.":
                pass
        
        $ Girl.RecentActions.append("ask topless")                      
        $ Girl.DailyActions.append("ask topless") 
        $ Tempmod = 0
        return


label Top_Off_Refused(Girl=0):                    
        #Called form Top_Off when you insist but she refuses          
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        $ Girl.FaceChange("angry")
        if Girl == RogueX:
                if "no topless" in Girl.RecentActions:  
                        ch_r "Get a clue, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:  
                        ch_r "Give it a rest, [Girl.Petname]."
                else:
                        $ Girl.FaceChange("sad")
                        ch_r "I'm afraid not this time, [Girl.Petname]. Sure we can't have some fun anyway?"
        elif Girl == KittyX:
                if "no topless" in Girl.RecentActions:  
                        ch_k "[Girl.Like]back off."
                elif "no topless" in Girl.DailyActions:  
                        ch_k "Not today, maybe not ever, [Girl.Petname]."
                else:
                        $ KittyX.FaceChange("sad")
                        ch_k "[Girl.Like], no way, but I don't want to go. . ."
        elif Girl == EmmaX:   
                if "no topless" in Girl.RecentActions:  
                        ch_e "You should probably back off now."
                elif "no topless" in Girl.DailyActions:  
                        ch_e "I'm tired of this, [Girl.Petname]."
                else:
                        ch_e "Is this a dealbreaker for you?"        
        elif Girl == LauraX: 
                if "no topless" in Girl.RecentActions:  
                        ch_l "You're getting real close to the line, [Girl.Petname]."
                elif "no topless" in Girl.DailyActions:  
                        ch_l "You keep coming back with this, [Girl.Petname]."
                else:                
                        ch_l "Let it go?"
        menu:
            extend ""
            "Sure, never mind." if "no topless" not in Girl.RecentActions:
                    $ Girl.FaceChange("sexy")
                    $ Girl.Statup("Love", 70, 2)
                    if Girl == RogueX or Girl == KittyX:
                            call AnyLine(Girl,"Great!")
                    else:
                            call AnyLine(Girl,"Good.")
            "Sorry, I'll drop it." if "no topless" in Girl.RecentActions:   
                    if Girl == RogueX:
                            ch_r "Fine. . ." 
                    elif Girl == KittyX:
                            ch_k "Good!" 
                    else:
                            call AnyLine(Girl,"Good.")
            "No, I insist. . .":
                    $ Girl.Brows = "angry"
                    if Girl == RogueX:
                            $ Girl.Brows = "confused"
                            ch_r "Ok [Girl.Petname], your loss."
                    elif Girl == KittyX:
                            ch_k "Fine then!"
                    elif Girl == EmmaX:    
                            ch_e "Very well."  
                    elif Girl == LauraX: 
                            ch_l "Your funeral."
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.Statup("Love", 70, -2, 1)
                    if "no topless" not in Girl.RecentActions:
                            $ Girl.Statup("Obed", 60, 4)    
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")   
        $ Girl.RecentActions.append("no topless")                      
        $ Girl.DailyActions.append("no topless") 
        return
              

label ToplessorNothing(Girl=0):  
        #Called from Top_Off if you insist she go topless after she's declined. 
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        $ Girl.FaceChange("angry")
        if ApprovalCheck(Girl, 800, "OI", TabM = 4) and ApprovalCheck(Girl, 400, "O", TabM = 3):        
            $ Girl.Statup("Love", 20, -2, 1)
            $ Girl.Statup("Love", 70, -5, 1)
            $ Girl.Statup("Inbt", 60, 3)
            $ Girl.FaceChange("sad")
            if Girl == RogueX:
                    if "no topless" in Girl.RecentActions: 
                        ch_r "Ok, ok, whatever."  
                    else:
                        ch_r "Fine, if that's what you want." 
            elif Girl == KittyX:            
                    if "no topless" in Girl.RecentActions:             
                        ch_k "Ok, fine. This time."                 
                    else:
                        $ Girl.FaceChange("sad")
                        ch_k "Whatever."                
            elif Girl == EmmaX:    
                    if "no topless" in Girl.RecentActions:             
                        ch_e "Oh, very well. . ."                 
                    else:
                        $ Girl.FaceChange("sad")
                        ch_e "Fine."               
            elif Girl == LauraX:    
                    if "no topless" in Girl.RecentActions:             
                        ch_l "Hrmph, whatever. . ."                 
                    else:
                        $ Girl.FaceChange("sad")
                        ch_l "Ugh, whatever."  
            $ Girl.Statup("Obed", 60, 4)
            $ Girl.Statup("Obed", 90, 2)
            $ Girl.Uptop = 1
            "[Girl.Name] slowly pulls her top up over her tits."
            call expression Girl.Tag + "_First_Topless"                       
        else:  
            $ Girl.Statup("Love", 200, -10)                
            $ Girl.Statup("Obed", 40, -1, 1)
            if Girl == RogueX:
                    if "no topless" in Girl.RecentActions: 
                        ch_r "Seriously, cut this shit out."    
                    else:
                        $Girl.Brows = "confused"
                        ch_r "\"Nothing\" it is then."  
            elif Girl == KittyX:            
                    if "no topless" in Girl.RecentActions: 
                        ch_k "It[Girl.like]wasn't cute the first time."      
                    else:
                        $ Girl.Brows = "angry"
                        ch_k "[Girl.Like]no way!" 
            elif Girl == EmmaX:
                    if "no topless" in Girl.RecentActions: 
                        $ Girl.Brows = "angry"
                        ch_e "Learn to take \"no\" for an answer."  
                    else: 
                        ch_e "I'm afraid not."         
            elif Girl == LauraX: 
                    if "no topless" in Girl.RecentActions: 
                        $ Girl.Brows = "angry"
                        ch_l "You have got to chill."  
                    else: 
                        ch_l "Nope."   
            $ Girl.RecentActions.append("no topless")                      
            $ Girl.DailyActions.append("no topless")     
            $ Girl.RecentActions.append("angry")
            $ Girl.DailyActions.append("angry")   
        return              
    
# Bottoms ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
label Bottoms_Off(Girl=0,Intro = 1, Line = 0, Cnt = 0):    
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        if not Girl.Legs and not Girl.Panties and not Girl.Hose:                              
                # If she's already bottomless. Just skip back.     
                $ Tempmod = 0
                return
        
        if "angry" in Girl.RecentActions:  
                if Girl == RogueX:
                        ch_r "I'm just too annoyed to deal with this right now."
                elif Girl == KittyX:
                        ch_k "The only \"kitty\" you're getting is up here."
                elif Girl == EmmaX:      
                        ch_e "I would give up on that."
                elif Girl == LauraX: 
                        ch_l "You're barking up the wrong tree."
                return
        
        # Will she take her bottoms off Modifiers
        if Girl.SeenPussy and ApprovalCheck(Girl, 700): #You've seen her Pussy.
                $ Tempmod += 20
        elif not Girl.Panties:
                $ Tempmod -= 20
        elif Girl.SeenPanties and ApprovalCheck(Girl, 500): #You've seen her panties.
                $ Tempmod += 5 
        if Intro == "dildo":
                $ Tempmod += 20
        if "exhibitionist" in Girl.Traits:
                $ Tempmod += (Taboo * 5)
        if ("dating" in Girl.Traits or "sex friend" in Girl.Petnames) and not Taboo:
                $ Tempmod += 10
        elif "ex" in Girl.Traits:
                $ Tempmod -= 40 
        if "no bottomless" in Girl.RecentActions: 
                $ Tempmod -= 20
            
        if Intro:
            if Girl.Legs and not Girl.Upskirt:
                    ch_p "This might be easier without your [Girl.Legs] on."
            elif Girl.Panties and not Girl.PantiesDown:
                    ch_p "This might be easier without your [Girl.Panties] on."
            
        $ Approval = ApprovalCheck(Girl, 1200, TabM = 5) # 120, 135, 150, -200(320) taboo, -25 if already seen
        
        if Situation == "auto":
            $ Cnt = 0
            
            if not Girl.Upskirt and not Girl.PantiesDown:                    
                if Girl.PantsNum() == 5:                                          
                    #If she's in a skirt with panties, hike it up?
                    if Approval >= 2 or (Girl.SeenPussy and not Taboo):
                            $ Girl.Statup("Inbt", 60, 1)
                            if Taboo:
                                    $ Girl.Statup("Inbt", 90, (int(Taboo/20)))                 
                            $ Girl.Upskirt = 1
                            "She slides her skirt up."
                            $ Cnt = 1 
                        
                if Girl.HoseNum() >= 6 or Girl.HoseNum() >= 6:            
                    if Girl.Panties:                                               
                        #she has pants and panties on
                        if not Approval or (not Girl.SeenPanties and Taboo):
                            return   
                    elif Approval < 2 or (not Girl.SeenPussy and Taboo):
                        return     
                    elif Girl.Upskirt:  
                        return
                    $ Girl.Statup("Inbt", 60, 1)
                    $ Girl.Upskirt = 1
                    if Girl.HoseNum() >= 6:
                            $ Line = Girl.Hose
                            $ Girl.Hose = 0
                    
                    if Girl == KittyX:
                            if Girl.PantsNum() >= 6: 
                                "[Girl.Name] grumbles to herself, and then allows her [Girl.Legs] to drop down her legs." 
                            else: #Girl.HoseNum() >= 6
                                "[Girl.Name] grumbles to herself, and then allows her [Line] to drop down her legs." 
                            if Girl.Panties:
                                    $ Girl.SeenPanties = 1
                    elif Girl.Panties:
                            if Girl.PantsNum() >= 6: 
                                "[Girl.Name] grumbles to herself, and then unzips her [Girl.Legs], sliding them down her legs." 
                            else: #Girl.HoseNum() >= 6
                                "[Girl.Name] grumbles to herself, and then pulls her [Line] down her legs." 
                            $ Girl.SeenPanties = 1
                    else:
                            if Girl.PantsNum() >= 6: 
                                "[Girl.Name] grumbles to herself, and then unzips her [Girl.Legs], sliding them off her bare ass." 
                            else: #Girl.HoseNum() >= 6 
                                "[Girl.Name] grumbles to herself, and then pulls her [Line] down her bare ass." 
                    call expression Girl.Tag + "_First_Bottomless" pass (1)  
                    if Taboo:
                        $ Girl.Statup("Inbt", 90, (int(Taboo/10)))  
                    $ Cnt = 1 
                
            if Girl.Panties and not Girl.PantiesDown:                                              
                # Just wearing panties, lose them?
                if Approval >= 2 or (Girl.SeenPussy and not Taboo):
                    $ Girl.Statup("Inbt", 70, 2)
                    if Taboo:
                            $ Girl.Statup("Inbt", 90, (int(Taboo/10)))  
                    $ Girl.PantiesDown = 1
                    if Girl == KittyX:
                            if Cnt:
                                "With a second thought, [Girl.Name] lets her [Girl.Panties] drop too."
                            else:
                                "[Girl.Name] tsks in irritation, and her [Girl.Panties] slide off to the ground." 
                    else:
                            if Cnt:
                                "[Girl.Name] tsks in irritation, and pulls down her [Girl.Panties] too."
                            else:
                                "[Girl.Name] tsks in irritation, and pulls down her [Girl.Panties]." 
                    call expression Girl.Tag + "_First_Bottomless" pass (1) 
                    if Girl == RogueX:
                            ch_r "I wasn't getting anything out of it with those on. Give it another go." 
                    elif Girl == KittyX:
                            ch_k "It's super annoying not being able to phase you through these."   
                    elif Girl == EmmaX:    
                            ch_e "That was just in the way."  
                    elif Girl == LauraX: 
                            ch_l "I guess all that was in the way."  
            return
                
        
        if Approval >= 2:                
            #will she volunteer to strip to underwear?     
            $ Girl.FaceChange("sexy", 1)
            if Girl.Forced:
                    $ Girl.FaceChange("sad", 1)              
                    $ Girl.Statup("Love", 20, -2, 1)
                    $ Girl.Statup("Love", 70, -3, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 60, 1)
            if Girl == RogueX:            
                    if Approval >= 3:
                        $ Line = "Hmmm, what do you want to see? . ."
                    else:    
                        $ Line = "Well, ok. I'd kinda like to keep {i}some{/i} modesty though. . ." 
            elif Girl == KittyX:
                    if Approval >= 3:
                        $ Line = "Heh, what would you like to see? . ."
                    else:    
                        $ Line = "Ok, maybe, but don't push it. . ." 
            elif Girl == EmmaX:    
                    if Approval >= 3:
                        $ Line = "Mmmm, what would you like?"
                    else:    
                        $ Line = "What would you have me take off?" 
            elif Girl == LauraX: 
                    if Approval >= 3:
                        $ Line = "What did you want off?"
                    else:    
                        $ Line = "Hm, what did you want me to lose?"
            call Bottoms_Off_Legs(Girl)
                
            if not Girl.Panties and Girl.RecentActions.count("bottomless") < 2: 
                    $ Girl.Statup("Obed", 50, 1)
                    $ Girl.Statup("Obed", 90, 1)
                    $ Girl.Statup("Inbt", 50, 3)
                    $ Girl.Statup("Lust", 80, 3)
                
        elif Girl.Legs or Girl.Panties or Girl.Hose:                                                      
            # She'd rather not strip but might        
            $ Girl.FaceChange("bemused", 1) 
            if Girl == RogueX:
                    if "no bottomless" in Girl.RecentActions: 
                        $ Girl.FaceChange("angry")
                        ch_r "What did I just tell you, [Girl.Petname]?"   
                    elif "no topless" in Girl.RecentActions: 
                        $ Girl.FaceChange("angry")
                        ch_r "I doubt your odds will be better here, [Girl.Petname]. . ."  
                    elif Approval and not Girl.SeenPussy:
                        ch_r "Not everything, right?"  
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_r "I'm not ready to show you that either."    
                    elif "no bottomless" in Girl.DailyActions: 
                        ch_r "Have you forgot what I said earlier, [Girl.Petname]?"   
                    elif Taboo:
                        ch_r "I don't know about doing it here. . ."  
                    elif Approval:
                        ch_r "I don't know if I want to take my bottoms off. . ."   
                    elif Girl.SeenPussy:
                        ch_r "Well, you've seen it before, but. . ."            
                    else:
                        ch_r "I'm not taking my bottoms off."
            elif Girl == KittyX:
                    if "no bottomless" in Girl.RecentActions: 
                        $ KittyX.FaceChange("angry")
                        ch_k "Last warning, [Girl.Petname]. No."   
                    elif "no topless" in Girl.RecentActions: 
                        $ KittyX.FaceChange("angry")
                        ch_k "Not learning from your mistakes here, [Girl.Petname]. . ."  
                    elif Approval and not Girl.SeenPussy:
                        ch_k "I'm not sure about that. . ."  
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_k "That's a bit too far."    
                    elif "no bottomless" in Girl.DailyActions: 
                        ch_k "Short memory, [Girl.Petname]?"             
                    elif Taboo:
                        ch_k "This is[Girl.like]kinda public. . ."  
                    elif Approval:
                        ch_k "I'm[Girl.like]not sure about this. . ."   
                    elif Girl.SeenPussy:
                        ch_k "Well, you've seen[Girl.like]it before . . ."            
                    elif Girl.PantsNum() > 6:
                        ch_k "I'm keeping my pants on."   
                    elif Girl.PantsNum() > 5:
                        ch_k "I'm keeping my shorts on."  
                    else:
                        ch_k "I'm keeping my panties on."
            elif Girl == EmmaX:   
                    if "no bottomless" in Girl.RecentActions: 
                        $ EmmaX.FaceChange("angry")
                        ch_e "Stop asking, you're embarrassing yourself."   
                    elif "no topless" in Girl.RecentActions: 
                        $ EmmaX.FaceChange("angry")
                        ch_e "Do you really think that's likely?"  
                    elif Approval and not Girl.SeenPussy:
                        ch_e "I don't know if you're ready for that."  
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_e "Be careful how far you push it. . ."  
                    elif "no bottomless" in Girl.DailyActions: 
                        ch_e "Don't you learn anything, [Girl.Petname]?"             
                    elif Taboo:
                        ch_e "Not with so many eyes around, [Girl.Petname]. . ."  
                    elif Approval:
                        ch_e "Probably not. . ."   
                    elif Girl.SeenPussy:
                        ch_e "I think you've seen enough . . ."            
                    elif Girl.PantsNum() > 6:
                        ch_e "I'm keeping my pants on."           
                    elif Girl.PantsNum() == 5:
                        ch_e "I'm keeping my skirt on."   
                    elif Girl.PantsNum() == 6:
                        ch_e "I'm keeping my shorts on."  
                    else:
                        ch_e "I'm keeping my panties on." 
            elif Girl == LauraX: 
                    if "no bottomless" in Girl.RecentActions: 
                        $ LauraX.FaceChange("angry")
                        ch_l "Now you're just embarrassing yourself."   
                    elif "no topless" in Girl.RecentActions: 
                        $ LauraX.FaceChange("angry")
                        ch_l "This is really pushing it."  
                    elif Approval and not Girl.SeenPussy:
                        ch_l "I don't know if you're earned that yet."  
                    elif not Girl.SeenPussy and "ask topless" in Girl.RecentActions:
                        ch_l "Kinda pushing it, [Girl.Petname]. . ."   
                    elif "no bottomless" in Girl.DailyActions: 
                        ch_l "So thirsty. . ."             
                    elif Taboo:
                        ch_l "This is pretty exposed, [Girl.Petname]. . ."  
                    elif Approval:
                        ch_l "Probably not. . ."   
                    elif Girl.SeenPussy:
                        ch_l "You've probably seen enough . . ."            
                    elif Girl.PantsNum() > 6:
                        ch_l "Well, I'm keeping my pants on."           
                    elif Girl.PantsNum() == 5:
                        ch_l "Well, I'm keeping my skirt on."   
                    elif Girl.PantsNum() == 6:
                        ch_l "Well, I'm keeping my shorts on."  
                    else:
                        ch_l "Well, I'm keeping my panties on."                 
            menu:            
                extend ""
                "Ok, never mind." if "no bottomless" not in Girl.RecentActions:  
                    if "ask bottomless" not in Girl.DailyActions:
                            $ Girl.Statup("Lust", 80, 2)
                            $ Girl.Statup("Love", 70, 1)
                            $ Girl.Statup("Love", 90, 1)
                            $ Girl.Statup("Inbt", 50, 3)
                    if Girl.Forced:
                            $ Girl.Mouth = "smile"
                            if Girl == RogueX:
                                    ch_r "I really appreciate that."
                            elif Girl == KittyX:
                                    ch_k ". . . thank you."
                            elif Girl == EmmaX:    
                                    ch_e "Very. . . generous."
                            elif Girl == LauraX: 
                                    ch_l "Right."
                            if "ask bottomless" not in Girl.DailyActions:
                                    $ Girl.Statup("Love", 20, 3)
                                    $ Girl.Statup("Love", 70, 4)
                                    $ Girl.Statup("Inbt", 60, 2)
                        
                "Sorry, sorry." if "no bottomless" in Girl.RecentActions:  
                            if Girl == RogueX:
                                    ch_r "Ok, fine, just chill out about it."
                            elif Girl == KittyX:
                                    ch_k "[Girl.Like], fine, whatever."
                            else:    
                                    call AnyLine(Girl,"Good.")
                 
                "Come on, Please?":   
                        if "no bottomless" in Girl.DailyActions:    
                                $ Girl.FaceChange("angry", 1)
                                if Girl == RogueX:
                                        ch_r "Listen up when I tell you \"no.\""
                                elif Girl == KittyX:
                                        ch_k "I already told you \"no.\""
                                elif Girl == EmmaX:    
                                        ch_e "I believe you've heard my answer on that."
                                elif Girl == LauraX: 
                                        ch_l "You heard me."
                        else:                      
                            if Approval and ApprovalCheck(Girl, 600, "L", TabM=1):   
                                $ Girl.FaceChange("sexy", 1)
                                $ D20 = renpy.random.randint(1, 3)
                                $ Approval += 1 if D20 == 3 else 0
                                if Girl == RogueX:
                                        $ Line = "Well, what were you thinking then. . ."
                                elif Girl == KittyX:
                                        $ Line = "I guess. . ."   
                                elif Girl == EmmaX:    
                                        $ Line = "Perhaps. . ." 
                                elif Girl == LauraX: 
                                        $ Line = "Maybe. . ."   
                                call Bottoms_Off_Legs(Girl)  
                            else:    
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)
                                        
                "It doesn't have to be everything. . ." if Girl.Legs or Girl.HoseNum() >= 10 or Girl.Panties == "shorts":    
                    if Approval and "no bottomless" not in Girl.DailyActions:                   
                            $ Girl.FaceChange("bemused", 1)
                            $ Line = "Well what did you have in mind then?"
                            call Bottoms_Off_Legs(Girl)  
                    else:    
                            # She refuses your request. . .
                            $ Girl.FaceChange("sexy")
                            call Bottoms_Off_Refused(Girl)                       
                "It doesn't have to be everything. . . (locked)" if not Girl.Legs and Girl.HoseNum() < 10 and Girl.Panties != "shorts":   
                            pass
                                
                "No, lose 'em.":            #85 and -200 taboo             
                    if (Approval and Girl.Obed >= 250) or (ApprovalCheck(Girl, 850, "OI", TabM = 5) and ApprovalCheck(Girl, 400, "O")):                    
                                $ Girl.Statup("Love", 20, -1, 1)
                                $ Girl.Statup("Love", 70, -5, 1)
                                $ Girl.Statup("Obed", 50, 4)
                                $ Girl.Statup("Inbt", 60, 3)
                                if Girl == RogueX:
                                        $ Line =  "Fine, if that's what you want. What do you want to see?"
                                elif Girl == KittyX:
                                        $ Line =  "Like geez, you're serious. . ." 
                                elif Girl == EmmaX:    
                                        $ Line =  "Don't test me. . ."   
                                elif Girl == LauraX: 
                                        $ Line =  "Don't push me. . ."  
                                $ Approval = 1 if Approval < 1 else Approval
                                $ Girl.Forced = 1
                                call Bottoms_Off_Legs(Girl)                     
                    else:          
                        $ Girl.Statup("Love", 200, -10)
                        if ApprovalCheck(Girl, 400, "O"):
                                if Girl == RogueX:
                                        ch_r "I. . . I really can't." 
                                elif Girl == KittyX:
                                        ch_k "Sorry[Girl.like]no way."
                                elif Girl == EmmaX:    
                                        ch_e "Definitely not."  
                                elif Girl == LauraX: 
                                        ch_l "No way." 
                        else:
                                $ Girl.FaceChange("angry")
                                if Girl == RogueX:
                                        ch_r "Well fuck off then!"  
                                elif Girl == KittyX:
                                        ch_k "GTFO."      
                                elif Girl == EmmaX:  
                                        ch_e "Out of my sight, [Girl.Petname]."    
                                elif Girl == LauraX: 
                                        ch_l "Fuck off." 
                                $ Girl.RecentActions.append("angry")
                                $ Girl.DailyActions.append("angry")   
                        $ Girl.RecentActions.append("no bottomless")                      
                        $ Girl.DailyActions.append("no bottomless")   
        
        $ Tempmod = 0
        $ Girl.RecentActions.append("ask bottomless")                      
        $ Girl.DailyActions.append("ask bottomless")     
        return           

label Bottoms_Off_Legs(Girl=0):     
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        if Girl.Forced:        
            $ Girl.FaceChange("sad", 1)
        elif ApprovalCheck(Girl, 1100, "OI", TabM = 3):        
            $ Girl.FaceChange("sly")
        elif ApprovalCheck(Girl, 1400, TabM = 3):  
            $ Girl.FaceChange("sexy", 1) 
        else:
            $ Girl.FaceChange("bemused", 1) 
            
        $ Line = "Well what did you want off?" if not Line else Line
        $ Cnt = 1
        while Cnt and (Girl.Legs or Girl.Panties or Girl.Hose):
            call AnyLine(Girl,Line)
            menu:                                       
                # She's asking what you'd like to see.
                extend ""
                "Take it all off" if Line != "Well what did you have in mind then?": 
                        #approval a given
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                call NoPantiesOn(Girl)
                        
                        if Girl.Legs:
                                $ Line = Girl.Legs      
                                $ Girl.Legs = 0
                                if not Girl.SeenPanties:
                                    if Girl == RogueX:
                                            "[Girl.Name] shyly removes her [Line]."
                                    elif Girl == KittyX:
                                            "[Girl.Name] shyly tugs her [Line] off of her legs." 
                                    else:
                                            "[Girl.Name] pulls off her [Line]."
                                    $ Girl.SeenPanties = 1
                                else:
                                    "[Girl.Name] pulls her [Line] off." 
                        
                        if Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                                call NoPantiesOn(Girl)   
                            
                        if Girl.Acc: #boots, mostly
                                $ Girl.Acc = 0
                                "She pulls her [Girl.Acc] off." 
                            
                        if Girl.Hose:
                                $ Line = Girl.Hose #HoseName 
                                $ Girl.Hose = 0
                                if Girl == KittyX:
                                        "Her [Line] drop to the ground in a heap."
                                else:
                                        "She pulls her [Line] down."
                               
                        if Approval < 2:
                                call NoPantiesOn(Girl)   
                            
                        if Girl.Panties:                               
                                $ Line = Girl.Panties   
                                $ Girl.Panties = 0  
                                if Girl == KittyX:
                                        "She glances up at you as her [Line] fall clear of her." 
                                else:
                                        "She glances up at you as she removes her [Line]." 
                        call expression Girl.Tag + "_First_Bottomless"   
                        
                        
                "Lose the [Girl.Legs]." if Girl.Legs: 
                        if Girl.Panties and Approval >= 2:
                            $ Girl.FaceChange("sexy")
                            if Girl == RogueX:
                                    ch_r "I guess I could do that. . ."
                            elif Girl == KittyX:
                                    ch_k "That's. . . doable. . ."
                            elif Girl == EmmaX:    
                                    ch_e "I can manage that. . ."
                            elif Girl == LauraX: 
                                    ch_l "I guess I could. . ."
                        elif Approval:          
                                $ Girl.FaceChange("sexy", 1)    
                                if Approval < 2 and not Girl.Panties and Girl.HoseNum() < 10:
                                    call NoPantiesOn(Girl)
                        else:    
                                $ Girl.FaceChange("sexy")
                                call Bottoms_Off_Refused(Girl)
                                return
                            
                        $ Line = Girl.Legs      
                        $ Girl.Legs = 0
                        if not Girl.Panties and Girl.HoseNum() < 10:
                                $ Girl.FaceChange("sly", 2)
                                if Girl == KittyX:
                                        "She blushes and looks at you as her [Line] drops at her feet." 
                                elif Girl == RogueX:
                                        "She blushes and looks at you slyly before removing her [Line]." 
                                else:
                                        "She glaces at you slyly before removing her [Line]." 
                                call expression Girl.Tag + "_First_Bottomless"   
                        elif not Girl.SeenPanties:
                                if Girl == KittyX:
                                        "She blushes and looks at you as her [Line] drops at her feet." 
                                elif Girl == RogueX:
                                        "She blushes and looks at you slyly before removing her [Line]." 
                                else:
                                        "She glaces at you slyly before removing her [Line]." 
                                $ Girl.SeenPanties = 1
                        else:
                                "[Girl.Name] pulls her [Line] off." 
                        $ Girl.FaceChange("bemused", 1)
                
                "Lose the [Girl.Panties]." if Girl.Panties:
                        if Approval < 2:
                                if Girl == RogueX:
                                        ch_r "No thanks, [Girl.Petname]." 
                                elif Girl == KittyX:
                                        ch_k "Sorry, no."
                                elif Girl == EmmaX:    
                                        ch_e "I'm afraid not."
                                elif Girl == LauraX: 
                                        ch_l "No way.."
                                $ Girl.RecentActions.append("no bottomless")                      
                                $ Girl.DailyActions.append("no bottomless")   
                                return                        
                        elif Girl.PantsNum() >= 6 or Girl.HoseNum() >= 6:
                            if Girl == RogueX:
                                    ch_r "A little backwards, but sure. . ."
                            elif Girl == KittyX:
                                    ch_k "[Girl.Like]I guess. . ."
                            elif Girl == EmmaX:   
                                    ch_e "I suppose that I could. . ."
                            elif Girl == LauraX:                                 
                                    ch_l "Huh, ok. . ."                         
                        else:
                            if Girl == EmmaX:     
                                    ch_e "Of course."      
                            elif Girl == LauraX: 
                                    ch_l "Huh, ok. . ." 
                            else:
                                    call AnyLine(Girl,"Ok, sure, "+Girl.Petname+".")                          
                        $ Line = Girl.Panties   
                        $ Girl.Panties = 0                      
                        if Girl == KittyX:
                            if Girl.PantsNum() >= 5:
                                "She reaches a hand into her [Girl.Legs] and pulls her [Line] out through the pocket."
                                "She gives a little wink as she drops them to the ground."                            
                            elif Girl.HoseNum() >= 5:
                                "She reaches a hand into her [Girl.Hose] and pulls her [Line] out through the pocket."
                                "She gives a little wink as she drops them to the ground."
                            else:
                                "With a little shimmy, her [Line] drop to the ground."
                        elif Girl.PantsNum() >= 6:
                                "She pulls her [Girl.Legs] off, then removes her [Line], before putting them back on."                        
                        elif Girl.HoseNum() >= 6:
                                "She pulls her [Girl.Hose] off, then removes her [Line], before putting them back on."   
                        elif Girl.Legs:                            
                                "She reaches under her [Girl.Legs] and pulls her [Line] down."
                        else:
                                "She glances up at you as she removes her [Line]."
                        call expression Girl.Tag + "_First_Bottomless"  
                
                "Just give me a clear view. . ." if (Girl.Panties and not Girl.PantiesDown) or (Girl.Legs and not Girl.Upskirt):
                        if Approval >= 2:
                                if Girl == LauraX: 
                                        ch_l "Whatever."
                                else:
                                        call AnyLine(Girl,"Fine.")      
                                $ Girl.PantiesDown = 1 if Girl.Panties else 0
                                $ Girl.Upskirt = 1 if Girl.Legs else 0
                                if Girl.Legs:
                                        "She shifts her [Girl.Legs] out of the way."
                                else:
                                        "She shifts her [Girl.Panties] out of the way."
                        elif Approval >= 1 and Girl.Legs and Girl.Panties and not Girl.PantiesDown:
                                if Girl == RogueX:
                                        ch_r "I'll show you a little bit. . ."
                                elif Girl == KittyX:
                                        ch_k "I guess I could show you something. . ."
                                elif Girl == EmmaX:    
                                        ch_e "I'll give at least give a little view. . ."
                                elif Girl == LauraX: 
                                        ch_l "Make do with this. . ."
                                $ Girl.Upskirt = 1
                        else:                        
                                call AnyLine(Girl,"No.")
                                $ Girl.RecentActions.append("no bottomless")                      
                                $ Girl.DailyActions.append("no bottomless")   
                                return   
                        call expression Girl.Tag + "_First_Bottomless"    
                        
                "Lose the [Girl.Hose]." if Girl.Hose:
                        $ Girl.FaceChange("bemused", 1) 
                        if Girl.Legs:  
                            call AnyLine(Girl,"All right, fine.")  
                        elif Approval < 2 and not Girl.Panties and Girl.HoseNum() >= 10:
                            call NoPantiesOn(Girl)                            
                        elif not Approval and Girl.HoseNum() >= 6:
                            if Girl == RogueX:
                                    ch_r "No thanks, [Girl.Petname]."
                            else:
                                    call AnyLine(Girl,"Sorry, no, "+Girl.Petname+".")
                            return                            
                        else:
                            if Girl == RogueX:
                                    ch_r "Ok, sure, [Girl.Petname]."  
                            else:
                                    call AnyLine(Girl,"Fine, "+Girl.Petname+".")
                        $ Line = Girl.Hose   
                        $ Girl.Hose = 0  
                        if Girl == KittyX:
                            if Girl.PantsNum() >= 5:
                                "She reaches a hand into her [Girl.Legs] and pulls her [Line] right through her legs."
                                "She makes a little flourish and drops them to the ground."              
                            else:
                                "She gives a little shake and her [Line] drop to the ground."
                        elif Girl.PantsNum() >= 6:
                                "She pulls off her [Girl.Legs] and pulls her [Line] off, then puts them back on."
                        elif Girl.Legs:                        
                                "She reaches under her [Girl.Legs] and pulls her [Line] down."                        
                        elif Girl.HoseNum() < 10:
                                "[Girl.Name] pulls her [Line] off." 
                        elif not Girl.Panties:
                                $ Girl.FaceChange("sly", 2)  
                                "She blushes and looks at you slyly before removing her [Line]." 
                                $ Girl.Blush = 1
                                call expression Girl.Tag + "_First_Bottomless"   
                        elif not Girl.SeenPanties:
                                "[Girl.Name] shyly removes her [Line]."
                                $ Girl.SeenPanties = 1
                        else:
                                "[Girl.Name] pulls her [Line] off." 
                            
                "Keep it all on for now." if Cnt == 1:
                    $ Cnt = 0
                    
                "Ok, that's enough for now." if Cnt == 2:
                    $ Cnt = 0
                    
            $ Cnt = 2 if Cnt else Cnt  
            $ Line = "Anything else?"
        return


label NoPantiesOn(Girl=0): #called when asked to remove pants with nothing on under    
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        if not Girl.Panties:
            return
        
        if Girl == RogueX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_r "Well, I'm not exactly decent under here, you know. . ." 
                else:
                        ch_r "This is the last bit. . ."  
        elif Girl == KittyX:
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_k "[Girl.Like]I'm not wearing any panties. . ."  
                else:
                        ch_k "Not much else on. . ."  
        elif Girl == EmmaX:   
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_e "I don't have anything on under this. . ."  
                else:
                        ch_e "This is all I have on. . ."  
        elif Girl == LauraX: 
                if Girl.Legs or Girl.HoseNum() >= 10:
                        ch_l "I don't have anything on under this. . ."  
                else:
                        ch_l "These are all I have on. . ."  
        menu:
            extend ""
            "Could you do it anyway?":
                if ApprovalCheck(Girl, 1000, "LI", TabM=1):  
                        if Girl == RogueX:
                                ch_r "Well, if you're gonna ask so nicely. . . "  
                        elif Girl == KittyX:                    
                                ch_k "I[Girl.like]guess so. . . " 
                        elif Girl == EmmaX:                
                                ch_e "I suppose. . . "
                        elif Girl == LauraX:              
                                ch_l "I guess. . . "
                else:
                        if Girl == RogueX:
                                ch_r "Sorry, I don't think so."
                        elif Girl == KittyX:
                                ch_k "No thanks."
                        elif Girl == EmmaX:   
                                ch_e "I'm afraid not." 
                        elif Girl == LauraX: 
                                ch_l "Nah, not right now."
                        call Bottoms_Off_Refused(Girl)
                        $ renpy.pop_call()  
            "Don't care, lose'em.":
                if ApprovalCheck(Girl, 800, "OI", TabM=1):
                        if Girl == RogueX:
                                ch_r "Fine, whatever."  
                        elif Girl == KittyX:
                                ch_k "Whatev."  
                        elif Girl == EmmaX:    
                                ch_e "If you insist." 
                        elif Girl == LauraX: 
                                ch_l "Fine."  
                else:
                        call Bottoms_Off_Refused(Girl)
                        $ renpy.pop_call()  
                                           
            "Ok, you can leave it on.":
                $ renpy.pop_call()   
        return 
        
label Bottoms_Off_Refused(Girl=0):    
        $ Girl = Ch_Focus if not Girl else Girl
        call Shift_Focus(Girl)
        
        if Girl == RogueX:
                if "no bottomless" in Girl.RecentActions:  
                        ch_r "What part of \"no\" escapes you, [Girl.Petname]?"
                elif "no bottomless" in Girl.DailyActions:  
                        ch_r "If you keep this up, not ever, [Girl.Petname]."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:            
                        ch_r "That's enough, [Girl.Petname]. Sure we can't have some fun anyway?" 
                    else:
                        ch_r "I'm afraid not this time, [Girl.Petname]. Sure we can't have some fun anyway?"   
        elif Girl == KittyX:
                if "no bottomless" in Girl.RecentActions:  
                        ch_k "You're[Girl.like]on my last nerve here."
                elif "no bottomless" in Girl.DailyActions:  
                        ch_k "Give it a rest."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:            
                        ch_k "What you see is what you get, but[Girl.like]can't we still have some fun?"   
                    else:
                        ch_k "The answer's \"no,\" but[Girl.like]can't we still have some fun?"  
        elif Girl == EmmaX:   
                if "no bottomless" in Girl.RecentActions:  
                        ch_e "Try to control your impulses."
                elif "no bottomless" in Girl.DailyActions:  
                        ch_e "Not today."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:            
                        ch_e "That's all I'm willing to do, is that a deal-breaker?"   
                    else:
                        ch_e "I'm afraid not, is that a deal-breaker?"     
        elif Girl == LauraX:  
                if "no bottomless" in Girl.RecentActions:  
                        ch_l "Reign it in."
                elif "no bottomless" in Girl.DailyActions:  
                        ch_l "No, not today."
                else:
                    $ Girl.FaceChange("sad")
                    if Cnt == 2:            
                        ch_l "No more, is that going to be a problem?"   
                    else:
                        ch_l "Nope, is that going to be a problem?"   
        menu:
            extend ""
            "Sure, never mind." if "no bottomless" not in Girl.RecentActions:
                    $ Girl.Mouth = "smile"
                    $ Girl.Statup("Love", 70, 2)    
                    $ Girl.Statup("Obed", 60, 2)          
                    if Girl == RogueX:
                            ch_r "Great."    
                    elif Girl == KittyX:
                            ch_k "Great!"    
                    elif Girl == EmmaX:  
                            ch_e "Excellent."    
                    elif Girl == LauraX:   
                            ch_l "Right."   
                        
            "Sorry, I'll drop it." if "no bottomless" in Girl.RecentActions:   
                    if Girl == EmmaX:   
                            ch_e "Good."   
                    elif Girl == LauraX: 
                            ch_l "Cool."
                    else:
                            call AnyLine(Girl,"Fine. . .")
                
            "No, let's do something else.":
                    $ Girl.Brows = "confused"
                    if Girl == RogueX:
                            ch_r "Ok [Girl.Petname], your loss." 
                    elif Girl == KittyX:
                            ch_k "Ok[Girl.like]whatever."
                    else:    
                            call AnyLine(Girl,"Your loss.")            
                    $ Girl.Statup("Lust", 50, 5)
                    $ Girl.Statup("Love", 70, -2, 1)
                    if "no bottomless" not in Girl.RecentActions:  
                            $ Girl.Statup("Obed", 60, 4)      
                    $ Girl.RecentActions.append("angry")
                    $ Girl.DailyActions.append("angry")   
                
        $ Girl.RecentActions.append("no bottomless")                      
        $ Girl.DailyActions.append("no bottomless")
        $ Tempmod = 0
        return       
        
    
# End Bottoms Off / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /    

        
        
# Start First Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Rogue Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Rogue_First_Topless(Silent = 0, TempLine=0):     
    if RogueX.ChestNum() > 1 or RogueX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return   
    if RogueX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return     
    $ RogueX.RecentActions.append("topless")                      
    $ RogueX.DailyActions.append("topless")
    $ RogueX.DrainWord("no topless")   
    $ RogueX.SeenChest += 1 
    if RogueX.SeenChest > 1:     
            return                  #ends portion if you've already seen them
    
    $ RogueX.Statup("Inbt", 70, 20)  
    if not Silent:
        $ RogueX.FaceChange("bemused", 1)
        "[RogueX.Name] looks a bit shy, and slowly lowers her hands from her chest."
        ch_r "Well, [RogueX.Petname]? Like what you see?"    
        menu:
            extend ""
            "Nod":            
                    $ RogueX.Statup("Love", 90, 20)
                    $ RogueX.Statup("Inbt", 70, 20)               
                    $ RogueX.FaceChange("smile")
                    ch_r ". . ."
                    $ RogueX.Statup("Love", 40, 20)
            "Whatever.":        
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 50, 20)
                    $ RogueX.Statup("Inbt", 70, -10)                          
                    $ RogueX.FaceChange("angry")
                    ch_r "Hmph!"
                    $ RogueX.Statup("Obed", 70, 20)
            "Well, they aren't that bad. . .":        
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 60, 25)
                    $ RogueX.Statup("Inbt", 70, -15)                          
                    $ RogueX.FaceChange("confused",2)
                    ch_r "Say what now?"
                    menu:      
                        "I, um, no, they're great!":                        
                                $ RogueX.FaceChange("angry",2, Mouth="smile")
                                $ RogueX.Statup("Inbt", 70, 10)   
                                ch_r "Of couse they are!"            
                        "[EmmaX.Name]'s were bigger, that's all." if EmmaX.SeenChest:                            
                                $ TempLine = EmmaX
                        "[KittyX.Name]'s were tighter, that's all." if KittyX.SeenChest:                            
                                $ TempLine = KittyX
                            
                    if TempLine:
                            $ RogueX.FaceChange("angry")
                            $ RogueX.Mouth = "surprised"                        
                            $ RogueX.Statup("Love", 90, -10)
                            $ RogueX.Statup("Obed", 80, 30)
                            $ RogueX.Statup("Inbt", 70, -25) 
                            ". . ."
                            $ RogueX.Mouth = "sad"
                            if TempLine == EmmaX:
                                    if RogueX.LikeEmma >= 800:
                                            $ RogueX.FaceChange("sly",2,Eyes="side")
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "Well, I mean they would be quite the handful. . ."       
                                            $ RogueX.LikeEmma += 20 
                                    elif RogueX.LikeEmma >= 700:
                                            $ RogueX.Eyes = "side" 
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "I mean, I guess, if you like that kind of thing. . ."
                                    else:                        
                                            $ RogueX.LikeEmma -= 50
                                            $ Templine = "bad"
                            elif TempLine == KittyX:
                                    if RogueX.LikeKitty >= 800:
                                            $ RogueX.FaceChange("sly",2,Eyes="side")
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "They are kind of adorable. . ."       
                                            $ RogueX.LikeKitty += 20 
                                    elif RogueX.LikeKitty >= 700:
                                            $ RogueX.Eyes = "side" 
                                            $ RogueX.Statup("Obed", 80, 5)
                                            ch_r "I mean, yeah, I guess. . ."    
                                    else:                        
                                            $ RogueX.LikeKitty -= 50
                                            $ Templine = "bad"
                            
                            if TempLine == "bad":
                                            $ RogueX.Statup("Love", 90, -20)
                                            ch_r "Yeah, that's enough outta you, [RogueX.Petname]."   
                                            $ RogueX.OutfitChange()
                                            $ RogueX.RecentActions.append("no topless")                      
                                            $ RogueX.DailyActions.append("no topless")  
                                            $ RogueX.RecentActions.append("angry")
                                            $ RogueX.DailyActions.append("angry")  
    else:
        if ApprovalCheck(RogueX, 800) and not RogueX.Forced:
                $ RogueX.Statup("Inbt", 70, 20) 
                $ RogueX.Statup("Obed", 70, 10)    
        else:        
                $ RogueX.Statup("Love", 90, -30)
                $ RogueX.Statup("Inbt", 70, -10)                          
                $ RogueX.FaceChange("angry")
                $ RogueX.Statup("Obed", 70, 30)
    return
    
    
label Rogue_First_Bottomless(Silent = 0):   
    if RogueX.PantiesNum() > 1 or RogueX.PantsNum() > 2 or RogueX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return     
    if RogueX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return   
    $ RogueX.RecentActions.append("bottomless")                      
    $ RogueX.DailyActions.append("bottomless")
    $ RogueX.DrainWord("no bottomless")
    $ RogueX.SeenPussy += 1 
    if RogueX.SeenPussy > 1:  
            #ends portion if you've already seen them  
            return                        
    
    $ RogueX.Statup("Inbt", 80, 40)     
    if not Silent:
        $ RogueX.FaceChange("bemused", 1)
        "[RogueX.Name] shyly moves her hands aside, revealing her pussy."        
        menu:        
            ch_r "Well, [RogueX.Petname]? Was it worth the wait?"
            "Lovely. . .":            
                    $ RogueX.Statup("Love", 90, 20)
                    $ RogueX.Statup("Inbt", 60, 30)            
                    $ RogueX.FaceChange("smile")          
                    ch_r ". . ."
                    $ RogueX.Statup("Love", 40, 20)
            "I suppose.":        
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Obed", 50, 20)
                    $ RogueX.Statup("Inbt", 70, -20)
                    $ RogueX.FaceChange("angry")           
                    ch_r ". . ."
                    $ RogueX.Statup("Obed", 70, 30)
    else:
            if ApprovalCheck(RogueX, 500):
                    $ RogueX.Statup("Love", 90, 20)
                    $ RogueX.Statup("Inbt", 60, 30)       
                    $ RogueX.Statup("Love", 40, 20)
            else:        
                    $ RogueX.Statup("Love", 90, -30)
                    $ RogueX.Statup("Inbt", 70, -10)
                    $ RogueX.FaceChange("angry")          
                    $ RogueX.Statup("Obed", 70, 30)
    return
    
# Kitty Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Kitty_First_Topless(Silent = 0, TempLine = 0):  
    if KittyX.ChestNum() > 1 or KittyX.OverNum() > 2:
            #if she's wearing substantial clothing. . .
            return          
    if KittyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ KittyX.RecentActions.append("topless")                      
    $ KittyX.DailyActions.append("topless")
    $ KittyX.DrainWord("no topless")    
    $ KittyX.SeenChest += 1 
    if KittyX.SeenChest > 1:     
            return                  #ends portion if you've already seen them
    
    
    $ KittyX.Statup("Inbt", 70, 15)  
    if not Silent:
        $ KittyX.FaceChange("bemused", 2)
        "Kitty looks a bit shy, and slowly lowers her hands from her chest."
        ch_k "[KittyX.Like]what do you think?"    
        $ KittyX.Blush = 1
        menu:
            extend ""
            "Lovely.":            
                $ KittyX.Statup("Love", 90, 20)
                $ KittyX.Statup("Inbt", 70, 20)               
                $ KittyX.FaceChange("smile",2)
                ch_k ". . ."
                $ KittyX.Statup("Love", 40, 20)  
                $ KittyX.Blush = 1
                        
            "That's it?":        
                    $ KittyX.Statup("Love", 90, -30)
                    $ KittyX.Statup("Obed", 60, 25)
                    $ KittyX.Statup("Inbt", 70, -15)                          
                    $ KittyX.FaceChange("confused",2)
                    ch_k "What?"
                    menu:      
                        "I, um, no, they're great!":                        
                            $ KittyX.FaceChange("angry",2, Mouth="smile")
                            $ KittyX.Statup("Inbt", 70, 10)   
                            ch_k "Obviously!"            
                        "[EmmaX.Name]'s were bigger, that's all." if EmmaX.SeenChest:                            
                                $ TempLine = EmmaX                                 
                        "[RogueX.Name]'s were bigger, that's all." if RogueX.SeenChest:                            
                                $ TempLine = RogueX
                        "[LauraX.Name]'s were bigger, that's all." if LauraX.SeenChest:                            
                                $ TempLine = LauraX
                                    
                    if TempLine:
                            $ KittyX.FaceChange("angry")
                            $ KittyX.Mouth = "surprised"                        
                            $ KittyX.Statup("Love", 90, -10)
                            $ KittyX.Statup("Obed", 80, 30)
                            $ KittyX.Statup("Inbt", 70, -25)  
                            ". . ."
                            $ KittyX.Mouth = "sad"
                            if TempLine == EmmaX:
                                    if KittyX.LikeEmma >= 800:
                                            $ KittyX.FaceChange("sly",2,Eyes="side")
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "Yeah, like you just wanna shove your head into there. . ."       
                                            $ KittyX.LikeEmma += 20 
                                    elif KittyX.LikeEmma >= 700:
                                            $ KittyX.Eyes = "side" 
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "I mean, I guess, if you like that kind of thing. . ."
                                    else:                        
                                            $ KittyX.LikeEmma -= 50
                                            $ Templine = "bad"                                    
                            elif TempLine:                                        
                                    if KittyX.GirlLikeCheck(TempLine) >= 800: 
                                            $ KittyX.FaceChange("sly",2,Eyes="side")
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "Yeah, like two ripe apples. . . I mean-"   
                                            $ KittyX.GirlLikeUp(TempLine,20)
                                    elif KittyX.GirlLikeCheck(TempLine) >= 700:
                                            $ KittyX.Eyes = "side" 
                                            $ KittyX.Statup("Obed", 80, 5)
                                            ch_k "[KittyX.Like]I guess. . ." 
                                    else:                           
                                            $ KittyX.GirlLikeUp(TempLine,-50)
                                            $ Templine = "bad"
                                                    
                            if TempLine == "bad":
                                            $ KittyX.Statup("Love", 90, -20)
                                            ch_k "Well you sure know how to ruin a mood."     
                                            $ KittyX.OutfitChange()
                                            $ KittyX.RecentActions.append("no topless")                      
                                            $ KittyX.DailyActions.append("no topless")  
                                            $ KittyX.RecentActions.append("angry")
                                            $ KittyX.DailyActions.append("angry") 
                        
                    
    else:
            if ApprovalCheck(KittyX, 800) and not KittyX.Forced:                #if she's not forced and happy about it
                    $ KittyX.Statup("Inbt", 70, 15) 
                    $ KittyX.Statup("Obed", 70, 15)     
            else:                                                           #if she's not happy about it
                    $ KittyX.Statup("Love", 90, -40)
                    $ KittyX.Statup("Inbt", 70, -20)                          
                    $ KittyX.FaceChange("angry")
                    $ KittyX.Statup("Obed", 70, 40)
    return
    
label Kitty_First_Bottomless(Silent = 0): 
    if KittyX.PantiesNum() > 1 or KittyX.PantsNum() > 2 or KittyX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return     
    if KittyX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return
    $ KittyX.RecentActions.append("bottomless")                      
    $ KittyX.DailyActions.append("bottomless")
    $ KittyX.DrainWord("no bottomless")
    $ KittyX.SeenPussy += 1 
    if KittyX.SeenPussy > 1:     
            return                  #ends portion if you've already seen them        
    
    
    $ KittyX.Statup("Inbt", 80, 30)  
    $ KittyX.Statup("Obed", 70, 10)   
    if not Silent:
        $ KittyX.FaceChange("bemused", 1)
        "[KittyX.Name] shyly moves her hands aside, revealing her pussy."        
        menu:        
            extend ""
            "Lovely. . .":            
                    $ KittyX.Statup("Love", 90, 20)
                    $ KittyX.Statup("Inbt", 60, 25)            
                    $ KittyX.FaceChange("smile")          
                    ch_k ". . ."
                    $ KittyX.Statup("Love", 40, 20)
            "Now {i}that's{/i} the \"Kitty\" I wanted to see.":   
                    $ KittyX.Statup("Love", 40, 25) 
                    $ KittyX.Statup("Inbt", 60, 30)           
                    $ KittyX.FaceChange("perplexed", 2)          
                    ch_k "[[snort]"            
                    $ KittyX.Statup("Love", 90, 25)
                    $ KittyX.Blush = 1
            "Pretty messy down there." if KittyX.Pubes:          
                    $ KittyX.FaceChange("surprised",2)  
                    ch_k "!"
                    if ApprovalCheck(KittyX, 800, "LO"):          
                            $ KittyX.FaceChange("bemused",1)     
                            $ KittyX.Statup("Obed", 50, 30)
                            $ KittyX.Statup("Inbt", 60, 25)        
                            ch_k "I guess I could trim it up a bit. . ."
                            $ KittyX.Todo.append("shave")  
                    else:                              
                            $ KittyX.FaceChange("angry",1)  
                            $ KittyX.Statup("Love", 40, -20) 
                            $ KittyX.Statup("Obed", 50, 25)
                            $ KittyX.Statup("Inbt", 60, -5)         
                            ch_k "Well[KittyX.like]sorry I don't keep it baby soft!"
            "I've seen better.":        
                    $ KittyX.Statup("Love", 90, -30)
                    $ KittyX.Statup("Obed", 50, 25)
                    $ KittyX.Statup("Inbt", 70, -30)
                    $ KittyX.FaceChange("angry")           
                    ch_k ". . ."
                    $ KittyX.Statup("Obed", 70, 35)
    else:
            if ApprovalCheck(KittyX, 800) and not KittyX.Forced:
                    $ KittyX.Statup("Love", 90, 20)
                    $ KittyX.Statup("Inbt", 60, 25)       
                    $ KittyX.Statup("Love", 40, 20)
                    $ KittyX.Statup("Obed", 70, 10)
            else:        
                    $ KittyX.Statup("Love", 90, -40)
                    $ KittyX.Statup("Inbt", 70, -20)
                    $ KittyX.FaceChange("angry")          
                    $ KittyX.Statup("Obed", 70, 30)
    return
    

# Emma Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Emma_First_Topless(Silent = 0, TempLine = 0):    
    if EmmaX.ChestNum() > 1 or EmmaX.OverNum() > 2:
        #if she's wearing substantial clothing. . .
        return     
    if EmmaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return   
    $ EmmaX.RecentActions.append("topless")                      
    $ EmmaX.DailyActions.append("topless")
    $ EmmaX.DrainWord("no topless")    
    $ EmmaX.SeenChest += 1 
    if EmmaX.SeenChest > 1:     
        return                  #ends portion if you've already seen them
    
    
    $ EmmaX.Statup("Inbt", 70, 15)  
    if not Silent:
        $ EmmaX.FaceChange("sly")
        "You get your first look at [EmmaX.Name]'s bare chest."
        ch_e "Well, [EmmaX.Petname]? Is it everything you dreamed?"    
        $ EmmaX.Blush = 1
        menu:
            extend ""
            "Definitely, and more.":            
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 70, 20)               
                    $ EmmaX.FaceChange("smile",1)
                    ch_e "I do aim to impress."
                    $ EmmaX.Statup("Love", 40, 20)  
                    $ EmmaX.Blush = 0
            ". . . [[stunned]":            
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 70, 30)
                    ch_e "Yes, that would be the usual reaction."
                    $ EmmaX.Statup("Love", 40, 10)  
            "Huh, not what I was expecting. . .":        
                    $ EmmaX.Statup("Love", 90, -30)
                    $ EmmaX.Statup("Obed", 60, 25)
                    $ EmmaX.Statup("Inbt", 70, -15)                          
                    $ EmmaX.FaceChange("confused",2)
                    ch_e "What?"
                    menu:        
                        "They're even better than I imagined!":    
                                $ EmmaX.Statup("Love", 90, 20)
                                $ EmmaX.Statup("Obed", 60, -20)
                                $ EmmaX.Statup("Inbt", 70, 20)                          
                                $ EmmaX.FaceChange("perplexed",1)
                                ch_e "Well, I suppose you managed to salvage that one. . ."
                        "I, um, no, they're great!":                        
                                $ EmmaX.FaceChange("angry",2, Mouth="smile")
                                $ EmmaX.Statup("Inbt", 70, 10)   
                                ch_e "Of couse they are!"            
                        "[RogueX.Name]'s were tighter, that's all." if RogueX.SeenChest:                            
                                $ TempLine = RogueX
                        "[KittyX.Name]'s were tighter, that's all." if KittyX.SeenChest:                            
                                $ TempLine = KittyX
                        "[LauraX.Name]'s were tighter, that's all." if LauraX.SeenChest:                            
                                $ TempLine = LauraX
                            
                    if TempLine:
                            $ EmmaX.FaceChange("angry")
                            $ EmmaX.Mouth = "surprised"                        
                            $ EmmaX.Statup("Love", 90, -10)
                            $ EmmaX.Statup("Obed", 80, 30)
                            $ EmmaX.Statup("Inbt", 70, -25)  
                            ". . ."
                            $ EmmaX.Mouth = "sad"
                            if TempLine == KittyX:
                                    if EmmaX.LikeKitty >= 800:
                                            $ EmmaX.FaceChange("sly",2,Eyes="side")
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "They are rather . . . pert. . ."       
                                            $ EmmaX.LikeKitty += 20 
                                    elif EmmaX.LikeKitty >= 700:
                                            $ EmmaX.Eyes = "side" 
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "Well, for a child. . ."    
                                    else:                        
                                            $ EmmaX.LikeKitty -= 50
                                            $ Templine = "bad"
                                        
                            elif TempLine:
                                    if EmmaX.GirlLikeCheck(TempLine) >= 800: 
                                            $ EmmaX.FaceChange("sly",2,Eyes="side")
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "They are rather . . . ripe. . ."    
                                            $ EmmaX.GirlLikeUp(TempLine,20)
                                    elif EmmaX.GirlLikeCheck(TempLine) >= 700:
                                            $ EmmaX.Eyes = "side" 
                                            $ EmmaX.Statup("Obed", 80, 5)
                                            ch_e "I suppose if you prefer that. . ."    
                                    else:                           
                                            $ EmmaX.GirlLikeUp(TempLine,-50)
                                            $ Templine = "bad"
                            
                            
                            if TempLine == "bad":
                                            $ EmmaX.Statup("Love", 90, -20)
                                            ch_e "I think you've seen enough for now, [EmmaX.Petname]."   
                                            $ EmmaX.OutfitChange()
                                            $ EmmaX.RecentActions.append("no topless")                      
                                            $ EmmaX.DailyActions.append("no topless")  
                                            $ EmmaX.RecentActions.append("angry")
                                            $ EmmaX.DailyActions.append("angry")  
                            
                    
    else:
            if ApprovalCheck(EmmaX, 800) and not EmmaX.Forced:                #if she's not forced and happy about it
                    $ EmmaX.Statup("Inbt", 70, 15) 
                    $ EmmaX.Statup("Obed", 70, 15)       
            else:                                                           #if she's not happy about it
                    $ EmmaX.Statup("Love", 90, -40)
                    $ EmmaX.Statup("Inbt", 70, -20)                          
                    $ EmmaX.FaceChange("angry")
                    $ EmmaX.Statup("Obed", 70, 40)
    return
    
    
label Emma_First_Bottomless(Silent = 0): 
    if EmmaX.PantiesNum() > 1 or EmmaX.PantsNum() > 2 or EmmaX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .  
            return     
    if EmmaX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return   
    $ EmmaX.RecentActions.append("bottomless")                      
    $ EmmaX.DailyActions.append("bottomless")
    $ EmmaX.DrainWord("no bottomless")
    $ EmmaX.SeenPussy += 1 
    if EmmaX.SeenPussy > 1:     
            return                  #ends portion if you've already seen them        
    
    
    $ EmmaX.Statup("Inbt", 80, 30)  
    $ EmmaX.Statup("Obed", 70, 10)   
    if not Silent:
        $ EmmaX.FaceChange("sly")
        "You find yourself staring at [EmmaX.Name]'s bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                    $ EmmaX.Statup("Love", 90, 20)
                    $ EmmaX.Statup("Inbt", 60, 25)            
                    $ EmmaX.FaceChange("smile")          
                    ch_e "I'm aware. . . "
                    $ EmmaX.Statup("Love", 40, 20)
            "I see you keep it smooth down there." if not EmmaX.Pubes:          
                $ EmmaX.FaceChange("confused",1)  
                ch_e "Yes?"
                if ApprovalCheck(EmmaX, 700, "LO"):    
                        $ EmmaX.FaceChange("bemused")     
                        menu:
                            ch_e "Do you prefer more fuzz?"
                            "Yes":
                                if ApprovalCheck(EmmaX, 900, "LO"):
                                        $ EmmaX.Statup("Obed", 50, 30)
                                        $ EmmaX.Statup("Inbt", 60, 25)        
                                        ch_e "I suppose I could let it go. . ."
                                        $ EmmaX.Todo.append("pubes")  
                                else:   
                                        $ EmmaX.FaceChange("normal")     
                                        ch_e "Well that's a pity."
                            "Up to you, I guess.":
                                        $ EmmaX.Statup("Love", 80, 10)
                                        ch_e "I'm glad you agree."
                            "No, leave it that way.":  
                                        if ApprovalCheck(EmmaX, 900, "LO"):
                                                $ EmmaX.FaceChange("sly")    
                                                $ EmmaX.Statup("Love", 80, 10)
                                        else:
                                                $ EmmaX.FaceChange("angry",Mouth="normal")    
                                        $ EmmaX.Statup("Inbt", 60, 25) 
                                        ch_e "I'm glad I have your. . . permission."
                                        $ EmmaX.Brows = "normal"
                else:                              
                        $ EmmaX.FaceChange("angry",1)  
                        $ EmmaX.Statup("Love", 40, -20) 
                        $ EmmaX.Statup("Obed", 50, 25)
                        $ EmmaX.Statup("Inbt", 60, -5)         
                        ch_e "Yes, I'm afraid I don't like an unkept garden."
            "Not bad for someone your age.":        
                $ EmmaX.Statup("Love", 90, -30)
                $ EmmaX.Statup("Obed", 50, 25)
                $ EmmaX.Statup("Inbt", 70, -30)
                $ EmmaX.FaceChange("angry",2)           
                if not EmmaX.Forced and not ApprovalCheck(EmmaX, 900, "LO"):                    
                        $ EmmaX.RecentActions.append("angry")
                        $ EmmaX.DailyActions.append("angry")  
                        $ EmmaX.Statup("Obed", 70, 25)
                ch_e "You will regret that remark. . ."
    else:
        
        if ApprovalCheck(EmmaX, 800) and not EmmaX.Forced:
                $ EmmaX.Statup("Love", 90, 20)
                $ EmmaX.Statup("Inbt", 60, 25)       
                $ EmmaX.Statup("Love", 40, 20)
                $ EmmaX.Statup("Obed", 70, 10)
        else:        
                $ EmmaX.Statup("Love", 90, -40)
                $ EmmaX.Statup("Inbt", 70, -20)
                $ EmmaX.FaceChange("angry")          
                $ EmmaX.Statup("Obed", 70, 30)
    return
    
# Laura Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
label Laura_First_Topless(Silent = 0, TempLine = 0):     
    if LauraX.ChestNum() > 1 or LauraX.OverNum() > 2:
        #if she's wearing substantial clothing. . .
        return     
    if LauraX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return   
    $ LauraX.RecentActions.append("topless")                      
    $ LauraX.DailyActions.append("topless")
    $ LauraX.DrainWord("no topless")    
    $ LauraX.SeenChest += 1 
    if LauraX.SeenChest > 1:     
            return                  #ends portion if you've already seen them
    
    $ LauraX.Statup("Inbt", 70, 15)  
    if not Silent:
        $ LauraX.FaceChange("sly")
        "You get your first look at Laura's bare chest."
        ch_l "So? What are you looking at?"    
        $ LauraX.Blush = 1
        menu:
            extend ""
            "Your tits, they look great.":            
                    $ LauraX.Statup("Love", 90, 20)
                    $ LauraX.Statup("Inbt", 70, 20)           
                    $ LauraX.FaceChange("sexy",1,Eyes="down")    
                    ch_l "Huh. I mean I guess so. . ."           
                    $ LauraX.FaceChange("smile",0)
                    $ LauraX.Statup("Love", 40, 20)
            ". . . [[stunned]":            
                    $ LauraX.Statup("Love", 90, 10)
                    $ LauraX.Statup("Inbt", 70, 10)
                    ch_l "Cat got your tongue?"
                    $ LauraX.Statup("Love", 40, 10)  
            "Huh, not what I was expecting. . .":        
                    $ LauraX.Statup("Love", 90, -30)
                    $ LauraX.Statup("Obed", 60, 25)
                    $ LauraX.Statup("Inbt", 70, -15)                          
                    $ LauraX.FaceChange("confused",2)
                    ch_l "Huh?"
                    menu:        
                        "They're really perky!":    
                                $ LauraX.Statup("Love", 90, 20)
                                $ LauraX.Statup("Obed", 60, -20)
                                $ LauraX.Statup("Inbt", 70, 20)                          
                                $ LauraX.FaceChange("perplexed",1)
                                ch_l "Oh. Right. . ."
                        "I, um, no, they're great!":                        
                                $ LauraX.FaceChange("angry",2, Mouth="smile")
                                $ LauraX.Statup("Inbt", 70, 10)   
                                ch_l "Why wouldn't they be?"  
                        "[KittyX.Name]'s were tighter, that's all." if KittyX.SeenChest:                            
                                $ TempLine = KittyX
                        "[EmmaX.Name]'s were a lot bigger, that's all." if EmmaX.SeenChest:                            
                                $ TempLine = EmmaX
                                                        
                    if TempLine:
                            $ LauraX.FaceChange("angry")
                            $ LauraX.Mouth = "surprised"                        
                            $ LauraX.Statup("Love", 90, -10)
                            $ LauraX.Statup("Obed", 80, 30)
                            $ LauraX.Statup("Inbt", 70, -25)  
                            ". . ."
                            $ LauraX.Mouth = "sad"
                            if TempLine == EmmaX:
                                    if LauraX.LikeEmma >= 800:
                                        $ LauraX.FaceChange("sly",2,Eyes="side")
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "They are kinda huge. . ."       
                                        $ LauraX.LikeEmma += 20 
                                    elif LauraX.LikeEmma >= 600:
                                        $ LauraX.Eyes = "side" 
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "I guess that's true. . ."    
                                    else:                        
                                        $ LauraX.LikeEmma -= 50
                                        $ Templine = "bad"
                                    
                            elif TempLine == KittyX:
                                    if LauraX.LikeKitty >= 800:
                                        $ LauraX.FaceChange("sly",2,Eyes="side")
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "She is very. . . streamlined. . ."       
                                        $ LauraX.LikeKitty += 20 
                                    elif LauraX.LikeKitty >= 700:
                                        $ LauraX.Eyes = "side" 
                                        $ LauraX.Statup("Obed", 80, 5)
                                        ch_l "they are kinda. . . pointy. . ."    
                                    else:                        
                                        $ LauraX.LikeKitty -= 50
                                        $ Templine = "bad"
                            
                            
                            if TempLine == "bad":
                                    $ LauraX.Statup("Love", 90, -20)
                                    ch_l "Still kinda rude though."   
                                    $ LauraX.OutfitChange()
                                    $ LauraX.RecentActions.append("no topless")                      
                                    $ LauraX.DailyActions.append("no topless")  
                                    $ LauraX.RecentActions.append("angry")
                                    $ LauraX.DailyActions.append("angry")  
                        
                    
    else:
            if ApprovalCheck(LauraX, 800) and not LauraX.Forced:                #if she's not forced and happy about it
                    $ LauraX.Statup("Inbt", 70, 15) 
                    $ LauraX.Statup("Obed", 70, 15)  
            else:                                                           #if she's not happy about it
                    $ LauraX.Statup("Love", 90, -40)
                    $ LauraX.Statup("Inbt", 70, -20)                          
                    $ LauraX.FaceChange("angry")
                    $ LauraX.Statup("Obed", 70, 40)
    return
    
    
label Laura_First_Bottomless(Silent = 0): 
    if LauraX.PantiesNum() > 1 or LauraX.PantsNum() > 2 or LauraX.HoseNum() > 9:
            #if she's wearing substantial clothing. . .
            return     
    if LauraX.Loc != bg_current and "phonesex" not in Player.RecentActions:
            return   
    $ LauraX.RecentActions.append("bottomless")                      
    $ LauraX.DailyActions.append("bottomless")
    $ LauraX.DrainWord("no bottomless")
    $ LauraX.SeenPussy += 1 
    if LauraX.SeenPussy > 1:     
            return                  #ends portion if you've already seen them        
    
    
    $ LauraX.Statup("Inbt", 80, 30)  
    $ LauraX.Statup("Obed", 70, 10)   
    if not Silent:
        $ LauraX.FaceChange("sly")
        if LauraX.Pubes:
                "You find yourself staring at [LauraX.Name]'s furry pussy."   
        else:
                "You find yourself staring at [LauraX.Name]'s bare pussy."        
        menu:        
            extend ""
            "Niiice. . .":            
                    $ LauraX.Statup("Love", 90, 20)
                    $ LauraX.Statup("Inbt", 60, 25)            
                    $ LauraX.FaceChange("smile")          
                    ch_l "You think?"
                    ch_l "Yeah, I like it too. . . "
                    $ LauraX.Statup("Love", 40, 20)
            "I see you keep it natural down there." if LauraX.Pubes:          
                $ LauraX.FaceChange("confused",1)  
                ch_l "Well. . . yeah."
                if ApprovalCheck(LauraX, 700, "LO"):    
                    $ LauraX.FaceChange("bemused")     
                    menu:
                        ch_l "What, am I supposed to shave it?"
                        "Yes":
                            if ApprovalCheck(LauraX, 900, "LO"):
                                    $ LauraX.Statup("Obed", 50, 30)
                                    $ LauraX.Statup("Inbt", 60, 25)        
                                    ch_l "I guess I could. . ."
                                    $ LauraX.Todo.append("pubes")  
                            else:   
                                    $ LauraX.FaceChange("normal")     
                                    ch_l "Seems like a waste of time."
                                    ch_l "Do you know how fast my hair grows?"
                        "Up to you, I guess.":
                                    $ LauraX.Statup("Love", 80, 10)
                                    ch_l "Yeah, I mean, shaving would be a lot of work."
                        "No, leave it that way.":  
                                    if ApprovalCheck(LauraX, 900, "LO"):
                                            $ LauraX.FaceChange("sly")    
                                            $ LauraX.Statup("Love", 80, 10)
                                    else:
                                            $ LauraX.FaceChange("angry",Mouth="normal")    
                                    $ LauraX.Statup("Inbt", 60, 25) 
                                    ch_l "Right."
                                    $ LauraX.Brows = "normal"
                else:                              
                        $ LauraX.FaceChange("angry",1)  
                        $ LauraX.Statup("Love", 40, -20) 
                        $ LauraX.Statup("Obed", 50, 25)
                        $ LauraX.Statup("Inbt", 60, -5)         
                        ch_l "I mean, what else would I do?"
            "What a mess.":        
                    $ LauraX.Statup("Love", 90, -30)
                    $ LauraX.Statup("Obed", 50, 25)
                    $ LauraX.Statup("Inbt", 70, -30)
                    $ LauraX.FaceChange("angry",2)           
                    if not LauraX.Forced and not ApprovalCheck(LauraX, 900, "LO"):                    
                            $ LauraX.RecentActions.append("angry")
                            $ LauraX.DailyActions.append("angry")  
                            $ LauraX.Statup("Obed", 70, 25)
                    ch_l "I'll make you a mess. . ."
    else:        
        if ApprovalCheck(LauraX, 800) and not LauraX.Forced:
                $ LauraX.Statup("Love", 90, 20)
                $ LauraX.Statup("Inbt", 60, 25)        
                $ LauraX.Statup("Love", 40, 20)
                $ LauraX.Statup("Obed", 70, 10)
        else:        
                $ LauraX.Statup("Love", 90, -40)
                $ LauraX.Statup("Inbt", 70, -20)
                $ LauraX.FaceChange("angry")          
                $ LauraX.Statup("Obed", 70, 30)
    return
# End First Topless/Bottomless / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# End Undressing / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start Dressing Screen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Display_DressScreen(Girl=Ch_Focus):
        #asks if you're willing to put up a protective dressing screen, XTaboo is the girl's local taboo
        # call Display_DressScreen(Girl)
        if renpy.showing('DressScreen'):
            return 1
                
        if Girl.Taboo:
            return 0
        
        $ Girl.FaceChange("bemused",1,Eyes="side")
        if "screen" in Girl.DailyActions:
                pass
        elif Girl == RogueX:
                ch_r "I'm not really comfortable like this."
        elif Girl == KittyX:
                ch_k "I'm getting kinda exposed here."
        elif Girl == EmmaX:
                ch_e "I'm feeling a bit exposed here. . ."
        elif Girl == LauraX:
                ch_l "I don't know about showing this much skin."
        $ Girl.AddWord(1,0,"screen") #adds screen to daily
        $ Girl.FaceChange("bemused",1)
        call AnyLine(Girl,"Mind if I get behind a dressing screen?")
        menu:
            extend ""
            "Go ahead":
                    show DressScreen zorder 150
                    if Girl == RogueX:
                            ch_r "Thanks."                   
                    elif Girl == KittyX:
                            ch_k "Great." 
                    elif Girl == EmmaX:
                            ch_e "Thank you." 
                    elif Girl == LauraX:
                            ch_l "K."  
                    return 1
            "No, don't":
                    if Girl == RogueX:
                            ch_r "Fine then. . ."                   
                    elif Girl == KittyX:
                            ch_k "Ok then. . ." 
                    elif Girl == EmmaX:
                            ch_e "Fair enough. . ." 
                    elif Girl == LauraX:
                            ch_l "Ok. . ."  
                
        return 0
# End Dressing Screen / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    

# End Clothes Stuff / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 