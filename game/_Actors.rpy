init -1 python:

    class Player(object):
    #''' Player object holds player data and does not
    #    control player interactions.'''
        def __init__(self, name = "Zero", color = "green"):
            # default player name is Zero
            self.name = name
            # Color can currently be green, white, or black. May need checker.
            self.color = color
            # Set level of the player to 1. May add func to calc level.
            self.level = 1
            # Set current xp to 0
            self.xp = 0
            # Used when upgrading skills 
            self.statpoints = 0
            # Amount of reputation
            self.rep = 0

            # Store sex stats together in a dict
            self.sex = {
                focus : 0,                      #progress towards orgasm
                focusX : 0,                     #when using focus to last longer
                semen : 3,                      #available semen
                semenMax : 3,                   #amount it maxes out at
                SEXP : 0,                       #how much sex you've had overall
                stamina : 0,                    #available stamina
                staminaMax : 0,                 #amount it maxes out at
                }
            # Inventory is a simple list.
            self.inventory = []
            # Money is stored as a separate value. Default start of $0
            self.cash = 0
            # Set an initial income value.
            self.income = 10

    class Girl(object):
        """docstring for Girl"""
        def __init__(
                self,
                name,
                inbt = 0,
                love = 0,
                lust = 0,
                obed = 0,
                addictionRate = 0,

            ):
            # Basic information:
            self.name = name
            self.inbt = inbt
            self.love = love
            self.lust = lust
            self.obed = obed
            self.xp = 0
            self.level = 0


            # Sex Stats:
            self.sex = {
                'actions': 3,
                'addiction': 0,
                'addictionRate': 0,
                'addictionResist': 0,
                'cheatedOn': 0,
                }

            # Seen counts.
            self.seen = {
                'bra': 0,
                'chest': 0,
                'panties': 0,
                'penis': 0,
                'pussy': 0,
                }

            # Sex history. Why is so much recorded? Trim if possible.
            # Lets move sexCounts to some sort of stats holder.
            self.sexCounts = {
                'anal': 0,
                'assSlapped': 0,
                'blowjob': 0,
                'caught': 0,
                'creamedAss': 0,
                'creamedPussy': 0,
                'dildoAss': 0,
                'dildoPussy': 0,
                'fondledA': 0,
                'fondledB': 0,
                'fondledP': 0,
                'fondledT': 0,
                'footRub': 0,
                'handHold': 0,
                'hotdogged': 0,
                'kissed': 0,
                'lesbian': 0,
                'lesWatch': 0,
                'lickedAss': 0,
                'lickedPenis': 0,
                'massaged': 0,
                'masturbated': 0,
                'orgasmed': 0,
                'sleepOver': 0,
                'stripped': 0,
                'swallowed': 0,
                'usedVibe': 0,
                'usedPlug': 0,
                }
