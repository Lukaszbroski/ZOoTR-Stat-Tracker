


#this file is solely dedicated towards defining states in
#the same way that the randomizer does in its logic and generation.

class Item(object):
    def __init__(self, name = '', value = 0, sphere = -1, location = ''):
        self.name = name
        self.value = value
        self.sphere = sphere
        self.location = location

class State(object):
    def __init__(self):
        self.item_table = []
        self.item_table.append(Item('Kokiri Sword', False, -1))
        self.item_table.append(Item('Bow', 0,  -1))
        self.item_table.append(Item('Hookshot', 0,  -1))
        self.item_table.append(Item('Hammer', False,  -1))
        self.item_table.append(Item('Slingshot', 0,  -1))
        self.item_table.append(Item('Boomerang', False,  -1))
        self.item_table.append(Item('Bombs', 0,  -1))
        self.item_table.append(Item('Lens', False,  -1))
        self.item_table.append(Item('Dins', False,  -1))
        self.item_table.append(Item('Fire Arrows', False,  -1))
        self.item_table.append(Item('Light Arrows', False,  -1))
        self.item_table.append(Item('Ruto', False,  -1))
        self.item_table.append(Item('Bottle', 0,  -1))
        self.item_table.append(Item('Wallet', 0,  -1))
        self.item_table.append(Item('Skulltula', 0,  -1))
        self.item_table.append(Item('Mirror Shield', False,  -1))
        self.item_table.append(Item('Goron Tunic', False,  -1))
        self.item_table.append(Item('Zora Tunic', False,  -1))
        self.item_table.append(Item('Iron Boots', False,  -1))
        self.item_table.append(Item('Hover Boots', False,  -1))
        self.item_table.append(Item('Strength', 0,  -1))
        self.item_table.append(Item('Scale', 0,  -1))
        self.item_table.append(Item('Agony', False,  -1))
        self.item_table.append(Item('Magic', 0,  -1))
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
        self.item_table.append(Item('Forest Medallion', False,  -1))
        self.item_table.append(Item('Fire Medallion', False,  -1))
        self.item_table.append(Item('Water Medallion', False,  -1))
        self.item_table.append(Item('Spirit Medallion', False,  -1))
        self.item_table.append(Item('Shadow Medallion', False,  -1))
        self.item_table.append(Item('Light Medallion', False,  -1))
        self.item_table.append(Item('Ganon Entry', False,  -1))
        temple = ['Forest Temple', 'Fire Temple', 'Water Temple', 'Shadow Temple', 'Spirit Temple', 'light temple']
        for x in temple:
            self.item_table.append(Item('Boss Key ' + temple[x], False,  -1))
            self.item_table.append(Item('Small Key ' + temple[x], 0, -1))
            self.item_table.append(Item(temple[x] + 'entry', 0 , -1))
        self.item_table.append(Item('Bottle with Blue Fire', False,  -1))
        self.item_table.append(Item('Weird Egg', False,  -1))
        self.item_table.append(Item('Adult Trade', 0,  -1))
        self.item_table.append(Item('Ocarina', 0,  -1))
        self.item_table.append(Item('Child Trade', 0,  -1))
        self.item_table.append(Item('Hearts', 3,  -1))
        self.item_table.append(Item('GTG entry', False,  -1))
        self.item_table.append(Item('Hyrule entry', False,  -1))
        self.item_table.append(Item('Adult', False,  -1))
        self.item_table.append(Item('Triforce', False,  -1))



    def has(self, item):
        for x in item_table:
            j =
            x =
            return j == x
            j = 'j' + str.j(1)
            j = 1 + 'j'
            return item_table[j]

    def get(self, item):