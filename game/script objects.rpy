init python:

    class Inventory(object):

        def __init__(self, money=0):
            self._lst = []
            self._money = money

        def __getitem__(self, item):
            return self._lst[item]


    class OutfitManager(object):

        def __init__(self, outfits = []):
            _outfits = outfits


    class Outfit(object):

        def __init__(self, name, outfit = [0,0,0,0,0,0,0,0,0,0]):
            self.name = name
            self.UpdateOutfit(outfit)

            self._outfit = [0,0,0,0,0,0,0,0,0,0]

            # Outfit stats
            self._undressed = 0
            self._upSkirt = 0
            self._upTop = 0
            self._pantiesDown = 0

            # Outfit pieces named:
            self.arms = 0
            self.legs = 0
            self.over = 0
            self.neck = 0
            self.chest = 0
            self.panties = 0
            self.acc = 0
            self.hair = 0
            self.hose = 0

        def __getitem__(self, item):
            return self._outfit[item]

        # Calculates shame based off of the pieces in the outfit.
        def _calcShame(self):
            self.shame = 0
            for x in self._outfit:
                self.shame += x._shame
            self.shame += self._undressed * 10

        # Calculates undressed state.
        def _calcUndressed(self):
            if self._outfit[2] and self._outfit[3] and self._outfit[5] and self._outfit[6] == 0:
                self._undressed = 1

        # Sanity check for outfit. Replaces any blanks with '0'.
        def _sanityCheck(self):
            if not self._outfit:
                self._outfit = [0,0,0,0,0,0,0,0,0,0]
            for x in self._outfit:
                if not x:
                    self._outfit[x] = 0

        # Updates outfit from input. Use TempOutfit as input.
        def UpdateOutfit(self, outfit = [0,0,0,0,0,0,0,0,0,0]):
            self._outfit = outfit
            self._sanityCheck()
            self._calcUndressed()
            self._calcShame()

            # Outfit pieces named:
            self.arms = self.outfit[1]
            self.legs = self.outfit[2]
            self.over = self.outfit[3]
            self.neck = self.outfit[4]
            self.chest = self.outfit[5]
            self.panties = self.outfit[6]
            self.acc = self.outfit[7]
            self.hair = self.outfit[8] if self.outfit[8] else self.hair
            self.hose = self.outfit[9]


    class Clothes(object):

        def __init__(self, name, path, shame, price):
            self._name = name
            self._path = path
            self._price = price
            self.shame = shame

        def __str__(self):
            return self._name
