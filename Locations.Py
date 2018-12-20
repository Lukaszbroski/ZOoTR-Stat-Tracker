


class Location:


    # Class Location :
    #
    # Lists all logic that the checks should follow.
    # Logic is written the way below to make things compact and efficient
    # Will check all items against what is stored in the current state, and run through the list each "Sphere"
    # Spheres will raise until all locations are obtainable.




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




    def __init__(self, name = '', ruleset = '', requirements = [], logic = []):
        self.name = name
        self.ruleset = ruleset
        self.requirements = requirements
        self.logic = logic

class Location_List:
    def __init__(self):
        self.location_table = []
        self.location_table.append(Location('Links Pocket',
                                            'accessible',
                                            (),
                                            ()))
        self.location_table.append(Location('Morpha',
                                            'accessible',
                                            (lambda state: state.has('Longshot') and state.has('Adult') and state.has('Iron_Boots') and state.has('Boss_Key_Water_Temple')),
                                            '-1'))
        self.location_table.append(Location('Twinrova',
                                            'accessible',
                                            'Adult,Mirror,Hookshot,Boss Key Spirit Temple,Small Key Spirit Temple-4,Strength-2,Bombs/Bombchus,Requiem+Ocarina/GTG Entry',
                                            'Adult,Small Key Spirit Temple-5,Mirror,Hookshot,Boss Key Spirit Temple,Strength-2,Bombs/Bombchus,Requiem+Ocarina/GTG Entry+Hover Boots+Lens/GTG Entry+Hookshot-2+Lens'))
        self.location_table.append(Location('Bongo Bongo',
                                            'accessible',
                                            'Adult,Hookshot,Hookshot-2+Ocarina/Bow/Bombchus,Boss Key Shadow Temple,Small Key Shadow Temple-5,Hover Boots,Bombs/Bombchus',
                                            'Adult,Hookshot,Boss Key Shadow Temple,Small Key Shadow Temple-5,Lens,Magic,Ocarina,Lullaby,Bombs/Bombchus,Bow/Hookshot-2,Hover Boots'))
        self.location_table.append(Location('Barinade',
                                            'accessible',
                                            'Boomerang,Ruto,Bottle,Scale/Bombs/Bombchus,',
                                            'Boomerang,Ruto,Bottle,Scale/Bombs+Ocarina+Lullaby/Bombchus+Ocarina+Lullaby,'))
        self.location_table.append(Location('Phantom Ganon',
                                            'accessible',
                                            'Adult,Bow,Hookshot,Boss Key Forest Temple,Small Key Forest Temple-5',
                                            'Adult,Bow,Hookshot,Boss Key Forest Temple,Small Key Forest Temple-5,Saria/Minuet,Ocarina'))
        self.location_table.append(Location('Volvagia',
                                            'accessible',
                                            'Adult,Hammer,Boss Key Fire Temple',
                                            'Adult,Hammer,Boss Key Fire Temple,Hover Boots/Small Key Fire Temple-7,Goron Tunic,Time+Ocarina/Bombs/Bombchus'))
        self.location_table.append(Location('Queen Gohma',
                                            'accessible',
                                            '',
                                            'Slingshot'))
        self.location_table.append(Location('King Dodongo',
                                            'accessible',
                                            'Bombchus+Strength_Hammer+Strength+Adult_Bombs',
                                            'Bombs/Bombchus,Bombs/Strength,Slingshot/Bow/Hover Boots/Hookshot-2'))
        self.location_table.append(Location('Song from Saria',
                                            'accessible',
                                            'Letter',
                                            '-1'))
        self.location_table.append(Location('Song from Ocarina of Time',
                                            'accessible',
                                            'Emerald,Sapphire,Ruby',
                                            '-1'))
        self.location_table.append(Location('Sheik at Colossus',
                                            'accessible',
                                            'GTG Entry,Adult_Requiem+Ocarina',
                                            'Requiem+Ocarina_GTG Entry,Lens,Hookshot-2/Hover Boots'))
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
                                            'Adult,Ocarina',
                                            '-1'))
        self.location_table.append(Location('Song from Composer Grave',
                                            'accessible',
                                            'Lullaby,Ocarina,Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Sheik in Crater',
                                            'accessible',
                                            'Adult+Bolero+Ocarina_Adult,Strength-1/Bombs/Bombchus/Bow,Hover Boots/Hookshot_Hammer/Bombs/Bombchus,Hookshot-2+Ocarina/Hover Boots',
                                            '-1'))
        self.location_table.append(Location('Sheik in Ice Cavern',
                                            'accessible',
                                            'Adult,Ruto,Bottle,Hover Boots/Lullaby+Ocarina,Scale/Bombs/Bombchus',
                                            'Lullaby,Ocarina,Adult,Ruto,Bottle,Scale/Bombs/Bombchus'))
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
                                            'Shield/Nuts/Bombs/Bombchus/Slingshot/Boomerang',
                                            '-1'))
        self.location_table.append(Location('Underwater Bottle',
                                            'accessible',
                                            'Scale',
                                            '-1'))
        self.location_table.append(Location('Lake Hylia Sun',
                                            'accessible',
                                            'Adult,Bow,Hookshot-2+Ocarina/Hookshot-2+Iron Boots+Boss Key Water Temple',
                                            '-1'))
        self.location_table.append(Location('Lake Hylia Freestanding PoH',
                                            'accessible',
                                            'Adult,Hookshot+Ocarina/Bombs/Bombchus/Scale',
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
                                            'Adult,Hookshot+Ocarina/Bombs/Bombchus/Scale',
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
                                            'Adult,Hookshot,Iron Boots,Ocarina,Lullaby+Strength/Water Temple Small Key-6+Time+Lullaby/Keysanity+Bow'))
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
                                            'Adult,Hookshot,Water Temple Small Key-6,Ocarina+Lullaby/Keysanity'))
        self.location_table.append(Location('Water Temple River Chest',
                                            'accessible',
                                            'Adult,Hookshot,Iron Boots/Scale-2,Water Temple Small Key-2,Bow,Time,Ocarina',
                                            'Adult,Hookshot,Iron Boots,Water Temple Small Key-6,Lullaby+Ocarina/Keysanity,Time,Bow'))
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
                                            'GTG Entry,Epona,Ocarina,Bow,Adult'))
        self.location_table.append(Location('Horseback Archery 1500 Points',
                                            'accessible',
                                            'GTG Entry,Epona,Ocarina,Bow,Adult',
                                            'GTG Entry,Epona,Ocarina,Bow,Adult'))
        self.location_table.append(Location('Haunted Wasteland Structure Chest',
                                            'accessible',
                                            'GTG Entry/Requiem+Ocarina,Magic,Fire Arrows+Bow/Dins',
                                            'GTG Entry,Hookshot-2/Hover Boots,Magic,Fire Arrows+Bow/Dins'))
        self.location_table.append(Location('Colossus Freestanding PoH',
                                            'accessible',
                                            'Bombs/Bombchus/Scale,Reqiuem,Ocarina,Adult',
                                            'Bombs/Bombchus/Scale,Requiem,Adult,Ocarina'))
        self.location_table.append(Location('Desert Colossus Fairy Reward',
                                            'accessible',
                                            'Bombs/Bombchus,Ocarina,Lullaby,Requiem/GTG Entry',
                                            'Bombs/Bombchus,Ocarina,Lullaby,GTG Entry+Lens+Magic+Hover Boots/Requiem/GTG Entry+Lens+Magic+Hookshot-2'))
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
        self.location_table.append(Location('Gerudo Training Grounds Beamos Chest',
                                            'accessible',
                                            'GTG Entry,Adult,Bombs/Bombchus',
                                            'GTG Entry,Adult,Bombs/Bombchus'))
        self.location_table.append(Location('Gerudo Training Grounds Hidden Ceiling Chest',
                                            'accessible',
                                            'GTG Key-1,GTG Entry,Adult',
                                            'GTG Key-3,Lens+Magic,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Maze Path First Chest',
                                            'accessible',
                                            'GTG Key-2,GTG Entry,Adult',
                                            'GTG Key-4,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Maze Path Second Chest',
                                            'accessible',
                                            'GTG Key-4,GTG Entry,Adult',
                                            'GTG Key-6,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Maze Path Third Chest',
                                            'accessible',
                                            'GTG Key-5,GTG Entry,Adult',
                                            'GTG Key-7,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Maze Path Final Chest'
                                            'accessible',
                                            'GTG Key-7,GTG Entry,Adult',
                                            'GTG Key-9,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Maze Right Central Chest',
                                            'accessible',
                                            'GTG Key-2/Bombs+Time+Ocarina/Bombchus+Time+Ocarina/Hookshot+Ocarina+Time,GTG Entry,Adult',
                                            'GTG Key-9/Bombs+Time+Ocarina/Bombchus+Time+Ocarina/Hookshot+Lens+Magic+Time+Ocarina,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Maze Right Side Chest',
                                            'accessible',
                                            'GTG Key-2/Bombs+Time+Ocarina/Bombchus+Time+Ocarina/Hookshot+Time+Ocarina,GTG Entry,Adult',
                                            'GTG Key-9/Bombs+Time+Ocarina/Bombchus+Time+Ocarina/Hookshot+Magic+Lens+Ocarina+Time,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Freestanding Key',
                                            'accessible',
                                            'GTG Key-2/Bombs+Time+Ocarina/Bombchus+Time+Ocarina/Hookshot+Ocarina+Time,GTG Entry,Adult',
                                            'GTG Key-9/Bombs+Time+Ocarina/Bombchus+Time+Ocarina/Hookshot+Lens+Magic+Ocarina+Time,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Underwater Silver Rupee Chest',
                                            'accessible',
                                            'Hookshot,Ocarina,Time,Iron Boots,GTG Entry,Adult',
                                            'Hookshot,Ocarina,Time,Iron Boots,Bombs/Bombchus/GTG Key-9/Lens+Magic,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Hammer Room Clear Chest',
                                            'accessible',
                                            'Hookshot,GTG Entry,Adult',
                                            'Hookshot,Bombs/Bombchus/Lens+Magic/GTG Key-9,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Hammer Room Switch Chest',
                                            'accessible',
                                            'Hookshot,GTG Entry,Adult',
                                            'Hookshot,Hammer,Bombs/Bombchus/Lens+Magic/GTG Key-9,GTG Entry,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Eye Statue Chest',
                                            'accessible',
                                            'Hookshot,GTG Entry,Bow,Adult',
                                            'Hookshot,Bow,Lens/Hammer,GTG Entry,GTG Key-9,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Near Scarecrow Chest',
                                            'accessible'
                                            'Hookshot,Bow,GTG Entry,Adult',
                                            'Hookshot,Bow,GTG Entry,Lens+Magic,GTG Key-9,Adult'))
        self.location_table.append(Location('Gerudo Training Grounds Before Heavy Block Chest',
                                            'accessible',
                                            'Hookshot,GTG Entry,Adult',
                                            '-1'))
        self.location_table.append(Location('Gerudo Training Grounds Heavy Block First Chest',
                                            'accessible',
                                            'Hookshot,Strength-2,Adult,GTG Entry',
                                            'Hookshot,Strength-2,Adult,GTG Entry,Lens'))
        self.location_table.append(Location('Gerudo Training Grounds Heavy Block Second Chest',
                                            'accessible',
                                            'Hookshot,Strength-2,Adult,GTG Entry',
                                            'Hookshot,Strength-2,Adult,GTG Entry,Lens'))
        self.location_table.append(Location('Gerudo Training Grounds Heavy Block Third Chest',
                                            'accessible',
                                            'Hookshot,Strength-2,Adult,GTG Entry',
                                            'Hookshot,Strength-2,Adult,GTG Entry,Lens'))
        self.location_table.append(Location('Gerudo Training Grounds Heavy Block Fourth Chest',
                                            'accessible',
                                            'Hookshot,Strength-2,Adult,GTG Entry',
                                            'Hookshot,Strength-2,Adult,GTG Entry,Lens'))
        self.location_table.append(Location('Spirit Temple Child Left Chest',
                                            'accessible',
                                            'Requiem,Ocarina,Boomerang/Slingshot/Bombchus',
                                            'Requiem,Ocarina,Boomerang/Slingshot/Bombchus'))
        self.location_table.append(Location('Spirit Temple Child Right Chest',
                                            'accessible',
                                            'Requiem,Ocarina,Boomerang/Slingshot/Bombchus',
                                            'Requiem,Ocarina,Boomerang/Slingshot/Bombchus'))
        self.location_table.append(Location('Spirit Temple Child Climb East Chest',
                                            'accessible',
                                            'Adult,Strength-2,Requiem+Ocarina/GTG Entry,Spirit Temple Small Key,Bombs/Bombchus/Hookshot/Bow_Requiem,Ocarina,Spirit Temple Small Key,Slingshot/Boomerang/Bombs/Bombchus',
                                            'Adult,GTG Entry+Hover Boots/GTG Entry+Hookshot-2,Lens,Spirit Temple Small key,Strength-2,Bombs/Hookshot+Boomerang/Hookshot+Slingshot/Bow+Boomerang/Bow+Slingshot/Spirit Temple Small Key-3+Strength-2+Hookshot/Spirit Temple Small Key-3+Strength-2+Bow/Spirit Temple Small Key-5+Requiem+Ocarina+Boomerang/Spirit Temple Sall Key-5+Ocarina+Requiem+Slingshot'))
        self.location_table.append(Location('Spirit Temple Child Climb North Chest',
                                            'accessible',
                                            'Adult,Strength-2,Requiem+Ocarina/GTG Entry,Spirit Temple Small Key,Bombs/Bombchus/Hookshot/Bow_Requiem,Ocarina,Spirit Temple Small Key,Slingshot/Boomerang/Bombs/Bombchus',
                                            'Adult,GTG Entry+Hover Boots/GTG Entry+Hookshot-2,Lens,Spirit Temple Small key,Strength-2,Bombs/Hookshot+Boomerang/Hookshot+Slingshot/Bow+Boomerang/Bow+Slingshot/Spirit Temple Small Key-3+Strength-2+Hookshot/Spirit Temple Small Key-3+Strength-2+Bow/Spirit Temple Small Key-5+Requiem+Ocarina+Boomerang/Spirit Temple Sall Key-5+Ocarina+Requiem+Slingshot'))
        self.location_table.append(Location('Spirit Temple Compass Chest',
                                            'accessible',
                                            'Adult,Strength-2,Ocarina,Lullaby,Hookshot,Requiem+Ocarina/GTG Entry',
                                            'Adult,Strength-2,Ocarina,Lullaby,Hookshot,Requiem+Ocarina/GTG Entry+Hover Boots/GTG Entry+Hookshot-2,Lens'))
        self.location_table.append(Location('Spirit Temple Early Adult Right Chest',
                                            'accessible',
                                            'Adult,Strength-2,Bow/Hookshot/Bombs/Bombchus,Requiem+Ocarina/GTG Entry',
                                            'Adult,Strength-2,Bow/Hookshot/Bombs/Bombchus,Requiem+Ocarina/GTG Entry+Hover Boots/GTG Entry+Hookshot-2,Lens'))
        self.location_table.append(Location('Spirit Temple First Mirror Right Chest',
                                            'accessible',
                                            'Adult,Requiem+Ocarina/GTG Entry,Strength-2,Spirit Temple Small Key-3',
                                            'Adult,Requiem+Ocarina/GTG Entry+Hover Boots/GTG Entry+Hookshot-2,Lens'))
        self.location_table.append(Location('Shield Grave Chest',
                                            'accessible',
                                            'Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location('Heart Piece Grave Chest',
                                            'accessible',
                                            'Sun+Ocarina+Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location("Composer Grave Chest",
                                            'accessible',
                                            'Lullaby,Ocarina,Dins/Bow+Fire Arrows+Adult,Magic,Hyrule Entry',
                                            '-1'))
        self.location_table.append(Location("Death Mountain Bombable Chest",
                                            'accessible',
                                            'Bombs/Bombchus/Hammer+Adult',
                                            '-1'))
        self.location_table.append(Location("Goron City Leftmost Maze Chest",
                                            'accessible',
                                            'Adult,Strength-2/Hammer/Bombs+Hover Boots/Bombchus+Hover Boots',
                                            'Adult,Strength-2/Hammer'))
        self.location_table.append(Location("Goron City Right Maze Chest",
                                            'accessible',
                                            'Bombs/Hammer+Adult/Bombchus/Strength-2+Adult',
                                            '-1'))
        self.location_table.append(Location("Goron City Left Maze Chest",
                                            'accessible',
                                            'Bombs/Adult+Hammer/Bombchus/Strength-2+Adult',
                                            '-1'))
        self.location_table.append(Location("Zoras Domain Torch Run",
                                            'accessible',
                                            'Scale/Bombs/Bombchus'
                                            'Bombs+Ocarina+Lullaby/Bombchus+Lullaby+Ocarina/Scale'))
        self.location_table.append(Location("Hookshot Chest",
                                            'accessible',
                                            'Adult',
                                            '-1'))
        self.location_table.append(Location("Redead Grotto Chest",
                                            'accessible',
                                            'Bombs/Bombchus/Hammer+Adult',
                                            '-1'))
        self.location_table.append(Location("Wolfos Grotto Chest",
                                            'accessible',
                                            'Bombs/Bombchus/Hammer+Adult',
                                            'Bombs_Bombchus_Hammer,Ocarina,Saria/Minuet'))
        self.location_table.append(Location("Silver Gauntlets Chest", # fix
                                            'accessible',
                                            'Spirit Temple Small Key-2,Bombs+Ocarina+Requiem/Ocarin+Requiem+Bombchus/Adult+Strength-2+Ocarina+Requiem/Adult+Strength-'
                                            'Spirit Temple Small Key-5,Bombs/Bombchus_Adult,Spirit Temple Small Key-3,Hookshot-2,Bombs/Bombchus'))
        self.location_table.append(Location("Mirror Shield Chest", # fix
                                            'accessible',
                                            'Adult,Strength-2,Spirit Temple Small Key-3,Bombs/Bombchus',
                                            'Ocarina+Requiem/Hookshot-2+Lens+GTG Access/Hover Boots+Lens+GTG Access,Adult,Strength-2,Spirit Temple Small Key-4,Bombs/Bombchus'
"Field West Castle Town Grotto Chest"
"Remote Southern Grotto Chest"
"Field Near Lake Outside Fence Grotto Chest"
"Kakariko Back Grotto Chest"
"Zora River Plateau Open Grotto Chest"
"Kokiri Forest Storms Grotto Chest"
"Lost Woods Generic Grotto Chest"
"Mountain Storms Grotto Chest"
"Top of Crater Grotto Chest"
"Treasure Chest Game"
"Gift from Saria"
"Malon Egg"
"Zeldas Letter"
"Zelda"
"Zoras Fountain Fairy Reward"
"Hyrule Castle Fairy Reward"
"Mountain Summit Fairy Reward"
"Crater Fairy Reward"
"Ganons Castle Fairy Reward"
"Darunias Joy"
"Diving Minigame"
"Link the Goron"
"King Zora Thawed"
"Bombchu Bowling Bomb Bag"
"Bombchu Bowling Piece of Heart"
"Dog Lady"
"10 Gold Skulltula Reward"
"20 Gold Skulltula Reward"
"30 Gold Skulltula Reward"
"40 Gold Skulltula Reward"
"50 Gold Skulltula Reward"
"Man on Roof"
"Frog Ocarina Game"
"Frogs in the Rain"
"Child Shooting Gallery"
"Adult Shooting Gallery"
"Deku Theater Skull Mask"
"Deku Theater Mask of Truth"
"Anju as Adult"
"Biggoron"
"Anjus Chickens"
"Talons Chickens"
"10 Big Poes"
"Rolling Goron as Child"
"Gerudo Fortress Membership Card"
"Ocarina of Time"
"Impa House Freestanding PoH"
"Tektite Grotto Freestanding PoH"
"Windmill Freestanding PoH"
"Dampe Race Freestanding PoH"
"Lon Lon Tower Freestanding PoH"
"Graveyard Freestanding PoH"
"Gravedigging Tour"
"Zora River Lower Freestanding PoH"
"Zora River Upper Freestanding PoH"
"Zoras Fountain Iceberg Freestanding PoH"
"Zoras Fountain Bottom Freestanding PoH"
"DM Trail Freestanding PoH"
"DM Crater Wall Freestanding PoH"
"DM Crater Volcano Freestanding PoH"
"Goron City Pot Freestanding PoH"
"Gerudo Fortress North F1 Carpenter"
"Gerudo Fortress North F2 Carpenter"
"Gerudo Fortress South F1 Carpenter"
"Gerudo Fortress South F2 Carpenter"
"Magic Bean Salesman"
"King Zora Moves"
"Master Sword Pedestal"
"Epona"
"Deku Baba Sticks"
"Deku Baba Nuts"
"Goron City Stick Pot"
"Bottom of the Well Stick Pot"
"Zoras Domain Stick Pot"
"Zoras Domain Nut Pot"
"Spirit Temple Nut Crate"
"Gerudo Fortress Carpenter Rescue"
"Haunted Wasteland Bombchu Salesman"
"Ganons Castle Forest Trial Clear"
"Ganons Castle Fire Trial Clear"
"Ganons Castle Water Trial Clear"
"Ganons Castle Shadow Trial Clear"
"Ganons Castle Spirit Trial Clear"
"Ganons Castle Light Trial Clear"
"Deku Tree Lobby Chest"
"Deku Tree Slingshot Chest"
"Deku Tree Slingshot Room Side Chest"
"Deku Tree Compass Chest"
"Deku Tree Compass Room Side Chest"
"Deku Tree Basement Chest"
"Chest Above King Dodongo"
"Dodongos Cavern Map Chest"
"Dodongos Cavern Compass Chest"
"Dodongos Cavern Bomb Flower Platform"
"Dodongos Cavern Bomb Bag Chest"
"Dodongos Cavern End of Bridge Chest"
"Boomerang Chest"
"Jabu Jabus Belly Map Chest"
"Jabu Jabus Belly Compass Chest"
"Forest Temple First Chest"
"Forest Temple Chest Behind Lobby"
"Forest Temple Well Chest"
"Forest Temple Map Chest"
"Forest Temple Outside Hookshot Chest"
"Forest Temple Falling Room Chest"
"Forest Temple Block Push Chest"
"Forest Temple Boss Key Chest"
"Forest Temple Floormaster Chest"
"Forest Temple Bow Chest"
"Forest Temple Red Poe Chest"
"Forest Temple Blue Poe Chest"
"Forest Temple Near Boss Chest"
"Fire Temple Chest Near Boss"
"Fire Temple Fire Dancer Chest"
"Fire Temple Boss Key Chest"
"Fire Temple Big Lava Room Bombable Chest"
"Fire Temple Big Lava Room Open Chest"
"Fire Temple Boulder Maze Lower Chest"
"Fire Temple Boulder Maze Upper Chest"
"Fire Temple Boulder Maze Side Room"
"Fire Temple Boulder Maze Bombable Pit"
"Fire Temple Scarecrow Chest"
"Fire Temple Map Chest"
"Fire Temple Compass Chest"
"Fire Temple Highest Goron Chest"
"Fire Temple Megaton Hammer Chest"
"Spirit Temple First Mirror Left Chest"
"Spirit Temple Map Chest"
"Spirit Temple Child Climb East Chest"
"Spirit Temple Child Climb North Chest"
"Spirit Temple Sun Block Room Chest"
"Spirit Temple Statue Hand Chest"
"Spirit Temple NE Main Room Chest"
"Spirit Temple Near Four Armos Chest"
"Spirit Temple Hallway Left Invisible Chest"
"Spirit Temple Hallway Right Invisible Chest"
"Spirit Temple Boss Key Chest"
"Spirit Temple Topmost Chest"
"Shadow Temple Map Chest"
"Shadow Temple Hover Boots Chest"
"Shadow Temple Compass Chest"
"Shadow Temple Early Silver Rupee Chest"
"Shadow Temple Invisible Blades Visible Chest"
"Shadow Temple Invisible Blades Invisible Chest"
"Shadow Temple Falling Spikes Lower Chest"
"Shadow Temple Falling Spikes Upper Chest"
"Shadow Temple Falling Spikes Switch Chest"
"Shadow Temple Invisible Spikes Chest"
"Shadow Temple Wind Hint Chest"
"Shadow Temple After Wind Enemy Chest"
"Shadow Temple After Wind Hidden Chest"
"Shadow Temple Spike Walls Left Chest"
"Shadow Temple Boss Key Chest"
"Shadow Temple Hidden Floormaster Chest"
"Shadow Temple Freestanding Key"
"Bottom of the Well Front Left Hidden Wall"
"Bottom of the Well Front Center Bombable"
"Bottom of the Well Right Bottom Hidden Wall"
"Bottom of the Well Center Large Chest"
"Bottom of the Well Center Small Chest"
"Bottom of the Well Back Left Bombable"
"Bottom of the Well Defeat Boss"
"Bottom of the Well Invisible Chest"
"Bottom of the Well Underwater Front Chest"
"Bottom of the Well Underwater Left Chest"
"Bottom of the Well Basement Chest"
"Bottom of the Well Locked Pits"
"Bottom of the Well Behind Right Grate"
"Bottom of the Well Freestanding Key"
"Ice Cavern Map Chest"
"Ice Cavern Compass Chest"
"Ice Cavern Iron Boots Chest"
"Ice Cavern Freestanding PoH"
"Ganons Tower Boss Key Chest"
"Ganons Castle Forest Trial Chest"
"Ganons Castle Water Trial Left Chest"
"Ganons Castle Water Trial Right Chest"
"Ganons Castle Shadow Trial First Chest"
"Ganons Castle Shadow Trial Second Chest"
"Ganons Castle Spirit Trial First Chest"
"Ganons Castle Spirit Trial Second Chest"
"Ganons Castle Light Trial First Left Chest"
"Ganons Castle Light Trial Second Left Chest"
"Ganons Castle Light Trial Third Left Chest"
"Ganons Castle Light Trial First Right Chest"
"Ganons Castle Light Trial Second Right Chest"
"Ganons Castle Light Trial Third Right Chest"
"Ganons Castle Light Trial Invisible Enemies Chest"
"Ganons Castle Light Trial Lullaby Chest"
"Ganon"
"Queen Gohma Heart"
"King Dodongo Heart"
"Barinade Heart"
"Phantom Ganon Heart"
"Volvagia Heart"
"Morpha Heart"
"Twinrova Heart"
"Bongo Bongo Heart"
"GS Deku Tree Basement Back Room"
"GS Deku Tree Basement Gate"
"GS Deku Tree Basement Vines"
"GS Deku Tree Compass Room"
"GS Dodongo's Cavern Vines Above Stairs"
"GS Dodongo's Cavern Scarecrow"
"GS Dodongo's Cavern Alcove Above Stairs"
"GS Dodongo's Cavern Back Room"
"GS Dodongo's Cavern East Side Room"
"GS Jabu Jabu Lobby Basement Lower"
"GS Jabu Jabu Lobby Basement Upper"
"GS Jabu Jabu Near Boss"
"GS Jabu Jabu Water Switch Room"
"GS Forest Temple Outdoor East"
"GS Forest Temple First Room"
"GS Forest Temple Outdoor West"
"GS Forest Temple Lobby"
"GS Forest Temple Basement"
"GS Fire Temple Song of Time Room"
"GS Fire Temple Basement"
"GS Fire Temple Unmarked Bomb Wall"
"GS Fire Temple East Tower Top"
"GS Fire Temple East Tower Climb"
"GS Water Temple South Basement"
"GS Water Temple Falling Platform Room"
"GS Water Temple Central Room"
"GS Water Temple Near Boss Key Chest"
"GS Water Temple Serpent River"
"GS Spirit Temple Hall to West Iron Knuckle"
"GS Spirit Temple Boulder Room"
"GS Spirit Temple Lobby"
"GS Spirit Temple Bomb for Light Room"
"GS Spirit Temple Metal Fence"
"GS Shadow Temple Single Giant Pot"
"GS Shadow Temple Crusher Room"
"GS Shadow Temple Triple Giant Pot"
"GS Shadow Temple Like Like Room"
"GS Shadow Temple Near Ship"
"GS Well Like Like Cage"
"GS Well East Inner Room"
"GS Well West Inner Room"
"GS Ice Cavern Push Block Room"
"GS Ice Cavern Spinning Scythe Room"
"GS Ice Cavern Heart Piece Room"
"GS Hyrule Field Near Gerudo Valley"
"GS Hyrule Field near Kakariko"
"GS Lon Lon Ranch Back Wall"
"GS Lon Lon Ranch Rain Shed"
"GS Lon Lon Ranch House Window"
"GS Lon Lon Ranch Tree"
"GS Kokiri Bean Patch"
"GS Kokiri Know It All House"
"GS Kokiri House of Twins"
"GS Lost Woods Bean Patch Near Bridge"
"GS Lost Woods Bean Patch Near Stage"
"GS Lost Woods Above Stage"
"GS Sacred Forest Meadow"
"GS Outside Ganon's Castle"
"GS Hyrule Castle Grotto"
"GS Hyrule Castle Tree"
"GS Castle Market Guard House"
"GS Mountain Crater Bean Patch"
"GS Mountain Trail Bean Patch"
"GS Mountain Trail Bomb Alcove"
"GS Mountain Trail Above Dodongo's Cavern"
"GS Mountain Trail Path to Crater"
"GS Goron City Center Platform"
"GS Goron City Boulder Maze"
"GS Death Mountain Crater Crate"
"GS Kakariko House Under Construction"
"GS Kakariko Skulltula House"
"GS Kakariko Guard's House"
"GS Kakariko Tree"
"GS Kakariko Watchtower"
"GS Kakariko Above Impa's House"
"GS Graveyard Wall"
"GS Graveyard Bean Patch"
"GS Zora River Ladder"
"GS Zora River Tree"
"GS Zora's Fountain Above the Log"
"GS Zora River Above Bridge"
"GS Zora River Near Raised Grottos"
"GS Zora's Fountain Hidden Cave"
"GS Zora's Domain Frozen Waterfall"
"GS Zora's Fountain Tree"
"GS Lake Hylia Bean Patch"
"GS Lake Hylia Small Island"
"GS Lake Hylia Lab Wall"
"GS Lab Underwater Crate"
"GS Lake Hylia Giant Tree"
"GS Gerudo Valley Bean Patch"
"GS Gerudo Valley Small Bridge"
"GS Gerudo Valley Pillar"
"GS Gerudo Valley Behind Tent"
"GS Gerudo Fortress Archery Range"
"GS Gerudo Fortress Top Floor"
"GS Desert Colossus Bean Patch"
"GS Wasteland Ruins"
"GS Desert Colossus Hill"
"GS Desert Colossus Tree"
"Kokiri Shop Item 1"
"Kokiri Shop Item 2"
"Kokiri Shop Item 3"
"Kokiri Shop Item 4"
"Kokiri Shop Item 5"
"Kokiri Shop Item 6"
"Kokiri Shop Item 7"
"Kokiri Shop Item 8"
"Kakariko Potion Shop Item 1"
"Kakariko Potion Shop Item 2"
"Kakariko Potion Shop Item 3"
"Kakariko Potion Shop Item 4"
"Kakariko Potion Shop Item 5"
"Kakariko Potion Shop Item 6"
"Kakariko Potion Shop Item 7"
"Kakariko Potion Shop Item 8"
"Bombchu Shop Item 1"
"Bombchu Shop Item 2"
"Bombchu Shop Item 3"
"Bombchu Shop Item 4"
"Bombchu Shop Item 5"
"Bombchu Shop Item 6"
"Bombchu Shop Item 7"
"Bombchu Shop Item 8"
"Castle Town Potion Shop Item 1"
"Castle Town Potion Shop Item 2"
"Castle Town Potion Shop Item 3"
"Castle Town Potion Shop Item 4"
"Castle Town Potion Shop Item 5"
"Castle Town Potion Shop Item 6"
"Castle Town Potion Shop Item 7"
"Castle Town Potion Shop Item 8"
"Castle Town Bazaar Item 1"
"Castle Town Bazaar Item 2"
"Castle Town Bazaar Item 3"
"Castle Town Bazaar Item 4"
"Castle Town Bazaar Item 5"
"Castle Town Bazaar Item 6"
"Castle Town Bazaar Item 7"
"Castle Town Bazaar Item 8"
"Kakariko Bazaar Item 1"
"Kakariko Bazaar Item 2"
"Kakariko Bazaar Item 3"
"Kakariko Bazaar Item 4"
"Kakariko Bazaar Item 5"
"Kakariko Bazaar Item 6"
"Kakariko Bazaar Item 7"
"Kakariko Bazaar Item 8"
"Zora Shop Item 1"
"Zora Shop Item 2"
"Zora Shop Item 3"
"Zora Shop Item 4"
"Zora Shop Item 5"
"Zora Shop Item 6"
"Zora Shop Item 7"
"Zora Shop Item 8"
"Goron Shop Item 1"
"Goron Shop Item 2"
"Goron Shop Item 3"
"Goron Shop Item 4"
"Goron Shop Item 5"
"Goron Shop Item 6"
"Goron Shop Item 7"
"Goron Shop Item 8"
"DC Deku Scrub Deku Nuts"
"DC Deku Scrub Deku Sticks"
"DC Deku Scrub Deku Seeds"
"DC Deku Scrub Deku Shield"
"Jabu Deku Scrub Deku Nuts"
"GC Deku Scrub Bombs"
"GC Deku Scrub Arrows"
"GC Deku Scrub Red Potion"
"GC Deku Scrub Green Potion"
"HF Grotto Deku Scrub Piece of Heart"
"ZR Grotto Deku Scrub Red Potion"
"ZR Grotto Deku Scrub Green Potion"
"SFM Grotto Deku Scrub Red Potion"
"SFM Grotto Deku Scrub Green Potion"
"LH Grotto Deku Scrub Deku Nuts"
"LH Grotto Deku Scrub Bombs"
"LH Grotto Deku Scrub Arrows"
"Valley Grotto Deku Scrub Red Potion"
"Valley Grotto Deku Scrub Green Potion"
"LW Deku Scrub Deku Nuts"
"LW Deku Scrub Deku Sticks"
"LW Grotto Deku Scrub Arrows"
"LW Grotto Deku Scrub Deku Nut Upgrade"
"Desert Grotto Deku Scrub Red Potion"
"Desert Grotto Deku Scrub Green Potion"
"DMC Deku Scrub Bombs"
"DMC Grotto Deku Scrub Deku Nuts"
"DMC Grotto Deku Scrub Bombs"
"DMC Grotto Deku Scrub Arrows"
"Goron Grotto Deku Scrub Deku Nuts"
"Goron Grotto Deku Scrub Bombs"
"Goron Grotto Deku Scrub Arrows"
"LLR Grotto Deku Scrub Deku Nuts"
"LLR Grotto Deku Scrub Bombs"
"LLR Grotto Deku Scrub Arrows"
"Death Mountain Crater Gossip Stone"
"Death Mountain Trail Gossip Stone"
"Desert Colossus Gossip Stone"
"Dodongos Cavern Gossip Stone"
"Generic Grotto Gossip Stone"
"Gerudo Valley Gossip Stone"
"Goron City Maze Gossip Stone"
"Goron City Medigoron Gossip Stone"
"Graveyard Gossip Stone"
"Hyrule Castle Malon Gossip Stone"
"Hyrule Castle Rock Wall Gossip Stone"
"Castle Storms Grotto Gossip Stone"
"Field Valley Grotto Gossip Stone"
"Deku Tree Gossip Stone (Left)"
"Deku Tree Gossip Stone (Right)"
"Kokiri Forest Gossip Stone"
"Lake Hylia Lab Gossip Stone"
"Lake Hylia Gossip Stone (Southeast)"
"Lake Hylia Gossip Stone (Southwest)"
"Lost Woods Gossip Stone"
"Sacred Forest Meadow Maze Gossip Stone (Lower)"
"Sacred Forest Meadow Maze Gossip Stone (Upper)"
"Sacred Forest Meadow Saria Gossip Stone"
"Temple of Time Gossip Stone (Left)"
"Temple of Time Gossip Stone (Left-Center)"
"Temple of Time Gossip Stone (Right)"
"Temple of Time Gossip Stone (Right-Center)"
"Zoras Domain Gossip Stone"
"Zoras Fountain Fairy Gossip Stone"
"Zoras Fountain Jabu Gossip Stone"
"Zoras River Plateau Gossip Stone"
"Zoras River Waterfall Gossip Stone"

