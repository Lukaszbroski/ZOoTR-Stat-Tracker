


#this file is solely dedicated towards defining states in
#the same way that the randomizer does in its logic and generation.

class Item:
    def __init__(self, name = '', value = 0, sphere = -1, location = ''):
        self.name = name
        self.value = value
        self.sphere = sphere
        self.location = location

class State:
    def __init__(self):
        self.item_table = []
        self.item_table.append(Item('Kokiri_Sword', False, -1))
        self.item_table.append(Item('Bow', False,  -1))
        self.item_table.append(Item('Hookshot', False,  -1))
        self.item_table.append(Item('Longshot', False,  -1))
        self.item_table.append(Item('Hammer', False,  -1))
        self.item_table.append(Item('Slingshot', False,  -1))
        self.item_table.append(Item('Boomerang', False,  -1))
        self.item_table.append(Item('Bombs', False,  -1))
        self.item_table.append(Item('Bombchus', False,  -1))
        self.item_table.append(Item('Lens', False,  -1))
        self.item_table.append(Item('Dins', False,  -1))
        self.item_table.append(Item('Fire_Arrows', False,  -1))
        self.item_table.append(Item('Light_Arrows', False,  -1))
        self.item_table.append(Item('Ruto', False,  -1))
        self.item_table.append(Item('Bottle', False,  -1))
        self.item_table.append(Item('Wallet', False,  -1))
        self.item_table.append(Item('Skulltula', 0,  -1))
        self.item_table.append(Item('Mirror_Shield', False,  -1))
        self.item_table.append(Item('Goron_Tunic', False,  -1))
        self.item_table.append(Item('Zora_Tunic', False,  -1))
        self.item_table.append(Item('Iron_Boots', False,  -1))
        self.item_table.append(Item('Hover_Boots', False,  -1))
        self.item_table.append(Item('Bracelet', False,  -1))
        self.item_table.append(Item('Silvers', False,  -1))
        self.item_table.append(Item('Golds', False,  -1))
        self.item_table.append(Item('Silver_Scale', 0,  -1))
        self.item_table.append(Item('Gold_Scale', False,  -1))
        self.item_table.append(Item('Agony', False,  -1))
        self.item_table.append(Item('Magic', False,  -1))
        self.item_table.append(Item('Lullaby', False,  -1))
        self.item_table.append(Item('Epona', False,  -1))
        self.item_table.append(Item('Sun', False,  -1))
        self.item_table.append(Item('Saria', False,  -1))
        self.item_table.append(Item('Time', False,  -1))
        self.item_table.append(Item('Storms', False,  -1))
        self.item_table.append(Item('Minuet', False,  -1))
        self.item_table.append(Item('Bolero', False,  -1))
        self.item_table.append(Item('Reqiuem', False,  -1))
        self.item_table.append(Item('Emerald', False,  -1))
        self.item_table.append(Item('Ruby', False,  -1))
        self.item_table.append(Item('Sapphire', False,  -1))
        self.item_table.append(Item('Forest_Medallion', False,  -1))
        self.item_table.append(Item('Fire_Medallion', False,  -1))
        self.item_table.append(Item('Water_Medallion', False,  -1))
        self.item_table.append(Item('Spirit_Medallion', False,  -1))
        self.item_table.append(Item('Shadow_Medallion', False,  -1))
        self.item_table.append(Item('Light_Medallion', False,  -1))
        self.item_table.append(Item('Ganon_Entry', False,  -1))
        temple = ['Forest_Temple', 'Fire_Temple', 'Water_Temple', 'Shadow_Temple', 'Spirit_Temple', 'Light_Temple']
        for x in temple:
            self.item_table.append(Item('Boss_Key_' + temple[x], False,  -1))
            self.item_table.append(Item('Small_Key_' + temple[x], 0, -1))
            self.item_table.append(Item(temple[x] + '_entry', False , -1))
        self.item_table.append(Item('Bottle_with_Blue_Fire', False,  -1))
        self.item_table.append(Item('Weird_Egg', False,  -1))
        self.item_table.append(Item('Adult_Trade', False,  -1))
        self.item_table.append(Item('Ocarina', False,  -1))
        self.item_table.append(Item('Ocarina_Of_Time', False,  -1))
        self.item_table.append(Item('Letter', False,  -1))
        self.item_table.append(Item('Heart_Piece', False,  -1))
        self.item_table.append(Item('Heart_Container', False,  -1))
        self.item_table.append(Item('GTG_entry', False,  -1))
        self.item_table.append(Item('Hyrule_entry', False,  -1))
        self.item_table.append(Item('Adult', False,  -1))
        self.item_table.append(Item('Triforce', False,  -1))
        self.item_table.append(Item('Sticks', False, -1))
        self.item_table.append(Item('Stick_Upgrade', False,  -1))
        self.item_table.append(Item('Nut_Upgrade', False,  -1))
        self.item_table.append(Item('Nuts', False, -1))
        self.item_table.append(Item('Deku_Shield', False, -1))
        self.item_table.append(Item('Keysanity', False, -1))
        self.item_table.append(Item('Scrubsanity', False, -1))
        self.item_table.append(Item('Keysy', False, -1,))



    def has(self, item, value):
        for x in self.item_table:
            if self.item_table[x].name == item:
                if self.item_table[x].value == 0 or self.item_table[x].value == False:
                    return False
                else:
                    if self.item_table[x].value == value or self.item_table[x].value > value or self.item_table[x].value == True:
                        return True
                    if self.item_table[x].value < value:
                        return False

    def has(self, item):
        for x in self.item_table:
            if self.item_table[x].name == item:
                if self.item_table[x].value == 0 or self.item_table[x].value == False:
                    return False
                else: return True



    def get(self, item):