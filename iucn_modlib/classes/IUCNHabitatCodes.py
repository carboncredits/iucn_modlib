#!/usr/bin/python3


class IUCNHabitatCodes_v3_1:
    """IUCN Habitat Codes
    
    A Habitat Codes class with useful functions to interpret and translate codes.
    """
    def __init__(self):
        self.codes = {
            "1": "Forest",
            "1.1": "Forest – Boreal",
            "1.2": "Forest – Subarctic",
            "1.3": "Forest – Subantarctic",
            "1.4": "Forest – Temperate",
            "1.5": "Forest – Subtropical/tropical dry",
            "1.6": "Forest – Subtropical/tropical moist lowland",
            "1.7": "Forest – Subtropical/tropical mangrove vegetation above high tide level",
            "1.8": "Forest – Subtropical/tropical swamp",
            "1.9": "Forest – Subtropical/tropical moist montane",

            "2": "Savanna",
            "2.1": "Savanna – Dry",
            "2.2": "Savanna – Moist",

            "3": "Shrubland",
            "3.1": "Shrubland – Subarctic",
            "3.2": "Shrubland – Subantarctic",
            "3.3": "Shrubland – Boreal",
            "3.4": "Shrubland – Temperate",
            "3.5": "Shrubland – Subtropical/tropical dry",
            "3.7": "Shrubland – Subtropical/tropical high altitude",
            "3.6": "Shrubland – Subtropical/tropical moist",
            "3.8": "Shrubland – Mediterranean-type shrubby vegetation",

            "4": "Grassland",
            "4.1": "Grassland – Tundra",
            "4.2": "Grassland – Subarctic",
            "4.3": "Grassland – Subantarctic",
            "4.4": "Grassland – Temperate",
            "4.5": "Grassland – Subtropical/tropical dry",
            "4.6": "Grassland – Subtropical/tropical seasonally wet/flooded",
            "4.7": "Grassland – Subtropical/tropical high altitude",

            "5": "Wetlands (inland)",
            "5.1": "Wetlands (inland) – Permanent rivers/streams/creeks (includes waterfalls)",
            "5.2": "Wetlands (inland) – Seasonal/intermittent/irregular rivers/streams/creeks",
            "5.3": "Wetlands (inland) – Shrub dominated wetlands",
            "5.4": "Wetlands (inland) – Bogs, marshes, swamps, fens, peatlands",
            "5.5": "Wetlands (inland) – Permanent freshwater lakes (over 8 ha)",
            "5.6": "Wetlands (inland) – Seasonal/intermittent freshwater lakes (over 8 ha)",
            "5.7": "Wetlands (inland) – Permanent freshwater marshes/pools (under 8 ha)",
            "5.8": "Wetlands (inland) – Seasonal/intermittent freshwater marshes/pools (under 8 ha)",
            "5.9": "Wetlands (inland) – Freshwater springs and oases",
            "5.10": "Wetlands (inland) – Tundra wetlands (inc. pools and temporary waters from snowmelt)",
            "5.11": "Wetlands (inland) – Alpine wetlands (inc. temporary waters from snowmelt)",
            "5.12": "Wetlands (inland) – Geothermal wetlands",
            "5.13": "Wetlands (inland) – Permanent inland deltas",
            "5.14": "Wetlands (inland) – Permanent saline, brackish or alkaline lakes",
            "5.15": "Wetlands (inland) – Seasonal/intermittent saline, brackish or alkaline lakes and flats",
            "5.16": "Wetlands (inland) – Permanent saline, brackish or alkaline marshes/pools",
            "5.17": "Wetlands (inland) – Seasonal/intermittent saline, brackish or alkaline marshes/pools",
            "5.18": "Wetlands (inland) – Karst and other subterranean hydrological systems (inland)",

            "6": "Rocky Areas (e.g., inland cliffs, mountain peaks)",

            "7": "Caves & Subterranean Habitats (non-aquatic)",
            "7.1": "Caves and Subterranean Habitats (non-aquatic) – Caves",
            "7.2": "Caves and Subterranean Habitats (non-aquatic) – Other subterranean habitats",

            "8": "Desert",
            "8.1": "Desert – Hot",
            "8.2": "Desert – Temperate",
            "8.3": "Desert – Cold",

            "9": "Marine Neritic",
            "9.1": "Marine Neritic – Pelagic",
            "9.2": "Marine Neritic – Subtidal rock and rocky reefs",
            "9.3": "Marine Neritic – Subtidal loose rock/pebble/gravel",
            "9.4": "Marine Neritic – Subtidal sandy",
            "9.5": "Marine Neritic – Subtidal sandy-mud",
            "9.6": "Marine Neritic – Subtidal muddy",
            "9.7": "Marine Neritic – Macroalgal/kelp",
            "9.8": "Marine Neritic – Coral Reef",
            "9.8.1": "Outer reef channel",
            "9.8.2": "Back slope",
            "9.8.3": "Foreslope (outer reef slope)",
            "9.8.4": "Lagoon",
            "9.8.5": "Inter-reef soft substrate",
            "9.8.6": "Inter-reef rubble substrate",
            "9.9": "Seagrass (Submerged)",
            "9.10": "Estuaries",

            "10": "Marine Oceanic",
            "10.1": "Epipelagic (0–200 m)",
            "10.2": "Mesopelagic (200–1,000 m)",
            "10.3": "Bathypelagic (1,000–4,000 m)",
            "10.4": "Abyssopelagic (4,000–6,000 m)",

            "11": "Marine Deep Ocean Floor (Benthic and Demersal)",
            "11.1": "Continental Slope/Bathyl Zone (200–4,000 m)",
            "11.1.1": "Hard Substrate",
            "11.1.2": "Soft Substrate",
            "11.2": "Abyssal Plain (4,000–6,000 m)",
            "11.3": "Abyssal Mountain/Hills (4,000–6,000 m)",
            "11.4": "Hadal/Deep Sea Trench (>6,000 m)",
            "11.5": "Seamount",
            "11.6": "Deep Sea Vents (Rifts/Seeps)",

            "12": "Marine Intertidal",
            "12.1": "Rocky Shoreline",
            "12.2": "Sandy Shoreline and/or Beaches, Sand Bars, Spits, etc.",
            "12.3": "Shingle and/or Pebble Shoreline and/or Beaches",
            "12.4": "Mud Shoreline and Intertidal Mud Flats",
            "12.5": "Salt Marshes (Emergent Grasses)",
            "12.6": "Tidepools",
            "12.7": "Mangrove Submerged Roots",

            "13": "Marine Coastal/Supratidal",
            "13.1": "Sea Cliffs and Rocky Offshore Islands",
            "13.2": "Coastal Caves/Karst",
            "13.3": "Coastal Sand Dunes",
            "13.4": "Coastal Brackish/Saline Lagoons/Marine Lakes",
            "13.5": "Coastal Freshwater Lakes",

            "14": "Artificial - Terrestrial",
            "14.1": "Arable Land",
            "14.2": "Pastureland",
            "14.3": "Plantations",
            "14.4": "Rural Gardens",
            "14.5": "Urban Areas",
            "14.6": "Subtropical/Tropical Heavily Degraded Former Forest",

            "15": "Artificial - Aquatic",
            "15.1": "Water Storage Areas [over 8 ha]",
            "15.2": "Ponds [below 8 ha]",
            "15.3": "Aquaculture Ponds",
            "15.4": "Salt Exploitation Sites",
            "15.5": "Excavations (open)",
            "15.6": "Wastewater Treatment Areas",
            "15.7": "Irrigated Land [includes irrigation channels]",
            "15.8": "Seasonally Flooded Agricultural Land",
            "15.9": "Canals and Drainage Channels, Ditches",
            "15.10": "Karst and Other Subterranean Hydrological Systems [human-made]",
            "15.11": "Marine Anthropogenic Structures",
            "15.12": "Mariculture Cages",
            "15.13": "Mari/Brackish-culture Ponds",

            "16": "Introduced Vegetation",
 
            "17": "Other",
 
            "18": "Unknown"
            }

    def isValid(self, c):
        """Is the code valid?

            Args:
                c (str): An IUCN habitat code (str or str- castable)

            Returns:
                bool: True if c is a valid IUCN habitat code v3.1, False otherwise.

            Examples:
                isValid(2)           -> True
                isValid('1.2')       -> True
                isValid('1.2.3.4')   -> False
                isValid('Apple pie') -> False
        """
        c = str(c)
        return c in self.codes.keys()

    def codeName(self, c):
        """Convert a habitat code into its name

            Args:
                c (str): An IUCN habitat code (str or str- castable)
            
            Retruns:
                str: The habitat type's name

            Example:
                codeName('1.1') -> 'Forest – Boreal'
        """
        c = str(c)
        if not self.isValid(c):
            raise ValueError(f'Invalid habitat code {c}')
        return self.codes[c]

    def codeLevel(self, c):
        """Convert a habitat code into its level

            Args:
                c (str): An IUCN habitat code (str or str- castable)
            
            Retruns:
                int: The habitat type's level

            Examples:
                codeLevel('11')     -> 1
                codeLevel('11.1')   -> 2
                codeLevel('11.1.1') -> 3
        """
        c = str(c)
        if not self.isValid(c):
            raise ValueError(f'Invalid habitat code {c}')
        return len(c.split('.'))

    def hasLower(self, c):
        """Does the habitat code have a lower level?

            Args:
                c (str): An IUCN habitat code (str or str- castable)
            
            Retruns:
                bool: True if a lower level exists, False otherwise

            Examples:
                hasLower('11')     -> False
                hasLower('11.1')   -> True
                hasLower('11.1.1') -> True
        """
        c = str(c)
        if not self.isValid(c):
            raise ValueError(f'Invalid habitat code {c}')
        return self.codeLevel(c) > 1

    def hasUpper(self, c):
        """Does the habitat code have an upper level?

            Args:
                c (str): An IUCN habitat code (str or str- castable)
            
            Retruns:
                bool: True if an upper level exists, False otherwise

            Examples:
                hasUpper('11')     -> True
                hasUpper('11.1')   -> True
                hasUpper('11.1.1') -> False
                hasUpper('17')     -> False
        """
        c = str(c)
        if not self.isValid(c):
            raise ValueError(f'Invalid habitat code {c}')
        return self.isValid(c + '.1')

    def _toUpper(self, c):
        """Internal: get the code's upper levels

            Args:
                c (str): An IUCN habitat code (str or str- castable)
            
            Retruns:
                list: IUCN habitat codes (str) in the upper level
                    If the code has no upper levels, the output will be a list
                    with only the current level, as this is technically the only
                    habitat code available at the upper resolution.

            Examples:
                _toUpper('13') -> ['13.1', '13.2', '13.3', '13.4', '13.5']
                _toUpper('17') -> ['17]
        """
        c = str(c)
        if not self.isValid(c):
            raise ValueError(f'Invalid habitat code {c}')
        upperCodes = []
        iter = 1
        iterCode = f'{c}.{str(iter)}'
        while self.isValid(iterCode):
            upperCodes.append(iterCode)
            iter += 1
            iterCode = f'{c}.{str(iter)}'
        if len(upperCodes) == 0:
            upperCodes.append(c)
        return upperCodes

    def toLevel(self, c, l):
        """Convert a habitat code to a different level

            Args:
                c (str, list or tuple): An IUCN habitat code
                    An element, list or tuple of str or str-castable elements.
                l (int): A level (1, 2 or 3)
            
            Retruns:
                list: IUCN habitat codes (str) at the desired level
                    If the code has no upper levels, the output will be a list
                    with the highest levels, available.

            Examples:
                toLevel('1.2', 1)    -> ['1']
                toLevel('11.1.1', 2) -> ['11.1']
                toLevel('11', 3)     -> ['11.1.1', '11.1.2', '11.2', '11.3', '11.4', '11.5', '11.6']
                toLevel('17', 3)     -> ['17']
                toLevel('1.2', 2)    -> ['1.2']
        """

        if l not in (1,2,3):
            raise ValueError('Invalid level')

        if type(c) in (list, tuple):
            output = []
            for cc in c:
                output.extend(self.toLevel(cc, l))
            output = list(set(output))
            output = sorted(output, key=lambda x: int(x.replace('.','')))
            return output
        else:
            c = str(c)

        if not self.isValid(c):
            raise ValueError(f'Invalid habitat code {c}')
        if self.codeLevel(c) == l:
            code = [c]
            return code
        if self.codeLevel(c) > l:
            code = ['.'.join(c.split('.')[:l])]
            return code
        if self.codeLevel(c) < l:
            steps = l - self.codeLevel(c)
            codes = [c]
            for _ in range(steps):
                upperCodes = []
                for c in codes:
                    upperCodes.extend(self._toUpper(c))
                codes = upperCodes
            return codes

    def levelCodes(self, l = None):
        """Get all valid habitat codes at a level

            Args:
                l (int): The desired level
            
            Returns:
                list: IUCN habitat codes (str)
                    All valid habitat codes at a level.
                    If a code has no upper level, it will go to the highest
                    level available, as these represent the highest thematic
                    resolution available.
                    For example, codes 16, 17 and 18 will be returned for all
                    calls of the function.

                    If l is not provided, it will return a list of all habitat
                    codes at all levels.
        """
        if l is None:
            codes = [k for k in self.codes.keys()]
            return codes
        else:
            codes = []
            for c in self.codes.keys():
                codes.extend(self.toLevel(c,l))
            uniqueCodes = []
            for code in codes:
                if code not in uniqueCodes:
                    uniqueCodes.append(code)
            codes = uniqueCodes
            return codes

    def levelNames(self, l = None):
        """Get all valid habitat names at a level

            Args:
                l (int): The desired level
            
            Returns:
                list: IUCN habitat names (str)
                    All valid habitat names at a level.
                    If a code has no upper level, it will go to the highest
                    level available, as these represent the highest thematic
                    resolution available.
                    For example, habitat names for codes 16, 17 and 18 will be
                    returned for all calls of the function.

                    If l is not provided, it will return a list of all habitat
                    codes at all levels.
        """
        codes = self.levelCodes(l)
        names = [self.codes[c] for c in codes]
        return names


# HIC SVNT DRACONES