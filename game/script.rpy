#This is the core game code


image title card = "images/titleimage.jpg"
image NightMask = "images/nightmask.png"

image Crossroads_E = "images/Crossroads_Evening.jpg"
image Crossroads_N = "images/Crossroads_Night.jpg"  
image Crossroads_D = "images/Crossroads_Day.jpg"

image UI_Backpack = "images/UI_Backpack_idle.png"
image UI_Dildo = "images/UI_Dildo.png"
image UI_VibA = "images/UI_VibA.png"
image UI_VibB = "images/UI_VibB.png"
image UI_Tongue = "images/UI_Tongue.png"
image UI_Finger = "images/UI_Finger.png"
image UI_Hand = "images/UI_Hand.png"
image UI_GirlFinger = "images/UI_GirlFinger.png" 
image UI_GirlHand = "images/UI_GirlHand.png" 
#image UI_GirlFinger:
#    "images/UI_GirlFinger.png" 
#    zoom .8
#image UI_GirlHand:
#    "images/UI_GirlHand.png" 
#    zoom .8


image blackscreen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

define ch_r = Character('Rogue', color="#85bb65", image = "arrow", show_two_window=True)
define ch_p = Character('[Playername]', color="#87CEEB", show_two_window=True)
define ch_x = Character('Professor X', color="#a09400", image = "arrow", show_two_window=True)
define ch_k = Character('Kitty', color="#F5A9D0", image = "arrow", show_two_window=True)
define ch_e = Character('[EmmaName]', color="#98bee7", image = "arrow", show_two_window=True)
define ch_b = Character('Dr. McCoy', color="#1033b2", image = "arrow", show_two_window=True)
define ch_l = Character('[LauraName]', color="#d8b600", image = "arrow", show_two_window=True)
define ch_u = Character('???', color="#85bb65", image = "arrow", show_two_window=True)
define ch_n = Character('Neutral', color="#85bb65", image = "arrow", show_two_window=True) #non-character, uses Ch_Focus
define ch_g = Character('[GwenName]', color="#F08080", image = "arrowG", show_two_window=True,background=Frame("images/WordballoonG.png",50,50))
define ch_usher = Character('Usher', color="#DF0174", show_two_window=True)
define ch_danger = Character('Danger Room:', color="#1033b2",what_color="#1033b2",what_font="dungeon.ttf",show_two_window=False)
#define e = Character("Eileen", what_color="#c8ffc8") #this sets the chat text color, handy

label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show image "images/Onirating.jpg"
        show text "This title is for ages 18 and up." with dissolve
        with Pause(2)
        
        show text "This is a very rough beta version of the game. It has limited function and has not been thoroughly tested. Please report any bugs you find." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return
    

init -1:  

#World Stats
    default SaveVersion = 984
    default Day = 1
    default Cheat = 0
    default Time_Options = ["Morning", "Midday", "Evening", "Night"]
    default Time_Count = 2
    default Current_Time = Time_Options[(Time_Count)]     
    default Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default Weekday = 6
    default DayofWeek = Week[Weekday]
    default bg_current = "bg study"
    default Party = []
    default Taboo = 0
    default Rules = []
    default Line = 0
    default Situation = 0               #Whether Auto/Shift
    default MultiAction = 1             #0 if the action cannot continue, 1 if it can
    default Trigger = 0                 #Mainhand
    default Trigger2 = 0                #Offhand
    default Trigger3 = 0                #Girl's offhand    
    default Trigger4 = 0                #this is the 4th sexual act performed by the second girl 
    default Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating
    default ThreeCount = 100              #This is a timer for changing sexual positions on auto
    default Adjacent = []               #this is the girl you're sitting next to in class
    default Nearby = []                 #this tracks girls in the same room, but distant from you
    default Present = []                #This list tracks which girls are in this scene
#    default LesFlag = 0                #This is triggered if a lesbian action is occurring
    default Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
    default Events = []  
    default Tempmod = 0
    default Approval = 0                #for approval checks
    default Count = 0                   #For within an event
    default Count2 = 0                  #For between several events
    default Round = 100                 #Tracks time within a turn
    default Stealth = 0                 #How careful you're being
    default Cnt = 0                     #a mini Count variable for discrete operations
    default Speed = 0
    default CountStore = 0              #Stores values for after an event ends
    default Achievements = []
    default Options = []
    default Vibration = 0
    default UI_Tool = 0
    default UI_Girl = "Rogue"           #girl used in UI elements
    default Ch_Focus = "Rogue"
    default TravelMode = 0              #used for wandering around, if 0, you use the worldmap
    default StageFarRight = 900         #these are values for location points on the screen
    default StageRight = 715        
    default StageCenter = 550
    default StageLeft = 350
    default StageFarLeft = 150
#Player Stats
    default Playername = "Zero"
    default P_Male = 1
    default R_Petname = "sugar"       #What Rogue calls the player
    default R_Petnames = ["sugar"]
    default R_Pet = "Rogue"           #What you call Rogue
    default R_Pets = ["Rogue"]
    default K_Petname = "sweetie"       #What Kitty calls the player
    default K_Petnames = ["sweetie"]
    default K_Pet = "Kitty"           #What you call Kitty
    default K_Pets = ["Kitty"]
    default E_Petname = "young man"       #What Emma calls the player
    default E_Petnames = ["young man"]
    default E_Pet = "Ms. Frost"           #What you call Emma
    default E_Pets = ["Ms. Frost"]
    default L_Petname = "guy"       #What Laura calls the player
    default L_Petnames = ["guy"]
    default L_Pet = "Laura"           #What you call Laura
    default L_Pets = ["Laura","X-23"]
    default P_Semen = 2
    default P_Semen_Max = 3
    default P_Focus = 0
    default P_FocusX = 0
    default P_XP = 0
    default P_StatPoints = 0    
    default P_XPgoal = 100
    default P_Lvl = 1
    default P_Traits = []
    default P_Rep = 600
    default P_RecentActions = []
    default P_DailyActions = []
    default P_Harem = [] #this is a list fo all girls the player is currently dating
# Player Inventory Variables 
    default P_Income = 12               #how much you make each day
    default P_Cash = 20
    default P_Inventory = []
    default Inventory_Count = 0
    default Digits = []
    default Keys = [] 
    default PunishmentX = 0
    default GwenName = "????"
# Player Sprite
    default P_Sprite = 0
    default P_Color = "green"
    default P_Cock = "out"
    default P_Spunk = 0
    default P_Wet = 0
#Rogue Stats   
    default R_Loc = "bg rogue"
    default R_Love = 500
    default R_Inbt = 0
    default R_Obed = 0
    default R_Lust = 10
    default R_Thirst = 0                 #set Thirst to go up when they see you do things
    default R_LikeKitty = 600
    default R_LikeEmma = 500
    default R_LikeLaura = 500
    default R_Addict = 0                #how addicted she is
    default R_Addictionrate = 0         #How faster her addiciton rises
    default R_AddictStore = 0           #stores her base addiction level
    default R_Resistance = 0            #how fast her rate falls
    default R_OCount = 0                #Orgasm counter
    default R_Loose = 0
    default R_Inventory = []
    default R_XP = 0
    default R_ShameLevel = 0
    default R_Cheated = 0               #number of times you've cheated on her    
    default R_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default R_StatPoints = 0    
    default R_XPgoal = 100
    default R_Lvl = 0
    default R_Traits = []
    default R_Rep = 800
    default R_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
    # nude(0), green(1), pink(2), Custom1(3), Sleepwear(4), Custom2(5), Custom3(6), Gymclothes(7), Temporary(8), Personal(9)
    default R_Shame = 0                 #The amount of shame Rogue generates with her current clothing/action
    default R_Taboo = 0                 #The taboo level of the location Rogue is at when not with you
    default R_Chat = [0,0,0,0,0,0]
    default R_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default R_Todo = []
    default R_PubeC = 0
  # Sexual Encounters
    default R_History = []
    default R_RecentActions = []
    default R_DailyActions = []
    default R_Action = 3
    default R_MaxAction = 3
    default R_Caught = 0
    default R_Kissed = 0              #How many times they've kissed
    default R_Hand = 0
    default R_Foot = 0
    default R_Slap = 0
    default R_Strip = 0
    default R_Tit = 0
    default R_Sex = 0
    default R_Anal = 0
    default R_Hotdog = 0
    default R_Mast = 0
    default R_Org = 0
    default R_FondleB = 0
    default R_FondleT = 0
    default R_FondleP = 0
    default R_FondleA = 0
    default R_DildoP = 0
    default R_DildoA = 0
    default R_Vib = 0
    default R_Plug = 0
    default R_SuckB = 0
    default R_InsertP = 0
    default R_InsertA = 0
    default R_LickP = 0    
    default R_LickA = 0
    default R_Blow = 0
    default R_Swallow = 0
    default R_CreamP = 0
    default R_CreamA = 0
    default R_Les = 0                           #how many times she's done lesbian stuff
    default R_LesWatch = 0
    default R_SexKitty = 0                      #how many times she's had sex involving Kitty
    default R_SEXP = 0
    default R_PlayerFav = 0                     #The player's favorite activity with her
    default R_Favorite = 0                      #her favorite activity
    default R_SeenChest = 0
    default R_SeenPanties = 0
    default R_SeenPussy = 0
    default R_SeenPeen = 0                      #How many times she's seen your cock
    default R_Sleep = 0 
    default R_Personality = "normal"
    default R_Date = 0 
    default R_Forced = 0                        #This is a toggle for if she's being coerced
    default R_ForcedCount = 0                   #This is a counter for each time she's been coerced lately
#Rogue Sprite Variables
    default R_Outfit = "evo_green"
    default R_OutfitDay = "evo_green"
    default Rogue_Arms = 1
    default R_Emote = "normal"
#    default R_EmoteDefault = "normal"
    default R_Arms = "gloved"
    default R_Legs = "skirt"
    default R_Over = "mesh top"
    default R_Under = 0
    default R_Chest = "tank"
    default R_Pierce = 0
    default R_Panties = "black panties"
    default R_Neck = "spiked collar"
    default R_Hose = "stockings"
    default R_Mouth = "normal"
    default R_Brows = "normal"
    default R_Eyes = "normal"
    default R_Hair = "evo"
    default R_Gag = 0    
    default R_Blush = 0
    default R_Spunk = []
    default R_Sperm = []
    default R_Pubes = 1
    default R_Wet = 0
    default R_Water = 0
    default R_Upskirt = 0
    default R_PantiesDown = 0
    default R_Uptop = 0
    default R_Held = 0
    # toggle(0),arms/gloves(1),pants(2),jacket(3),necklace(4),bra(5),panties(6),boots(7),hair(8),hose(9)
    default R_Custom = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
    default R_Custom3 = [0,0,0,0,0,0,0,0,0,0,0] 
    default R_TempClothes = [0,0,0,0,0,0,0,0,0,0,0]  
    default R_Gym = [2,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
    default R_Sleepwear = [0,0,0,0,0,"tank","green panties",0,0,0]
    default R_Swim = [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0] 
    # (0-6) = Mon-Sun, (7) Datewear, (8) null, (9) Private
    default R_Schedule = [0,0,0,0,0,0,0,0,0,0]                  
    default R_SpriteVer = 0
    default RogueLayer = 50
    default R_SpriteLoc = StageRight                        #Sets Rogue to default to the right side  
#Kitty Stats   
    default K_Loc = 0
    default K_Love = 400
    default K_Obed = 100
    default K_Inbt = 0
    default K_Lust = 10
    default K_Thirst = 0 
    default K_LikeRogue = 700
    default K_LikeEmma = 400
    default K_LikeLaura = 500
    default K_Addict = 0 #how addicted she is
    default K_Addictionrate = 0 #How faster her addiciton rises
    default K_Resistance = 0 #how fast her rate falls
    default K_Inventory = []    
    default K_OCount = 0                #Orgasm counter
    default K_Loose = 0
    default K_XP = 0
    default K_Cheated = 0               #number of times you've cheated on her    
    default K_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default K_StatPoints = 0    
    default K_XPgoal = 100
    default K_Lvl = 0
    default K_Traits = []
    default K_Rep = 800
    default K_OutfitShame = [50,0,0,0,20,0,0,10,0,0,0,0,0,0,0]
    # nude(0), Pink(1), Red(2), Custom1(3), Sleepwear(4), Custom2(5), Custom3(6), Gymclothes(7), Temporary(8)
    default K_Shame = 0                 #The amount of shame Kitty generates with her current clothing/action
    default K_Taboo = 0                 #The taboo level of the location Kitty is at when not with you
    default K_Chat = [0,0,0,0,0,0]
    default K_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default K_Todo = []
    default K_PubeC = 0    
    default K_Like = "Like, "
    default K_like = ", like, "
#Kitty Sprite Variables
    default K_Outfit = "pink outfit"
    default K_OutfitDay = "pink outfit"
    default Kitty_Arms = 1
    default K_Emote = "normal"
    default K_EmoteDefault = "normal"
    default K_Arms = 0
    default K_Legs = "capris"
    default K_Over = "pink top"
    default K_Under = "pink top"
    default K_Chest = "cami"    
    default K_Pierce = 0
    default K_Panties = "green panties"
    default K_Neck = "gold necklace"
    default K_Hose = 0
    default K_Mouth = "normal"
    default K_Brows = "normal"
    default K_Eyes = "normal"
    default K_Hair = "evo"
    default K_Gag = 0    
    default K_Blush = 0
    default K_Spunk = []
    default K_Pubes = 1
    default K_Wet = 0
    default K_Water = 0
    default K_Upskirt = 0
    default K_PantiesDown = 0
    default K_Uptop = 0
    # toggle(0),arms/gloves(1),pants(2),jacket(3),necklace(4),bra(5),panties(6),boots(7),hair(8),hose(9)
    default K_Custom = [0,0,0,0,0,0,0,0,0,0]
    default K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
    default K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]   
    default K_TempClothes = [0,0,0,0,0,0,0,0,0,0,0]    
    default K_Gym = [2,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
    default K_Sleepwear = [0,0,"shorts",0,0,"cami","green panties",0,0,0]
    default K_Swim = [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0] 
    # (0-6) = Mon-Sun, (7) Datewear, (8) null, (9) Private
    default K_Schedule = [0,0,0,0,0,0,0,0,0,0]                      #chooses when she wears what
    default KittyLayer = 100
    default K_SpriteLoc = StageCenter                        #Sets Kitty to default to the center
  # Sexual Encounters
    default K_History = []
    default K_RecentActions = []
    default K_DailyActions = []
    default K_Action = 3
    default K_MaxAction = 3
    default K_Caught = 0
    default K_Kissed = 0              #How many times they've kissed
    default K_Hand = 0
    default K_Foot = 0
    default K_Slap = 0
    default K_Strip = 0
    default K_Tit = 0
    default K_Sex = 0
    default K_Anal = 0
    default K_Hotdog = 0
    default K_Mast = 0
    default K_Org = 0
    default K_FondleB = 0
    default K_FondleT = 0
    default K_FondleP = 0
    default K_FondleA = 0
    default K_DildoP = 0
    default K_DildoA = 0
    default K_Vib = 0
    default K_Plug = 0
    default K_SuckB = 0
    default K_InsertP = 0
    default K_InsertA = 0
    default K_LickP = 0    
    default K_LickA = 0
    default K_Blow = 0
    default K_Swallow = 0
    default K_CreamP = 0
    default K_CreamA = 0
    default K_Les = 0  
    default K_LesWatch = 0  
    default K_SexRogue = 0
    default K_SEXP = 0
    default K_ShameLevel = 0
    default K_PlayerFav = 0                     #The player's favorite activity with her
    default K_Favorite = 0                      #her favorite activity
    default K_SeenChest = 0
    default K_SeenPanties = 0
    default K_SeenPussy = 0   
    default K_SeenPeen = 0
    default K_Sleep = 0
    default K_Personality = "normal"
    default K_Date = 0 
    default K_Forced = 0                                        #This is a toggle for if she's being coerced
    default K_ForcedCount = 0                                   #This is a counter for each time she's been coerced lately
#Emma Stats   
    default EmmaName = "Ms Frost"
    default E_Loc = 0
    default E_Love = 300
    default E_Obed = 0
    default E_Inbt = 200
    default E_Lust = 10
    default E_Thirst = 0 
    default E_LikeRogue = 500
    default E_LikeKitty = 500
    default E_LikeLaura = 500
    default E_Addict = 0 #how addicted she is
    default E_Addictionrate = 0 #How faster her addiciton rises
    default E_Resistance = 0 #how fast her rate falls
    default E_Inventory = []    
    default E_OCount = 0                #Orgasm counter
    default E_Loose = 2
    default E_XP = 0
    default E_Cheated = 0               #number of times you've cheated on her    
    default E_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default E_StatPoints = 0    
    default E_XPgoal = 100
    default E_Lvl = 0
    default E_Traits = []
    default E_Rep = 800
    default E_OutfitShame = [50,0,5,0,25,0,0,10,0,0,0,0,0,0,0]
    # nude(0), teacher(1), uniform(2), Custom1(3), Sleepwear(4), Custom2(5), Custom3(6), Gymclothes(7), Temporary(8)
    default E_Shame = 0                 #The amount of shame she generates with her current clothing/action
    default E_Taboo = 0                 #The taboo level of the location she is at when not with you
    default E_Chat = [0,0,0,0,0,0]
    default E_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default E_Todo = []
    default E_PubeC = 0    
#Emma Sprite Variables
    default E_Outfit = "teacher"
    default E_OutfitDay = "teacher"
    default E_Emote = "normal"
    default E_EmoteDefault = "normal"
    default Emma_Arms = 1               #her arm position
    default E_Arms = 0                  #her gloves
    default E_Legs = "pants"
    default E_Over = "jacket"
    default E_Chest = "corset"    
    default E_Pierce = 0
    default E_Panties = "white panties"
    default E_Boots = 0
    default E_Neck = "choker"
    default E_Hose = 0
    default E_Mouth = "normal"
    default E_Brows = "normal"
    default E_Eyes = "normal"
    default E_Hair = "wavy"
    default E_Gag = 0    
    default E_Blush = 0
    default E_Spunk = []
    default E_Pubes = 0
    default E_Wet = 0
    default E_Water = 0
    default E_TitsUp = 1
    default E_Upskirt = 0
    default E_PantiesDown = 0
    default E_Uptop = 0
    # toggle(0),arms/gloves(1),pants(2),jacket(3),necklace(4),bra(5),panties(6),boots(7),hair(8),hose(9)
    default E_Custom = [0,0,0,0,0,0,0,0,0,0]
    default E_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
    default E_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]   
    default E_TempClothes = [0,0,0,0,0,0,0,0,0,0,0]   
    default E_Gym = [2,0,0,0,0,"sports bra","sports panties",0,0,0,0]
    default E_Sleepwear = [0,0,0,0,0,"corset","white panties",0,0,0]
    default E_Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
    # (0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private
    default E_Schedule = [0,0,0,0,0,0,0,"teacher","teacher",0]                      #chooses when she wears what [0,0,0,0,0,0,0,0,0,0]
    default EmmaLayer = 101
    default E_SpriteLoc = StageCenter                        #Sets Emma to default to the center
  # Sexual Encounters
    default E_History = []
    default E_RecentActions = []
    default E_DailyActions = []
    default E_Action = 3
    default E_MaxAction = 4
    default E_Caught = 0
    default E_Kissed = 0              #How many times they've kissed
    default E_Hand = 0
    default E_Foot = 0
    default E_Slap = 0
    default E_Strip = 0
    default E_Tit = 0
    default E_Sex = 0
    default E_Anal = 0
    default E_Hotdog = 0
    default E_Mast = 0
    default E_Org = 0
    default E_FondleB = 0
    default E_FondleT = 0
    default E_FondleP = 0
    default E_FondleA = 0
    default E_DildoP = 0
    default E_DildoA = 0
    default E_Vib = 0
    default E_Plug = 0
    default E_SuckB = 0
    default E_InsertP = 0
    default E_InsertA = 0
    default E_LickP = 0    
    default E_LickA = 0
    default E_Blow = 0
    default E_Swallow = 0
    default E_CreamP = 0
    default E_CreamA = 0
    default E_Les = 0    
    default E_LesWatch = 0
    default E_SexRogue = 0
    default E_SexKitty = 0
    default E_SEXP = 0
    default E_ShameLevel = 0
    default E_PlayerFav = 0                     #The player's favorite activity with her
    default E_Favorite = 0                      #her favorite activity
    default E_SeenChest = 0
    default E_SeenPanties = 0
    default E_SeenPussy = 0   
    default E_SeenPeen = 0
    default E_Sleep = 0
    default E_Personality = "normal"
    default E_Date = 0 
    default E_Forced = 0                                        #This is a toggle for if she's being coerced
    default E_ForcedCount = 0                                   #This is a counter for each time she's been coerced lately    
#Laura Stats   
    default LauraName = "X-23"
    default L_Loc = 0
    default L_Love = 400
    default L_Obed = 0
    default L_Inbt = 200
    default L_Lust = 20
    default L_Thirst = 0 
    default L_LikeRogue = 500
    default L_LikeKitty = 500
    default L_LikeEmma = 500
    default L_Addict = 0 #how addicted she is
    default L_Addictionrate = 0 #How faster her addiciton rises
    default L_Resistance = 0 #how fast her rate falls
    default L_Inventory = []    
    default L_OCount = 0                #Orgasm counter
    default L_Loose = 2
    default L_XP = 0
    default L_Cheated = 0               #number of times you've cheated on her    
    default L_Break = [0,0]                 #minimum time between break-ups/number of total break-ups
    default L_StatPoints = 0    
    default L_XPgoal = 100
    default L_Lvl = 0
    default L_Traits = []
    default L_Rep = 800
    default L_OutfitShame = [50,0,5,0,25,0,0,10,0,0,0,0,0,0,0]
    # nude(0), teacher(1), uniform(2), Custom1(3), Sleepwear(4), Custom2(5), Custom3(6), Gymclothes(7), Temporary(8)
    default L_Shame = 0                 #The amount of shame she generates with her current clothing/action
    default L_Taboo = 0                 #The taboo level of the location she is at when not with you
    default L_Chat = [0,0,0,0,0,0]
    default L_Event = [0,0,0,0,0,0,0,0,0,0,0]  
    default L_Todo = []
    default L_PubeC = 0    
#Laura Sprite Variables
    default L_Outfit = "leathers"
    default L_OutfitDay = "leathers"
    default L_Emote = "normal"
    default L_EmoteDefault = "normal"
    default Laura_Arms = 1               #her arm position
    default L_Claws = 0                  #her claws
    default L_Arms = "wrists"                  #her gloves
    default L_Legs = "leather pants"
    default L_Over = 0
    default L_Chest = "leather bra"    
    default L_Pierce = 0
    default L_Panties = "black panties"
    default L_Boots = 0
    default L_Neck = "leash choker"
    default L_Hose = 0
    default L_Mouth = "normal"
    default L_Brows = "normal"
    default L_Eyes = "normal"
    default L_Hair = "long"
    default L_Gag = 0    
    default L_Blush = 0
    default L_Spunk = []
    default L_Pubes = 1
    default L_Wet = 0
    default L_Water = 0
    default L_TitsUp = 1
    default L_Upskirt = 0
    default L_PantiesDown = 0
    default L_Uptop = 0
    # toggle(0),arms/gloves(1),pants(2),jacket(3),necklace(4),bra(5),panties(6),boots(7),hair(8),hose(9)
    default L_Custom = [0,0,0,0,0,0,0,0,0,0]
    default L_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
    default L_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]   
    default L_TempClothes = [0,0,0,0,0,0,0,0,0,0,0]   
    default L_Gym = [2,0,"leather pants",0,0,"leather bra","black panties",0,0,0,0]
    default L_Sleepwear = [0,0,0,0,0,"leather bra","black panties",0,0,0]
    default L_Swim = [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0] 
    # (0-6) = Mon-Sun, (7) Datewear, (8) Teachingwear, (9) Private
    default L_Schedule = [0,0,0,0,0,0,0,0,0,0]                      #chooses when she wears what
    default LauraLayer = 101
    default L_SpriteLoc = StageCenter                        #Sets Laura to default to the center
  # Sexual Encounters
    default L_History = []
    default L_RecentActions = []
    default L_DailyActions = []
    default L_Action = 3
    default L_MaxAction = 4
    default L_Caught = 0
    default L_Kissed = 0              #How many times they've kissed
    default L_Hand = 0
    default L_Foot = 0
    default L_Slap = 0
    default L_Strip = 0
    default L_Tit = 0
    default L_Sex = 0
    default L_Anal = 0
    default L_Hotdog = 0
    default L_Mast = 0
    default L_Org = 0
    default L_FondleB = 0
    default L_FondleT = 0
    default L_FondleP = 0
    default L_FondleA = 0
    default L_DildoP = 0
    default L_DildoA = 0
    default L_Vib = 0
    default L_Plug = 0
    default L_SuckB = 0
    default L_InsertP = 0
    default L_InsertA = 0
    default L_LickP = 0    
    default L_LickA = 0
    default L_Blow = 0
    default L_Swallow = 0
    default L_CreamP = 0
    default L_CreamA = 0
    default L_Les = 0    
    default L_LesWatch = 0
    default L_SexRogue = 0
    default L_SexKitty = 0
    default L_SexEmma = 0
    default L_SEXP = 0
    default L_ShameLevel = 0
    default L_PlayerFav = 0                     #The player's favorite activity with her
    default L_Favorite = 0                      #her favorite activity
    default L_SeenChest = 0
    default L_SeenPanties = 0
    default L_SeenPussy = 0   
    default L_SeenPeen = 0
    default L_Sleep = 0
    default L_Personality = "normal"
    default L_Date = 0 
    default L_Forced = 0                                        #This is a toggle for if she's being coerced
    default L_ForcedCount = 0                                   #This is a counter for each time she's been coerced lately    
#Xavier Sprite Variables    
    default X_Brows = "happy"
    default X_Mouth = "happy"
    default X_Eyes = "happy"
    default X_Psychic = 0
    default X_Emote = "happy"
    default XSpriteLoc = StageCenter




label start:       
# Official game start  ////////////////////////////////////////////////////////////////////

    
    show screen R_Status_screen    
    show screen Inventorybutton            
        
    if config.developer:
#        show screen roguebutton
#        show screen statbutton
            # Testing settings
            $ P_Cash = 200
            $ Cheat = 1
            $ R_Kissed = 5
            $ Digits.append("Rogue") 
            $ Keys.append("Rogue") 
            $ K_Kissed = 5      
            $ Digits.append("Kitty")
            $ Keys.append("Kitty")
            $ K_History.append("met")
            $ E_Kissed = 5      
            $ E_Petname = "Mr. Zero"
            $ Digits.append("Emma")
            $ Keys.append("Emma")
            $ E_History.append("met")
            $ E_History.append("classcaught")         
            $ Digits.append("Laura")
            $ Keys.append("Laura")
            $ L_History.append("met")
            $ P_Traits.append("focus")
            $ R_Event[1] = 1 
            $ R_Addictionrate = 10
            #$ R_Resistance = 1 #how fast her rate falls
            $ Day = 16
            $ Time_Options = ["Morning", "Midday", "Evening", "Night"]
            $ Time_Count = 4
            $ Current_Time = "Midday"   
            $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            $ Weekday = 6
            $ DayofWeek = Week[Weekday]
            call Wait
            jump Rogue_Room_Test             
        
    jump Prologue


