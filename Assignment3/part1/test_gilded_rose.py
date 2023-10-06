# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def setUp(self):
        self.aged_brie = Item("Aged Brie", 2, 0)
        self.aged_brie1 = Item("Aged Brie", 2, 49)
        self.sulfuras = Item("Sulfuras, Hand of Ragnaros", 2, 80)
        self.backstage_pass = Item("Backstage passes", 15, 20)
        self.conjured = Item("Conjured Mana Cake", 3, 6)
        self.normal_item = Item("Normal Item", 5, 10)
        self.items = [self.aged_brie, self.aged_brie1, self.sulfuras, self.backstage_pass, self.conjured, self.normal_item]
        self.gilded_rose = GildedRose(self.items)

    def test_aged_brie(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie.quality, 1)  # Quality should increase by 1
        self.assertEqual(self.aged_brie.sell_in, 1)  # SellIn should decrease by 1
        # test for quality higher than 50
        self.assertEqual(self.aged_brie1.quality, 50)  # Quality should increase by 1
        self.assertEqual(self.aged_brie.sell_in, 1)  # SellIn should decrease by 1
        self.gilded_rose.update_quality()
        self.assertEqual(self.aged_brie1.quality, 50)  # Quality should keep 50
        self.assertEqual(self.aged_brie1.sell_in, 0)  # SellIn should decrease by 1

    def test_sulfuras(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.sulfuras.quality, 80)  # Quality should remain 80
        self.assertEqual(self.sulfuras.sell_in, 2) # SellIn should remain the same
        
    def test_backstage_pass(self):
        for _ in range(5):
            self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 25)  # Increase by 1 till 10 days left
        self.assertEqual(self.backstage_pass.sell_in, 10)
        
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 27)  # Increase by 2 from 10 days
        self.assertEqual(self.backstage_pass.sell_in, 9)
        
        for _ in range(4):
            self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 35)  # Increase by 2 till 5 days left
        self.assertEqual(self.backstage_pass.sell_in, 5)
        
        self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 38)  # Increase by 3 from 5 days
        self.assertEqual(self.backstage_pass.sell_in, 4)
        
        for _ in range(5):
            self.gilded_rose.update_quality()
        self.assertEqual(self.backstage_pass.quality, 0)  # Drops to 0 after concert
        self.assertEqual(self.backstage_pass.sell_in, -1)

    def test_conjured(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.conjured.quality, 4)  # Quality decreases by 2
        self.assertEqual(self.conjured.sell_in, 2)  # SellIn decreases by 1
        
        self.gilded_rose.update_quality()
        self.gilded_rose.update_quality()
        self.assertEqual(self.conjured.quality, 0)  # Quality decreases twice as fast after sell_in passed
    
    def test_normal_item(self):
        self.gilded_rose.update_quality()
        self.assertEqual(self.normal_item.quality, 9)  # Quality decreases by 1
        self.assertEqual(self.normal_item.sell_in, 4)  # SellIn decreases by 1
        
        for _ in range(4):
            self.gilded_rose.update_quality()
        self.assertEqual(self.normal_item.quality, 5)  # Quality continues decreasing by 1
        
        self.gilded_rose.update_quality()
        self.assertEqual(self.normal_item.quality, 3)  # Quality decreases twice as fast after sell_in passed
        self.assertEqual(self.normal_item.sell_in, -1)

    def test_quality_never_negative(self):
        for _ in range(20):
            self.gilded_rose.update_quality()
        self.assertTrue(all(item.quality >= 0 for item in self.items))

    def test_quality_never_more_than_50(self):
        for _ in range(100):
            self.gilded_rose.update_quality()
        self.assertTrue(all(item.quality <= 50 or item.name == "Sulfuras, Hand of Ragnaros" for item in self.items))

if __name__ == '__main__':
    unittest.main()
