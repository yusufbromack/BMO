from re import T
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Item(models.Model):    
    itemId = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100)
    categoryPri = models.PositiveSmallIntegerField(null=True)
    categorySec = models.PositiveSmallIntegerField(null=True)
    grade = models.PositiveSmallIntegerField(null=True)
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Category(models.IntegerChoices):
#     MAIN_WEAPON = 1
#     SUB_WEAPON = 5
#     AWAKENING_WEAPON = 10
#     ARMOR = 15
#     ACCESSORY = 20
#     MATERIAL = 25
#     ENHANCEMENT_UPGRADE = 30
#     CONSUMABLES = 35
#     LIFE_TOOLS = 40
#     ALCHEMY_STONE = 45
#     MAGIC_CRYSTAL = 50
#     PEARL_ITEMS = 55
#     DYE = 60
#     MOUNT = 65
#     SHIP = 70
#     WAGON = 75
#     FURNITURE = 80

#     CHOICES = (
#     (MAIN_WEAPON, _('Main Weapon')),
#     (SUB_WEAPON, _('Sub Weapon')),
#     (AWAKENING_WEAPON, _('Awakening Weapon')),
#     (ARMOR, _('Armor')),
#     (ACCESSORY, _('Accessory')),
#     (MATERIAL, _('Material')),
#     (ENHANCEMENT_UPGRADE, _('Enhancement/Upgrade')),
#     (CONSUMABLES, _('Consumables')),
#     (LIFE_TOOLS, _('Life Tools')),
#     (ALCHEMY_STONE, _('Alchemy Stone')),
#     (MAGIC_CRYSTAL, _('Magic Crystal')),
#     (PEARL_ITEMS, _('Pearl Items')),
#     (DYE, _('Dye')),
#     (MOUNT, _('Mount')),
#     (SHIP, _('Ship')),
#     (WAGON, _('Wagon')),
#     (FURNITURE, _('Furniture')),
#     )

#     category = models.IntegerField(choices=CHOICES)

#     def __str__(self):
#         return self.category