# After loading, this runs ////////////////////////////////////////////////////////////////
label after_load: 
label VersionNumber: 
    $ SaveVersion = 0 if "SaveVersion" not in globals().keys() else SaveVersion    
    if SaveVersion == 975: #error correction, remove this eventually
        $ SaveVersion = 957  
        
    if SaveVersion < 983:
        if SaveVersion < 976:
                if SaveVersion < 94:
                    $ R_Love = R_Love * 10
                    $ R_Inbt = R_Inbt * 10
                    $ R_Obed = R_Obed * 10
                    $ SaveVersion = 940
                    $ R_Under = 0        
                    $ R_OutfitShame[0] = 50
                if SaveVersion < 95:
                    $ R_Event[3] = 0
                    if "hungry" in R_Traits:
                        while "hungry" in R_Traits:
                            $ R_Traits.remove("hungry")  
                        $ R_Traits.append("hungry")
                    $ SaveVersion = 950
                if SaveVersion < 955:
                    if R_Schedule[7] == 4:
                        $ R_Schedule[7] = 0
                    $ R_Schedule[8] = 4     #changes which slot is in gym clothes
                    $ SaveVersion = 955    
                if SaveVersion < 957:
                    $ R_OutfitShame[4] = 20
                    $ SaveVersion = 957    
                if SaveVersion < 960:
                    $ R_Schedule[0] = R_Schedule[1]
                    $ R_Schedule[1] = R_Schedule[2]
                    $ R_Schedule[2] = R_Schedule[3]
                    $ R_Schedule[3] = R_Schedule[4]
                    $ R_Schedule[4] = R_Schedule[5]
                    $ R_Schedule[5] = R_Schedule[6]
                    $ R_Schedule[6] = R_Schedule[7]
                    $ R_Schedule[7] = 0   
                    $ R_Hose = "stockings" if R_Hose == 1 else 0            
                    $ R_Custom[9] = "stockings" if R_Custom[9] == 1 else 0
                    $ R_Sleepwear[6] = "stockings" if R_Sleepwear[6] == 1 else 0    
                    $ TravelMode = 0 if "TravelMode" not in globals().keys() else TravelMode         
                    $ P_RecentActions = [] if "P_RecentActions" not in globals().keys() else P_RecentActions
                    $ P_DailyActions = [] if "P_DailyActions" not in globals().keys() else P_DailyActions         
                    $ R_RecentActions = [] if "R_RecentActions" not in globals().keys() else R_RecentActions
                    $ R_DailyActions = [] if "R_DailyActions" not in globals().keys() else R_DailyActions
                    $ SaveVersion = 960      
                if SaveVersion < 966:
                    $ K_History = []
                    $ K_Arms = Kitty_Arms
                    $ StageFarLeft = 150
                    $ SaveVersion = 966  
                    while len(R_OutfitShame) < 15:
                        $ R_OutfitShame.append(0)  
                if SaveVersion < 970:        
                    hide screen roguebutton
                    hide screen statbutton  
                    $ R_Sperm = []  
                    while len(Event) < 4:
                        $ Event.append(0)
                    while len(R_Chat) < 6:
                        $ R_Chat.append(0)
                    while len(R_Event) < 11:
                        $ R_Event.append(0)
                    while len(R_Custom) < 11:
                        $ R_Custom.append(0)
                    while len(R_Custom2) < 11:
                        $ R_Custom2.append(0)
                    while len(R_Custom3) < 11:
                        $ R_Custom3.append(0)
                    while len(R_Gym) < 11:
                        $ R_Gym.append(0)
                    while len(R_Sleepwear) < 7:
                        $ R_Sleepwear.append(0)
                    while len(R_Schedule) < 10:
                        $ R_Schedule.append(0)
                    while len(K_Custom) < 10:
                        $ K_Custom.append(0)  
                    $ K_Spunk = []            
                    $ K_Custom = [0,0,0,0,0,0,0,0,0,0]
                    $ K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]        
                    $ K_Gym = [0,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ K_Sleepwear = [0,0,0,0,"tank","green panties",0]
                    $ K_Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
                    $ K_Chat = [0,0,0,0,0,0]
                    $ K_Event = [0,0,0,0,0,0,0,0,0,0,0]  
                    $ K_Todo = []
                    $ SaveVersion = 970  
                if SaveVersion < 971:      
                    $ K_Gym = [1,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
                    $ K_Sleepwear = [0,"shorts",0,0,"cami","green panties",0]
                
                    $ R_Gym = [0,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ R_Sleepwear = [0,0,0,0,"tank","green panties",0] 
                    $ R_LikeKitty = 600
                    $ K_Traits = []
                    $ K_Petname = Playername[:1]    
                    $ K_Petnames = ["sweetie"]
                    $ K_Pet = "Kitty"       
                    $ K_Pets = ["Kitty"]
                    $ K_Loose = 0
                    $ K_PantiesDown = 0
                    $ K_Water = 0
                    $ K_Pierce = 0
                    $ K_ForcedCount = 0
                    $ R_ForcedCount = 0
                    $ SaveVersion = 971         
                if SaveVersion < 972:            
                    $ RogueLayer = 50
                    $ KittyLayer = 100
                                
                    if Current_Time == 'Night':
                        show NightMask onlayer nightmask      
                    if K_Over == "pink top":
                        $ K_Neck = "gold necklace"
                    else:
                        $ K_Neck = 0
                    $ R_Spunk = R_Sperm
                    if renpy.showing("setting", layer='master'):
                        scene setting onlayer backdrop
                        hide setting
                    if renpy.showing("bg_entry", layer='master'):
                        scene bg_entry onlayer backdrop
                        hide bg_entry
                    $ SaveVersion = 972 
                if SaveVersion < 973:
                    $ K_Pierce = 0 if "K_Pierce" not in globals().keys() else K_Pierce  
                    $ Trigger4 = 0                #this is the 4th sexual act performed by the second girl  
                    $ Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating 
                    $ Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
                    $ K_Sleepwear[3] = 0
                    
                    if R_Custom[1] == "collargloved":
                            $ R_Custom[1] = "gloved"
                            $ R_Custom[4] = "spiked collar"
                    elif R_Custom[1] == "collarbare":  
                            $ R_Custom[1] = 0
                            $ R_Custom[4] = "spiked collar"
                    elif R_Custom[1] == "gloved":
                            $ R_Custom[1] = "gloved"
                            $ R_Custom[4] = 0
                    else:
                            $ R_Custom[1] = 0
                            $ R_Custom[4] = 0
                            
                    if R_Custom2[1] == "collargloved":
                            $ R_Custom2[1] = "gloved"
                            $ R_Custom2[4] = "spiked collar"
                    elif R_Custom2[1] == "collarbare":  
                            $ R_Custom2[1] = 0
                            $ R_Custom2[4] = "spiked collar"
                    elif R_Custom2[1] == "gloved":
                            $ R_Custom2[1] = "gloved"
                            $ R_Custom2[4] = 0
                    else:
                            $ R_Custom2[1] = 0
                            $ R_Custom2[4] = 0
                    
                    if R_Custom3[1] == "collargloved":
                            $ R_Custom3[1] = "gloved"
                            $ R_Custom3[4] = "spiked collar"
                    elif R_Custom3[1] == "collarbare":  
                            $ R_Custom3[1] = 0
                            $ R_Custom3[4] = "spiked collar"
                    elif R_Custom3[1] == "gloved":
                            $ R_Custom3[1] = "gloved"
                            $ R_Custom3[4] = 0
                    else:
                            $ R_Custom3[1] = 0
                            $ R_Custom3[4] = 0
                            
                    if R_Gym[1] == "collargloved":
                            $ R_Gym[1] = "gloved"
                            $ R_Gym[4] = "spiked collar"
                    elif R_Gym[1] == "collarbare":  
                            $ R_Gym[1] = 0
                            $ R_Gym[4] = "spiked collar"
                    elif R_Gym[1] == "gloved":
                            $ R_Gym[1] = "gloved"
                            $ R_Gym[4] = 0
                    else:
                            $ R_Gym[1] = 0
                            $ R_Gym[4] = 0
                    
                    if R_Sleepwear[0] == "collargloved":
                            $ R_Sleepwear[0] = "gloved"
                            $ R_Sleepwear[3] = "spiked collar"
                    elif R_Sleepwear[0] == "collarbare":  
                            $ R_Sleepwear[0] = 0
                            $ R_Sleepwear[3] = "spiked collar"
                    elif R_Sleepwear[0] == "gloved":
                            $ R_Sleepwear[0] = "gloved"
                            $ R_Sleepwear[3] = 0
                    else:
                            $ R_Sleepwear[0] = 0
                            $ R_Sleepwear[3] = 0
                            
                    if R_Arms == "collargloved":
                            $ R_Arms = "gloved"
                            $ R_Neck = "spiked collar"
                    elif R_Arms == "collarbare":    
                            $ R_Arms = 0
                            $ R_Neck = "spiked collar"
                    elif R_Arms == "gloved":    
                            $ R_Arms = "gloved"
                            $ R_Neck = 0            
                    else:  
                            $ R_Arms = 0
                            $ R_Neck = 0
                    
                    $ P_Rep = 600
                    $ R_Rep = R_Rep * 10
                    $ K_Rep = K_Rep * 10
                    $ R_History = []            
                    $ R_PlayerFav = 0
                    $ R_Favorite = 0
                    $ K_PlayerFav = 0
                    $ K_Favorite = 0   
                    $ R_SeenPeen = 0   
                    $ K_SeenPeen = 0
                    $ R_Les = 0    
                    $ R_SexKitty = 0
                    $ K_Les = 0    
                    $ K_SexRogue = 0
                    $ R_SEXP += 5 if R_LickA else 0
                    $ Trigger = "fondle pussy" if Trigger == "insert pussy" else Trigger
                    $ Trigger2 = "fondle pussy" if Trigger2 == "insert pussy" else Trigger2
                    $ Trigger2 = "jackin" if Trigger2 == "masturbation" else Trigger2
                    $ R_SeenPeen = R_Sex + R_Anal + R_Hotdog + R_Blow + R_Hand + R_Tit    
                    $ K_SeenPeen = K_Sex + K_Anal + K_Hotdog + K_Blow + K_Hand + K_Tit                  
                    if "around" in R_Traits:
                        while "around" in R_Traits:
                            $ R_Traits.remove("around") 
                    if "around" in K_Traits:
                        while "around" in K_Traits:
                            $ K_Traits.remove("around") 
                    $ R_OutfitDay = R_Outfit
                    $ K_OutfitDay = K_Outfit
                    $ SaveVersion = 973 
                if SaveVersion < 974:
                    $ Adjacent = 0    
                    $ R_Resistance = 1 if R_Resistance >= 1 else 0
                    $ K_Resistance = 1 if K_Resistance >= 1 else 0
                    $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    if "All" in Keys and "Kitty" not in Keys:
                        $ Keys.append("Kitty")
                    $ Present = []
                    $ R_Date = 0 
                    $ K_Date = 0 
                    $ SaveVersion = 974 
        if SaveVersion < 976:
            if R_History == 0: 
                $ R_History = []
            if K_History == 0: 
                $ K_History = []
            if "saw with Kitty" in R_Traits:
                while "saw with Kitty" in R_Traits:
                        $ R_Traits.remove("saw with Kitty") 
            if "saw with Rogue" in K_Traits:
                while "saw with Rogue" in K_Traits:
                        $ K_Traits.remove("saw with Rogue") 
            $ R_Gag = 0   
            $ K_Gag = 0  
            $ SaveVersion = 976 
        if SaveVersion < 977:
            if K_Rep <= 400:
                $ P_Rep -= 100
            if R_Rep <= 400:
                $ P_Rep -= 100
            $ SaveVersion = 977 
        if SaveVersion < 978:            
            if "stockings and garterbelt" not in R_Inventory and ApprovalCheck("Rogue", 1500):
                    $ R_Inventory.append("stockings and garterbelt")
            $ E_Loose = 2
            $ SaveVersion = 978
        if SaveVersion < 979:      
            $ StageFarRight = 900            #these are values for location points on the screen
            $ StageRight = 715            #these are values for location points on the screen
            $ StageCenter = 550
            $ StageLeft = 350
            $ StageFarLeft = 150
            #make sure to set K_SpriteLoc etc. to new values, 
            # $ K_SpriteLoc = 200 if K_SpriteLoc = 550 else K_SpriteLoc
            if "exhibitionist" in E_Traits:
                    $ E_Traits.remove("exhibitionist")
            if len(R_Sleepwear) <= 9: #this should be the case on any busted-ass og versions
                    $ R_Sleepwear.append(0)
                    $ R_Sleepwear.append(0)
                    $ R_Sleepwear.append(0)
                    $ R_Sleepwear[9] = R_Sleepwear[6] #Hose 6>9
                    $ R_Sleepwear[8] = "evo"            #Hair
                    $ R_Sleepwear[6] = R_Sleepwear[5] #Panties 5>6
                    $ R_Sleepwear[5] = R_Sleepwear[4] #Chest 4>5
                    $ R_Sleepwear[4] = R_Sleepwear[3] #Neck 3>4 "choker"  
                    $ R_Sleepwear[3] = R_Sleepwear[2] #Over 2>3
                    $ R_Sleepwear[2] = R_Sleepwear[1] #Legs 1>2
                    $ R_Sleepwear[1] = R_Sleepwear[0] #Arms 0>1
                    $ R_Sleepwear[0] = 1                #new toggle
                    
                    $ K_Sleepwear.append(0)
                    $ K_Sleepwear.append(0)
                    $ K_Sleepwear.append(0)
                    $ K_Sleepwear[9] = K_Sleepwear[6] #Hose 6>9
                    $ K_Sleepwear[8] = "long"           #Hair
                    $ K_Sleepwear[6] = K_Sleepwear[5] #Panties 5>6
                    $ K_Sleepwear[5] = K_Sleepwear[4] #Chest 4>5
                    $ K_Sleepwear[4] = K_Sleepwear[3] #Neck 3>4 "choker"  
                    $ K_Sleepwear[3] = K_Sleepwear[2] #Over 2>3
                    $ K_Sleepwear[2] = K_Sleepwear[1] #Legs 1>2
                    $ K_Sleepwear[1] = K_Sleepwear[0] #Arms 0>1
                    $ K_Sleepwear[0] = 1                #new toggle
                    
                    $ E_Sleepwear.append(0)
                    $ E_Sleepwear.append(0)
                    $ E_Sleepwear.append(0)
                    $ E_Sleepwear[9] = E_Sleepwear[6] #Hose 6>9
                    $ E_Sleepwear[8] = E_Hair          #Hair
                    $ E_Sleepwear[6] = E_Sleepwear[5] #Panties 5>6
                    $ E_Sleepwear[5] = E_Sleepwear[4] #Chest 4>5
                    $ E_Sleepwear[4] = E_Sleepwear[3] #Neck 3>4 "choker"  
                    $ E_Sleepwear[3] = E_Sleepwear[2] #Over 2>3
                    $ E_Sleepwear[2] = E_Sleepwear[1] #Legs 1>2
                    $ E_Sleepwear[1] = E_Sleepwear[0] #Arms 0>1
                    $ E_Sleepwear[0] = 1                #new toggle
            #end of sleepwear overhaul
            
                
            if Trigger == "kissing": #add to update
                    if Trigger5 == "kiss girl":
                        $ Trigger = "kiss girl"
                    elif Trigger5 == "kiss both":
                        $ Trigger = "kiss both"
                    else:
                        $ Trigger = "kiss you"
            if Trigger2 == "kissing":
                        $ Trigger2 = "kiss you"        
            if Trigger3 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger3 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger3 = "kiss girl"
                    else:
                        $ Trigger3 = "kiss you"
            if Trigger4 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger4 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger4 = "kiss girl"
                    else:
                        $ Trigger4 = "kiss you"
            if Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                    $ Trigger5 = 0 #Clear out Trigger 5 if it's for kissing.  
            $ E_Caught = 0
            if Rules == 1:
                $ Rules = []
            elif Rules == 0:
                $ Rules = ["rules"]
            if "exhibitionist" in E_Traits:  
                    $ E_Traits.remove("exhibitionist")
            $ E_Gym = [2,0,0,0,0,"sports bra","sports panties",0,0,0,0]                        
            $ SaveVersion = 979   
            
        if SaveVersion < 980:                     
            $ SaveVersion = 980   
            if "met" not in K_History:
                $ K_Loc = 0
            if "met" not in E_History:
                $ E_Loc = 0
            if "vocal" not in R_Traits:
                    $ R_Traits.append("vocal")
            if "vocal" not in K_Traits:
                    $ K_Traits.append("vocal")
            if "vocal" not in E_Traits:
                    $ E_Traits.append("vocal")
            if bg_current in ("date","bg restaurant","bg movies"):
                    #this should reset dates. 
                    show blackscreen onlayer black 
                    $ bg_current = "bg player"
                    call Wait
                    call Wait
                    call Set_The_Scene(Dress=0)
                    "You wake up in your room, you had a weird dream, apparently."
                    jump Player_Room   
        if SaveVersion < 981:                     
            $ SaveVersion = 981   
            if Trigger == "kissing": #add to update
                    if Trigger5 == "kiss girl":
                        $ Trigger = "kiss girl"
                    elif Trigger5 == "kiss both":
                        $ Trigger = "kiss both"
                    else:
                        $ Trigger = "kiss you"
            if Trigger2 == "kissing":
                        $ Trigger2 = "kiss you"        
            if Trigger3 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger3 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger3 = "kiss girl"
                    else:
                        $ Trigger3 = "kiss you"
            if Trigger4 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger4 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger4 = "kiss girl"
                    else:
                        $ Trigger4 = "kiss you"
            if Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                    $ Trigger5 = 0 #Clear out Trigger 5 if it's for kissing.  
            if "nighty" in P_Inventory: 
                $ P_Inventory.remove("nighty")
                $ P_Cash += 75
            if "lace bra" in P_Inventory: 
                $ P_Inventory.remove("lace bra")
                $ P_Cash += 90  
            if "lace panties" in P_Inventory: 
                $ P_Inventory.remove("lace panties")
                $ P_Cash += 110   
            if E_Schedule[8] == 4:
                $ E_Schedule[8] = 0
            if "locked" in E_RecentActions:
                $ P_RecentActions.append("lockedclass")
                $ E_RecentActions.remove("locked")
            if ("movie" in P_DailyActions or "dinner" in P_DailyActions) and not Party:
                    #this should reset dates. 
                    $ Primary = 0 if "Primary" not in locals().keys() else Primary 
                    $ Secondary = 0 if "Secondary" not in locals().keys() else Secondary
                    $ Party = [Primary,Secondary]

            if Adjacent:
                $ X_Psychic = Adjacent
                $ Adjacent = [X_Psychic]                
                $ X_Psychic = 0
            else:
                $ Adjacent = [] 
            if "dating" in R_Traits and "Rogue" not in P_Harem:
                $ P_Harem.append("Rogue")
            if "dating" in K_Traits and "Kitty" not in P_Harem:
                $ P_Harem.append("Kitty")    
        if SaveVersion < 982:        
            #this bit removes the annoying leftover 
            if Time_Count > 0 or Round < 90:
                    #should only apply after morning or after a little time has passed
                    if "sleepover" in R_Traits and R_Loc != bg_current: 
                            $ R_Traits.remove("sleepover")
                    if "sleepover" in K_Traits and K_Loc != bg_current: 
                            $ K_Traits.remove("sleepover")
                    if "sleepover" in E_Traits and E_Loc != bg_current: 
                            $ E_Traits.remove("sleepover")
                    if "sleepover" in L_Traits and L_Loc != bg_current: 
                            $ L_Traits.remove("sleepover")
            $ L_Pubes = 1
            if "passive" in R_Traits:
                    while "passive" in R_Traits:
                        $ R_Traits.remove("passive")     
                    $ R_Traits.append("passive") 
            if P_Harem:
                $ X_Psychic = P_Harem[0] 
                
                while P_Harem.count("Rogue") > 1:
                        $ P_Harem.remove("Rogue")    
                while P_Harem.count("Kitty") > 1:
                        $ P_Harem.remove("Kitty")       
                while P_Harem.count("Emma") > 1:
                        $ P_Harem.remove("Emma") 
                if P_Harem[0] != X_Psychic:                                    
                        $ P_Harem.remove(X_Psychic)    
                        $ P_Harem.insert(0,X_Psychic) 
                $ X_Psychic = 0  
            if "saw with kitty" in R_Traits:
                    $ R_Traits.append("saw with Kitty")
                    $ R_Traits.remove("saw with kitty")
            if "saw with kitty" in E_Traits:
                    $ E_Traits.append("saw with Kitty")
                    $ E_Traits.remove("saw with kitty")                    
            if "saw with rogue" in K_Traits:
                    $ K_Traits.append("saw with Rogue")
                    $ K_Traits.remove("saw with rogue")
            if "saw with rogue" in E_Traits:
                    $ E_Traits.append("saw with Rogue")
                    $ E_Traits.remove("saw with rogue")                    
            if "saw with emma" in R_Traits:
                    $ R_Traits.append("saw with Emma")
                    $ R_Traits.remove("saw with emma")
            if "saw with emma" in K_Traits:
                    $ K_Traits.append("saw with Emma")
                    $ K_Traits.remove("saw with emma")
            # / / / / / /        
            if "poly kitty" in R_Traits:
                    $ R_Traits.append("poly Kitty")
                    $ R_Traits.remove("poly kitty")
            if "poly kitty" in E_Traits:
                    $ E_Traits.append("poly Kitty")
                    $ E_Traits.remove("poly kitty")                    
            if "poly rogue" in K_Traits:
                    $ K_Traits.append("poly Rogue")
                    $ K_Traits.remove("poly rogue")
            if "poly rogue" in E_Traits:
                    $ E_Traits.append("poly Rogue")
                    $ E_Traits.remove("poly rogue")                    
            if "poly emma" in R_Traits:
                    $ R_Traits.append("poly Emma")
                    $ R_Traits.remove("poly emma")
            if "poly emma" in K_Traits:
                    $ K_Traits.append("poly Emma")
                    $ K_Traits.remove("poly emma")
            # / / / / / /        
            if "noticed kitty" in R_RecentActions:
                    $ R_RecentActions.append("noticed Kitty")
                    $ R_RecentActions.remove("noticed kitty")
            if "noticed kitty" in E_RecentActions:
                    $ E_RecentActions.append("noticed Kitty")
                    $ E_RecentActions.remove("noticed kitty")                    
            if "noticed rogue" in K_RecentActions:
                    $ K_RecentActions.append("noticed Rogue")
                    $ K_RecentActions.remove("noticed rogue")
            if "noticed rogue" in E_RecentActions:
                    $ E_RecentActions.append("noticed Rogue")
                    $ E_RecentActions.remove("noticed rogue")                 
            if "noticed emma" in K_RecentActions:
                    $ K_RecentActions.append("noticed Emma")
                    $ K_RecentActions.remove("noticed emma")
            if "noticed emma" in R_RecentActions:
                    $ R_RecentActions.append("noticed Emma")
                    $ R_RecentActions.remove("noticed emma")
            # / / / / / /        
            if "ask kitty" in R_RecentActions:
                    $ R_RecentActions.append("ask Kitty")
                    $ R_RecentActions.remove("ask kitty")
            if "ask kitty" in E_RecentActions:
                    $ E_RecentActions.append("ask Kitty")
                    $ E_RecentActions.remove("ask kitty")                    
            if "ask rogue" in K_RecentActions:
                    $ K_RecentActions.append("ask Rogue")
                    $ K_RecentActions.remove("ask rogue")
            if "ask rogue" in E_RecentActions:
                    $ E_RecentActions.append("ask Rogue")
                    $ E_RecentActions.remove("ask rogue")                 
            if "ask emma" in K_RecentActions:
                    $ K_RecentActions.append("ask Emma")
                    $ K_RecentActions.remove("ask emma")
            if "ask emma" in R_RecentActions:
                    $ R_RecentActions.append("ask Emma")
                    $ R_RecentActions.remove("ask emma")
                    
            if "lockedclass" in P_RecentActions:
                $ P_RecentActions.remove("lockedclass")
                $ P_Traits.append("locked")
            $ SaveVersion = 982
            #end Save 982 prep          
            
        if SaveVersion < 983:        
            $ Kitty_Arms = K_Arms   
            call Clothing_Schedule_Check("Rogue",3,1)  
            call Clothing_Schedule_Check("Rogue",4,1) 
            call Clothing_Schedule_Check("Rogue",5,1) 
            call Clothing_Schedule_Check("Rogue",6,1) 
            call Clothing_Schedule_Check("Kitty",3,1)  
            call Clothing_Schedule_Check("Kitty",4,1) 
            call Clothing_Schedule_Check("Kitty",5,1) 
            call Clothing_Schedule_Check("Kitty",6,1) 
            call Clothing_Schedule_Check("Emma",3,1)  
            call Clothing_Schedule_Check("Emma",4,1) 
            call Clothing_Schedule_Check("Emma",5,1) 
            call Clothing_Schedule_Check("Emma",6,1) 
            call Clothing_Schedule_Check("Laura",3,1)  
            call Clothing_Schedule_Check("Laura",4,1) 
            call Clothing_Schedule_Check("Laura",5,1) 
            call Clothing_Schedule_Check("Laura",6,1) 
#            $ K_Arms = 0
            $ SaveVersion = 983
            #end Save 983 prep          
                    
        if SaveVersion < 984:   
            #shifts case of these words. . .
            if "les kitty" in R_History:
                    $ R_History.remove("les kitty")
                    $ R_History.append("les Kitty")
            if "les emma" in R_History:
                    $ R_History.remove("les emma")
                    $ R_History.append("les Emma")
            if "les laura" in R_History:
                    $ R_History.remove("les laura")
                    $ R_History.append("les Laura")                    
            if "les rogue" in K_History:
                    $ K_History.remove("les rogue")
                    $ K_History.append("les Rogue")
            if "les emma" in K_History:
                    $ K_History.remove("les emma")
                    $ K_History.append("les Emma")
            if "les laura" in K_History:
                    $ K_History.remove("les laura")
                    $ K_History.append("les Laura")                    
            if "les rogue" in E_History:
                    $ E_History.remove("les rogue")
                    $ E_History.append("les Rogue")
            if "les kitty" in E_History:
                    $ E_History.remove("les kitty")
                    $ E_History.append("les Kitty")
            if "les laura" in E_History:
                    $ E_History.remove("les laura")
                    $ E_History.append("les Laura")                    
            if "les rogue" in L_History:
                    $ L_History.remove("les rogue")
                    $ L_History.append("les Rogue")
            if "les kitty" in L_History:
                    $ L_History.remove("les kitty")
                    $ L_History.append("les Kitty")
            if "les emma" in L_History:
                    $ L_History.remove("les emma")
                    $ L_History.append("les Emma")
            #end shifts case of these words. . .
             
            if "locked" in P_RecentActions:
                $ P_RecentActions.remove("locked")
                $ P_Traits.append("locked")       
                    
#            $ SaveVersion = 984
            #end Save 983 prep    
                
                
        
#        call Failsafe
    return


# Event calls ////////////////////////////////////////////////////////////////////
label EventCalls:
        call Present_Check           
        $ D20 = renpy.random.randint(1, 20)       
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
                            jump Campus_Entry
                        "No":
                            "Suit yourself. . ."
        
        if Day < 5 or Round <= 10:
                    #Disables events when it's too early in the game or the turn is about to end 
                    return
                    
#        #Activate's "Rogue like spunk" chat        
#        if "hungry" not in R_Traits and (R_Swallow + R_Chat[2]) >= 10 and R_Loc == bg_current:      #She's swallowed a lot
#                    call Set_The_Scene            
#                    call Rogue_Hungry
#                    return   
        
#        #Activate's "Kitty like spunk" chat
#        if "hungry" not in K_Traits and (K_Swallow + K_Chat[2]) >= 10 and K_Loc == bg_current:      #She's swallowed a lot
#                    call Set_The_Scene            
#                    call Kitty_Hungry
#                    return   
                    
        #Activates Kitty meet    
        if "traveling" in P_RecentActions and "met" not in K_History and bg_current == "bg classroom": 
                    jump KittyMeet
                    return
        
        #Activates Laura meet    
        if "traveling" in P_RecentActions and "met" not in L_History and bg_current == "bg dangerroom":
                if Day >= 10:
                    call LauraMeet
                    return       
        
        #Calls Kitty starting dressup event
        if bg_current == "bg campus" and Current_Time != "Night" and "met" in L_History and "met" in K_History:
                if "dress3" not in L_History and "dress1" not in L_History:
                    call Laura_Dressup
            
        #Activates Emma meet and class stuff
        if "traveling" in P_RecentActions and bg_current == "bg classroom" and Weekday < 5:
                #if you are in motion, in the classroom, and it's a school day, 
                if "met" not in E_History:     
                        jump EmmaMeet
                        return   
                elif Current_Time == "Evening" and not Party:
                    #If you've met Emma, it's evening, and nobody is with you, 
                    if "classcaught" not in E_History:     
                        jump Emma_Caught_Classroom
                        return     
                    elif D20 <= 10:  
                        #50/50 chance of catching Emma in class
                        if E_Lust >= 50:
                                jump Emma_Caught_Classroom
                                return   
                        else:
                            $ E_Loc = "bg classroom"
        elif bg_current == "bg classroom" and Current_Time == "Evening" and Weekday < 5 and Round >= 70:
                #if you are in class and not travelling. . .
                if "met" in E_History:    
                        $ E_Loc = "bg classroom"
            
        if "detention" in P_Traits and bg_current == "bg classroom" and Weekday < 5 and Current_Time == "Evening" and not Party:    
                jump Emma_Detention
                return     
        
        if "locked" in P_Traits:
            #exits if the door is locked, but maybe open this up a bit later. 
            return
            
        #activates if you haven't done an addiciton event today 
        if "angry" not in R_RecentActions and "addiction" not in R_DailyActions and R_Action >= 1:                    
                    #Activates if she needs her fix
                    if R_Addict >= 60 and R_Resistance and not R_Event[3]:
                                if (bg_current == "bg rogue" or bg_current == "bg player") and R_Loc == bg_current:
                                    jump Rogue_Fix
                                elif bg_current == "bg player":
                                    "Rogue pops into the room, looking a little jumpy."
                                    jump Rogue_Fix
                                else:
                                    call RogueFace("manic", 1)
                                    if "asked meet" in R_RecentActions:
                                        pass
                                    elif "asked meet" in R_DailyActions and R_Addict >= 80:
                                        "Rogue texts you. . ."
                                        ch_r "I know I asked to meet you in your room earlier, but I'm serious, this is important."
                                        $ R_RecentActions.append("asked meet")  
                                        return
                                    else:
                                        "Rogue texts and asks if you could meet her in your room later."
                                        $ R_RecentActions.append("asked meet")
                                        $ R_DailyActions.append("asked meet")  
                                        return
                    #Activates if you don't need a fix but already have resistance                    
                    elif R_Resistance:
                        pass
                        
                    #These are the "first time addict" event chains
                    elif R_Addict >= 35 and not R_Event[1]: #"I'm addicted" event
                        jump Rogue_Addicted            
                    elif R_Addict >= 60 and not R_Event[2]: #"I'm super-addicted" event
                        jump Rogue_Addicted2        
                    elif R_Addict >= 90:                    #"I'm crazy-addicted" event
                        jump Rogue_Addicted3               
                   
        #Activates if Rogue or Kitty caught you cheating
        if "meet girl" in P_DailyActions:
                #skips if you already have an appointment
                pass
        else:
                #checks to see if any of the girls noticed you cheating on them
                #returns if not
                call CheatCheck
                                        
        #This scene has Rogue ask Kitty if she wants to have a poly Relationship with you    
        call ShareCheck
        
        call JumperCheck #checks to see if a girl wants to jump you. . .
              
        #Checks to see if any girls want to fap. 
        #If they have "wannafap" in their daily, and "nofap" in their traits, and are not in the room, they will ask you
        #otherwise, they will automatically fap. If you meet them after this, they will be fapping, 
        #if you keep them busy, they will do it overnight
        if Time_Count >= 2 and "fapcall" not in P_DailyActions:
                #if it's evening or later and nobody has yet called you about fapping. . .
                $ Options = ["Rogue","Kitty","Emma","Laura"]
                $ renpy.random.shuffle(Options)
                while Options:
                    if CheckWord(Options[0],"Daily","wannafap"):
                            #if she's wants to fap and is not in the room with you                         
                            call CalltoFap(Options[0]) #checks to see if she's allowed
                    $ Options.remove(Options[0])
        #end fap call check
        
        #Rogue relationship stuff        
        if "relationship" not in R_DailyActions and "angry" not in R_DailyActions:
                if "stoodup" in R_Traits: #you stood her up
                            call Rogue_Date_Stood_Up
                            return  
                if R_Break[0]:
                        #skip all this if you're broken up
                        pass
                elif not R_Event[0] and R_Sleep >= 5:               
                        if R_Loc == bg_current or "Rogue" in Party:
                            call Rogue_Key
                            return  
                elif "boyfriend" not in R_Petnames and R_Love >= 800 and R_Event[5] != 20 and "RogueNo" not in P_Traits: # R_Event[5]
                        # R_Event[5] is 20 if you refused due to other girlfriend    
                        # if "RogueNo" it means you can't date her.                    
                        if P_Harem and "RogueYes" not in P_Traits:
                            call Poly_Start("Rogue")    
                            return
                        elif bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_BF
                        else:
                            call AskedMeet("Rogue","bemused")   
                elif "lover" not in R_Petnames and R_Love >= 950 and K_Event[6] < 15: # R_Event[6]   
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Love
                        else:
                            call AskedMeet("Rogue","bemused")   
                elif "sir" not in R_Petnames and R_Obed >= 500: # R_Event[7]
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Sub
                        else:
                            call AskedMeet("Rogue","bemused")
                elif "master" not in R_Petnames and R_Obed >= 900 and R_Event[8] <2: # R_Event[8]
                        if bg_current == "bg rogue" or bg_current == "bg player":
                            jump Rogue_Slave
                        else:
                            call AskedMeet("Rogue","bemused")
                elif "daddy" not in R_Petnames and ApprovalCheck("Rogue", 750, "L") and ApprovalCheck("Rogue", 500, "O") and ApprovalCheck("Rogue", 500, "I"): # R_Event[5]
                        if bg_current == "bg rogue" or bg_current == "bg player" and R_Loc == bg_current:
                            call Rogue_Daddy
                            return
                elif "sex friend" not in R_Petnames and R_Inbt >= 500: # R_Event[9]  Fix this one
                        if bg_current == "bg rogue" or bg_current == "bg player" or "dating" in R_Traits:
                            jump Rogue_Sexfriend
                        elif "dating" in R_Traits and R_Loc == bg_current:
                            jump Rogue_Sexfriend                            
                        else:
                            call AskedMeet("Rogue","bemused")
                elif "fuck buddy" not in R_Petnames and R_Inbt >= 900: # R_Event[10]  Fix this one
                        if bg_current == "bg rogue" or bg_current == "bg player" or "dating" in R_Traits:
                            jump Rogue_Fuckbuddy
                        elif "dating" in R_Traits and R_Loc == bg_current:
                            jump Rogue_Fuckbuddy    
                        else:
                            call AskedMeet("Rogue","bemused")
        #end Rogue relationship stuff
                
        #Kitty relationship stuff, not finished
        if "relationship" not in K_DailyActions and "angry" not in K_DailyActions: 
                if "stoodup" in K_Traits: #you stood her up
                            call Kitty_Date_Stood_Up
                            return                    
                 
                if K_Break[0]:
                        #skip all this if you're broken up
                        pass
                elif not K_Event[0] and K_Sleep >= 5:               
                            if K_Loc == bg_current or "Kitty" in Party:
                                call Kitty_Key
                                return                              
                elif "boyfriend" not in K_Petnames and K_Love >= 800 and K_Event[5] != 20 and "KittyNo" not in P_Traits: # K_Event[5]
                        # K_Event[5] is 20 if you refused due to other girlfriend
                        # if "KittyNo" it means you can't date her.
                        if P_Harem and "KittyYes" not in P_Traits:
                            call Poly_Start("Kitty")    
                            return
                        elif bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_BF
                            return
                        else:
                            call AskedMeet("Kitty","bemused") 
                elif "lover" not in K_Petnames and K_Love >= 950 and K_Event[6] != 20: # K_Event[6] 
                        # it gets set at 20 if you refuse her advances,
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Love
                            return
                        else:
                            call AskedMeet("Kitty","bemused") 
                elif "sir" not in K_Petnames and K_Obed >= 500 and "sir" not in K_History: # K_Event[7]
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Sub
                            return 
                        else:
                            call AskedMeet("Kitty","bemused")
                elif "master" not in K_Petnames and K_Obed >= 800 and "sir" in K_Petnames and "master" not in K_History: # K_Event[8]
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Master
                            return 
                        else:
                            call AskedMeet("Kitty","bemused")
                elif "daddy" not in K_Petnames and ApprovalCheck("Kitty", 750, "L") and ApprovalCheck("Kitty", 500, "O") and ApprovalCheck("Kitty", 500, "I"): # K_Event[5]
                        if bg_current == "bg kitty" or bg_current == "bg player" and K_Loc == bg_current:
                            call Kitty_Daddy
                            return                         
                elif "sex friend" not in K_Petnames and K_Inbt >= 500: # K_Event[9]
                        if bg_current == "bg kitty" or bg_current == "bg player":
                            call Kitty_Sexfriend
                            return 
                           
                elif "fuck buddy" not in K_Petnames and K_Inbt >= 800 and bg_current != K_Loc: # K_Event[10]  Fix this one
                        #if she's not a fuckbuddy yet, and is not around at the time
                        call Kitty_Fuckbuddy
                        return  
        #End Kitty relationsip stuff
        
        #Emma relationship stuff, not finished
        if "relationship" not in E_DailyActions and "angry" not in E_DailyActions: 
                if "stoodup" in E_Traits: #you stood her up
                            call Emma_Date_Stood_Up
                            return    
                if E_Break[0]:
                        #skip all this if you're broken up
                        pass
                elif not E_Event[0] and E_Sleep >= 5:               
                            if E_Loc == bg_current or "Emma" in Party:
                                call Emma_Key
                                return            
                elif "boyfriend" not in E_Petnames and E_Love >= 800 and E_Event[5] != 20 and "EmmaNo" not in P_Traits: # E_Event[5]
                        if P_Harem and "EmmaYes" not in P_Traits:
                            call Poly_Start("Emma")    
                            return
                        elif bg_current == "bg emma" or bg_current == "bg player":
                            call Emma_BF
                            return
                        else:
                            call AskedMeet("Emma","bemused") 
                elif "lover" not in E_Petnames and E_Love >= 950 and E_Event[6] != 20: # E_Event[6]   
                        if bg_current == "bg emma" or bg_current == "bg player":
                            call Emma_Love
                            return
                        else:
                            call AskedMeet("Emma","bemused") 
                elif "sir" not in E_History and E_Obed >= 500: # E_Event[7]
                        if bg_current == "bg emma" or bg_current == "bg player":
                            call Emma_Sub
                            return 
                        else:
                            call AskedMeet("Emma","bemused")
                elif "master" not in E_History and E_Obed >= 800 and "sir" in E_Petnames: # E_Event[8]
                        if bg_current == "bg emma" or bg_current == "bg player":
                            call Emma_Master
                            return 
                        else:
                            call AskedMeet("Emma","bemused")
                elif "daddy" not in E_Petnames and ApprovalCheck("Emma", 750, "L") and ApprovalCheck("Emma", 500, "O") and ApprovalCheck("Emma", 500, "I"): # E_Event[5]
                        if (bg_current == "bg emma" or bg_current == "bg player") and E_Loc == bg_current:
                            call Emma_Daddy
                            return 
                elif "sex friend" not in E_Petnames and E_Inbt >= 500 and bg_current == "bg classroom" and Time_Count == 2: # E_Event[9]  Fix this one
                            call Emma_Sexfriend
                            return 
                           
                elif "fuck buddy" not in E_Petnames and E_Inbt >= 800 and bg_current != E_Loc: # E_Event[10]  Fix this one
                        #if she's not a fuckbuddy yet, and is not around at the time
                        call Emma_Fuckbuddy
                        return  
        #End Emma relationsip stuff
         
        #Laura relationship stuff, not finished
        if "relationship" not in L_DailyActions and "angry" not in L_DailyActions: 
                if "stoodup" in L_Traits: #you stood her up
                            call Laura_Date_Stood_Up
                            return  
                 
                if L_Break[0]:
                        #skip all this if you're broken up
                        pass
                elif not L_Event[0] and L_Sleep >= 5:               
                            if L_Loc == bg_current or "Laura" in Party:
                                call Laura_Key
                                return                    
                elif "boyfriend" not in L_Petnames and L_Love >= 800 and L_Event[5] != 20 and "LauraNo" not in P_Traits: # L_Event[5]
                        if P_Harem and "LauraYes" not in P_Traits:
                            call Poly_Start("Laura")    
                            return
                        elif bg_current == "bg laura" or bg_current == "bg player":
                            call Laura_BF
                            return
                        else:
                            call AskedMeet("Laura","bemused") 
                elif "lover" not in L_Petnames and L_Love >= 950 and L_Event[6] != 20: # L_Event[6]   
                        if bg_current == "bg laura" or bg_current == "bg player":
                            call Laura_Love
                            return
                        else:
                            call AskedMeet("Laura","bemused") 
                elif "sir" not in L_History and L_Obed >= 500: # L_Event[7]
                        if bg_current == "bg laura" or bg_current == "bg player":
                            call Laura_Sub
                            return 
                        else:
                            call AskedMeet("Laura","bemused")
                elif "master" not in L_History and L_Obed >= 800 and "sir" in L_Petnames: # L_Event[8]
                        if bg_current == "bg laura" or bg_current == "bg player":
                            call Laura_Master
                            return 
                        else:
                            call AskedMeet("Laura","bemused")
                elif "daddy" not in L_Petnames and ApprovalCheck("Laura", 750, "L") and ApprovalCheck("Laura", 500, "O") and ApprovalCheck("Laura", 500, "I"): # L_Event[5]
                        if (bg_current == "bg laura" or bg_current == "bg player") and L_Loc == bg_current:
                            call Laura_Daddy
                            return 
                        else:
                            call AskedMeet("Laura","bemused")
                elif "sex friend" not in L_Petnames and L_Inbt >= 500: # L_Event[9]
                            call Laura_Sexfriend
                            return 
                           
                elif "fuck buddy" not in L_Petnames and L_Inbt >= 800 and bg_current == "bg player" and bg_current != L_Loc: # L_Event[10]
                            #if she's not a fuckbuddy yet, and is not around at the time
                            call Laura_Fuckbuddy
                            return  
        #End Laura relationsip stuff                   
#End primary events
        
        
                     
label QuickEvents:                                              
        #These events get checked every screen refresh

        $ Options = []       
        call Present_Check
        #If Rogue is around
        if R_Loc == bg_current:
                if R_Lust >= 90:       
                        $ R_Blush = 1
                        $ R_Wet = 2 
                elif R_Lust >= 60:        
                        $ R_Blush = 1
                        $ R_Wet = 1
                else:
                        $ R_Wet = 0
                        
                #Rogue reacts to getting horny
                if Taboo and R_Lust >= 75:
                        if R_Inbt > 800 or "exhibitionist" in R_Traits:
                                "Rogue gets a sly smile on her face and squirms a bit."
                        elif R_Inbt > 500 and R_Lust < 90:
                                "Rogue looks a bit flushed and uncomfortable."
                        elif bg_current != "bg showerroom":
                                "Rogue gets an embarrassed look on her face and suddenly leaves the room."
                                call Remove_Girl("Rogue")
                                call Set_The_Scene        
        else:
                #if Rogue is not around
                if R_Loc == "bg showerroom" and "showered" in R_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Rogue_Schedule
                        call RogueOutfit(Changed=1) 
                        call Girls_Location
                        call RogueOutfit(Changed=1) 
        #End Rogue Quick Events  
        
        if K_Loc == bg_current:
                if K_Lust >= 90:       
                        $ K_Blush = 1
                        $ K_Wet = 2 
                elif K_Lust >= 60:        
                        $ K_Blush = 1
                        $ K_Wet = 1
                else:
                        $ K_Wet = 0
                  
                #Kitty reacts to getting horny      
                if Taboo and K_Lust >= 75:
                    if K_Inbt > 800 or "exhibitionist" in K_Traits:
                            "Kitty gets a sly smile on her face and squirms a bit."
                    elif K_Inbt > 500 and K_Lust < 90:
                            "Kitty looks a bit flushed and uncomfortable."
                    elif bg_current != "bg showerroom":
                            "Kitty gets an embarrassed look on her face and suddenly phases through the floor."
                            call Remove_Girl("Kitty")
                            call Set_The_Scene
        else:
                #if Kitty is not around
                if K_Loc == "bg showerroom" and "showered" in K_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Kitty_Schedule
                        call KittyOutfit(Changed=1)
                        call Girls_Location    
                        call KittyOutfit(Changed=1)        
        # End Kitty Quick Events
        
        if E_Loc == bg_current:
                if E_Lust >= 90:       
                        $ E_Blush = 1
                        $ E_Wet = 2 
                elif E_Lust >= 60:        
                        $ E_Blush = 1
                        $ E_Wet = 1
                else:
                        $ E_Wet = 0
                  
                #Emma reacts to getting horny      
                if Taboo and E_Lust >= 75:
                    if E_Inbt > 800 or "exhibitionist" in E_Traits:
                            "Emma gets a sly smile on her face and squirms a bit."
                    elif E_Inbt > 500 and E_Lust < 90:
                            "Emma looks a bit flushed and uncomfortable."
                    elif bg_current != "bg showerroom":
                            "Emma gets an embarrassed look on her face and dashes out of the room."
                            call Remove_Girl("Emma")
                            call Set_The_Scene
        else:
                #if Emma is not around
                if E_Loc == "bg showerroom" and "showered" in E_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Emma_Schedule  
                        call EmmaOutfit(Changed=1)
                        call Girls_Location   
                        call EmmaOutfit(Changed=1)
        #end Emma Quick Events
        
        if L_Loc == bg_current:
                if L_Lust >= 90:       
                        $ L_Blush = 1
                        $ L_Wet = 2 
                elif L_Lust >= 60:        
                        $ L_Blush = 1
                        $ L_Wet = 1
                else:
                        $ L_Wet = 0
                  
                #Laura reacts to getting horny      
                if Taboo and L_Lust >= 75:
                    if L_Inbt > 800 or "exhibitionist" in L_Traits:
                            "Laura gets a sly smile on her face and squirms a bit."
                    elif L_Inbt > 500 and L_Lust < 90:
                            "Laura looks a bit flushed."
                    elif bg_current != "bg showerroom":
                            "Laura gets an odd look on her face and dashes out of the room."
                            call Remove_Girl("Laura")
                            call Set_The_Scene
        else:
                #if Laura is not around
                if L_Loc == "bg showerroom" and "showered" in L_DailyActions:
                        #if she's recently showered and still in the shower, send her elsewhere
                        call Laura_Schedule  
                        call LauraOutfit(Changed=1)
                        call Girls_Location   
                        call LauraOutfit(Changed=1)
        #end Laura Quick Events
        return   
#End Quick Events

label AskedMeet(Girl = "Rogue", Emotion = "bemused"): # Use AskedMeet("Rogue","angry")
    #This asks the player to meet the chosen character later    
    if CheckWord(Girl,"Daily","asked meet"):
                    call AnyFace(Girl,Emotion)
                    "[Girl] asks if you could meet her in your room later."
                    call AnyWord(Girl,1,0,"asked meet",0,0) #$ R_DailyActions.append("asked meet") 
                    $ P_DailyActions.append("meet girl")
    return
                    
#    if Girl == "Rogue":
#            if "asked meet" not in R_DailyActions:
#                    call RogueFace(Emotion)
#                    "Rogue asks if you could meet her in your room later."
#                    $ R_DailyActions.append("asked meet") 
#    elif Girl == "Kitty":
#            if "asked meet" not in K_DailyActions:
#                    call KittyFace(Emotion)
#                    "Kitty asks if you could meet her in your room later."
#                    $ K_DailyActions.append("asked meet") 
#    elif Girl == "Emma":
#            if "asked meet" not in E_DailyActions:
#                    call EmmaFace(Emotion)
#                    "Emma asks if you could meet her in your room later."
#                    $ E_DailyActions.append("asked meet") 
#    elif Girl == "Laura":
#            if "asked meet" not in L_DailyActions:
#                    call LauraFace(Emotion)
#                    "Laura asks if you could meet her in your room later."
#                    $ L_DailyActions.append("asked meet") 
#    return
    
# End Event Calls //////////////////////////////////////////////////////////////    
    
    
    

# Rogue's Outfit //////////////////////////////////////////////
label RogueOutfit(R_OutfitTemp = R_Outfit, Spunk = 0, Undressed = 0, Changed = 1):                                                      #add transitions    
        # R_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed
        
        if R_OutfitTemp == 5: 
                #this sets it to default if using AnyOutfit
                $ R_OutfitTemp = R_Outfit
        elif R_OutfitTemp == 6: 
                #this sets it to daily default if using AnyOutfit
                $ R_OutfitTemp = R_OutfitDay
            
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
                #Skips theis check if it's a sleepover
                return
        
        if R_OutfitTemp != R_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1
        if "Rogue" in Party and R_OutfitTemp == R_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ R_OutfitTemp = R_Outfit
#        if R_Loc == "bg showerroom" and "Rogue" not in Party and R_OutfitTemp != "nude":
#                #Automatically puts her in the towel while in the shower
#                $ R_OutfitTemp = "towel" 
        if R_Loc != "bg showerroom" or (R_OutfitTemp != "nude" and R_OutfitTemp != "towel"):
                #Dries her off
                $ R_Water = 0
                
        if R_Spunk:
                #Removes spunk if told to do so. 
                if "painted" not in R_DailyActions or "cleaned" not in R_DailyActions:        
                    $ del R_Spunk[:]  
         
        #Resets "half-dressed" states
        $ R_Upskirt = 0
        $ R_Uptop = 0
        $ R_PantiesDown = 0
        
        if R_OutfitTemp == "evo_green":
                    if 0 in (R_Legs,R_Over,R_Chest,R_Hose):
                        $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1      
                            
                    $ R_Arms = "gloved"
                    $ R_Legs = "skirt"
                    $ R_Over = "mesh top"
                    $ R_Neck = "spiked collar"        
                    $ R_Chest = "tank"
                    $ R_Panties = "black panties"
                    if "stockings and garterbelt" in R_Inventory:
                        $ R_Hose = "stockings and garterbelt"
                    elif ApprovalCheck("Rogue", 300, "I"):                        
                        $ R_Hose = "stockings"
                    else:
                        $ R_Hose = "tights"
                    $ R_Shame = 0
        elif R_OutfitTemp == "evo_pink":
                    if 0 in (R_Legs,R_Over,R_Chest):
                            $ Undressed = 1
                    elif R_Panties == 0 and "pantyless" not in R_DailyActions:                        
                            $ Undressed = 1                        
                        
                    $ R_Neck = 0
                    $ R_Arms = "gloved"
                    $ R_Legs = "pants"
                    $ R_Over = "pink top"
                    $ R_Neck = 0
                    $ R_Chest = "buttoned tank"
                    $ R_Panties = "black panties"
                    $ R_Hose = 0
                    $ R_Shame = 0
        elif R_OutfitTemp == "nude":
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Over = 0
                    $ R_Neck = 0
                    $ R_Chest = 0
                    $ R_Panties = 0        
                    $ R_Hose = 0
                    $ R_Shame = 50
        elif R_OutfitTemp == "towel":
                    if R_Over == 0:
                        $ Undressed = 2
                    $ R_Neck = 0
                    $ R_Arms = 0
                    $ R_Legs = 0
                    $ R_Chest = 0
                    $ R_Over = "towel"
                    $ R_Panties = 0        
                    $ R_Hose = 0        
                    $ R_Shame = 35
        elif R_OutfitTemp == "custom1":
                    if not R_Legs and R_Custom[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom[9]:          
                        $ Undressed = 1
            
                    $ R_Arms = R_Custom[1]
                    $ R_Legs = R_Custom[2]
                    $ R_Over = R_Custom[3]
                    $ R_Neck = R_Custom[4]
                    $ R_Chest = R_Custom[5]
                    $ R_Panties = R_Custom[6]
            #        $ R_Pubes = R_Custom[7]
                    $ R_Hair = R_Custom[8] if R_Custom[8] else "evo"
                    $ R_Hose = R_Custom[9]        
                    $ R_Shame = R_OutfitShame[3]
        elif R_OutfitTemp == "custom2":
                    if not R_Legs and R_Custom2[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom2[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom2[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom2[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom2[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom2[1]
                    $ R_Legs = R_Custom2[2]
                    $ R_Over = R_Custom2[3]
                    $ R_Neck = R_Custom2[4] 
                    $ R_Chest = R_Custom2[5]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom2[6]
            #        $ R_Pubes = R_Custom2[7]
                    $ R_Hair = R_Custom2[8] if R_Custom2[8] else "evo"
                    $ R_Hose = R_Custom2[9]        
                    $ R_Shame = R_OutfitShame[5]
        elif R_OutfitTemp == "custom3":
                    if not R_Legs and R_Custom3[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom3[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom3[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom3[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom3[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom3[1]
                    $ R_Legs = R_Custom3[2]
                    $ R_Over = R_Custom3[3]
                    $ R_Neck = R_Custom3[4] 
                    $ R_Chest = R_Custom3[5]
                    $ R_Panties = R_Custom3[6]
            #        $ R_Pubes = R_Custom3[7]
                    $ R_Hair = R_Custom3[8] if R_Custom3[8] else "evo"
                    $ R_Hose = R_Custom3[9]        
                    $ R_Shame = R_OutfitShame[6]
        elif R_OutfitTemp == "temporary":
                    if not R_Legs and R_TempClothes[2]:            
                            $ Undressed = 1
                    elif not R_Over and R_TempClothes[3]:          
                            $ Undressed = 1
                    elif not R_Chest and R_TempClothes[5]:          
                            $ Undressed = 1
                    elif not R_Panties and R_TempClothes[6] and "pantyless" not in R_DailyActions:         
                            $ Undressed = 1
                    elif not R_Hose and R_TempClothes[9]:          
                            $ Undressed = 1
                            
                    $ R_Arms = R_TempClothes[1]
                    $ R_Legs = R_TempClothes[2]
                    $ R_Over = R_TempClothes[3]
                    $ R_Neck = R_TempClothes[4]
                    $ R_Chest = R_TempClothes[5]
                    $ R_Panties = R_TempClothes[6] 
#                    $ R_Boots = R_TempClothes[7]  
                    $ R_Hair = R_TempClothes[8] if R_TempClothes[8] else R_Hair  
                    $ R_Hose = R_TempClothes[9]                         
                    $ R_Shame = R_OutfitShame[8]
        elif R_OutfitTemp == "sleep":     
                    if not R_Legs and R_Sleepwear[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Sleepwear[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Sleepwear[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Sleepwear[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Sleepwear[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Sleepwear[1] #0
                    $ R_Legs = R_Sleepwear[2] #0
                    $ R_Over = R_Sleepwear[3] #0
                    $ R_Neck = R_Sleepwear[4] #0 
                    $ R_Chest = R_Sleepwear[5] #"tank"
                    $ R_Panties = R_Sleepwear[6] #"green panties"
                    $ R_Hair = R_Sleepwear[8] if R_Sleepwear[8] else "evo"
                    $ R_Hose = R_Sleepwear[9] #0 
                    $ R_Shame = R_OutfitShame[4]
        elif R_OutfitTemp == "gym":
                    if not R_Legs and R_Gym[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Gym[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Gym[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Gym[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Gym[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Gym[1]
                    $ R_Legs = R_Gym[2]
                    $ R_Over = R_Gym[3]        
                    $ R_Neck = R_Gym[4]
                    $ R_Chest = R_Gym[5]
                    $ R_Panties = R_Gym[6]
                    $ R_Hair = R_Gym[8] if R_Gym[8] else "evo"
                    $ R_Hose = R_Gym[9]     
                    $ R_Shame = R_OutfitShame[7]        
                    if R_Inbt <= 300 and not R_Over:   
                        #Puts a hoodie on if she's shy
                        $ R_Over = "hoodie"  
                        $ R_Shame -= 10 if R_Shame >=10 else R_Shame
        elif R_OutfitTemp == "custom2":
                    if not R_Legs and R_Custom2[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Custom2[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Custom2[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Custom2[6] and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Custom2[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Custom2[1]
                    $ R_Legs = R_Custom2[2]
                    $ R_Over = R_Custom2[3]
                    $ R_Neck = R_Custom2[4] 
                    $ R_Chest = R_Custom2[5]
                    if "pantyless" not in R_DailyActions:
                        $ R_Panties = R_Custom2[6]
            #        $ R_Pubes = R_Custom2[7]
                    $ R_Hair = R_Custom2[8] if R_Custom2[8] else "evo"
                    $ R_Hose = R_Custom2[9]        
                    $ R_Shame = R_OutfitShame[5]
        elif R_OutfitTemp == "swimwear":
                    if not R_Swim[0]:
                            if "bikini top" not in R_Inventory or "bikini bottoms" not in R_Inventory:
                                #if she doesn't own her swimsuit components. . .
                                if not CheckWord("Rogue","Daily","swim"):
                                        ch_r "I don't really have any swimsuit I could wear. . ."
                                return
                            else:
                                $ R_Swim[0] = 1
                    if not R_Swim[0] and R_Inbt >= 500:
                            $ R_Swim[3] = 0
                    if not R_Legs and R_Swim[2]:            
                        $ Undressed = 1
                    elif not R_Over and R_Swim[3]:          
                        $ Undressed = 1
                    elif not R_Chest and R_Swim[5]:          
                        $ Undressed = 1
                    elif not R_Panties and R_Swim[6]:# and "pantyless" not in R_DailyActions:          
                        $ Undressed = 1
                    elif not R_Hose and R_Swim[9]:          
                        $ Undressed = 1
                        
                    $ R_Arms = R_Swim[1]
                    $ R_Legs = R_Swim[2]
                    $ R_Over = R_Swim[3]
                    $ R_Neck = R_Swim[4] 
                    $ R_Chest = R_Swim[5]
                    $ R_Panties = R_Swim[6]
            #        $ R_Pubes = R_Swim[7]
                    $ R_Hair = R_Swim[8] if R_Swim[8] else "evo"
                    $ R_Hose = R_Swim[9]        
                    $ R_Shame = R_OutfitShame[6]
                
        if R_Panties and R_Panties != "shorts" and "pantyless" in R_DailyActions:       
                # This checks the pantyless state from flirting 
                if R_OutfitTemp != "sleep" and R_OutfitTemp != "gym":
                        if R_Legs == "pants" or HoseNum("Rogue") >= 10:
                            $ R_Shame -= 5    
                        elif R_Legs:
                            $ R_Shame -= 10  
                        elif R_Panties == "green panties":
                            $ R_Shame -= 20  
                        elif R_Panties == "lace panties":
                            $ R_Shame -= 25             
                        else:
                            $ R_Shame -= 23  
                        
                        $ R_Panties = 0        
                        $ R_Shame = 0 if R_Shame < 0 else R_Shame
                
        if not Changed and R_OutfitTemp == R_Outfit and R_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "Rogue throws on a towel."
                elif Undressed:
                        "Rogue throws her clothes back on."        
        
        return
#End Rogue Outfits


#Rogue Add/Remove gloves function //////////////

label Rogue_Schedule(Clothes = 1, Location = 1, LocTemp = R_Loc):
        #Rogue's natural movements
        # If not Clothes, don't bother with her outfit in the schedule
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "Rogue" in Party and Clothes != 2 or not Location: 
                #if she's in a party, never mind
                return         
        elif Clothes != 2 and "sleepover" in R_Traits and Current_Time == "morning":
                #she slept over, so just forget this for now  
                return           
                                        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #In the morning, or if ordered to reschedule, pick an outfit for the day. 
                $ R_OutfitDay = 0
                if R_Break[0]:
                    pass #she won't pick clothes if she's mad at you
                elif R_Schedule[Weekday] == 1:
                        $ R_OutfitDay = "evo_green"
                elif R_Schedule[Weekday] == 2:
                        $ R_OutfitDay = "evo_pink"
                elif R_Schedule[Weekday] == 3 and R_Custom[0]:
                        $ R_OutfitDay = "custom1"
                elif R_Schedule[Weekday] == 4:
                        $ R_OutfitDay = "gym"
                elif R_Schedule[Weekday] == 5 and R_Custom2[0]:
                        $ R_OutfitDay = "custom2"
                elif R_Schedule[Weekday] == 6 and R_Custom3[0]:
                        $ R_OutfitDay = "custom3"
                if not R_OutfitDay: 
                        $ Options = ["evo_pink", "evo_green"]
                        if not R_Break[0]:
                            $ Options.append("custom1") if R_Custom[0] == 2 else Options
                            $ Options.append("custom2") if R_Custom2[0] == 2 else Options
                            $ Options.append("custom3") if R_Custom3[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ R_OutfitDay = Options[0]
                        $ del Options[:] 
                $ R_Outfit = R_OutfitDay
        #End clothing portion
                
        #Location portion
        if "Rogue" in Party or R_Loc == "hold":
                pass
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:            
        #MoWeFr   
                if Current_Time == "Midday": 
                        $ R_Loc = "bg classroom"
                else:
                        $ R_Loc = "bg rogue"
        elif Weekday == 1 or Weekday == 3:                          
        #TuThu        
                if Current_Time == "Morning":
                        $ R_Loc = "bg classroom"
                elif Current_Time == "Midday":
                        $ R_Loc = "bg dangerroom"
                else:
                        $ R_Loc = "bg rogue"
        else:                                                       
        #Weekend                               
                if Current_Time == "Morning":
                        $ R_Loc = "bg dangerroom"
                elif Current_Time == "Midday":
                        $ R_Loc = "bg pool"
                else:
                        $ R_Loc = "bg rogue"
                                                 
        if R_Loc != LocTemp and "Rogue" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ R_RecentActions.append("leaving") 
                elif R_Loc == bg_current: #If she's showed up
                    $ R_RecentActions.append("arriving") 
        if "Rogue" in Nearby:
                $ Nearby.remove("Rogue")                    
        return
#End Rogue's Schedule


label Rogue_Todo:
        #Actions checked each night 
        #causes her to grow her pubes out over a week   
        if "pubes" in R_Todo:               
                $ R_PubeC -= 1
                if R_PubeC >= 1:
                        pass
                else:            
                        $ R_Pubes = 1
                        $ R_Todo.remove("pubes")  
                
        #causes her to wax her pubes       
        if "shave" in R_Todo:         
                $ R_Pubes = 0
                $ R_Todo.remove("shave")
             
        #causes her to put in piercings 
        if "ring" in R_Todo:               
                $ R_Pierce = "ring"
                $ R_Todo.remove("ring")
        if "barbell" in R_Todo:
                $ R_Pierce = "barbell"
                $ R_Todo.remove("barbell")
        
        return
           

# Kitty's Outfit //////////////////////////////////////////////
label KittyOutfit(K_OutfitTemp = K_Outfit, Spunk = 0, Undressed = 0, Changed = 1):   
        # K_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if K_OutfitTemp == 5: #this sets it to default if using AnyOutfit
                $ K_OutfitTemp = K_Outfit
        elif K_OutfitTemp == 6: #this sets it to default if using AnyOutfit
                $ K_OutfitTemp = K_OutfitDay
                
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return
        
        if K_OutfitTemp != K_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Kitty" in Party and K_OutfitTemp == K_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ K_OutfitTemp = K_Outfit
#        if K_Loc == "bg showerroom" and "Kitty" not in Party and K_OutfitTemp != "nude":
#                #Automatically puts her in the towel while in the shower
#                $ K_OutfitTemp = "towel"                                  
        elif K_Loc != "bg showerroom" or (K_OutfitTemp != "nude" and K_OutfitTemp != "towel"):
                #Dries her off
                $ K_Water = 0
                
        if K_Spunk:
                if "painted" not in K_DailyActions or "cleaned" not in K_DailyActions:        
                    $ del K_Spunk[:] 
                
        $ K_Upskirt = 0
        $ K_Uptop = 0
        $ K_PantiesDown = 0
        if K_OutfitTemp == "pink outfit":
                    if 0 in (K_Legs,K_Over,K_Chest):
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Legs = "capris"
                    $ K_Over = "pink top"
                    $ K_Chest = "cami"
                    $ K_Panties = "green panties"        
                    $ K_Neck = "gold necklace"
                    $ K_Hair = "evo"
                    $ K_Hose = 0    
        elif K_OutfitTemp == "red outfit":
                    if 0 in (K_Legs,K_Over,K_Chest):
                            $ Undressed = 1
                    elif K_Panties == 0 and "pantyless" not in K_DailyActions:                        
                            $ Undressed = 1   
                    $ K_Legs = "black jeans"
                    $ K_Over = "red shirt"
                    $ K_Chest = "bra"
                    $ K_Panties = "green panties"      
                    $ K_Neck = 0
                    $ K_Hair = "evo"
                    $ K_Hose = 0    
        elif K_OutfitTemp == "towel":
                    if K_Over == 0:
                            $ Undressed = 2
                    $ K_Arms = 0
                    $ K_Legs = 0
                    $ K_Chest = 0
                    $ K_Over = "towel"
                    $ K_Panties = 0        
                    $ K_Hose = 0          
                    $ K_Neck = 0  
                    $ K_Hair = "long"
                    $ K_Shame = 35
        elif K_OutfitTemp == "nude":
                    $ K_Legs = 0
                    $ K_Chest = 0
                    $ K_Over = 0
                    $ K_Panties = 0              
                    $ K_Neck = 0
                    $ K_Hose = 0   
                    $ K_Shame = 50
        elif K_OutfitTemp == "custom1":
                    if not K_Legs and K_Custom[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom[6] and "pantyless" not in K_DailyActions:          
                            $ Undressed = 1
                    elif not K_Hose and K_Custom[9]:          
                            $ Undressed = 1
                    
                    $ K_Arms = K_Custom[1]
                    $ K_Legs = K_Custom[2]
                    $ K_Over = K_Custom[3]    
                    $ K_Neck = K_Custom[4]
                    $ K_Chest = K_Custom[5]
                    $ K_Panties = K_Custom[6]  
                    $ K_Hose = K_Custom[9]                     
                    $ K_Hair = K_Custom[8] if K_Custom[8] else K_Hair 
                    $ K_Shame = K_OutfitShame[3]
        elif K_OutfitTemp == "custom2":
                    if not K_Legs and K_Custom2[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom2[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom2[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom2[6] and "pantyless" not in K_DailyActions:          
                            $ Undressed = 1
                    elif not K_Hose and K_Custom2[9]:          
                            $ Undressed = 1
                        
                    $ K_Arms = K_Custom2[1]
                    $ K_Legs = K_Custom2[2]
                    $ K_Over = K_Custom2[3]   
                    $ K_Neck = K_Custom2[4]
                    $ K_Chest = K_Custom2[5]
                    $ K_Panties = K_Custom2[6] 
                    $ K_Hose = K_Custom2[9]                      
                    $ K_Hair = K_Custom2[8] if K_Custom2[8] else K_Hair
                    $ K_Shame = K_OutfitShame[5]
        elif K_OutfitTemp == "custom3":
                    if not K_Legs and K_Custom3[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Custom3[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Custom3[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Custom3[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_Custom3[9]:          
                            $ Undressed = 1
                        
                    $ K_Arms = K_Custom3[1]
                    $ K_Legs = K_Custom3[2]
                    $ K_Over = K_Custom3[3]
                    $ K_Neck = K_Custom3[4]
                    $ K_Chest = K_Custom3[5]
                    $ K_Panties = K_Custom3[6]    
                    $ K_Hose = K_Custom3[9]   
                    $ K_Hair = K_Custom3[8] if K_Custom3[8] else K_Hair
                    $ K_Shame = K_OutfitShame[6]
        elif K_OutfitTemp == "temporary":
                    if not K_Legs and K_TempClothes[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_TempClothes[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_TempClothes[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_TempClothes[6] and "pantyless" not in K_DailyActions:         
                            $ Undressed = 1
                    elif not K_Hose and K_TempClothes[9]:          
                            $ Undressed = 1
                            
                    $ K_Arms = K_TempClothes[1]
                    $ K_Legs = K_TempClothes[2]
                    $ K_Over = K_TempClothes[3]
                    $ K_Neck = K_TempClothes[4]
                    $ K_Chest = K_TempClothes[5]
                    $ K_Panties = K_TempClothes[6] 
#                    $ K_Boots = K_TempClothes[7]  
                    $ K_Hair = K_TempClothes[8] if K_TempClothes[8] else K_Hair  
                    $ K_Hose = K_TempClothes[9]                         
                    $ K_Shame = K_OutfitShame[8]
        elif K_OutfitTemp == "sleep":  
                    if not K_Legs and K_Sleepwear[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Sleepwear[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Sleepwear[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Sleepwear[6] and "pantyless" not in K_DailyActions:        
                            $ Undressed = 1
                    elif not K_Hose and K_Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ K_Arms = K_Sleepwear[1] #0
                    $ K_Legs = K_Sleepwear[2] #shorts
                    $ K_Over = K_Sleepwear[3] #0
                    $ K_Neck = K_Sleepwear[4] #0
                    $ K_Chest = K_Sleepwear[5] #"cami"
                    $ K_Panties = K_Sleepwear[6] #"green panties"
                    $ K_Hair = K_Sleepwear[8] if K_Sleepwear[8] else K_Hair
                    $ K_Hose = K_Sleepwear[9] #0  
                    
                    $ K_Hair = "long"
                    $ K_Shame = K_OutfitShame[4]
                    
        elif K_OutfitTemp == "gym":
                    if not K_Legs and K_Gym[2]:            
                            $ Undressed = 1
                    elif not K_Over and K_Gym[3]:          
                            $ Undressed = 1
                    elif not K_Chest and K_Gym[5]:          
                            $ Undressed = 1
                    elif not K_Panties and K_Gym[6] and "pantyless" not in K_DailyActions:        
                            $ Undressed = 1
                    elif not K_Hose and K_Gym[9]:          
                            $ Undressed = 1
                        
                    $ K_Arms = K_Gym[1]
                    $ K_Legs = K_Gym[2]
                    $ K_Over = K_Gym[3] 
                    $ K_Neck = K_Gym[4]
                    $ K_Chest = K_Gym[5]
                    $ K_Panties = K_Gym[6]   
                    $ K_Hair = K_Gym[8] if K_Gym[8] else K_Hair 
                    $ K_Hose = K_Gym[9]     
                    $ K_Shame = K_OutfitShame[7]   
        elif K_OutfitTemp == "swimwear":
                    if not K_Swim[0]:
                            if "bikini top" not in K_Inventory or "bikini bottoms" not in K_Inventory:
                                #if she doesn't own her swimsuit components. . .
                                if not CheckWord("Kitty","Daily","swim"):
                                        ch_k "I wish I had something cute to wear, but I don't. . ."
                                return
                            elif K_Inbt <= 400 and "blue skirt" not in K_Inventory:
                                if not CheckWord("Kitty","Daily","swim"):
                                        ch_k "I don't know, I do have a suit, but it's a little daring. . ."
                                        ch_k "If only I had a little skirt or something. . ."
                                return                                
                            else:
                                $ K_Swim[0] = 1
                                
                            if K_Inbt > 400:
                                $ K_Legs = 0      
                                        
                    if not K_Swim[0] and K_Inbt >= 500:
                            $ K_Swim[2] = 0
                    if not K_Legs and K_Swim[2]:            
                        $ Undressed = 1
                    elif not K_Over and K_Swim[3]:          
                        $ Undressed = 1
                    elif not K_Chest and K_Swim[5]:          
                        $ Undressed = 1
                    elif not K_Panties and K_Swim[6]:# and "pantyless" not in K_DailyActions:          
                        $ Undressed = 1
                    elif not K_Hose and K_Swim[9]:          
                        $ Undressed = 1
                        
                    $ K_Arms = K_Swim[1]                    
                    $ K_Legs = K_Swim[2]
                    $ K_Over = K_Swim[3]
                    $ K_Neck = K_Swim[4] 
                    $ K_Chest = K_Swim[5]
                    $ K_Panties = K_Swim[6]
            #        $ K_Pubes = K_Swim[7]
                    $ K_Hair = K_Swim[8] if K_Swim[8] else K_Hair
                    $ K_Hose = K_Swim[9]        
                    $ K_Shame = K_OutfitShame[6]
                
        if K_Panties and "pantyless" in K_DailyActions:       
                # This checks the pantyless state from flirting 
                if K_OutfitTemp != "sleep" and K_OutfitTemp != "gym":
                        if K_Legs == "pants" or HoseNum("Kitty") >= 10:
                            $ K_Shame -= 5    
                        elif K_Legs:
                            $ K_Shame -= 10  
                        elif K_Panties == "green panties":
                            $ K_Shame -= 20  
                        elif K_Panties == "lace panties":
                            $ K_Shame -= 25             
                        else:
                            $ K_Shame -= 23  
                        
                        $ K_Panties = 0        
                        $ K_Shame = 0 if K_Shame < 0 else K_Shame
                    
        if not Changed and K_OutfitTemp == K_Outfit and K_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."
        
        if Undressed:
            return 1
        else:
            return 0
#End Kitty's Outfits
      
label Kitty_Schedule(Clothes = 1, Location = 1, LocTemp = K_Loc): 
        #Kitty's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in K_History or ("Kitty" in Party and Clothes != 2): 
            #if she's in a party, never mind
            return   
        if Clothes != 2 and "sleepover" in K_Traits and Current_Time == "morning":
                #she slept over, so just forget this for now  
                return           
                
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #Pick clothes for the day
                $ K_OutfitDay = 0
                if K_Break[0]:
                    pass #she won't pick clothes if she's mad at you
                elif K_Schedule[Weekday] == 1: #Tue
                        $ K_OutfitDay = "pink outfit"
                elif K_Schedule[Weekday] == 2: #Wed
                        $ K_OutfitDay = "red outfit"
                elif K_Schedule[Weekday] == 3 and K_Custom[0]: #Thu
                        $ K_OutfitDay = "custom1"
                elif K_Schedule[Weekday] == 4: #Fri
                        $ K_OutfitDay = "gym"
                elif K_Schedule[Weekday] == 5 and K_Custom2[0]: #Sat
                        $ K_OutfitDay = "custom2"
                elif K_Schedule[Weekday] == 6 and K_Custom3[0]: #Sun
                        $ K_OutfitDay = "custom3"
                if not K_OutfitDay: 
                        $ Options = ["pink outfit", "red outfit"]
                        if not K_Break[0]:
                                $ Options.append("custom1") if K_Custom[0] == 2 else Options
                                $ Options.append("custom2") if K_Custom2[0] == 2 else Options
                                $ Options.append("custom3") if K_Custom3[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ K_OutfitDay = Options[0]
                        $ del Options[:]  
                $ K_Outfit = K_OutfitDay 
        #End clothing portion
        
        
        #Location portion   
        if "Kitty" in Party or K_Loc == "hold" or not Location:
                pass          
                
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ K_Loc = "bg classroom"
                elif Current_Time == "Midday": 
                        $ K_Loc = "bg dangerroom"
                else:
                        $ K_Loc = "bg kitty"
        elif Weekday == 1 or Weekday == 3:
        #TuThu        
                if Current_Time == "Morning":
                        $ K_Loc = "bg classroom"
                elif Current_Time == "Midday":
                        $ K_Loc = "bg pool"
                else:
                        $ K_Loc = "bg kitty"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ K_Loc = "bg campus"
                elif Current_Time == "Midday":
                        $ K_Loc = "bg dangerroom"
                else:
                        $ K_Loc = "bg kitty"
                        
        #If Kitty has moved from where she started this action. . .   
        if K_Loc != LocTemp and "Kitty" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    #this is not applied if she was merely "nearby."
                    $ K_RecentActions.append("leaving") 
                elif K_Loc == bg_current: #If she's showed up
                    $ K_RecentActions.append("arriving")
        if "Kitty" in Nearby:
                $ Nearby.remove("Kitty") 
        return
#End Kitty's Schedule


label Kitty_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in K_Todo:
                $ K_PubeC -= 1
                if K_PubeC >= 1:
                        pass
                else:            
                        $ K_Pubes = 1
                        $ K_Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in K_Todo:               
                $ K_Pubes = 0
                $ K_Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in K_Todo:                
                $ K_Pierce = "ring"
                $ K_Todo.remove("ring")
        if "barbell" in K_Todo:
                $ K_Pierce = "barbell"
                $ K_Todo.remove("barbell")            
        return
 

# Emma's Outfit //////////////////////////////////////////////
label EmmaOutfit(E_OutfitTemp = E_Outfit, Spunk = 0, Undressed = 0, Changed = 1):   
        # E_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if E_OutfitTemp == 5: #this sets it to default if using AnyOutfit
                $ E_OutfitTemp = E_Outfit
        elif E_OutfitTemp == 6: #this sets it to default if using AnyOutfit
                $ E_OutfitTemp = E_OutfitDay
                
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
            #Skips theis check if it's a sleepover
            return
        
        if E_OutfitTemp != E_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Emma" in Party and E_OutfitTemp == E_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ E_OutfitTemp = E_Outfit
#        if E_Loc == "bg showerroom" and "Emma" not in Party and E_OutfitTemp != "nude":
#                #Automatically puts her in the towel while in the shower
#                $ E_OutfitTemp = "towel"                                  
        if E_Loc != "bg showerroom" or (E_OutfitTemp != "nude" and E_OutfitTemp != "towel"):
                #Dries her off
                $ E_Water = 0
                
        if E_Spunk:
                if "painted" not in E_DailyActions or "cleaned" not in E_DailyActions:        
                    $ del E_Spunk[:] 
                
        $ E_Upskirt = 0
        $ E_Uptop = 0
        $ E_PantiesDown = 0
        if E_OutfitTemp == "teacher":
                    if 0 in (E_Legs,E_Over,E_Chest):
                            $ Undressed = 1
                    elif E_Panties == 0 and "pantyless" not in E_DailyActions:                        
                            $ Undressed = 1   
                    $ E_Arms = 0
                    $ E_Legs = "pants"
                    $ E_Over = "jacket"
                    $ E_Chest = "corset"
                    $ E_Panties = "white panties"        
                    $ E_Neck = "choker"                 
                    $ E_Boots = 0
                    $ E_Hair = "wavy"
                    $ E_Hose = 0  
        elif E_OutfitTemp == "costume":
                    if 0 in (E_Legs,E_Chest):
                            $ Undressed = 1
                    elif E_Panties == 0 and "pantyless" not in E_DailyActions:                        
                            $ Undressed = 1   
                    $ E_Arms = 1
                    $ E_Legs = "pants"
                    $ E_Over = 0
                    $ E_Chest = "corset"
                    $ E_Panties = "white panties"        
                    $ E_Neck = "choker"                 
                    $ E_Boots = 0
                    $ E_Hair = "wavy"
                    $ E_Hose = 0     
        elif E_OutfitTemp == "towel":
                    if E_Over == 0:
                            $ Undressed = 2
                    $ E_Arms = 0
                    $ E_Legs = 0
                    $ E_Chest = 0
                    $ E_Over = "towel"
                    $ E_Panties = 0        
                    $ E_Hose = 0          
                    $ E_Neck = 0                   
                    $ E_Boots = 0
                    $ E_Hair = "wet" 
                    $ E_Shame = 35
        elif E_OutfitTemp == "nude":
                    $ E_Arms = 0
                    $ E_Legs = 0
                    $ E_Chest = 0
                    $ E_Over = 0
                    $ E_Panties = 0              
                    $ E_Neck = 0                    
                    $ E_Boots = 0
                    $ E_Hose = 0   
                    $ E_Shame = 50
        elif E_OutfitTemp == "custom1":
                    if not E_Legs and E_Custom[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom[6] and "pantyless" not in E_DailyActions:          
                            $ Undressed = 1
                    elif not E_Hose and E_Custom[9]:          
                            $ Undressed = 1
                    
                    $ E_Arms = E_Custom[1]
                    $ E_Legs = E_Custom[2]
                    $ E_Over = E_Custom[3]    
                    $ E_Neck = E_Custom[4]
                    $ E_Chest = E_Custom[5]
                    $ E_Panties = E_Custom[6]  
                    $ E_Boots = E_Custom[7] 
                    $ E_Hair = E_Custom[8] if E_Custom[8] else E_Hair 
                    $ E_Hose = E_Custom[9]                     
                    $ E_Shame = E_OutfitShame[3]
        elif E_OutfitTemp == "custom2":
                    if not E_Legs and E_Custom2[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom2[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom2[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom2[6] and "pantyless" not in E_DailyActions:          
                            $ Undressed = 1
                    elif not E_Hose and E_Custom2[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom2[1]
                    $ E_Legs = E_Custom2[2]
                    $ E_Over = E_Custom2[3]   
                    $ E_Neck = E_Custom2[4]
                    $ E_Chest = E_Custom2[5]
                    $ E_Panties = E_Custom2[6] 
                    $ E_Boots = E_Custom2[7] 
                    $ E_Hair = E_Custom2[8] if E_Custom2[8] else E_Hair
                    $ E_Hose = E_Custom2[9]                      
                    $ E_Shame = E_OutfitShame[5]
        elif E_OutfitTemp == "custom3":
                    if not E_Legs and E_Custom3[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Custom3[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Custom3[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Custom3[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_Custom3[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Custom3[1]
                    $ E_Legs = E_Custom3[2]
                    $ E_Over = E_Custom3[3]
                    $ E_Neck = E_Custom3[4]
                    $ E_Chest = E_Custom3[5]
                    $ E_Panties = E_Custom3[6] 
                    $ E_Boots = E_Custom3[7]  
                    $ E_Hair = E_Custom3[8] if E_Custom3[8] else E_Hair  
                    $ E_Hose = E_Custom3[9]                         
                    $ E_Shame = E_OutfitShame[6]
        elif E_OutfitTemp == "temporary":
                    if not E_Legs and E_TempClothes[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_TempClothes[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_TempClothes[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_TempClothes[6] and "pantyless" not in E_DailyActions:         
                            $ Undressed = 1
                    elif not E_Hose and E_TempClothes[9]:          
                            $ Undressed = 1
                            
                    $ E_Arms = E_TempClothes[1]
                    $ E_Legs = E_TempClothes[2]
                    $ E_Over = E_TempClothes[3]
                    $ E_Neck = E_TempClothes[4]
                    $ E_Chest = E_TempClothes[5]
                    $ E_Panties = E_TempClothes[6] 
                    $ E_Boots = E_TempClothes[7]  
                    $ E_Hair = E_TempClothes[8] if E_TempClothes[8] else E_Hair  
                    $ E_Hose = E_TempClothes[9]                         
                    $ E_Shame = E_OutfitShame[8]
        elif E_OutfitTemp == "sleep":  
                    if not E_Legs and E_Sleepwear[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Sleepwear[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Sleepwear[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Sleepwear[6] and "pantyless" not in E_DailyActions:        
                            $ Undressed = 1
                    elif not E_Hose and E_Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Sleepwear[1] #0
                    $ E_Legs = E_Sleepwear[2] #shorts
                    $ E_Over = E_Sleepwear[3] #nighty
                    $ E_Neck = E_Sleepwear[4] #0
                    $ E_Chest = E_Sleepwear[5] #corset
                    $ E_Panties = E_Sleepwear[6] #"white panties"
                    $ E_Boots = E_Sleepwear[7] 
                    $ E_Hair = E_Sleepwear[8] if E_Sleepwear[8] else E_Hair 
                    $ E_Hose = E_Sleepwear[9] #0  
                    $ E_Shame = E_OutfitShame[4]                    
        elif E_OutfitTemp == "gym":
                    if not E_Legs and E_Gym[2]:            
                            $ Undressed = 1
                    elif not E_Over and E_Gym[3]:          
                            $ Undressed = 1
                    elif not E_Chest and E_Gym[5]:          
                            $ Undressed = 1
                    elif not E_Panties and E_Gym[6] and "pantyless" not in E_DailyActions:        
                            $ Undressed = 1
                    elif not E_Hose and E_Gym[9]:          
                            $ Undressed = 1
                        
                    $ E_Arms = E_Gym[1]
                    $ E_Legs = E_Gym[2]
                    $ E_Over = E_Gym[3] 
                    $ E_Neck = E_Gym[4]
                    $ E_Chest = E_Gym[5]
                    $ E_Panties = E_Gym[6]  
                    $ E_Boots = E_Gym[7]  
                    $ E_Hair = E_Gym[8] if E_Gym[8] else E_Hair 
                    $ E_Hose = E_Gym[9]     
                    $ E_Shame = E_OutfitShame[7]   
        elif E_OutfitTemp == "swimwear":
                    if not E_Swim[0]:
                            if "bikini top" not in E_Inventory or "bikini bottoms" not in E_Inventory:
                                #if she doesn't own her swimsuit components. . .
                                if not CheckWord("Emma","Daily","swim"):
                                        ch_e "I really don't own the proper attire. . ."
                                return
                            else:
                                $ E_Swim[0] = 1
                                
                    if not E_Legs and E_Swim[2]:            
                        $ Undressed = 1
                    elif not E_Over and E_Swim[3]:          
                        $ Undressed = 1
                    elif not E_Chest and E_Swim[5]:          
                        $ Undressed = 1
                    elif not E_Panties and E_Swim[6]:# and "pantyless" not in E_DailyActions:          
                        $ Undressed = 1
                    elif not E_Hose and E_Swim[9]:          
                        $ Undressed = 1
                        
                    $ E_Arms = E_Swim[1]
                    $ E_Legs = E_Swim[2]
                    $ E_Over = E_Swim[3]
                    $ E_Neck = E_Swim[4] 
                    $ E_Chest = E_Swim[5]
                    $ E_Panties = E_Swim[6]
            #        $ E_Pubes = E_Swim[7]
                    $ E_Hair = E_Swim[8] if E_Swim[8] else E_Hair
                    $ E_Hose = E_Swim[9]        
                    $ E_Shame = E_OutfitShame[6]
                
        if E_Panties and "pantyless" in E_DailyActions:       
                # This checks the pantyless state from flirting 
                if E_OutfitTemp != "sleep" and E_OutfitTemp != "gym":
                        if E_Legs == "pants" or HoseNum("Emma") >= 10:
                            $ E_Shame -= 5    
                        elif E_Legs:
                            $ E_Shame -= 10  
                        elif E_Panties == "white panties":
                            $ E_Shame -= 20  
                        elif E_Panties == "lace panties":
                            $ E_Shame -= 25             
                        else:
                            $ E_Shame -= 23  
                        
                        $ E_Panties = 0        
                        $ E_Shame = 0 if E_Shame < 0 else E_Shame
                    
        if not Changed and E_OutfitTemp == E_Outfit and E_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."  
        return
#End Emma's Outfits
      
label Emma_Schedule(Clothes = 1, Location = 1, LocTemp = E_Loc): 
        #Emma's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in E_History or ("Emma" in Party and Clothes != 2): 
                #if she's in a party, never mind
                return  
        if Clothes != 2 and "sleepover" in E_Traits and Current_Time == "morning":
                #she slept over, so just forget this for now  
                return              
        
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #Pick clothes for the day
                $ E_OutfitDay = 0
                if E_Break[0]:
                        pass #she won't pick clothes if she's mad at you
                elif E_Schedule[Weekday] == 1:
                        $ E_OutfitDay = "teacher"
                elif E_Schedule[Weekday] == 2:
                        $ E_OutfitDay = "costume"
                elif E_Schedule[Weekday] == 3 and E_Custom[0]:
                        $ E_OutfitDay = "custom1"
                elif E_Schedule[Weekday] == 4:
                        $ E_OutfitDay = "gym"
                elif E_Schedule[Weekday] == 5 and E_Custom2[0]:
                        $ E_OutfitDay = "custom2"
                elif E_Schedule[Weekday] == 6 and E_Custom3[0]: 
                        $ E_OutfitDay = "custom3"
                if not E_OutfitDay: 
                        $ Options = ["teacher"]
                        $ Options.append("costume") if ApprovalCheck("Emma", 1000) else Options
                        if not E_Break[0]:
                                $ Options.append("custom1") if E_Custom[0] == 2 else Options
                                $ Options.append("custom2") if E_Custom2[0] == 2 else Options
                                $ Options.append("custom3") if E_Custom3[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ E_OutfitDay = Options[0]
                        $ del Options[:]  
                $ E_Outfit = E_OutfitDay 
        #End clothing portion
        
        #Location portion   
        if "Emma" in Party or E_Loc == "hold" or not Location:
                pass          
                
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ E_Loc = "bg teacher"
                elif Current_Time == "Midday": 
                        $ E_Loc = "bg teacher"
                elif Current_Time == "Evening": 
                        $ E_Loc = "bg classroom"
                else:
                        $ E_Loc = "bg emma"
        elif Weekday == 1 or Weekday == 3:
        #TuThu      
                if Current_Time == "Morning":
                        $ E_Loc = "bg teacher"
                elif Current_Time == "Midday":
                        $ E_Loc = "bg teacher"
                elif Current_Time == "Evening":
                        $ E_Loc = "bg dangerroom"
                else:
                        $ E_Loc = "bg emma"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ E_Loc = "bg pool"
                elif Current_Time == "Midday":
                        $ E_Loc = "bg pool"
                else:
                        $ E_Loc = "bg emma"
        
        #If Emma has moved from where she started this action. . .   
        if E_Loc != LocTemp and "Emma" not in Party:   
                if LocTemp == bg_current: #If she was where you were
                    $ E_RecentActions.append("leaving") 
                elif E_Loc == bg_current: #If she's showed up
                    $ E_RecentActions.append("arriving")         
        if "Emma" in Nearby:
                $ Nearby.remove("Emma")
        return
#End Emma's Schedule


label Emma_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out nightly
        if "pubes" in E_Todo:    
                $ E_Pubes = 1
                $ E_Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in E_Todo:               
                $ E_Pubes = 0
                $ E_Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in E_Todo:                
                $ E_Pierce = "ring"
                $ E_Todo.remove("ring")
        if "barbell" in E_Todo:
                $ E_Pierce = "barbell"
                $ E_Todo.remove("barbell")            
        return
        

# Laura's Outfit //////////////////////////////////////////////
label LauraOutfit(L_OutfitTemp = L_Outfit, Spunk = 0, Undressed = 0, Changed = 1):   
        # L_OutfitTemp is the chosen new outfit, Spunk removes sperm on her, Undressed determines whether she is under dressed  
        
        if L_OutfitTemp == 5: #this sets it to default if using AnyOutfit
                $ L_OutfitTemp = L_Outfit
        elif L_OutfitTemp == 6: #this sets it to default if using AnyOutfit
                $ L_OutfitTemp = L_OutfitDay
        
        if renpy.showing("NightMask", layer='nightmask') and Current_Time == "Morning":
                #Skips theis check if it's a sleepover
                return
        
        if L_OutfitTemp != L_Outfit:
                #if her new outfit is not what she was wearing before,
                #don't flag the undressed mechanic
                $ Changed = 1    
        if "Laura" in Party and L_OutfitTemp == L_OutfitDay:
                #this ignores her daily outfit if she's in a party
                $ L_OutfitTemp = L_Outfit
#        if L_Loc == "bg showerroom" and "Laura" not in Party and L_OutfitTemp != "nude":
#                #Automatically puts her in the towel while in the shower
#                $ L_OutfitTemp = "towel"                                  
        elif L_Loc != "bg showerroom" or (L_OutfitTemp != "nude" and L_OutfitTemp != "towel"):
                #Dries her off
                $ L_Water = 0
                
        if L_Spunk:
                if "painted" not in L_DailyActions or "cleaned" not in L_DailyActions:        
                    $ del L_Spunk[:] 
                
        $ L_Upskirt = 0
        $ L_Uptop = 0
        $ L_PantiesDown = 0
        if L_OutfitTemp == "mission":
                    if 0 in (L_Legs,L_Over,L_Chest):
                            $ Undressed = 1
                    elif L_Panties == 0 and "pantyless" not in L_DailyActions:                        
                            $ Undressed = 1   
                    $ L_Arms = "wrists"
                    $ L_Legs = "leather pants"
                    $ L_Over = 0
                    $ L_Chest = "leather bra"
                    $ L_Panties = "leather panties"        
                    $ L_Neck = "leash choker"                 
                    $ L_Boots = 0
                    $ L_Hair = "long"
                    $ L_Hose = 0  
                    $ L_Shame = 0
        elif L_OutfitTemp == "streets":
                    if 0 in (L_Legs,L_Chest):
                            $ Undressed = 1
                    elif L_Panties == 0 and "pantyless" not in L_DailyActions:                        
                            $ Undressed = 1   
                    $ L_Arms = 0
                    $ L_Legs = "skirt"
                    $ L_Over = "jacket"
                    $ L_Chest = "corset" if ("corset" in L_Inventory and L_Inbt >= 800) else "leather bra"
                    $ L_Panties = "lace panties" if "lace panties" in L_Inventory else "black panties"
                    $ L_Neck = 0                 
                    $ L_Boots = 0
                    $ L_Hair = "long"
                    $ L_Hose = "stockings and garterbelt" if ("lace panties" in L_Inventory and L_Inbt >= 800) else "stockings"      
                    $ L_Shame = 0
        elif L_OutfitTemp == "towel":
                    if L_Over == 0:
                            $ Undressed = 2
                    $ L_Arms = 0
                    $ L_Legs = 0
                    $ L_Chest = 0
                    $ L_Over = "towel"
                    $ L_Panties = 0        
                    $ L_Hose = 0          
                    $ L_Neck = 0                   
                    $ L_Boots = 0
                    $ L_Hair = "wet" 
                    $ L_Shame = 35
        elif L_OutfitTemp == "nude":
                    $ L_Arms = 0
                    $ L_Legs = 0
                    $ L_Chest = 0
                    $ L_Over = 0
                    $ L_Panties = 0              
                    $ L_Neck = 0                    
                    $ L_Boots = 0
                    $ L_Hose = 0   
                    $ L_Shame = 50
        elif L_OutfitTemp == "custom1":
                    if not L_Legs and L_Custom[2]:            
                            $ Undressed = 1
                    elif not L_Over and L_Custom[3]:          
                            $ Undressed = 1
                    elif not L_Chest and L_Custom[5]:          
                            $ Undressed = 1
                    elif not L_Panties and L_Custom[6] and "pantyless" not in L_DailyActions:          
                            $ Undressed = 1
                    elif not L_Hose and L_Custom[9]:          
                            $ Undressed = 1
                    
                    $ L_Arms = L_Custom[1]
                    $ L_Legs = L_Custom[2]
                    $ L_Over = L_Custom[3]    
                    $ L_Neck = L_Custom[4]
                    $ L_Chest = L_Custom[5]
                    $ L_Panties = L_Custom[6]  
                    $ L_Boots = L_Custom[7] 
                    $ L_Hair = L_Custom[8] if L_Custom[8] else L_Hair 
                    $ L_Hose = L_Custom[9]                     
                    $ L_Shame = L_OutfitShame[3]
        elif L_OutfitTemp == "custom2":
                    if not L_Legs and L_Custom2[2]:            
                            $ Undressed = 1
                    elif not L_Over and L_Custom2[3]:          
                            $ Undressed = 1
                    elif not L_Chest and L_Custom2[5]:          
                            $ Undressed = 1
                    elif not L_Panties and L_Custom2[6] and "pantyless" not in L_DailyActions:          
                            $ Undressed = 1
                    elif not L_Hose and L_Custom2[9]:          
                            $ Undressed = 1
                        
                    $ L_Arms = L_Custom2[1]
                    $ L_Legs = L_Custom2[2]
                    $ L_Over = L_Custom2[3]   
                    $ L_Neck = L_Custom2[4]
                    $ L_Chest = L_Custom2[5]
                    $ L_Panties = L_Custom2[6] 
                    $ L_Boots = L_Custom2[7] 
                    $ L_Hair = L_Custom2[8] if L_Custom2[8] else L_Hair
                    $ L_Hose = L_Custom2[9]                      
                    $ L_Shame = L_OutfitShame[5]
        elif L_OutfitTemp == "custom3":
                    if not L_Legs and L_Custom3[2]:            
                            $ Undressed = 1
                    elif not L_Over and L_Custom3[3]:          
                            $ Undressed = 1
                    elif not L_Chest and L_Custom3[5]:          
                            $ Undressed = 1
                    elif not L_Panties and L_Custom3[6] and "pantyless" not in L_DailyActions:         
                            $ Undressed = 1
                    elif not L_Hose and L_Custom3[9]:          
                            $ Undressed = 1
                        
                    $ L_Arms = L_Custom3[1]
                    $ L_Legs = L_Custom3[2]
                    $ L_Over = L_Custom3[3]
                    $ L_Neck = L_Custom3[4]
                    $ L_Chest = L_Custom3[5]
                    $ L_Panties = L_Custom3[6] 
                    $ L_Boots = L_Custom3[7]  
                    $ L_Hair = L_Custom3[8] if L_Custom3[8] else L_Hair  
                    $ L_Hose = L_Custom3[9]                         
                    $ L_Shame = L_OutfitShame[6]
        elif L_OutfitTemp == "temporary":
                    if not L_Legs and L_TempClothes[2]:            
                            $ Undressed = 1
                    elif not L_Over and L_TempClothes[3]:          
                            $ Undressed = 1
                    elif not L_Chest and L_TempClothes[5]:          
                            $ Undressed = 1
                    elif not L_Panties and L_TempClothes[6] and "pantyless" not in L_DailyActions:         
                            $ Undressed = 1
                    elif not L_Hose and L_TempClothes[9]:          
                            $ Undressed = 1
                            
                    $ L_Arms = L_TempClothes[1]
                    $ L_Legs = L_TempClothes[2]
                    $ L_Over = L_TempClothes[3]
                    $ L_Neck = L_TempClothes[4]
                    $ L_Chest = L_TempClothes[5]
                    $ L_Panties = L_TempClothes[6] 
                    $ L_Boots = L_TempClothes[7]  
                    $ L_Hair = L_TempClothes[8] if L_TempClothes[8] else L_Hair  
                    $ L_Hose = L_TempClothes[9]                         
                    $ L_Shame = L_OutfitShame[8]
        elif L_OutfitTemp == "sleep":  
                    if not L_Legs and L_Sleepwear[2]:            
                            $ Undressed = 1
                    elif not L_Over and L_Sleepwear[3]:          
                            $ Undressed = 1
                    elif not L_Chest and L_Sleepwear[5]:          
                            $ Undressed = 1
                    elif not L_Panties and L_Sleepwear[6] and "pantyless" not in L_DailyActions:        
                            $ Undressed = 1
                    elif not L_Hose and L_Sleepwear[9]:          
                            $ Undressed = 1
                        
                    $ L_Arms = L_Sleepwear[1] #0
                    $ L_Legs = L_Sleepwear[2] #shorts
                    $ L_Over = L_Sleepwear[3] #nighty
                    $ L_Neck = L_Sleepwear[4] #0
                    $ L_Chest = L_Sleepwear[5] #corset
                    $ L_Panties = L_Sleepwear[6] #"white panties"
                    $ L_Boots = L_Sleepwear[7] 
                    $ L_Hair = L_Sleepwear[8] if L_Sleepwear[8] else L_Hair 
                    $ L_Hose = L_Sleepwear[9] #0  
                    
                    $ L_Shame = L_OutfitShame[4]                    
        elif L_OutfitTemp == "gym":
                    if not L_Legs and L_Gym[2]:            
                            $ Undressed = 1
                    elif not L_Over and L_Gym[3]:          
                            $ Undressed = 1
                    elif not L_Chest and L_Gym[5]:          
                            $ Undressed = 1
                    elif not L_Panties and L_Gym[6] and "pantyless" not in L_DailyActions:        
                            $ Undressed = 1
                    elif not L_Hose and L_Gym[9]:          
                            $ Undressed = 1
                        
                    $ L_Arms = L_Gym[1]
                    $ L_Legs = L_Gym[2]
                    $ L_Over = L_Gym[3] 
                    $ L_Neck = L_Gym[4]
                    $ L_Chest = L_Gym[5]
                    $ L_Panties = L_Gym[6]  
                    $ L_Boots = L_Gym[7]  
                    $ L_Hair = L_Gym[8] if L_Gym[8] else L_Hair 
                    $ L_Hose = L_Gym[9]     
                    $ L_Shame = L_OutfitShame[7]   
        elif L_OutfitTemp == "swimwear":
                    if not L_Swim[0]:
                            if "bikini top" not in L_Inventory or "bikini bottoms" not in L_Inventory:
                                #if she doesn't own her swimsuit components. . .
                                if not CheckWord("Laura","Daily","swim"):
                                        ch_l "Don't have a suit. . ."
                                return
                            else:
                                $ L_Swim[0] = 1
                    if not L_Legs and L_Swim[2]:            
                        $ Undressed = 1
                    elif not L_Over and L_Swim[3]:          
                        $ Undressed = 1
                    elif not L_Chest and L_Swim[5]:          
                        $ Undressed = 1
                    elif not L_Panties and L_Swim[6]:# and "pantyless" not in L_DailyActions:          
                        $ Undressed = 1
                    elif not L_Hose and L_Swim[9]:          
                        $ Undressed = 1
                        
                    $ L_Arms = L_Swim[1]
                    $ L_Legs = L_Swim[2]
                    $ L_Over = L_Swim[3]
                    $ L_Neck = L_Swim[4] 
                    $ L_Chest = L_Swim[5]
                    $ L_Panties = L_Swim[6]
            #        $ L_Pubes = L_Swim[7]
                    $ L_Hair = L_Swim[8] if L_Swim[8] else L_Hair
                    $ L_Hose = L_Swim[9]        
                    $ L_Shame = L_OutfitShame[6]
                
        if L_Panties and "pantyless" in L_DailyActions:       
                # This checks the pantyless state from flirting 
                if L_OutfitTemp != "sleep" and L_OutfitTemp != "gym":
                        if L_Legs == "leather pants" or HoseNum("Laura") >= 10:
                            $ L_Shame -= 5    
                        elif L_Legs:
                            $ L_Shame -= 10  
                        elif L_Panties == "leather panties":
                            $ L_Shame -= 20   
                        elif L_Panties == "lace panties":
                            $ L_Shame -= 25            
                        else:
                            $ L_Shame -= 23  
                        
                        $ L_Panties = 0        
                        $ L_Shame = 0 if L_Shame < 0 else L_Shame
                    
        if not Changed and L_OutfitTemp == L_Outfit and L_Loc == bg_current:
                #If she was partially dressed then it says she gets dressed
                if Undressed == 2:
                        "She throws on a towel."
                elif Undressed:
                        "She throws her clothes back on."  
        return
#End Laura's Outfits
      
label Laura_Schedule(Clothes = 1, Location = 1, LocTemp = L_Loc): 
        #Laura's natural movements   
        # If not Clothes, don't bother with her outfit in the scheduel
        # Clothes 2 is ordered to change regardless of time of day
        # If not Location, don't bother with the location portion of the schedule
        
        if "met" not in L_History or ("Laura" in Party and Clothes != 2): 
                #if she's in a party, never mind
                return  
        if Clothes != 2 and "sleepover" in L_Traits and Current_Time == "morning":
                #she slept over, so just forget this for now  
                return             
                
        if (Current_Time == "Morning" and Clothes and Round >= 90) or Clothes == 2:
                #Pick clothes for the day
                $ L_OutfitDay = 0
                if L_Break[0]:
                    pass #she won't pick clothes if she's mad at you
                elif L_Schedule[Weekday] == 1:
                        $ L_OutfitDay = "mission"
                elif L_Schedule[Weekday] == 2:
                        $ L_OutfitDay = "streets"               # fix, make this second costume
                elif L_Schedule[Weekday] == 3 and L_Custom[0]:
                        $ L_OutfitDay = "custom1"
                elif L_Schedule[Weekday] == 4:
                        $ L_OutfitDay = "gym"
                elif L_Schedule[Weekday] == 5 and L_Custom2[0]:
                        $ L_OutfitDay = "custom2"
                elif L_Schedule[Weekday] == 6 and L_Custom3[0]: 
                        $ L_OutfitDay = "custom3"
                if not L_OutfitDay:
                        # random
                        $ Options = ["mission"]
                        $ Options.append("streets") if ApprovalCheck("Laura", 500, "I") else Options
                        if not L_Break[0]:
                                $ Options.append("custom1") if L_Custom[0] == 2 else Options
                                $ Options.append("custom2") if L_Custom2[0] == 2 else Options
                                $ Options.append("custom3") if L_Custom3[0] == 2 else Options
                        $ renpy.random.shuffle(Options) 
                        $ L_OutfitDay = Options[0]
                        $ del Options[:]  
                $ L_Outfit = L_OutfitDay 
        #End clothing portion
        
        #Location portion  
        if "Laura" in Party or L_Loc == "hold" or not Location:
                pass    
        elif Weekday == 0 or Weekday == 2 or Weekday == 4:
        #MoWeFr   
                if Current_Time == "Morning":
                        $ L_Loc = "bg pool"
                elif Current_Time == "Midday": 
                        $ L_Loc = "bg classroom"
                elif Current_Time == "Evening":
                        $ L_Loc = "bg dangerroom"
                else:
                        $ L_Loc = "bg laura"
        elif Weekday == 1 or Weekday == 3:
        #TuThu      
                if Current_Time == "Morning":
                        $ L_Loc = "bg dangerroom"
                elif Current_Time == "Midday":
                        $ L_Loc = "bg classroom"
                else:
                        $ L_Loc = "bg laura"
        else:
        #Weekend                               
                if Current_Time == "Morning":
                        $ L_Loc = "bg pool"
                elif Current_Time == "Midday":
                        $ L_Loc = "bg laura"
                elif Current_Time == "Evening":
                        $ L_Loc = "bg dangerroom"
                else:
                        $ L_Loc = "bg laura"
        
        #If Laura has moved from where she started this action. . .   
        if L_Loc != LocTemp and "Laura" not in Party:    
                if LocTemp == bg_current: #If she was where you were
                    $ L_RecentActions.append("leaving") 
                elif L_Loc == bg_current: #If she's showed up
                    $ L_RecentActions.append("arriving") 
        if "Laura" in Nearby:
                $ Nearby.remove("Laura")
        return
#End Laura's Schedule


label Laura_Todo:                       
        #Actions checked each night  
        #causes her to grow her pubes out over a week
        if "pubes" in L_Todo:
                $ L_PubeC -= 1
                if L_PubeC >= 1:
                        pass
                else:            
                        $ L_Pubes = 1
                        $ L_Todo.remove("pubes") 
                        
        #causes her to wax her pubes
        if "shave" in L_Todo:               
                $ L_Pubes = 0
                $ L_Todo.remove("shave")
                
        #causes her to put in piercings     
        if "ring" in L_Todo:                
                $ L_Pierce = "ring"
                $ L_Todo.remove("ring")
        if "barbell" in L_Todo:
                $ L_Pierce = "barbell"
                $ L_Todo.remove("barbell")            
        return
# Xavier Faces ///////////////////////////////

label XavierFace (Face = X_Emote):
        if Face == "psychic":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "concentrate"
                $ X_Psychic = 1
        if Face == "hypno":
                $ X_Mouth = "neutral"
                $ X_Brows = "neutral"
                $ X_Eyes = "hypno"
        if Face == "shocked":
                $ X_Mouth = "neutral"
                $ X_Brows = "shocked"
                $ X_Eyes = "shocked"
                $ X_Psychic = 0
        if Face == "happy":
                $ X_Mouth = "happy"
                $ X_Brows = "happy"
                $ X_Eyes = "happy"        
                $ X_Psychic = 0
        if Face == "angry":
                $ X_Mouth = "concentrate"
                $ X_Brows = "concentrate"
                $ X_Eyes = "happy"
                $ X_Psychic = 0
        return
        
# Wait/Sleep Cycle //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #Wait    
    
    
    
    
    
# Wait/Sleep Cycle //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #Wait
label Wait (Outfit = 1, Lights = 1):
    # If Outfit is 1, it changes her clothes to the scheduled default, otherwise it does not. 
    # If Lights is 1, it removes the blackout screen, otherwise it does not. 
    show blackscreen onlayer black 
    
    $ R_Addict += R_Addictionrate 
    $ K_Addict += K_Addictionrate
    $ E_Addict += E_Addictionrate
    $ L_Addict += L_Addictionrate
    call Checkout(1)
    $ P_XP = 3330 if P_XP > 3330 else P_XP
    $ R_XP = 3330 if R_XP > 3330 else R_XP
    $ K_XP = 3330 if K_XP > 3330 else K_XP
    $ E_XP = 3330 if E_XP > 3330 else E_XP
    $ L_XP = 3330 if L_XP > 3330 else L_XP
    
        
                    
    if Time_Count < 3:  #not sleep time                                          
                $ Time_Count += 1
                $ R_Action += 1  
                $ K_Action += 1 
                $ E_Action += 1   
                $ L_Action += 1   
                
    # Things that happen when you sleep   
    else:                                                          
                $ del Party[:]
                
                #Setting the time/date
                $ Time_Count = 0   
                $ Day += 1
                if Weekday < 6:
                    $ Weekday += 1
                else:
                    $ Weekday = 0
                $ DayofWeek = Week[Weekday]
                
                if PunishmentX: #Event[3]:   
                        #If you're under punishment
                        $ P_Cash += int(P_Income / 2)
                        if PunishmentX == 1:
                            "Your punishment from Xavier has expired."
                        $ PunishmentX -= 1
                else:
                        #otherwise, you make money
                        $ P_Cash += P_Income             
                
                
        # Things about you when you sleep:
                $ P_Semen = P_Semen_Max    
                $ P_Spunk = 0      
                $ P_Rep = 0 if P_Rep < 0 else P_Rep 
                $ P_Rep += 10 if P_Rep < 800 else 0
                $ P_Rep = 1000 if P_Rep > 1000 else P_Rep     
                
                #Clearing colognes
                if "mandrill" in P_Traits:  
                        $ P_Traits.remove("mandrill")
                if "purple" in P_Traits:
                        $ P_Traits.remove("purple")  
                if "corruption" in P_Traits:
                        $ P_Traits.remove("corruption")  
                
                call Favorite_Actions # Sets the girl's favorite activities once per day
                        
                        
        # Things about Rogue when you sleep:  
                if R_Loc == "hold":
                        $ R_Loc = "bg rogue"      
                if R_Todo:
                        call Rogue_Todo
                $ R_Outfit = "sleepwear"
                call RogueOutfit(Changed=1)
                $ R_Addict += R_Addictionrate
                $ R_Addict -= (3*R_Resistance)
                
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ R_Addictionrate -= 2
                        $ R_Addict -= 5
                elif R_Addictionrate:
                        $ R_Addictionrate -= R_Resistance
                $ R_ForcedCount -= 1 if R_ForcedCount > 0 else 0
                if R_ForcedCount > 0:
                        $ R_ForcedCount -= 1 if ApprovalCheck("Rogue", 1000, "LO") else 0 
                $ R_Action = R_MaxAction   
                
                $ R_Rep = 0 if R_Rep < 0 else R_Rep 
                $ R_Rep += 10 if R_Rep < 800 else 0
                $ R_Rep = 1000 if R_Rep > 1000 else R_Rep 
                $ R_Lust -= 5 if R_Lust >= 50 else 0
                
                if R_SEXP >= 15: #raises thirst if you've had sex before
                        if R_SEXP >= 50:
                            $ R_Thirst += 8 if R_Thirst <= 70 else 4
                        elif R_SEXP >= 25:
                            $ R_Thirst += 5 if R_Thirst <= 60 else 2
                        else:
                            $ R_Thirst += 3 if R_Thirst <= 50 else 1
                            
                        $ R_Thirst -= 5 if R_Break[0] else 0
                        $ R_Thirst += 1 if R_Lust >= 50 else 0  
                
                if "gonnafap" in R_DailyActions and Zero_Loc("Rogue") != bg_current:
                        #if it's morning and she wanted to fap yesterday. . .
                        $ R_Lust = 25
                        $ R_Thirst -= int(R_Thirst/2) if R_Thirst >= 50 else int(R_Thirst/4) 
                elif "wannafap" in R_DailyActions:
                        #if it's morning and she didn't get to fap yesterday. . .
                        $ R_Thirst += 10 if R_Thirst <= 50 else 5  
                        
                $ R_Break[0] -= 1 if R_Break[0] > 0 else 0
                
                if "painted" not in R_DailyActions or "cleaned" not in R_DailyActions:   
                        $ del R_Spunk[:]  
                    
                if "lover" in R_Petnames and R_Love > 800:
                        $ R_Love += 10
                if "master" in R_Petnames and R_Obed > 600:
                        $ R_Obed += 10
                if "fuck buddy" in R_Petnames:
                        $ R_Inbt += 10   
                    
        # Things about Kitty when you sleep:
                if K_Loc == "hold":
                        $ K_Loc = "bg kitty"  
                if K_Todo:
                        call Kitty_Todo
                
                $ K_Outfit = "sleepwear"
                call KittyOutfit(Changed=1)
                if "addict kitty" in P_Traits:
                        $ K_Addict += K_Addictionrate
                        $ K_Addict -= (3*K_Resistance)
                else:
                        $ K_Addict = 0
                        $ K_Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ K_Addictionrate -= 2
                        $ K_Addict -= 5
                elif K_Addictionrate:
                        $ K_Addictionrate -= K_Resistance
                    
                $ K_ForcedCount -= 1 if K_ForcedCount > 0 else 0
                if K_ForcedCount > 0:
                        $ K_ForcedCount -= 1 if ApprovalCheck("Kitty", 1000, "LO") else 0 
                $ K_Action = K_MaxAction    
                
                $ K_Rep = 0 if K_Rep < 0 else K_Rep 
                $ K_Rep += 10 if K_Rep < 800 else 0
                $ K_Rep = 1000 if K_Rep > 1000 else K_Rep 
                $ K_Lust -= 5 if K_Lust >= 50 else 0
                
                if K_SEXP >= 15: #raises thirst if you've had sex before
                        if K_SEXP >= 50:
                            $ K_Thirst += 8 if K_Thirst <= 70 else 4
                        elif K_SEXP >= 25:
                            $ K_Thirst += 5 if K_Thirst <= 60 else 2
                        else:
                            $ K_Thirst += 3 if K_Thirst <= 50 else 1
                        $ K_Thirst -= 5 if K_Break[0] else 0
                        $ K_Thirst += 1 if K_Lust >= 50 else 0  
                
                if "gonnafap" in K_DailyActions and Zero_Loc("Kitty") != bg_current:
                        #if it's morning and she wanted to fap yesterday. . .
                        $ K_Lust = 25
                        $ K_Thirst -= int(K_Thirst/2) if K_Thirst >= 50 else int(K_Thirst/4) 
                elif "wannafap" in K_DailyActions:
                        #if it's morning and she didn't get to fap yesterday. . .
                        $ K_Thirst += 10 if K_Thirst <= 50 else 5  
                        
                $ K_Break[0] -= 1 if K_Break[0] > 0 else 0
                
                if "painted" not in K_DailyActions or "cleaned" not in K_DailyActions:   
                        $ del K_Spunk[:]  
                
                if "lover" in K_Petnames and K_Love > 800:
                        $ K_Love += 10
                if "master" in K_Petnames and K_Obed > 600:
                        $ K_Obed += 10
                if "fuck buddy" in K_Petnames:
                        $ K_Inbt += 10   
                        
        # Things about Emma when you sleep:
                if E_Loc == "hold":
                        $ E_Loc = "bg emma"  
                if E_Todo:
                        call Emma_Todo
                
                $ E_Outfit = "sleepwear"
                call EmmaOutfit(Changed=1)
                if "addict emma" in P_Traits:
                        $ E_Addict += E_Addictionrate
                        $ E_Addict -= (3*E_Resistance)
                else:
                        $ E_Addict = 0
                        $ E_Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ E_Addictionrate -= 2
                        $ E_Addict -= 5
                elif E_Addictionrate:
                        $ E_Addictionrate -= E_Resistance
                    
                $ E_ForcedCount -= 1 if E_ForcedCount > 0 else 0
                if E_ForcedCount > 0:
                        $ E_ForcedCount -= 1 if ApprovalCheck("Emma", 1000, "LO") else 0 
                $ E_Action = E_MaxAction    
                
                $ E_Rep = 0 if E_Rep < 0 else E_Rep 
                $ E_Rep += 10 if E_Rep < 800 else 0
                $ E_Rep = 1000 if E_Rep > 1000 else E_Rep 
                $ E_Lust -= 5 if E_Lust >= 50 else 0
                
                if E_SEXP >= 15: #raises thirst if you've had sex before
                        if E_SEXP >= 50:
                            $ E_Thirst += 8 if E_Thirst <= 70 else 4
                        elif E_SEXP >= 25:
                            $ E_Thirst += 5 if E_Thirst <= 60 else 2
                        else:
                            $ E_Thirst += 3 if E_Thirst <= 50 else 1
                        $ E_Thirst -= 5 if E_Break[0] else 0
                        $ E_Thirst += 1 if E_Lust >= 50 else 0  
                  
                if "gonnafap" in E_DailyActions and Zero_Loc("Emma") != bg_current:
                        #if it's morning and she wanted to fap yesterday. . .
                        $ E_Lust = 25
                        $ E_Thirst -= int(E_Thirst/2) if E_Thirst >= 50 else int(E_Thirst/4) 
                elif "wannafap" in E_DailyActions:
                        #if it's morning and she didn't get to fap yesterday. . .
                        $ E_Thirst += 10 if E_Thirst <= 50 else 5  
                        
                $ E_Break[0] -= 1 if E_Break[0] > 0 else 0
                
                if "painted" not in E_DailyActions or "cleaned" not in E_DailyActions:   
                        $ del E_Spunk[:]  
                
                if "lover" in E_Petnames and E_Love > 800:
                        $ E_Love += 10
                if "master" in E_Petnames and E_Obed > 600:
                        $ E_Obed += 10
                if "fuck buddy" in E_Petnames:
                        $ E_Inbt += 10       
                                
        # Things about Laura when you sleep:
                if L_Loc == "hold":
                        $ L_Loc = "bg laura"  
                if L_Todo:
                        call Laura_Todo
                
                $ L_Outfit = "sleepwear"
                call LauraOutfit(Changed=1)
                if "addict emma" in P_Traits:
                        $ L_Addict += L_Addictionrate
                        $ L_Addict -= (3*L_Resistance)
                else:
                        $ L_Addict = 0
                        $ L_Addictionrate = 0
        
                if "addictive" in P_Traits:  
                        pass
                elif "nonaddictive" in P_Traits:        
                        $ L_Addictionrate -= 2
                        $ L_Addict -= 5
                elif L_Addictionrate:
                        $ L_Addictionrate -= L_Resistance
                    
                $ L_ForcedCount -= 1 if L_ForcedCount > 0 else 0
                if L_ForcedCount > 0:
                        $ L_ForcedCount -= 1 if ApprovalCheck("Laura", 1000, "LO") else 0 
                $ L_Action = L_MaxAction    
                
                $ L_Rep = 0 if L_Rep < 0 else L_Rep 
                $ L_Rep += 10 if L_Rep < 800 else 0
                $ L_Rep = 1000 if L_Rep > 1000 else L_Rep 
                $ L_Lust -= 5 if L_Lust >= 50 else 0
                
                if L_SEXP >= 15: #raises thirst if you've had sex before
                        if L_SEXP >= 50:
                            $ L_Thirst += 8 if L_Thirst <= 70 else 4
                        elif L_SEXP >= 25:
                            $ L_Thirst += 5 if L_Thirst <= 60 else 2
                        else:
                            $ L_Thirst += 3 if L_Thirst <= 50 else 1
                        $ L_Thirst -= 5 if L_Break[0] else 0
                        $ L_Thirst += 1 if L_Lust >= 50 else 0  
                    
                if "gonnafap" in L_DailyActions and Zero_Loc("Laura") != bg_current:
                        #if it's morning and she wanted to fap yesterday. . .
                        $ L_Lust = 25
                        $ L_Thirst -= int(L_Thirst/2) if L_Thirst >= 50 else int(L_Thirst/4) 
                elif "wannafap" in L_DailyActions:
                        #if it's morning and she didn't get to fap yesterday. . .
                        $ L_Thirst += 10 if L_Thirst <= 50 else 5  
                        
                $ L_Break[0] -= 1 if L_Break[0] > 0 else 0
                
                if "painted" not in L_DailyActions or "cleaned" not in L_DailyActions:   
                        $ del L_Spunk[:]  
                
                if "lover" in L_Petnames and L_Love > 800:
                        $ L_Love += 10
                if "master" in L_Petnames and L_Obed > 600:
                        $ L_Obed += 10
                if "fuck buddy" in L_Petnames:
                        $ L_Inbt += 10   
    #End of things when you sleep
                    
        
    # Things that happen every time you wait   
                                                        
    #Things that are about you:
    $ P_Semen += 1    
    $ MultiAction = 1 
    $ P_Focus -= 5 if P_Focus >= 10 else 0  
    $ Situation = 0      
    $ Current_Time = Time_Options[(Time_Count)]    
    $ Round = 100
    $ R_OCount = 0    
    $ K_OCount = 0     
    $ E_OCount = 0     
    $ L_OCount = 0       
    # Clears out recent and daily actions    
    $ del P_RecentActions[:]                            
    if Time_Count == 0: 
            $ del P_DailyActions[:]            
    call Taboo_Level  
    call GirlWaitAttract #checks girls attraction based on who's in the room
    
    #Things that are about Rogue:      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    if R_Lust >= 70 or R_Thirst >= 30 or renpy.random.randint(1, 20) >= 15:
                # checks if she wants to fap
                if "nofap" in R_Traits:
                        call AnyWord("Rogue",1,0,"wannafap")  #adds "wannafap" tag to daily 
                else:
                        call AnyWord("Rogue",1,0,"gonnafap")  #adds "gonnafap" tag to daily 
                    
    if "les" in R_RecentActions: #if she had a lesbian encounter without you. . .
                $ R_Thirst -= int(R_Thirst/2) 
                $ R_Lust = 20 
    
    #Resets her flirt  options
    $ R_Chat[5] = 0  
    #Resets her addiction fix attempts
    if R_Event[3]:
        $ R_Event[3] -= 1               
    
    $ R_Forced = 0
    if R_Loc == "bg classroom" or R_Loc == "bg dangerroom" :
            $ R_XP += 10    
    elif R_Loc == "bg showerroom": 
            call Remove_Girl("Rogue")
          
    #Appearance clean-up
    $ R_Blush = 0
    $ R_Water = 0
    $ R_Held = 0 
    
    #Reduced addiction
    $ R_Addictionrate -= R_Resistance if R_Addictionrate > 3 else 0 #else R_Addictionrate?
    $ R_Addictionrate = 0 if R_Addictionrate < 0 else R_Addictionrate    
        
    #Adjusts shame rate
    if R_Taboo and R_Shame:
            if R_Loc == "bg dangerroom":            
                    $ R_Shame -= 10 if R_Shame >=10 else R_Shame
            $ Count = int((R_Taboo * R_Shame) / 200)
            call Statup("Rogue", "Inbt", 90, Count)         
            call Statup("Rogue", "Obed", 90, Count) 
            $ R_Rep -= Count
            
    #subtracts R_Love by 5* the number of recent unsatisfieds
    $ R_Love -= 5*(Action_Check("Rogue","recent","unsatisfied")) 
    
    # Clears out recent and daily actions    
    
    $ del R_RecentActions[:] 
    if "angry" in R_DailyActions:
        $ R_RecentActions.append("angry")
    if Time_Count == 0: 
            $ del R_DailyActions[:]
    elif Time_Count == 3 and "yesdate" in R_DailyActions and "stoodup" not in R_Traits:
                        #if you stood her up for a date. . .
                        $ R_Traits.append("stoodup")
            
    call Rogue_Schedule
    call Stat_Checks    
    if Outfit:
            call RogueOutfit(R_OutfitDay)
    
    #end Rogue hourly actions
        
        
    #Things that are about Kitty:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    if "met" in K_History:
            if K_Lust >= 70 or K_Thirst >= 30 or renpy.random.randint(1, 20) >= 15:
                        # checks if she wants to fap
                        if "nofap" in K_Traits:
                                call AnyWord("Kitty",1,0,"wannafap")  #adds "wannafap" tag to daily 
                        else:
                                call AnyWord("Kitty",1,0,"gonnafap")  #adds "gonnafap" tag to daily 
            if "les" in K_RecentActions: #if she had a lesbian encounter without you. . .
                        $ K_Thirst -= 30 
                        $ K_Lust = 20 
                    
            #Resets her flirt  options
            $ K_Chat[5] = 0 
            
            #Resets her addiction fix attempts
            if K_Event[3]:
                $ K_Event[3] -= 1               
            
            $ K_Forced = 0
            if K_Loc == "bg classroom" or K_Loc == "bg dangerroom" :
                    $ K_XP += 10    
            elif K_Loc == "bg showerroom":
                    call Remove_Girl("Kitty")
                
            #Appearance clean-up
            $ K_Blush = 0
            $ K_Water = 0
            $ K_Held = 0 
            
            # Reduce addiction
            $ K_Addictionrate -= K_Resistance if K_Addictionrate > 3 else 0    
            $ K_Addictionrate = 0 if K_Addictionrate < 0 else K_Addictionrate    
            
            #Adjusts shame rate
            if K_Taboo and K_Shame:
                    if K_Loc == "bg dangerroom":            
                            $ K_Shame -= 10 if K_Shame >=10 else K_Shame
                    $ Count = int((K_Taboo * K_Shame) / 200)
                    call Statup("Kitty", "Inbt", 90, Count)         
                    call Statup("Kitty", "Obed", 90, Count) 
                    $ K_Rep -= Count
            
            $ K_Love -= 5*(Action_Check("Kitty","recent","unsatisfied")) #subtracts K_Love by 5* the number of recent unsatisfieds
            
            # Clears out recent and daily actions
            $ del K_RecentActions[:]
            if "angry" in K_DailyActions:
                $ K_RecentActions.append("angry")
            if Time_Count == 0: 
                $ del K_DailyActions[:]
            elif Time_Count == 3 and "yesdate" in K_DailyActions and "stoodup" not in K_Traits:
                                #if you stood her up for a date. . .
                                $ K_Traits.append("stoodup")
                
            call Kitty_Schedule
            call Stat_Checks    
            if Outfit:
                    call KittyOutfit(K_OutfitDay)
            #end Kitty hourly actions
        
    #Things that are about Emma:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
    if "met" in E_History:
            if E_Lust >= 70 or E_Thirst >= 30 or renpy.random.randint(1, 20) >= 15:
                        # checks if she wants to fap
                        if "nofap" in E_Traits:
                                call AnyWord("Emma",1,0,"wannafap")  #adds "wannafap" tag to daily 
                        else:
                                call AnyWord("Emma",1,0,"gonnafap")  #adds "gonnafap" tag to daily 
            if "les" in E_RecentActions: #if she had a lesbian encounter without you. . .
                        $ E_Thirst -= 30 
                        $ E_Lust = 20 
                    
            #Resets her flirt  options
            $ E_Chat[5] = 0 
            
            #Resets her addiction fix attempts
            if E_Event[3]:
                $ E_Event[3] -= 1               
            
            $ E_Forced = 0
            if E_Loc == "bg teacher" and "bg classroom" in (bg_current, R_Loc, K_Loc):
                    $ E_XP += 10 
            if E_Loc == "bg classroom" or E_Loc == "bg dangerroom" :
                    $ E_XP += 10    
            elif E_Loc == "bg showerroom":
                    call Remove_Girl("Emma")
                
            #Appearance clean-up
            $ E_Blush = 0
            $ E_Water = 0
            $ E_Held = 0 
            
            # Reduce addiction
            $ E_Addictionrate -= E_Resistance if E_Addictionrate > 3 else 0    
            $ E_Addictionrate = 0 if E_Addictionrate < 0 else E_Addictionrate    
            
            #Adjusts shame rate
            if E_Taboo and E_Shame:
                    if E_Loc == "bg dangerroom":            
                            $ E_Shame -= 10 if E_Shame >=10 else E_Shame
                    $ Count = int((E_Taboo * E_Shame) / 200)
                    call Statup("Emma", "Inbt", 90, Count)         
                    call Statup("Emma", "Obed", 90, Count) 
                    $ E_Rep -= int(1.5 * Count)
            
            $ E_Love -= 5*(Action_Check("Emma","recent","unsatisfied")) #subtracts E_Love by 5* the number of recent unsatisfieds
            
            # Clears out recent and daily actions
            $ del E_RecentActions[:]
            if "angry" in E_DailyActions:
                $ E_RecentActions.append("angry")
            if Time_Count == 0: 
                $ del E_DailyActions[:]
            elif Time_Count == 3 and "yesdate" in E_DailyActions and "stoodup" not in E_Traits:
                                #if you stood her up for a date. . .
                                $ E_Traits.append("stoodup")
                
            call Emma_Schedule
            call Stat_Checks    
            if Outfit:
                    call EmmaOutfit(E_OutfitDay)
            #end Emma hourly actions
       
    #Things that are about Laura:   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
    if "met" in L_History:
            if L_Lust >= 70 or L_Thirst >= 30 or renpy.random.randint(1, 20) >= 15:
                        # checks if she wants to fap
                        if "nofap" in L_Traits:
                                call AnyWord("Laura",1,0,"wannafap")  #adds "wannafap" tag to daily 
                        else:
                                call AnyWord("Laura",1,0,"gonnafap")  #adds "gonnafap" tag to daily 
            if "les" in L_RecentActions: #if she had a lesbian encounter without you. . .
                        $ L_Thirst -= 30 
                        $ L_Lust = 20 
                    
            #Resets her flirt  options
            $ L_Chat[5] = 0 
            
            #Resets her addiction fix attempts
            if L_Event[3]:
                $ L_Event[3] -= 1               
            
            $ L_Forced = 0
            if L_Loc == "bg classroom" or L_Loc == "bg dangerroom" :
                    $ L_XP += 10    
            elif L_Loc == "bg showerroom":
                    call Remove_Girl("Laura")
                
            #Appearance clean-up
            $ L_Blush = 0
            $ L_Water = 0
            $ L_Held = 0 
            
            # Reduce addiction
            $ L_Addictionrate -= L_Resistance if L_Addictionrate > 3 else 0    
            $ L_Addictionrate = 0 if L_Addictionrate < 0 else L_Addictionrate    
            
            #Adjusts shame rate
            if L_Taboo and L_Shame:
                    if L_Loc == "bg dangerroom":            
                            $ L_Shame -= 10 if L_Shame >=10 else L_Shame
                    $ Count = int((L_Taboo * L_Shame) / 200)
                    call Statup("Laura", "Inbt", 90, Count)         
                    call Statup("Laura", "Obed", 90, Count) 
                    $ L_Rep -= int(1.5 * Count)
            
            $ L_Love -= 5*(Action_Check("Laura","recent","unsatisfied")) #subtracts L_Love by 5* the number of recent unsatisfieds
            
            # Clears out recent and daily actions
            $ del L_RecentActions[:]
            if "angry" in L_DailyActions:
                $ L_RecentActions.append("angry")
            if Time_Count == 0: 
                $ del L_DailyActions[:]
            elif Time_Count == 3 and "yesdate" in L_DailyActions and "stoodup" not in L_Traits:
                                #if you stood her up for a date. . .
                                $ L_Traits.append("stoodup")
                
            call Laura_Schedule
            call Stat_Checks    
            if Outfit:
                    call LauraOutfit(L_OutfitDay)
            #end Laura hourly actions
    
    if Time_Count == 1:  
        if "sleepover" in R_Traits: 
                $ R_Traits.remove("sleepover")
        if "sleepover" in K_Traits: 
                $ K_Traits.remove("sleepover")
        if "sleepover" in E_Traits: 
                $ E_Traits.remove("sleepover")
        if "sleepover" in L_Traits: 
                $ L_Traits.remove("sleepover")
                
    call LesCheck #checks to see if the girls hook up with each other. . . 
        
    #end wait items: 
    call Faces #Sets girls faces based on their emotions
    call Checkout
    if Current_Time != "Night":        
            hide NightMask onlayer nightmask  
    if Lights:
            hide blackscreen onlayer black 
    
    return


# End Wait/Sleep Cycle ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
    
    
    
    
    
    
# //////////////////////////////////////////////////////////////////                                                            End Wait/Sleep Cycle 



label Taboo_Level(Taboo_Loc=0):
    #cycles through each girl, setting their taboo level.
    #Set your taboo level
        call CheckTaboo("Player",bg_current)          
    #Set Rogue's Taboo level
        if "Rogue" in Party:
                    $ R_Loc = bg_current
        if R_Loc == "nearby":
                $ Taboo_Check = bg_current
        else:
                $ Taboo_Check = R_Loc
        call CheckTaboo("Rogue",Taboo_Check)    
    #Set Kitty's Taboo level
        if "Kitty" in Party:
                    $ K_Loc = bg_current
        if K_Loc == "nearby":
                $ Taboo_Check = bg_current
        else:
                $ Taboo_Check = K_Loc
        call CheckTaboo("Kitty",Taboo_Check)
    #Set Emma's Taboo level
        if "Emma" in Party:
                    $ E_Loc = bg_current
        if E_Loc == "nearby":
                $ Taboo_Check = bg_current
        else:
                $ Taboo_Check = E_Loc
        call CheckTaboo("Emma",Taboo_Check)
    #Set Laura's Taboo level
        if "Laura" in Party:
                    $ L_Loc = bg_current
        if L_Loc == "nearby":
                $ Taboo_Check = bg_current
        else:
                $ Taboo_Check = L_Loc
        call CheckTaboo("Laura",Taboo_Check)
        return
            
        #end taboo level

label CheckTaboo(Girl=0,Taboo_Check=0):
        # Taboo_Check is the location, Girl is the girl being tested
    
        if Taboo_Check in ("bg player", "bg rogue", "bg kitty", "bg emma", "bg laura"): 
                    call Set_Taboo(Girl,0)
        elif Taboo_Check in ("bg classroom", "bg study"):
                if Current_Time == "Night":
                    call Set_Taboo(Girl,5)
                elif Current_Time == "Evening" or Weekday >= 5:
                    if "locked" in P_Traits:
                            call Set_Taboo(Girl,0)
                    else:
                            call Set_Taboo(Girl,30)
                else:
                    call Set_Taboo(Girl,40)
        elif Taboo_Check == "bg dangerroom":
                if Current_Time == "Night":
                    if "locked" in P_Traits:
                            call Set_Taboo(Girl,0)
                    else:
                            call Set_Taboo(Girl,5)
                else:
                    call Set_Taboo(Girl,40)
        elif Taboo_Check == "bg campus" or Taboo_Check == "bg pool":
                if Current_Time == "Night":
                    call Set_Taboo(Girl,20)
                else:
                    call Set_Taboo(Girl,40)
        elif Taboo_Check == "bg showerroom":   
                    call Set_Taboo(Girl,20)
        else:
                    call Set_Taboo(Girl,40)
        call Taboo_Buddy_Check(Girl) #checks the girl against all other girls
        return
        
label Set_Taboo(Girl=0,Value=0):
        #Sets "Girl's" Taboo to the given value
        if Girl == "Rogue":
                $ R_Taboo = Value
        elif Girl == "Kitty":
                $ K_Taboo = Value
        elif Girl == "Emma":
                $ E_Taboo = Value
        elif Girl == "Laura":
                $ L_Taboo = Value
        else:
                $ Taboo = Value
        return
    
label Taboo_Buddy_Check(Girl="Rogue",TempTaboo=Taboo):
    #checks if the girl is comfortable with the other girls present
    if Girl == "Rogue":
            if R_Taboo >= 20:
                        # if it's already 20+, there's no point to this
                        return
            if R_Loc == K_Loc and R_LikeKitty <= 800 and not ("Rogue" in P_Harem and "Kitty" in P_Harem):
                        #if either she likes Kitty, or both are in the harem, skip
                        $ R_Taboo = 20
            if R_Loc == E_Loc and R_LikeEmma <= 800 and not ("Rogue" in P_Harem and "Emma" in P_Harem):
                        $ R_Taboo = 20
            if R_Loc == L_Loc and R_LikeLaura <= 800 and not ("Rogue" in P_Harem and "Laura" in P_Harem):
                        $ R_Taboo = 20                
            $ Taboo = R_Taboo if (R_Taboo > Taboo and bg_current == R_Loc) else Taboo
    elif Girl == "Kitty":
            if K_Taboo >= 20:
                        return
            if K_Loc == R_Loc and K_LikeRogue <= 800 and not ("Kitty" in P_Harem and "Rogue" in P_Harem):
                        $ K_Taboo = 20
            if K_Loc == E_Loc and K_LikeEmma <= 800 and not ("Kitty" in P_Harem and "Emma" in P_Harem):
                        $ K_Taboo = 20 
            if K_Loc == L_Loc and K_LikeLaura <= 800 and not ("Kitty" in P_Harem and "Laura" in P_Harem):
                        $ K_Taboo = 20 
            $ Taboo = K_Taboo if (K_Taboo > Taboo and bg_current == K_Loc) else Taboo
    elif Girl == "Emma":
            if E_Taboo >= 20:
                        return
            if E_Loc == R_Loc and E_LikeRogue <= 800 and not ("Emma" in P_Harem and "Rogue" in P_Harem):
                        $ E_Taboo = 20
            if E_Loc == K_Loc and E_LikeKitty <= 800 and not ("Emma" in P_Harem and "Kitty" in P_Harem):
                        $ E_Taboo = 20
            if E_Loc == L_Loc and E_LikeLaura <= 800 and not ("Emma" in P_Harem and "Laura" in P_Harem):
                        $ E_Taboo = 20                
            $ Taboo = E_Taboo if (E_Taboo > Taboo and bg_current == E_Loc) else Taboo
    elif Girl == "Laura":
            if L_Taboo >= 20:
                        return
            if L_Loc == R_Loc and L_LikeRogue <= 800 and not ("Laura" in P_Harem and "Rogue" in P_Harem):
                        $ L_Taboo = 20
            if L_Loc == K_Loc and L_LikeKitty <= 800 and not ("Laura" in P_Harem and "Kitty" in P_Harem):
                        $ L_Taboo = 20
            if L_Loc == E_Loc and L_LikeEmma <= 800 and not ("Laura" in P_Harem and "Emma" in P_Harem):
                        $ L_Taboo = 20                
            $ Taboo = L_Taboo if (L_Taboo > Taboo and bg_current == L_Loc) else Taboo
    return
        
# Overrun checking //////////////////////////////////////////////////////////////////////
label Checkout(Total = 0):    
            call VersionNumber
        #Rogue
            $ R_Love = 1000 if R_Love > 1000 else R_Love    
            $ R_Obed = 1000 if R_Obed > 1000 else R_Obed    
            $ R_Inbt = 1000 if R_Inbt > 1000 else R_Inbt    
            $ R_Lust = 99 if R_Lust > 99 else R_Lust   
                
            $ R_Love = 0 if R_Love < 0 else R_Love    
            $ R_Obed = 0 if R_Obed < 0 else R_Obed    
            $ R_Inbt = 0 if R_Inbt < 0 else R_Inbt    
            $ R_Lust = 0 if R_Lust < 0 else R_Lust    
                        
            $ R_Action = R_MaxAction if R_Action > R_MaxAction else R_Action  
            $ R_Action = 0 if R_Action < 0 else R_Action  
            
            $ R_Addict = 100 if R_Addict > 100 else R_Addict  
            $ R_Addict = 0 if R_Addict < 0 else R_Addict  
            $ R_Addictionrate = 10 if R_Addictionrate > 10 else R_Addictionrate  
            $ R_Addictionrate = 0 if R_Addictionrate < 0 else R_Addictionrate  
            $ R_Thirst = 100 if R_Thirst > 100 else R_Thirst 
            $ R_Thirst = 0 if R_Thirst < 0 else R_Thirst 
            
            $ R_LikeKitty = 1000 if R_LikeKitty > 1000 else R_LikeKitty     
            $ R_LikeKitty = 0 if R_LikeKitty < 0 else R_LikeKitty 
            $ R_LikeEmma = 1000 if R_LikeEmma > 1000 else R_LikeEmma     
            $ R_LikeEmma = 0 if R_LikeEmma < 0 else R_LikeEmma 
            $ R_LikeLaura = 1000 if R_LikeLaura > 1000 else R_LikeLaura     
            $ R_LikeLaura = 0 if R_LikeLaura < 0 else R_LikeLaura 
            if R_Forced and R_ForcedCount < 10:
                        $ R_ForcedCount += 1
            
        #Kitty
            $ K_Love = 1000 if K_Love > 1000 else K_Love    
            $ K_Obed = 1000 if K_Obed > 1000 else K_Obed    
            $ K_Inbt = 1000 if K_Inbt > 1000 else K_Inbt    
            $ K_Lust = 99 if K_Lust > 99 else K_Lust   
                
            $ K_Love = 0 if K_Love < 0 else K_Love    
            $ K_Obed = 0 if K_Obed < 0 else K_Obed    
            $ K_Inbt = 0 if K_Inbt < 0 else K_Inbt    
            $ K_Lust = 0 if K_Lust < 0 else K_Lust   
                        
            $ K_Action = K_MaxAction if K_Action > K_MaxAction else K_Action  
            $ K_Action = 0 if K_Action < 0 else K_Action  
            
            $ K_Addict = 100 if K_Addict > 100 else K_Addict  
            $ K_Addict = 0 if K_Addict < 0 else K_Addict  
            $ K_Addictionrate = 10 if K_Addictionrate > 10 else K_Addictionrate  
            $ K_Addictionrate = 0 if K_Addictionrate < 0 else K_Addictionrate   
            $ K_Thirst = 100 if K_Thirst > 100 else K_Thirst 
            $ K_Thirst = 0 if K_Thirst < 0 else K_Thirst 
            
            $ K_LikeRogue = 1000 if K_LikeRogue > 1000 else K_LikeRogue     
            $ K_LikeRogue = 0 if K_LikeRogue < 0 else K_LikeRogue 
            $ K_LikeEmma = 1000 if K_LikeEmma > 1000 else K_LikeEmma     
            $ K_LikeEmma = 0 if K_LikeEmma < 0 else K_LikeEmma 
            $ K_LikeLaura = 1000 if K_LikeLaura > 1000 else K_LikeLaura     
            $ K_LikeLaura = 0 if K_LikeLaura < 0 else K_LikeLaura 
            if K_Forced and K_ForcedCount < 10:
                $ K_ForcedCount += 1

        #Emma
            $ E_Love = 1000 if E_Love > 1000 else E_Love    
            $ E_Obed = 1000 if E_Obed > 1000 else E_Obed    
            $ E_Inbt = 1000 if E_Inbt > 1000 else E_Inbt    
            $ E_Lust = 99 if E_Lust > 99 else E_Lust   
                
            $ E_Love = 0 if E_Love < 0 else E_Love    
            $ E_Obed = 0 if E_Obed < 0 else E_Obed    
            $ E_Inbt = 0 if E_Inbt < 0 else E_Inbt    
            $ E_Lust = 0 if E_Lust < 0 else E_Lust   
                        
            $ E_Action = E_MaxAction if E_Action > E_MaxAction else E_Action  
            $ E_Action = 0 if E_Action < 0 else E_Action  
            
            $ E_Addict = 100 if E_Addict > 100 else E_Addict  
            $ E_Addict = 0 if E_Addict < 0 else E_Addict  
            $ E_Addictionrate = 10 if E_Addictionrate > 10 else E_Addictionrate  
            $ E_Addictionrate = 0 if E_Addictionrate < 0 else E_Addictionrate   
            $ E_Thirst = 100 if E_Thirst > 100 else E_Thirst 
            $ E_Thirst = 0 if E_Thirst < 0 else E_Thirst 
            
            $ E_LikeRogue = 1000 if E_LikeRogue > 1000 else E_LikeRogue     
            $ E_LikeRogue = 0 if E_LikeRogue < 0 else E_LikeRogue 
            $ E_LikeKitty = 1000 if E_LikeKitty > 1000 else E_LikeKitty     
            $ E_LikeKitty = 0 if E_LikeKitty < 0 else E_LikeKitty 
            $ E_LikeLaura = 1000 if E_LikeLaura > 1000 else E_LikeLaura     
            $ E_LikeLaura = 0 if E_LikeLaura < 0 else E_LikeLaura 
            if E_Forced and E_ForcedCount < 10:
                $ E_ForcedCount += 1
                
        #Laura
            $ L_Love = 1000 if L_Love > 1000 else L_Love    
            $ L_Obed = 1000 if L_Obed > 1000 else L_Obed    
            $ L_Inbt = 1000 if L_Inbt > 1000 else L_Inbt    
            $ L_Lust = 99 if L_Lust > 99 else L_Lust   
                
            $ L_Love = 0 if L_Love < 0 else L_Love    
            $ L_Obed = 0 if L_Obed < 0 else L_Obed    
            $ L_Inbt = 0 if L_Inbt < 0 else L_Inbt    
            $ L_Lust = 0 if L_Lust < 0 else L_Lust   
                        
            $ L_Action = L_MaxAction if L_Action > L_MaxAction else L_Action  
            $ L_Action = 0 if L_Action < 0 else L_Action  
            
            $ L_Addict = 100 if L_Addict > 100 else L_Addict  
            $ L_Addict = 0 if L_Addict < 0 else L_Addict  
            $ L_Addictionrate = 10 if L_Addictionrate > 10 else L_Addictionrate  
            $ L_Addictionrate = 0 if L_Addictionrate < 0 else L_Addictionrate   
            $ L_Thirst = 100 if L_Thirst > 100 else L_Thirst 
            $ L_Thirst = 0 if L_Thirst < 0 else L_Thirst 
            
            $ L_LikeRogue = 1000 if L_LikeRogue > 1000 else L_LikeRogue     
            $ L_LikeRogue = 0 if L_LikeRogue < 0 else L_LikeRogue 
            $ L_LikeKitty = 1000 if L_LikeKitty > 1000 else L_LikeKitty     
            $ L_LikeKitty = 0 if L_LikeKitty < 0 else L_LikeKitty 
            $ L_LikeEmma = 1000 if L_LikeEmma > 1000 else L_LikeEmma     
            $ L_LikeEmma = 0 if L_LikeEmma < 0 else L_LikeEmma 
            if L_Forced and L_ForcedCount < 10:
                $ L_ForcedCount += 1
            $ L_ScentTimer = 0
                
        #Player
            $ P_Focus = 99 if P_Focus > 99 else P_Focus
            $ P_Focus = 0 if P_Focus < 0 else P_Focus
            $ P_Semen = P_Semen_Max if P_Semen > P_Semen_Max else P_Semen  
            $ P_Semen = 0 if P_Semen < 0 else P_Semen   
            
            if Total:
                    call DrainWord("Player","cockout")
                    call DrainWord("Player","nude")
#                    $ LesFlag = 0
                    $ Trigger = 0        
                    $ Trigger2 = 0
                    $ Trigger3 = 0
                    $ Trigger4 = 0
                    $ Trigger5 = 0
                    $ ThreeCount = 100
                    $ Partner = 0 
                    $ P_FocusX = 0
            return

# end Overrun checking //////////////////////////////////////////////////////////////////////

# Scene Setting ///////////////////////////////////////////////////////////////////////

transform SpriteLoc(Loc = StageRight, LocY = 50):  
        #This puts the sprite at a location relative to the sent variable
        pos (Loc,LocY)
    
label Set_The_Scene(Chr = 1, Entry = 0, Dress = 1, TrigReset = 1, Quiet=0):
        # If Chr, then display the characters in the room
        # If Entry, then show the "entry" version of a room, such as a closed door, does not display characters
        # If Dress, then check whether the character is underdressed when displaying her
        # Trigreset resets triggers
        # if Quiet, no fade to black
        
        if not Quiet:
            show blackscreen onlayer black 
        
        if Entry:
            $ Chr = 0
            call AllHide 
            
        call Display_Background(Entry) 
        
        if Current_Time == 'Night':
                show NightMask onlayer nightmask
        else:          
                hide NightMask onlayer nightmask  
        
        if Chr:
                call Present_Check  #culls out Party to 2, 
                #sets location to bg_current, removes extra girls, sets Focus to a girl in the room   
                
                if Ch_Focus == "Kitty" and K_Loc == bg_current: 
                        $ E_SpriteLoc = StageRight   
                        $ R_SpriteLoc = StageRight
                        $ L_SpriteLoc = StageRight
                        $ K_SpriteLoc = StageCenter
                        $ RogueLayer = 75
                        $ EmmaLayer = 75
                        $ LauraLayer = 75
                        $ KittyLayer = 100
                        call Display_Emma(Dress,TrigReset)
                        call Display_Rogue(Dress,TrigReset)
                        call Display_Laura(Dress,TrigReset)
                        call Display_Kitty(Dress,TrigReset)
                        
                elif Ch_Focus == "Emma" and E_Loc == bg_current:  
                        $ K_SpriteLoc = StageRight  
                        $ R_SpriteLoc = StageRight
                        $ L_SpriteLoc = StageRight
                        $ E_SpriteLoc = StageCenter
                        $ KittyLayer = 75
                        $ RogueLayer = 75
                        $ LauraLayer = 75
                        $ EmmaLayer = 100
                        call Display_Rogue(Dress,TrigReset)
                        call Display_Kitty(Dress,TrigReset)
                        call Display_Laura(Dress,TrigReset)
                        call Display_Emma(Dress,TrigReset)
                        
                elif Ch_Focus == "Laura" and L_Loc == bg_current:  
                        $ K_SpriteLoc = StageRight  
                        $ R_SpriteLoc = StageRight
                        $ E_SpriteLoc = StageRight
                        $ L_SpriteLoc = StageCenter
                        $ KittyLayer = 75
                        $ RogueLayer = 75
                        $ EmmaLayer = 75
                        $ LauraLayer = 100
                        call Display_Rogue(Dress,TrigReset)
                        call Display_Kitty(Dress,TrigReset)
                        call Display_Emma(Dress,TrigReset)
                        call Display_Laura(Dress,TrigReset)
                
                else: #if Ch_Focus == "Rogue" and R_Loc == bg_current:   
                        $ K_SpriteLoc = StageRight
                        $ E_SpriteLoc = StageRight
                        $ L_SpriteLoc = StageRight
                        $ R_SpriteLoc = StageCenter
                        $ KittyLayer = 75
                        $ EmmaLayer = 75
                        $ LauraLayer = 75
                        $ RogueLayer = 100
                        call Display_Emma(Dress,TrigReset)
                        call Display_Kitty(Dress,TrigReset)
                        call Display_Laura(Dress,TrigReset)
                        call Display_Rogue(Dress,TrigReset)
                if bg_current == "bg study" and Current_Time != "Night":   
                        show Professor at SpriteLoc(StageLeft) zorder 25 
                else:
                        hide Professor
                
        else:            
                call AllHide(1) #removes all girls that aren't there.  
        show Chibi_UI
        hide Cellphone
        
        if bg_current == "bg classroom" and E_Loc == "bg teacher": 
                #if Emma is teaching, sets teaching outfit 
                call E_AltClothes(8)                            
                call EmmaOutfit(Changed=1)
                        
        if TrigReset and Dress:       
                #resets your clothing if nude
                call Get_Dressed
            
        if "Historia" in P_Traits: #Simulation haze
                show BlueScreen onlayer black
        else:
                hide BlueScreen onlayer black
        hide blackscreen onlayer black
        return
# End primary Display function <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<  <<
        
        
        
label Shift_Focus(Chr = "Rogue", Second = 0):      
        #When used like Shift_Focus("Kitty"), changes the focus character and relative default positions
        if Ch_Focus == Partner:
                    #if somehow the partner and main girl are the same. . .
                    if Partner != "Rogue" and R_Loc == bg_current:
                                $ Partner = "Rogue"
                    elif Partner != "Kitty" and K_Loc == bg_current:
                                $ Partner = "Kitty"
                    elif Partner != "Emma" and E_Loc == bg_current:
                                $ Partner = "Emma"
                    elif Partner != "Laura" and L_Loc == bg_current:
                                $ Partner = "Laura"
        if Chr == "Kitty":
                if K_Loc == bg_current:
                        #If Kitty is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                        if E_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                        if L_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ L_SpriteLoc = StageRight
                            $ LauraLayer = 75
                        #and move Kitty to first position
                        $ K_SpriteLoc = StageCenter
                        $ KittyLayer = 100
                        
                if Ch_Focus == "Kitty": 
                    #If Kitty was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Kitty": 
                    #If Kitty was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Kitty"
        elif Chr == "Emma":
                if E_Loc == bg_current:
                        #If Emma is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                        if K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                        if L_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ L_SpriteLoc = StageRight
                            $ LauraLayer = 75
                        #and move Emma to first position
                        $ E_SpriteLoc = StageCenter
                        $ EmmaLayer = 100
                        
                if Ch_Focus == "Emma": 
                    #If Emma was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Emma": 
                    #If Emma was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Emma"
        elif Chr == "Laura":
                if L_Loc == bg_current:
                        #If Laura is where you're at. . .
                        if R_Loc == bg_current:
                            #if Rogue is there, shift her to second position
                            $ R_SpriteLoc = StageRight
                            $ RogueLayer = 75
                        if K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                        if E_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                        #and move Laura to first position
                        $ L_SpriteLoc = StageCenter
                        $ LauraLayer = 100
                        
                if Ch_Focus == "Laura": 
                    #If Laura was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Laura": 
                    #If Laura was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Laura"
        else: #if Chr == "Rogue":
                if R_Loc == bg_current:
                        #If Rogue is where you're at. . .
                        if K_Loc == bg_current:
                            #if Kitty is there, shift her to second position
                            $ K_SpriteLoc = StageRight
                            $ KittyLayer = 75
                        if E_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ E_SpriteLoc = StageRight
                            $ EmmaLayer = 75
                        if L_Loc == bg_current:
                            #if Emma is there, shift her to second position
                            $ L_SpriteLoc = StageRight
                            $ LauraLayer = 75
                        #and move Rogue to first position
                        $ R_SpriteLoc = StageCenter
                        $ RogueLayer = 100
                        
                if Ch_Focus == "Rogue": 
                    #If Rogue was already the focal character, return
                    pass
                elif Second:
                    $ Partner = Second
                elif Partner == "Rogue": 
                    #If Rogue was the Partner in a scene, make the existing focal character the Partner
                    $ Partner = Ch_Focus
                $ Ch_Focus = "Rogue"        
        $ renpy.restart_interaction() 
        return
    
label Display_Rogue(Dress = 1, TrigReset = 1, DLoc = R_SpriteLoc, YLoc=50):
    # If Dress, then check whether the character is underdressed when displaying her
    if Taboo and Dress:   
            call RogueOutfit(Changed=1)
            $ R_Water = 0
            
    if R_Loc != "bg showerroom" and R_Loc != "bg pool":
            $ R_Water = 0
            
    if "Rogue" not in Party and R_Loc != bg_current:  
            # If Rogue isn't there, put her away
            hide Rogue
            call Rogue_Hide
            return                           
    
    $ R_SpriteLoc = DLoc
    
    if TrigReset:
            # resets triggers
            $ Trigger = 0    
            $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
            $ Trigger3 = 0
            $ Trigger4 = 0
            $ Trigger5 = 0
    
    if Partner == "Rogue":
        $DLoc = StageFarRight #Moves Rogue over if she's secondary
        
    call Rogue_Hide      
    #displays Rogue if present, Sets her as local if in a party
    $ R_Loc = bg_current        
    
    if Dress:              
        #If in public, check to see if clothes are too sexy, and change them if necessary
        call Rogue_OutfitShame
    
    if bg_current == "bg movies" or bg_current == "bg restaurant":
        #shifts them downward if on a date
        $ YLoc = 250
        
    #Display Rogue    
    if not renpy.showing('Rogue'):
        show Rogue at SpriteLoc(1000,YLoc) zorder RogueLayer:
                offset (0,0)
                anchor (0.5, 0.0)  
                pos (1000,YLoc)
    show Rogue:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            easeout .5 pos (DLoc,YLoc)     
    show Rogue:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            pos (DLoc,YLoc)    
            
#    show Rogue at SpriteLoc(DLoc,YLoc) zorder RogueLayer:
#            alpha 1
#            zoom 1
#            offset (0,0)
#            anchor (0.6, 0.0)
#    with easeinright
    return                

label Display_Kitty(Dress = 1, TrigReset = 1, DLoc = K_SpriteLoc, YLoc=50):
   # If Dress, then check whether the character is underdressed when displaying her
   
    if Taboo and Dress: #If not in the showers, get dressed and dry off   
            call KittyOutfit(Changed=1)
            $ K_Wet = 0
              
    if K_Loc != "bg showerroom" and K_Loc != "bg pool":
            $ K_Water = 0
            
    if "Kitty" not in Party and K_Loc != bg_current:  
            # If Kitty isn't there, put her away 
            call KittyOutfit(Changed=1)
            hide Kitty_Sprite
            call Kitty_Hide    
            return
            
    $ K_SpriteLoc = DLoc
    
    if TrigReset:
            # resets triggers
            $ Trigger = 0    
            $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
            $ Trigger3 = 0
            $ Trigger4 = 0
            $ Trigger5 = 0
    
    if Partner == "Kitty":
        $DLoc = StageFarRight #Moves Kitty over if she's secondary
      
    call Kitty_Hide        
    #displays Kitty if present, Sets her as local if in a party
    $ K_Loc = bg_current 
    
    if Dress:                       
        #If in public, check to see if clothes are too sexy, and change them if necessary
        call Kitty_OutfitShame
    
    if bg_current == "bg movies" or bg_current == "bg restaurant":
        #shifts them downward if on a date
        $ YLoc = 250
        
    #Display Kitty    
    if not renpy.showing('Kitty_Sprite'):
        show Kitty_Sprite at SpriteLoc(1000,YLoc) zorder KittyLayer:
                offset (0,0)
                anchor (0.5, 0.0)  
                pos (1000,YLoc)            
    show Kitty_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            easeout .5 pos (DLoc,YLoc)    
    show Kitty_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            pos (DLoc,YLoc)
            
#    show Kitty_Sprite at SpriteLoc(DLoc,YLoc) zorder KittyLayer:
#            alpha 1
#            zoom 1
#            offset (0,0)
#            anchor (0.5, 0.0)  
#    with easeinright
    return

label Display_Emma(Dress = 1, TrigReset = 1, DLoc = E_SpriteLoc, Location = E_Loc, YLoc=50):
    # If Dress, then check whether the character is underdressed when displaying her
    
    if Taboo and Dress: #If not in the showers, get dressed and dry off        
            call EmmaOutfit(Changed=1)
            $ E_Wet = 0
              
    if E_Loc != "bg showerroom" and E_Loc != "bg pool":
            $ E_Water = 0
            
    if "Emma" not in Party and E_Loc != bg_current:  
            # If Emma isn't there, put her away      
            call EmmaOutfit(Changed=1)
            hide Emma_Sprite
            call Emma_Hide  
            return            
        
    $ E_SpriteLoc = DLoc
    
    if TrigReset:
            # resets triggers
            $ Trigger = 0    
            $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
            $ Trigger3 = 0
            $ Trigger4 = 0
            $ Trigger5 = 0
    
    if Partner == "Emma":
        $DLoc = StageFarRight #Moves Emma over if she's secondary
        
    call Emma_Hide       
    #displays Emma if present, Sets her as local if in a party
    if "Emma" in Party: 
            $ E_Loc = bg_current 
    
    if Dress:                       #If in public, check to see if clothes are too sexy, and change them if necessary
        call Emma_OutfitShame
                        
    #hide podium/desk shot
    hide Emma_At_Podium onlayer backdrop
    hide Emma_At_Desk onlayer backdrop
    
    if bg_current == "bg movies" or bg_current == "bg restaurant":
        #shifts them downward if on a date
        $ YLoc = 250
        
    #Display Emma    
    if not renpy.showing('Emma_Sprite'):
        show Emma_Sprite at SpriteLoc(1000,YLoc) zorder EmmaLayer:
                offset (0,0)
                anchor (0.5, 0.0)  
                pos (1000,YLoc)
    show Emma_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            easeout .5 pos (DLoc,YLoc)    
    show Emma_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            pos (DLoc,YLoc)    
            
#    show Emma_Sprite at SpriteLoc(DLoc,YLoc) zorder EmmaLayer:
#            alpha 1
#            zoom 1
#            offset (0,0)
#            anchor (0.5, 0.0)
#    with easeinright
    return
    
label Display_Laura(Dress = 1, TrigReset = 1, DLoc = L_SpriteLoc, YLoc=50):
   # If Dress, then check whether the character is underdressed when displaying her
    if Taboo and Dress: #If not in the showers, get dressed and dry off        
            call LauraOutfit(Changed=1)
            $ L_Wet = 0
              
    if L_Loc != "bg showerroom" and L_Loc != "bg pool":
            $ L_Water = 0
            
    if "Laura" not in Party and L_Loc != bg_current:  
            # If Laura isn't there, put her away    
            call LauraOutfit(Changed=1)
            hide Laura_Sprite
            call Laura_Hide 
            return
                
    $ L_SpriteLoc = DLoc
    
    if TrigReset:
            # resets triggers
            $ Trigger = 0    
            $ Trigger2 = 0 if Trigger2 != "jackin" else "jackin"
            $ Trigger3 = 0
            $ Trigger4 = 0
            $ Trigger5 = 0
    
    if Partner == "Laura":
        $DLoc = StageFarRight #Moves Laura over if she's secondary
      
    call Laura_Hide         
    #displays Laura if present, Sets her as local if in a party
    $ L_Loc = bg_current 
    
    if Dress:   
            #If in public, check to see if clothes are too sexy, and change them if necessary
            call Laura_OutfitShame
    
    
    $ L_Claws = 0 # Resets her claws
                    
    if bg_current == "bg movies" or bg_current == "bg restaurant":
        #shifts them downward if on a date
        $ YLoc = 250
        
    #Display Laura    
    if not renpy.showing('Laura_Sprite'):
        show Laura_Sprite at SpriteLoc(1000,YLoc) zorder LauraLayer:
                offset (0,0)
                anchor (0.5, 0.0)  
                pos (1000,YLoc)
    show Laura_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            easeout .5 pos (DLoc,YLoc)    
    show Laura_Sprite:
            alpha 1
            zoom 1
            offset (0,0)
            anchor (0.5, 0.0)  
            pos (DLoc,YLoc)    
#    show Laura_Sprite at SpriteLoc(DLoc,YLoc) zorder LauraLayer:
#            alpha 1
#            zoom 1
#            offset (0,0)
#            anchor (0.5, 0.0)  
#    with easeinright
            
    return
# end Scene Setting ///////////////////////////////////////////////////////////////////////



# Player Leveling
label Stat_Checks:
           
    if P_XP >= P_XPgoal and P_Lvl < 10:        
        $ P_XPgoal = int((1.15 * P_XPgoal) + 100)
        $ P_Lvl += 1
        $ P_StatPoints += 1
        if P_Lvl <5:
            $ Count = 1
        elif P_Lvl <9:
            $ Count = 2
        else:
            $ Count = 3
        $ P_Income += Count
        "You've leveled up!"
        "Xavier has noticed your achievements and raised your stipend by $[Count] per day. It is now $[P_Income]."
        if P_Lvl == 10:
            "You've reached max level!"
    
    if R_Loose < 2:  #checks how tight Rogue's asshole is   
        if (R_Anal + R_DildoA + R_Plug) >= 3:
            $ R_Loose = 1
        if (R_Anal + R_DildoA + R_Plug) >= 15:
            $ R_Loose = 2   
            
    if R_XP >= R_XPgoal and R_Lvl < 10:
        $ R_XPgoal = int((1.15 * R_XPgoal) + 100)
        $ R_Lvl += 1
        $ R_StatPoints += 1
        "Rogue's leveled up! I bet she has some new tricks to learn."
        if R_Lvl == 10:
            "Rogue's reached max level!"
            
            
    if K_Loose < 2:  #checks how tight Kitty's asshole is   
        if (K_Anal + K_DildoA + K_Plug) >= 3:
            $ K_Loose = 1
        if (K_Anal + K_DildoA + K_Plug) >= 15:
            $ K_Loose = 2   
            
    if K_XP >= K_XPgoal and K_Lvl < 10:
        $ K_XPgoal = int((1.15 * K_XPgoal) + 100)
        $ K_Lvl += 1
        $ K_StatPoints += 1
        "Kitty's leveled up! I bet she has some new tricks to learn."
        if K_Lvl == 10:
            "Kitty's reached max level!"
      
    if K_Loose < 2:  #checks how tight Kitty's asshole is   
        if (K_Anal + K_DildoA + K_Plug) >= 3:
            $ K_Loose = 1
        if (K_Anal + K_DildoA + K_Plug) >= 15:
            $ K_Loose = 2   
            
    if E_XP >= E_XPgoal and E_Lvl < 10:
        $ E_XPgoal = int((1.15 * E_XPgoal) + 100)
        $ E_Lvl += 1
        $ E_StatPoints += 1
        "Emma's leveled up! I bet she has some new tricks to learn."
        if E_Lvl == 10:
            "Emma's reached max level!"
            
    if L_XP >= L_XPgoal and L_Lvl < 10:
        $ L_XPgoal = int((1.15 * L_XPgoal) + 100)
        $ L_Lvl += 1
        $ L_StatPoints += 1
        "Laura's leveled up! I bet she has some new tricks to learn."
        if L_Lvl == 10:
            "Laura's reached max level!"     
    return

label P_Level_Up:
    menu:
        "You have [P_StatPoints] points to spend. How would you like to spend them?"
        "Increase sexual stamina. [[One point]" if "focus" not in P_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving you more time before you blow."
                "Unlock Focus.":
                    if P_StatPoints:
                        $ P_StatPoints -= 1  
                        $ P_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Increase your addictiveness. [[One point]" if "addict control" not in P_Traits and "nonaddictive" not in P_Traits and "addictive" not in P_Traits:
            menu:
                "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                "Increase addictiveness.":
                    if P_StatPoints:
                        $ P_StatPoints -= 1 
                        $ P_Traits.append("addictive") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Reduce your addictiveness. [[One point]" if "addict control" not in P_Traits and "nonaddictive" not in P_Traits and "addictive" not in P_Traits:
            menu:
                "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                "Reduce addictiveness.":
                    if P_StatPoints:
                        $ P_StatPoints -= 1 
                        $ P_Traits.append("nonaddictive") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Control your Addiction level. [[Two points]" if "addict control" not in P_Traits and ("nonaddictive" in P_Traits or "addictive" in P_Traits):
            menu:
                "This trait will allow you to freely control the amount you addict girls to your touch."
                "Gain addiction control.":
                    if P_StatPoints >= 2:
                        $ P_StatPoints -= 2 
                        $ P_Traits.append("addict control") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass       
                    
        "Increase your addictiveness. [[Free]" if "addict control" in P_Traits: #If you have Addict-control
            menu:
                "This trait will increase the addictiveness of your touch, making you harder for girls to quit."
                "Increase addictiveness, no cost.":
                    if "nonaddictive" in P_Traits:
                        $ P_Traits.remove("nonaddictive")
                        "You are now at the baseline addictiveness level."
                    elif "addictive" not in P_Traits:
                        $ P_Traits.append("addictive") 
                        "You are now at the enhanced addictiveness level."
                    else:
                        "You are already at the max addictiveness level."
                "Cancel.":
                    pass
        "Reduce your addictiveness. [[Free]" if "addict control" in P_Traits:
            menu:
                "This trait will reduce the addictiveness of your touch, making it easier for girls to resist it."
                "Reduce addictiveness.":
                    if "addictive" in P_Traits:
                        $ P_Traits.remove("addictive")
                        "You are now at the baseline addictiveness level."
                    elif "nonaddictive" not in P_Traits:
                        $ P_Traits.append("nonaddictive") 
                        "You are now at the reduced addictiveness level."
                    else:
                        "You are already at the minimum addictiveness level."                
                    
                    if "addictive" in P_Traits:
                        $ P_Traits.remove("addictive") 
                        $ P_Traits.append("nonaddictive") 
                        $ P_Traits.append("addict control") 
                    else:
                        $ P_Traits.append("nonaddictive") 
                "Cancel.":
                    pass
                    
        "Increase semen production. [[One point]" if P_Semen_Max < 5:            
            menu:
                "This trait will increase by 1 the number of times you can climax before needing a break."
                "Increase max semen.":                    
                    if P_StatPoints:
                        $ P_StatPoints -= 1  
                        $ P_Semen_Max += 1
                    else:
                        "You don't have enough points for that."
                    if P_Semen_Max >= 5:
                        "You're already at the max level."
                "Cancel.":
                    pass
                    
#        "Make yourself addictive to Kitty. [[One point]" if "met" in K_History and "addict kitty" not in P_Traits:
#            menu:
#                "This trait will adjust the \"flavor\" of your touch so that it is also addictive to Kitty."
#                "Increase addictiveness.":
#                    if P_StatPoints:
#                        $ P_StatPoints -= 1 
#                        $ P_Traits.append("addict kitty") 
#                    else:
#                        "You don't have enough points for that."
#                "Cancel.":
#                    pass
                    
        "Never Mind, I'll come back later.":
            return

    if P_StatPoints > 0:
        jump P_Level_Up
    return

# End Player Leveling

# Rogue Leveling
label R_Level_Up:
    menu:
        "Rogue is Level [R_Lvl] and has [R_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in R_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Rogue more time before she orgasms."
                "Unlock Focus.":
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Rogue's resistance. [[One point]]" if 0 < R_Resistance < 3:
            menu:
                "This trait will increase Rogue's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if R_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Rogue can take before needing a break."
            menu:
                "She currently has [R_MaxAction] actions."
                "Increase sex actions.":
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_MaxAction += 2
                        if R_MaxAction > 10:
                            $ R_MaxAction = 10
                            "Rogue has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Allow Rogue to touch. [[One point]" if "touch" not in R_Traits and R_Lvl >= 5:
            "This trait will allow Rogue to touch other people, not just you, without harming them."
            menu:
                "She can still borrow their abilities if they have any."
                "Unlock touch ability.":                    
                    if R_StatPoints:
                        $ R_StatPoints -= 1  
                        $ R_Traits.append("touch") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
                    
        "Allow Rogue to permanently Steal. [[Two points]" if "touch" in R_Traits and "steal" not in R_Traits:
            "This trait will allow Rogue to permanently copy one other mutant ability at a time."            
            menu:
                "This does not harm the person she borrows from and can switch abilities with a touch."
                "Unlock steal ability.":
                    if R_StatPoints >= 2:
                        $ R_StatPoints -= 2  
                        $ R_Traits.append("steal") 
                    else:
                        "You don't have enough points for that."                    
                "Cancel.":
                    pass
        "Never Mind, I'll come back later.":
            return
    if R_StatPoints > 0:
        jump R_Level_Up
    return

# End Rogue Leveling


# Kitty Leveling
label K_Level_Up:
    menu:
        "Kitty is Level [K_Lvl] and has [K_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in K_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Kitty more time before she orgasms."
                "Unlock Focus.":
                    if K_StatPoints:
                        $ K_StatPoints -= 1  
                        $ K_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Kitty's resistance. [[One point]]" if 0 < K_Resistance < 3:
            menu:
                "This trait will increase Kitty's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if K_StatPoints:
                        $ K_StatPoints -= 1  
                        $ K_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if K_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Kitty can take before needing a break."
            menu:
                "She currently has [K_MaxAction] actions."
                "Increase sex actions.":
                    if K_StatPoints:
                        $ K_StatPoints -= 1  
                        $ K_MaxAction += 2
                        if K_MaxAction > 10:
                            $ K_MaxAction = 10
                            "Kitty has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
        "Do. . . Something else?" if K_MaxAction >= 10:
                "I don't know, what {i}should{/i} she be doing at this point?"
        "Never Mind, I'll come back later.":
            return
    if K_StatPoints > 0:
        jump K_Level_Up
    return

# End Kitty Leveling

# Emma Leveling
label E_Level_Up:
    menu:
        "Emma is Level [E_Lvl] and has [E_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in E_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Emma more time before she orgasms."
                "Unlock Focus.":
                    if E_StatPoints:
                        $ E_StatPoints -= 1  
                        $ E_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Emma's resistance. [[One point]]" if 0 < E_Resistance < 3:
            menu:
                "This trait will increase Emma's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if E_StatPoints:
                        $ E_StatPoints -= 1  
                        $ E_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if E_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Emma can take before needing a break."
            menu:
                "She currently has [E_MaxAction] actions."
                "Increase sex actions.":
                    if E_StatPoints:
                        $ E_StatPoints -= 1  
                        $ E_MaxAction += 2
                        if E_MaxAction > 10:
                            $ E_MaxAction = 10
                            "Emma has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
        "Do. . . Something else?" if E_MaxAction >= 10:
                "I don't know, what {i}should{/i} she be doing at this point?"
        "Never Mind, I'll come back later.":
            return
    if E_StatPoints > 0:
        jump E_Level_Up
    return

# End Emma Leveling


# Laura Leveling
label L_Level_Up:
    menu:
        "Laura is Level [L_Lvl] and has [L_StatPoints] points to spend. How would you like to spend them?"
                            
        "Increase sexual focus. [[One point]" if "focus" not in L_Traits:
            menu:
                "This trait will unlock the \"Focus\" option during sex, giving Laura more time before she orgasms."
                "Unlock Focus.":
                    if L_StatPoints:
                        $ L_StatPoints -= 1  
                        $ L_Traits.append("focus") 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass                   
     
        "Increase Laura's resistance. [[One point]]" if 0 < L_Resistance < 3:
            menu:
                "This trait will increase Laura's resistance to your touch's addictive properties."
                "Increase Resistance.":
                    if L_StatPoints:
                        $ L_StatPoints -= 1  
                        $ L_Resistance += 1 
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass    
                
                    
        "Increase stamina. [[One point]" if L_MaxAction < 10:
            "This trait will increase by 2 the number of sex actions Laura can take before needing a break."
            menu:
                "She currently has [L_MaxAction] actions."
                "Increase sex actions.":
                    if L_StatPoints:
                        $ L_StatPoints -= 1  
                        $ L_MaxAction += 2
                        if L_MaxAction > 10:
                            $ L_MaxAction = 10
                            "Laura has reached her maximum actions."
                    else:
                        "You don't have enough points for that."
                "Cancel.":
                    pass
        "Do. . . Something else?" if L_MaxAction >= 10:
                "I don't know, what {i}should{/i} she be doing at this point?"
        "Never Mind, I'll come back later.":
            return
    if L_StatPoints > 0:
        jump L_Level_Up
    return

# End Laura Leveling

# Shop Interface //////////////////////////////////////////////////////////////////////
                                                 
label Shop:
    menu:
        "You are logged into the store. You have %(P_Cash)d dollars."       
        "Buy dildo for $20.":
            $ Count = Inventory_Check("dildo")
            if Count >= 10:
                "You already have way more dildos than you need. 2, 4, 6. . . yes, way too many."
            elif P_Cash >= 20:                
                "You purchase one dildo."
                $ P_Inventory.append("dildo")
                $ P_Cash -= 20
            else:
                "You don't have enough for that."
        "Buy \"Shocker\" vibrator for $25.":
            $ Count = Inventory_Check("vibrator")
            if Count >= 10:
                "If you bought one more vibrator, you would risk a geological event."
            elif P_Cash >= 25:
                "You purchase one vibrator."
                $ P_Inventory.append("vibrator")
                $ P_Cash -= 25
            else:
                "You don't have enough for that."   
        "Gifts for Rogue":
            menu:
                "Buy green lace nighty for $75." if "nighty" not in R_Inventory and "r nighty" not in P_Inventory:            
                    if P_Cash >= 75:
                        "You purchase the nighty, this will look nice on Rogue."
                        $ P_Inventory.append("r nighty")
                        $ P_Cash -= 75
                    else:
                        "You don't have enough for that."    
                "Buy black lace bra for $90." if "lace bra" not in R_Inventory and "r lace bra" not in P_Inventory:            
                    if P_Cash >= 90:
                        "You purchase the lace bra, this will look nice on Rogue."
                        $ P_Inventory.append("r lace bra")
                        $ P_Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy black lace panties for $110." if "lace panties" not in R_Inventory and "r lace panties" not in P_Inventory:            
                    if P_Cash >= 110:
                        "You purchase the lace panties, these will look nice on Rogue."
                        $ P_Inventory.append("r lace panties")
                        $ P_Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in R_Inventory and "stockings and garterbelt" not in P_Inventory and ApprovalCheck("Rogue", 1500):          
                    if P_Cash >= 100:
                        "You purchase the stockings, these will look nice on Rogue."             
                        $ P_Inventory.append("stockings and garterbelt")
                        $ P_Cash -= 100
                    else:
                        "You don't have enough for that."   
                "Buy yellow bikini top for $50." if "bikini top" not in R_Inventory and "r bikini top" not in P_Inventory:            
                        if P_Cash >= 50:
                            "You purchase the bikini top, this will look nice on Rogue."
                            $ P_Inventory.append("r bikini top")
                            $ P_Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy green bikini bottoms for $50." if "bikini bottoms" not in R_Inventory and "r bikini bottoms" not in P_Inventory:            
                        if P_Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on Rogue."
                            $ P_Inventory.append("r bikini bottoms")
                            $ P_Cash -= 50
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for Kitty":
            menu:  
                "Buy white lace bra for $90." if "lace bra" not in K_Inventory and "k lace bra" not in P_Inventory:            
                    if P_Cash >= 90:
                        "You purchase the lace bra, this will look nice on Kitty."
                        $ P_Inventory.append("k lace bra")
                        $ P_Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in K_Inventory and "k lace panties" not in P_Inventory:            
                    if P_Cash >= 110:
                        "You purchase the lace panties, these will look nice on Kitty."
                        $ P_Inventory.append("k lace panties")
                        $ P_Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Buy blue cat bikini top for $60." if "bikini top" not in K_Inventory and "k bikini top" not in P_Inventory:            
                        if P_Cash >= 60:
                            "You purchase the bikini top, this will look nice on Kitty."
                            $ P_Inventory.append("k bikini top")
                            $ P_Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy blue bikini bottoms for $60." if "bikini bottoms" not in K_Inventory and "k bikini bottoms" not in P_Inventory:            
                        if P_Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on Kitty."
                            $ P_Inventory.append("k bikini bottoms")
                            $ P_Cash -= 60
                        else:
                            "You don't have enough for that."  
                "Buy blue miniskirt for $50." if "blue skirt" not in K_Inventory and "k blue skirt" not in P_Inventory:            
                        if P_Cash >= 50:
                            "You purchase the blue skirt, this will look nice on Kitty."
                            $ P_Inventory.append("k blue skirt")
                            $ P_Cash -= 50
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for Emma":
            menu:  
                "Buy white lace bra for $90." if "lace bra" not in E_Inventory and "e lace bra" not in P_Inventory:            
                        if P_Cash >= 90:
                            "You purchase the lace bra, this will look nice on Emma."
                            $ P_Inventory.append("e lace bra")
                            $ P_Cash -= 90
                        else:
                            "You don't have enough for that."
                "Buy white lace panties for $110." if "lace panties" not in E_Inventory and "e lace panties" not in P_Inventory:            
                        if P_Cash >= 110:
                            "You purchase the lace panties, these will look nice on Emma."
                            $ P_Inventory.append("e lace panties")
                            $ P_Cash -= 110
                        else:
                            "You don't have enough for that."   
                "Buy pantyhose for $50." if "pantyhose" not in E_Inventory and "e pantyhose" not in P_Inventory:          
                    if P_Cash >= 50:
                        "You purchase the hose, these will look nice on Emma."             
                        $ P_Inventory.append("e pantyhose")
                        $ P_Cash -= 50
                    else:
                        "You don't have enough for that."   
                "Buy stockings and garterbelt for $100." if "stockings and garterbelt" not in E_Inventory and "e stockings and garterbelt" not in P_Inventory and ApprovalCheck("Emma", 1500):          
                    if P_Cash >= 100:
                        "You purchase the stockings, these will look nice on Emma."             
                        $ P_Inventory.append("e stockings and garterbelt")
                        $ P_Cash -= 100
                    else:
                        "You don't have enough for that."   
                "Buy white bikini top for $60." if "bikini top" not in E_Inventory and "e bikini top" not in P_Inventory:            
                        if P_Cash >= 60:
                            "You purchase the bikini top, this will look nice on Emma."
                            $ P_Inventory.append("e bikini top")
                            $ P_Cash -= 60
                        else:
                            "You don't have enough for that."
                "Buy white bikini bottoms for $60." if "bikini bottoms" not in E_Inventory and "e bikini bottoms" not in P_Inventory:            
                        if P_Cash >= 60:
                            "You purchase the bikini bottoms, these will look nice on Emma."
                            $ P_Inventory.append("e bikini bottoms")
                            $ P_Cash -= 60
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Gifts for Laura":
            menu:  
                "Buy red corset for $70." if "corset" not in L_Inventory and "l corset" not in P_Inventory:            
                    if P_Cash >= 70:
                        "You purchase the corset, this will look nice on Laura."
                        $ P_Inventory.append("l corset")
                        $ P_Cash -= 70
                    else:
                        "You don't have enough for that."
                "Buy red lace corset for $90." if "lace corset" not in L_Inventory and "l lace corset" not in P_Inventory:            
                    if P_Cash >= 90:
                        "You purchase the lace corset, this will look nice on Laura."
                        $ P_Inventory.append("l lace corset")
                        $ P_Cash -= 90
                    else:
                        "You don't have enough for that."
                "Buy red lace panties for $110." if "lace panties" not in L_Inventory and "l lace panties" not in P_Inventory:            
                    if P_Cash >= 110:
                        "You purchase the lace panties, these will look nice on Laura."
                        $ P_Inventory.append("l lace panties")
                        $ P_Cash -= 110
                    else:
                        "You don't have enough for that."  
                "Buy black bikini top for $50." if "bikini top" not in L_Inventory and "l bikini top" not in P_Inventory:            
                        if P_Cash >= 50:
                            "You purchase the bikini top, this will look nice on Laura."
                            $ P_Inventory.append("l bikini top")
                            $ P_Cash -= 50
                        else:
                            "You don't have enough for that."
                "Buy black bikini bottoms for $50." if "bikini bottoms" not in L_Inventory and "l bikini bottoms" not in P_Inventory:            
                        if P_Cash >= 50:
                            "You purchase the bikini bottoms, these will look nice on Laura."
                            $ P_Inventory.append("l bikini bottoms")
                            $ P_Cash -= 50
                        else:
                            "You don't have enough for that."  
                "Never mind.":
                    pass
        "Buy books":
            menu Shop_Books:
                "Buy \"Dazzler and Longshot\" for $20.":
                    "A sappy romantic novel about two starcrossed lovers."
                    if "Dazzler and Longshot" in P_Inventory:
                        "You already have a copy, and really only need one."
                    elif P_Cash >= 20:                
                        "You purchase the book."
                        $ P_Inventory.append("Dazzler and Longshot")
                        $ P_Cash -= 20
                    else:
                        "You don't have enough for that."        
                "Buy \"256 Shades of Grey\" for $20.":
                    "A gripping sexual thriller about a stern red-headed \"goblin queen\" and her subject."
                    if "256 Shades of Grey" in P_Inventory:
                        "You already have a copy, and really only need one."
                    elif P_Cash >= 20:                
                        "You purchase the book."
                        $ P_Inventory.append("256 Shades of Grey")
                        $ P_Cash -= 20
                    else:
                        "You don't have enough for that."
                "Buy \"Avengers Tower Penthouse\" for $20.":
                    "A book filled with nude pictures of various Avengers, sexy."
                    if "Avengers Tower Penthouse" in P_Inventory:
                        "You already have a copy, and really only need one."
                    elif P_Cash >= 20:                
                        "You purchase the book."
                        $ P_Inventory.append("Avengers Tower Penthouse")
                        $ P_Cash -= 20
                    else:
                        "You don't have enough for that."
                "Back":
                    jump Shop
            jump Shop_Books
        "Buy Cologne":
            if Day < 50:
                "These are currently out of stock, check back later."
                jump Shop
            menu:
                "Examine the Mandrill Cologne (\"Nothin says lovin like a shiny red butt\").":            
                    menu:
                        "This cologne is guaranteed to make women love you more [[+Love]]."
                        "Buy Mandrill Cologne for $150":
                            pass
                        "Never mind.":
                            jump Shop                 
                    if "Mandrill Cologne" in P_Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif P_Cash >= 150:                
                        "You purchase one bottle of Mandrill Cologne."
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Inventory.append("Mandrill Cologne")
                        $ P_Cash -= 150
                    else:
                        "You don't have enough for that."
                "Examine the Purple Rain Cologne (\"They can't resist your charms\").":
                    menu:
                        "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]]."
                        "Buy Purple Rain Cologne for $200":
                            pass
                        "Never mind.":
                            jump Shop   
                    if "Purple Rain Cologne" in P_Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif P_Cash >= 200:                
                        "You purchase one bottle of Purple Rain Cologne."
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Inventory.append("Purple Rain Cologne")
                        $ P_Cash -= 200
                    else:
                        "You don't have enough for that."
                "Examine the Corruption Cologne (\"Let the wild out\").":
                    menu:
                        "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]]."
                        "Buy Corruption Cologne for $250":
                            pass
                        "Never mind.":
                            jump Shop   
                    if "Corruption Cologne" in P_Inventory:
                        "They seem to be out of stock, maybe check back later."
                    elif P_Cash >= 250:                
                        "You purchase one bottle of Corruption Cologne."
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Inventory.append("Corruption Cologne")
                        $ P_Cash -= 250
                    else:
                        "You don't have enough for that."
                "Back":
                    pass                
        "Exit Store":
            return
    jump Shop
return

# end Shop Interface //////////////////////////////////////////////////////////////////////

# Inventory Interface //////////////////////////////////////////////////////////////////////


label Show_Inventory:
    menu:
        "Check Inventory":
            show screen P_Inventory_screen
            "You search your bags. . ."
            hide screen P_Inventory_screen

        "Use items.":
            if P_Inventory == []:
                "There's nothing in here."
                jump Show_Inventory
            menu:
                "View the Mandrill Cologne." if "Mandrill Cologne" in P_Inventory:
                    $ Count = Inventory_Check("Mandrill Cologne")
                    "This cologne is guaranteed to make women love you more [[+Love]]. You have [Count] doses left."
                    "Product warning, any love gained while under the effects may be lost when this wears off, if the limits are reached."
                    menu:
                        "Use it now?"
                        "Yes":
                            if "mandrill" in P_Traits:
                                "You already have this on."
                            if "purple" in P_Traits or "corruption" in P_Traits:
                                "You'll confuse the scent you already have on."
                            else:
                                $ P_Traits.append("mandrill")
                                $ P_Inventory.remove("Mandrill Cologne")   
                        "No":
                            pass
                            
                "View the Purple Rain Cologne." if "Purple Rain Cologne" in P_Inventory:
                    $ Count = Inventory_Check("Purple Rain Cologne")
                    "This cologne is guaranteed to make women more suggestible to your orders until tomorrow [[+Obedience]]. You have [Count] doses left."
                    "Product warning, any obedience gained whie under the effects may be lost when this wears off, if the limits are reached."
                    menu:
                        "Use it now?"
                        "Yes":
                            if "purple" in P_Traits:
                                "You already have this on."
                            if "mandrill" in P_Traits or "corruption" in P_Traits:
                                "You'll confuse the scent you already have on."
                            else:
                                $ P_Traits.append("purple")
                                $ P_Inventory.remove("Purple Rain Cologne") 
                        "No":
                            pass
                            
                "View the Corruption Cologne." if "Corruption Cologne" in P_Inventory:
                    $ Count = Inventory_Check("Corruption Cologne")
                    "This cologne is guaranteed to make women let loose their wild side [[-Inhibition]]. You have [Count] doses left."
                    "Product warning, any Inhibition lost whie under the effects may be regained when this wears off, if the limits are reached."
                    menu:
                        "Use it now?"
                        "Yes":
                            if "corruption" in P_Traits:
                                "You already have this on."
                            if "purple" in P_Traits or "mandrill" in P_Traits:
                                "You'll confuse the scent you already have on."
                            else:
                                $ P_Traits.append("corruption")
                                $ P_Inventory.remove("Corruption Cologne")  
                                    
                        "No":
                            pass    
                
                
                "Exit":
                    return
        "Exit":
                    return
    jump Show_Inventory
# end Inventory Interface //////////////////////////////////////////////////////////////////////


return