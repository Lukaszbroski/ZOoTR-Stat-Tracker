


class Location(object):

    # for ruleset, I will split with ","

    #### input = string and delimiter. "Iron Boots, Hookshot", "," -> "Iron Boots" "Hookshot"
    # delimiters , = all required
    # / = exchangable requirements (Strength upgrade, bombchus / bombs)
    # - = what level do I need of this item
    # + = I need this + that to make it work.
    #### _ = Split each set of requirements.

    #### Order is:
    # _ to seperate each set of Item Requirements (Set x _OR_ set Y _OR_ Item z) to grab this item. (First OR Operator)
    # , to seperate each item in each set or each duo in each set. (AND operator that works BEFORE OR splitting)
    # / to Seperate OR checks on the single item level.
    # ***** OR SPLITTING COMES BEFORE THIS AND SPLITTING ***** If you cannot make it work with / and +, use _ to split it into sets
    # + to seperate AND checks (AND operator that works AFTER OR single level splitting)
    #### - to seperate item level requirements from the item.

    #### Big Logic test that should verify this works in all ways
    # Total Requirements in 1 string
    #### 1-x,2/3,4,6_7/8/9,1/2,3-4_5 : 6/7-x,8,9_1/2

    #### first well only process Required, to show minimum requirements of all the sets and store them in a list
    # [
    # 1-x,2/3+4,6   ,
    # 7/8/9,1/2,3-4   ,
    # 5
    #### ]

    #### Next well process each seperate item requirement in each set. and store them into a list of their own. Only 1 set needs to return true to pass.
    # [
    # 1-x   ,
    # 2/3+4-x   ,
    # 6
    # ]

    # [
    # 7/8/9   ,
    # 1/2   ,
    # 3-4
    # ]

    # [
    # 5
    #### ]

    #### Next well split up the items in the list even further to check each OR
    # [
    # 1-x   ,
    # [ 2 , 3+4-x ]   , -> [ 2 , [ 3 , 4-x] ]
    # 4   ,
    # 6   ,
    # ]

    # [
    # [ 7 , 8 , 9 ]   ,
    # [ 1 , 2 ]   ,
    # 3-4
    # ]

    # [
    # 5
    #### ]

    # Now We will directly check each item in the list for a boolean of true or not whether we have it.
    # It will generate a boolean for each List and will see if any are true.
    # As processing it will grab the Highest sphere number of each requirement we HAVE, and will return that sphere number + 1 for Required Sphere

    # Next it will process the Logic Items following the same steps, and will generate the Logic Sphere #

    # It will process the whole list twice in order to get a Required # and a Logic # for each item, and what is Required, and what it required for Logic.




    def __init__(self, name = '', ruleset = '', requirements = '', logic = ''):
        self.name = name
        self.ruleset = ruleset
        self.requirements = requirements
        self.logic = logic

