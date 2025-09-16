from django.db import models


class Weapon(models.Model):
    WEAPON_PROFICIENCYS = (
        ('SW', 'Simple Weapon'),
        ('TW', 'Tatical Weapon'),
        ('HW', 'Heavy Weapon'),
    )

    WEAPON_TYPES = (
        ('ML', 'Melee - Light'),
        ('MOH', 'Melee - One Hand'),
        ('MTH', 'Melee - Two Hands'),
        ('SWTH', 'Shooting Weapon - Two Hands'),
        ('FWL', 'Fire Weapons - Light'),
        ('FWOH', 'Fire Weapons - One Hand'),
        ('FWTH', 'Fire Weapons - Two Hands'),
        ('RTH', 'Ranged - Two Hands'),
    )

    WEAPON_RANGES = (
        ('ML', 'Melee'),
        ('S', 'Short'),
        ('M', 'Medium'),
        ('L', 'Long'),
    )

    DAMAGE_TYPE = (
        ('I', 'Impact'),
        ('S', 'Sharp'),
        ('P', 'Piercing'),
        ('B', 'Ballistic'),
        ('F', 'Fire'),
    )

    AMMO = (
        ('N', '---'),
        ('SB', 'Short Bullets'),
        ('LB', 'Long Bullets'),
        ('SS', 'Shotgun Shells'),
        ('F', 'Fuel'),
        ('A', 'Arrow'),
        ('R', 'Rocket'),
    )

    weapon_name = models.CharField(max_length=50, null=False, blank=False)
    weapon_proficiency = models.CharField(
        max_length=50, choices=WEAPON_PROFICIENCYS, default='SW', null=False, blank=False)
    weapon_type = models.CharField(
        max_length=50, choices=WEAPON_TYPES, default='ML', null=False, blank=False)
    weapon_category = models.IntegerField(blank=False)
    weapon_damage_dice_quantity = models.IntegerField()
    weapon_damage_dice = models.IntegerField()
    weapon_threat_range = models.IntegerField(
        default=0, null=False, blank=False)
    weapon_critical_multiplier = models.IntegerField(
        default=2, null=False, blank=False)
    weapon_range = models.CharField(
        max_length=50, choices=WEAPON_RANGES, default='ML')
    weapon_damage_type = models.CharField(
        max_length=50, choices=DAMAGE_TYPE, default='I', blank=False, null=False)
    weapon_spaces = models.IntegerField(null=False, blank=False, default=0)
    weapon_ammo = models.CharField(max_length=50, choices=AMMO, default='N')
    ammo_capacity = models.IntegerField(default=0, null=False, blank=False)


class Ammo(models.Model):
    AMMO = (
        ('N', '---'),
        ('SB', 'Short Bullets'),
        ('LB', 'Long Bullets'),
        ('SS', 'Shotgun Shells'),
        ('F', 'Fuel'),
        ('A', 'Arrow'),
        ('R', 'Rocket'),
    )

    ammo = models.CharField(max_length=50, choices=AMMO, default='N')
    category = models.IntegerField(blank=False)
    pack_quantity = models.IntegerField(null=False, blank=False)
    pack_cenes = models.IntegerField(null=False, blank=False)
    spaces = models.IntegerField(null=False, blank=False)


class WeponMods(models.Model):
    WEAPON_TYPES = (
        ('MS', 'Melee and Shooting'),
        ('FW', 'Fire Weapons'),
        ('AM', 'AMMO'),
    )

    BUFF_TYPE = (
        ('ATK', 'Attack'),
        ('DMG', 'Damage'),
        ('CTRC', 'Critical Chance'),
        ('CTRM', 'Critical Multiplier'),
        ('OTH', 'Other'),
    )

    weapon_types = models.CharField(
        max_length=2, choices=WEAPON_TYPES, default='MS', null=False, blank=False)
    modification = models.CharField(max_length=100, null=False, blank=False)
    effect = models.TextField(null=False, blank=False)
    buff_type = models.CharField(
        max_length=4, choices=BUFF_TYPE, default='ATK', null=False, blank=False)
    buff_value = models.IntegerField(null=True, blank=True)


class Armor(models.Model):
    ARMOR_TYPES = (
        ('L', 'Light'),
        ('S', 'Shild'),
        ('H', 'Heavy'),
    )

    armor_type = models.CharField(
        max_length=50, choices=ARMOR_TYPES, default='L', null=False, blank=False)
    category = models.IntegerField(blank=False)
    ac_bonus = models.IntegerField(null=False, blank=False)
    spaces = models.IntegerField(null=False, blank=False)


class ArmorMod(models.Model):

    modification = models.CharField(max_length=50, null=False, blank=False)
    effect = models.TextField(null=False, blank=False)
    bonus = models.IntegerField(null=False, blank=False)
    spaces_bonus = models.IntegerField(null=False, blank=False)


class GeneralEquipment(models.Model):
    EQUIPMENT_TYPE = (
        ('A', 'Accessories'),
        ('E', 'Explosives'),
        ('OPI', 'Operetional Items'),
    )

    equipment_name = models.CharField(max_length=50, null=False, blank=False)
    equipment_category = models.IntegerField(null=False, blank=False)
    equipment_description = models.TextField(null=False, blank=False)
    equipment_type = models.CharField(
        choices=EQUIPMENT_TYPE, default='A', max_length=50, null=False, blank=False)
    spaces = models.IntegerField(null=False, blank=False)


class AccessoriesMod(models.Model):
    modificattion = models.CharField(max_length=50, null=False, blank=False)
    effect = models.TextField(null=False, blank=False)
    bonus = models.IntegerField(null=False, blank=False)
    spaces_bonus = models.IntegerField(null=False, blank=False)


class ParanormalItens(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    category = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    spaces = models.IntegerField(null=False, blank=False)
    