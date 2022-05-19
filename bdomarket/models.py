from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

CATEGORY_MATERIAL = 25
CATEGORY_CONSUMABLES = 35

CATEGORY_CHOICES = (
    (CATEGORY_MATERIAL, _('Material')),
    (CATEGORY_CONSUMABLES, _('Consumables')),
)

class Item(models.Model):
    itemId = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    category = models.PositiveSmallIntegerField(
        choices=CATEGORY_CHOICES,
        default=CATEGORY_MATERIAL
    )

    # class SubCategory(models.Model):
    #     class Category(models.IntegerChoices):
    #         MAIN_WEAPON = 1
    #         SUB_WEAPON = 5
    #         AWAKENING_WEAPON = 10
    #         ARMOR = 15
    #         ACCESSORY = 20
    #         MATERIAL = 25
    #         ENHANCEMENT_UPGRADE = 30
    #         CONSUMABLES = 35
    #         LIFE_TOOLS = 40
    #         ALCHEMY_STONE = 45
    #         MAGIC_CRYSTAL = 50
    #         PEARL_ITEMS = 55
    #         DYE = 60
    #         MOUNT = 65
    #         SHIP = 70
    #         WAGON = 75
    #         FURNITURE = 80
        
    #     category = models.IntegerField(choices=Category.choices)