class Location_List:
    def __init__(self):
        self.location_table = []
        self.location_table.append(Location('Links Pocket',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Morpha',
                                            'accessible',
                                            'Hookshot-2,Iron Boots,Boss Key Water Temple',
                                            '-1'))
        self.location_table.append(Location('Twinrova',
                                            'accessible',
                                            'Mirror Shield,Hookshot,Boss Key Spirit Temple,Small Key Spirit Temple-4,Strength-2,Bombs/Bombchus',
                                            'Small Key Spirit Temple-5,Mirror Shield,Hookshot,Boss Key Spirit Temple,Strength-2,Bombs'))
        self.location_table.append(Location('Bongo Bongo',
                                            'accessible',
                                            'Hookshot,Hookshot-2+Ocarina/Bow/Bombchus,Boss Key Shadow Temple,Small Key Shadow Temple-5',
                                            'Hookshot,Boss Key Shadow Temple,Small Key Shadow Temple-5,Lens,Magic,Bow/Hookshot-2+Ocarina'))
        self.location_table.append(Location('Barinade',
                                            'accessible',
                                            'Boomerang,Ruto,Bottle,Scale/bombs,',
                                            'Boomerang,Ruto,Bottle,Scale/bombs,Lullaby'))
        self.location_table.append(Location('Phantom Ganon',
                                            'accessible',
                                            'Bow,Hookshot,Boss Key Forest Temple,Small Key Forest Temple-6',
                                            '-1'))
        self.location_table.append(Location('Volvagia',
                                            'accessible',
                                            'Hammer,Boss Key Fire Temple',
                                            'Hammer,Boss Key Fire Temple,Hover Boots/Small Key Fire Temple-7,Goron Tunic'))
        self.location_table.append(Location('Queen Gohma',
                                            'accessible',
                                            '',
                                            'Slingshot'))
        self.location_table.append(Location('King Dodongo',
                                            'accessible',
                                            'Bombchus+Strength_Hammer+Strength+Adult_Bombs',
                                            'Bombs'))
        self.location_table.append(Location('Song from Saria',
                                            'accessible',
                                            'Weird Egg,Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Song from Ocarina of Time',
                                            'accessible',
                                            'Emerald,Sapphire,Ruby',
                                            '-1'))
        self.location_table.append(Location('Sheik at Colossus',
                                            'accessible',
                                            'Hookshot,Adult_Requiem',
                                            'Requiem_Hookshot-2/Epona,Hookshot-2/Hover Boots,Lens'))
        self.location_table.append(Location('Sheik at Temple',
                                            'accessible',
                                            'Forest Medallion,Adult',
                                            '-1'))
        self.location_table.append(Location('Impa at Castle',
                                            'accessible',
                                            'Weird Egg,Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Sheik in Kakariko',
                                            'accessible',
                                            'Water Medallion,Forest Medallion,Fire Medallion,Adult',
                                            '-1'))
        self.location_table.append(Location('Song at Windmill',
                                            'accessible',
                                            'Adult',
                                            '-1'))
        self.location_table.append(Location('Song from Composer Grave',
                                            'accessible',
                                            'Lullaby,Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Sheik in Crater',
                                            'accessible',
                                            'Adult,Hookshot+Bombchu/Hookshot-2+Ocarina:Hover Boots_Hookshot+Bombs/Bow_Bolero',
                                            'Adult,Hookshot,Bombs/Bow_Adult,Hookshot-2,Ocarina_Adult,Hover Boots_Bolero,Adult'))
        self.location_table.append(Location('Sheik in Ice Cavern',
                                            'accessible',
                                            'Adult,Ruto,Bottle,Hover Boots/Lullaby',
                                            'Lullaby,Adult,Ruto,Bottle'))
        self.location_table.append(Location('Song from Malon',
                                            'accessible',
                                            'Hyrule Entry,Weird egg,Ocarina',
                                            '-1'))
        self.location_table.append(Location('Sheik Forest Song',
                                            'accessible',
                                            'Adult',
                                            'Adult,Saria/Minuet'))
        self.location_table.append(Location('Kokiri Sword Chest',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Mido Chest Top Left',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Mido Chest Top Right',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Mido Chest Bottom Left',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Mido Chest Bottom Right',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Skull Kid',
                                            'accessible',
                                            'Ocarina,Saria',
                                            '-1'))
        self.location_table.append(Location('Ocarina Memory Game',
                                            'accessible',
                                            'Ocarina',
                                            '-1'))
        self.location_table.append(Location('Target in Woods',
                                            'accessible',
                                            'Slingshot',
                                            '-1'))
        self.location_table.append(Location('LW Deku Scrub Deku Stick Upgrade',
                                            'accessible',
                                            '',
                                            ''))
        self.location_table.append(Location('Underwater Bottle',
                                            'accessible',
                                            'Scale',
                                            '-1'))
        self.location_table.append(Location('Lake Hylia Sun',
                                            'accessible',
                                            'Adult,Bow,Water Medallion/Hookshot-2+Ocarina',
                                            '-1'))
        self.location_table.append(Location('Lake Hylia Freestanding PoH',
                                            'accessible',
                                            'Adult,Hookshot+Ocarina/Bomb',
                                            '-1'))
        self.location_table.append(Location('Diving in the Lab',
                                            'accessible',
                                            'Adult+Iron Boots+Hookshot/Scale-2',
                                            'Scale-2'))
        self.location_table.append(Location('Child Fishing',
                                            'accessible',
                                            'Kokiri Sword,Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Adult Fishing',
                                            'accessible',
                                            'Adult',
                                            '-1'))
        self.location_table.append(Location('Water Temple Map Chest',
                                            'accessible',
                                            'Adult,Hookshot-2+Scale-2/Hookshot+Iron Boots',
                                            'Adult,Hookshot,Iron Boots'))
        self.location_table.append(Location('Water Temple Compass Chest',
                                            'accessible',
                                            'Adult,Hookshot+Iron Boots/Hookshot-2+Scale-2',
                                            'Adult,Hookshot+Iron Boots'))
        self.location_table.append(Location('Water Temple Torches Chest',
                                            'accessible',
                                            'Adult,Ocarina,Lullaby,Hookshot+Iron Boots/Hookshot-2+Scale-2',
                                            'Adult,Hookshot+Iron Boots,Ocarina,Lullaby'))
        self.location_table.append(Location('Water Temple Dragon Chest',
                                            'accessible',
                                            'Adult,Hookshot+Iron Boots/Hookshot-2+Scale-2,Ocarina,Lullaby/Time+Bow+Water Temple Small Key-2',
                                            'Adult,Hookshot,Iron Boots,Ocarina,Lullaby+Strength/Water Temple Small Key-6+Time+Lullaby+Bow'))
        self.location_table.append(Location('Water Temple Central Bow Target Chest',
                                            'accessible',
                                            'Adult,Hookshot+Iron Boots+Hover Boots/Hookshot-2+Scale-2/Hookshot-2+Iron Boots,Ocarina,Lullaby,Bow,Strength',
                                            'Adult,Hookshot-2/Hover Boots,Hookshot,Bow,Lullaby,Ocarina,Iron Boots,Strength'))
        self.location_table.append(Location('Water Temple Boss Key Chest',
                                            'accessible',
                                            'Adult,Hookshot,Iron Boots/Scale-2+Ocarina+Lullaby+Hookshot-2,Hookshot-2/Hover Boots,Water Temple Small Key-2',
                                            'Adult,Hookshot-2,Strength+Bombs/Hover Boots,Lullaby,Ocarina,Iron Boots,Water Temple Small Key-6'))
        self.location_table.append(Location('Morpha Heart',
                                            'accessible',
                                            'Adult,Hookshot-2,Iron Boots/Scale-2,Water Temple Boss Key',
                                            'Iron Boots, Adult, Water Temple Boss Key,Longshot'))
        self.location_table.append(Location('Water Temple Central Pillar Chest',
                                            'accessible',
                                            'Adult,Iron Boots,Hookshot,Ocarina,Lullaby,Water Temple Small Key,Zora Tunic',
                                            'Adult,Iron Boots,Hookshot,Bow/Dins/Water Temple Small Key-5,Ocarina,Lullaby'))
        self.location_table.append(Location('Water Temple Cracked Wall Chest',
                                            'accessible',
                                            'Adult,Hookshot,Iron Boots/Scale-2+Hookshot-2,Ocarina,Lullaby,Bombs/Bombchus',
                                            'Adult,Iron Boots,Hookshot,Ocarina,Lullaby,Bow/Dins/Water Temple Small Key-5,Bombs'))
        self.location_table.append(Location('Water Temple Dark Link Chest',
                                            'accessible',
                                            'Adult,Hookshot,Iron Boots/Scale-2,Water Temple Small Key-2',
                                            'Adult,Hookshot,Water Temple Small Key-6'))
        self.location_table.append(Location('Water Temple River Chest',
                                            'accessible',
                                            'Adult,Hookshot,Iron Boots/Scale-2,Water Temple Small Key-2,Bow,Time,Ocarina',
                                            'Adult,Hookshot,Iron Boots,Water Temple Small Key-6,Lullaby,Ocarina,Time,Bow'))
        self.location_table.append(Location('Gerudo Valley Waterfall Freestanding PoH',
                                            'accessible',
                                            'Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Gerudo Valley Crate Freestanding PoH',
                                            'accessible',
                                            'Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Gerudo Valley Hammer Rocks Chest'
                                            'accessible',
                                            'Hammer,Requiem/Epona+Ocarina/Hookshot/GTG Entry,Adult',
                                            'Hammer,Epona+Ocarina/Hookshot-2/GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Fortress Rooftop Chest',
                                            'accessible',
                                            'Hookshot+Ocarina/Hover Boots/Hookshot-2,Requiem/Epona+Ocarina/Hookshot/GTG Entry,Adult',
                                            'Hover Boots/Hookshot+Ocarina/Hookshot-2,Hookshot-2/Epona+Ocarina/GTG Entry, Adult'))
        self.location_table.append(Location('Horseback Archery 1000 Points',
                                            'accessible',
                                            'GTG Entry,Epona,Ocarina,Bow,Adult',
                                            '-1'))
        self.location_table.append(Location('Horseback Archery 1500 Points',
                                            'accessible',
                                            'GTG Entry,Epona,Ocarina,Bow,Adult',
                                            '-1'))
        self.location_table.append(Location('Haunted Wasteland Structure Chest',
                                            'accessible',
                                            'GTG Entry/Requiem+Ocarina,Magic,Fire Arrows+Bow/Dins',
                                            'GTG Entry,Magic,Fire Arrows+Bow/Dins'))
        self.location_table.append(Location('Colossus Freestanding PoH',
                                            'accessible',
                                            'Bombs/Bombchus/Scale,Reqiuem,Ocarina,Adult',
                                            'Bombs/Scale,Requiem,Adult,Ocarina'))
        self.location_table.append(Location('Desert Colossus Fairy Reward',
                                            'accessible',
                                            'Bombs/Bombchus,Ocarina,Lullaby,Requiem/GTG Entry',
                                            'Bombs,Ocarina,Lullaby,GTG Entry/Requiem'))
        self.location_table.append(Location('Gerudo Training Grounds Lobby Left Chest',
                                            'accessible',
                                            'GTG Entry,Bow,Adult',
                                            '-1'))
        self.location_table.append(Location('Gerudo Training Grounds Lobby Right Chest',
                                            'accessible',
                                            'GTG Entry,Bow,Adult',
                                            '-1'))
        self.location_table.append(Location('Gerudo Training Grounds Stalfos Chest',
                                            'accessible',
                                            'GTG Entry,Adult'
                                            '-1'))
        Gerudo Training Grounds Beamos Chest
        Gerudo Training Grounds Hidden Ceiling Chest
        Gerudo Training Grounds Maze Path First Chest
        Gerudo Training Grounds Maze Path Second Chest
        Gerudo Training Grounds Maze Path Third Chest
        Gerudo Training Grounds Maze Path Final Chest
        Gerudo Training Grounds Maze Right Central Chest
        Gerudo Training Grounds Maze Right Side Chest
        Gerudo Training Grounds Freestanding Key
        Gerudo Training Grounds Underwater Silver Rupee Chest
        Gerudo Training Grounds Hammer Room Clear Chest
        Gerudo Training Grounds Hammer Room Switch Chest
        Gerudo Training Grounds Eye Statue Chest
        Gerudo Training Grounds Near Scarecrow Chest
        Gerudo Training Grounds Before Heavy Block Chest
        Gerudo Training Grounds Heavy Block First Chest
        Gerudo Training Grounds Heavy Block Second Chest
        Gerudo Training Grounds Heavy Block Third Chest
        Gerudo Training Grounds Heavy Block Fourth Chest
        Spirit Temple Child Left Chest
        Spirit Temple Child Right Chest
        Spirit Temple Child Climb East Chest
        Spirit Temple Child Climb North Chest
        Spirit Temple Compass Chest
        Spirit Temple Early Adult Right Chest
        Spirit Temple First Mirror Right Chest
        Spirit Temple First Mirror Left Chest
        Spirit Temple Map Chest
        Spirit Temple Sun Block Room Chest
        Spirit Temple Statue Hand Chest
        Spirit Temple NE Main Room Chest
        Silver Gauntlets Chest
        Mirror Shield Chest
        Spirit Temple Near Four Armos Chest
        Spirit Temple Hallway Left Invisible Chest
        Spirit Temple Hallway Right Invisible Chest
        Spirit Temple Boss Key Chest
        Spirit Temple Topmost Chest
        Twinrova Heart
        Zelda
        Hyrule Castle Fairy Reward
        Ganons Castle Fairy Reward
        10 Big Poes
        Child Shooting Gallery
        Bombchu Bowling Bomb Bag
        Bombchu Bowling Piece of Heart
        Treasure Chest Game
        Dog Lady
        Man on Roof
        Anju as Adult
        Anjus Chickens
        10 Gold Skulltulla Reward
        20 Gold Skulltulla Reward
        30 Gold Skulltulla Reward
        40 Gold Skulltulla Reward
        50 Gold Skulltulla Reward
        Impa House Freestanding PoH
        Windmill Freestanding PoH
        Adult Shooting Gallery
        Bottom of the Well Front Left Hidden Wall
        Bottom of the Well Front Center Bombable
        Bottom of the Well Right Bottom Hidden Wall
        Bottom of the Well Center Large Chest
        Bottom of the Well Center Small Chest
        Bottom of the Well Back Left Bombable
        Bottom of the Well Freestanding Key
        Bottom of the Well Defeat Boss
        Bottom of the Well Invisible Chest
        Bottom of the Well Underwater Front Chest
        Bottom of the Well Underwater Left Chest
        Bottom of the Well Basement Chest
        Bottom of the Well Locked Pits
        Bottom of the Well Behind Right Grate
        Graveyard Freestanding PoH
        Gravedigging Tour
        Shield Grave Chest
        Heart Piece Grave Chest
        Composer Grave Chest
        Hookshot Chest
        Dampe Race Freestanding PoH
        Shadow Temple Map Chest
        Shadow Temple Hover Boots Chest
        Shadow Temple Compass Chest
        Shadow Temple Early Silver Rupee Chest
        Shadow Temple Invisible Blades Visible Chest
        Shadow Temple Invisible Blades Invisible Chest
        Shadow Temple Falling Spikes Lower Chest
        Shadow Temple Falling Spikes Upper Chest
        Shadow Temple Falling Spikes Switch Chest
        Shadow Temple Invisible Spikes Chest
        Shadow Temple Freestanding Key
        Shadow Temple Wind Hint Chest
        Shadow Temple After Wind Enemy Chest
        Shadow Temple After Wind Hidden Chest
        Shadow Temple Spike Walls Left Chest
        Shadow Temple Boss Key Chest
        Shadow Temple Hidden Floormaster Chest
        Bongo Bongo Heart
        Death Mountain Bombable Chest
        DM Trail Freestanding PoH
        Goron City Leftmost Maze Chest
        Goron City Left Maze Chest
        Goron City Right Maze Chest
        Goron City Pot Freestanding PoH
        Rolling Goron as Child
        Link the Goron
        Darunias Joy
        DM Crater Wall Freestanding PoH
        Biggoron
        DM Crater Volcano Freestanding PoH
        Crater Fairy Reward
        Mountain Summit Fairy Reward
        Frog Ocarina Game
        Frogs in the Rain
        Zora River Lower Freestanding PoH
        Zora River Upper Freestanding PoH
        Diving Minigame
        Zoras Domain Torch Run
        King Zora Thawed
        Zoras Fountain Iceberg Freestanding PoH
        Zoras Fountain Bottom Freestanding PoH
        Ice Cavern Map Chest
        Ice Cavern Compass Chest
        Ice Cavern Iron Boots Chest
        Ice Cavern Freestanding PoH
        Zoras Fountain Fairy Reward
        Boomerang Chest
        Jabu Jabus Belly Map Chest
        Jabu Jabus Belly Compass Chest
        Barinade Heart
        Talons Chickens
        Lon Lon Tower Freestanding PoH
        Forest Temple First Chest
        Forest Temple Chest Behind Lobby
        Forest Temple Well Chest
        Forest Temple Map Chest
        Forest Temple Outside Hookshot Chest
        Forest Temple Falling Room Chest
        Forest Temple Block Push Chest
        Forest Temple Boss Key Chest
        Forest Temple Floormaster Chest
        Forest Temple Bow Chest
        Forest Temple Red Poe Chest
        Forest Temple Blue Poe Chest
        Forest Temple Near Boss Chest
        Phantom Ganon Heart
        Fire Temple Chest Near Boss
        Fire Temple Fire Dancer Chest
        Fire Temple Boss Key Chest
        Fire Temple Big Lava Room Bombable Chest
        Fire Temple Big Lava Room Open Chest
        Volvagia Heart
        Fire Temple Boulder Maze Lower Chest
        Fire Temple Boulder Maze Upper Chest
        Fire Temple Boulder Maze Side Room
        Fire Temple Boulder Maze Bombable Pit
        Fire Temple Scarecrow Chest
        Fire Temple Map Chest
        Fire Temple Compass Chest
        Fire Temple Highest Goron Chest
        Fire Temple Megaton Hammer Chest
        Ganons Castle Forest Trial Chest
        Ganons Castle Water Trial Left Chest
        Ganons Castle Water Trial Right Chest
        Ganons Castle Shadow Trial First Chest
        Ganons Castle Shadow Trial Second Chest
        Ganons Castle Spirit Trial First Chest
        Ganons Castle Spirit Trial Second Chest
        Ganons Castle Light Trial First Left Chest
        Ganons Castle Light Trial Second Left Chest
        Ganons Castle Light Trial Third Left Chest
        Ganons Castle Light Trial First Right Chest
        Ganons Castle Light Trial Second Right Chest
        Ganons Castle Light Trial Third Right Chest
        Ganons Castle Light Trail Invisible Enemies Chest
        Ganons Castle Light Trial Lullaby Chest
        Ganons Tower Boss Key Chest
        Kokiri Forest Storms Grotto Chest
        Lost Woods Generic Grotto Chest
        Deku Theater Skull Mask
        Deku Theater Mask of Truth
        LW Grotto Deku Scrub Deku Nut Upgrade
        Wolfos Grotto Chest
        Remote Southern Grotto Chest
        Field Near Lake Outside Fence Grotto Chest
        HF Grotto Deku Scrub Piece of Heart
        Field West Castle Town Grotto Chest
        Tektite Grotto Freestanding PoH
        Redead Grotto Chest
        Kakariko Back Grotto Chest
        Mountain Storms Grotto Chest
        Top of Crater Grotto Chest
        Zora River Plateau Open Grotto Chest
        Deku Tree Lobby Chest
        Deku Tree Compass Chest
        Deku Tree Compass Room Side Chest
        Deku Tree Basement Chest
        Deku Tree Slingshot Chest
        Deku Tree Slingshot Room Side Chest
        Queen Gohma Heart
        Dodongos Cavern Map Chest
        Dodongos Cavern Compass Chest
        Dodongos Cavern Bomb Flower Platform
        Dodongos Cavern Bomb Bag Chest
        Dodongos Cavern End of Bridge Chest
        Chest Above King Dodongo
        King Dodongo Heart