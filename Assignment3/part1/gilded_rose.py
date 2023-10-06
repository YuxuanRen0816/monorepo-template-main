# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            # "Sulfuras" item
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            # # "Aged Brie" item
            if item.name == "Aged Brie":
                self.increase_quality(item, 1)
            # "Backstage passes" item
            elif item.name == "Backstage passes":
                if item.sell_in > 10:
                    self.increase_quality(item, 1)
                elif item.sell_in <= 10 and item.sell_in > 5:
                    self.increase_quality(item, 2)
                elif item.sell_in <= 5 and item.sell_in > 0:
                    self.increase_quality(item, 3)
                elif item.sell_in <= 0:
                    item.quality = 0
            # "Conjured" item
            elif "Conjured" in item.name:
                if 0 < item.quality <= 50:
                    self.decrease_quality(item, 2)
                    if item.sell_in <= 0:
                        self.decrease_quality(item, 2)
            # All other items
            else:
                self.decrease_quality(item, 1)
                if item.sell_in <= 0:
                    self.decrease_quality(item, 1)

            # Decrease sell_in value for all items except "Sulfuras"
            item.sell_in -= 1
            

    def increase_quality(self, item, amount):
        item.quality = min(item.quality + amount, 50)
        
    def decrease_quality(self, item, amount):
        item.quality = max(item.quality - amount, 0)
