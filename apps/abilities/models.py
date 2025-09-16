from django.db import models
from apps.character.models import Class, Origin, Subclass


class Ability(models.Model):
    ATTRIBUTES_REQUIREMENT = (
        ('strength', 'str'),
        ('dexterity', 'dex'),
        ('intelligence', 'int'),
        ('presence', 'pre'),
        ('vigor', 'vig'),
    )
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='ability', null=True, blank=True)
    subclass = models.ForeignKey(Subclass, on_delete=models.CASCADE, related_name='ability', null=True, blank=True)
    origin = models.OneToOneField(Origin, on_delete=models.CASCADE, related_name='ability', null=True, blank=True)
    level = models.IntegerField(default=0, blank=True, null=True)
    passive = models.BooleanField(default=False, blank=False, null=False)
    description = models.TextField()
    attribute_requirement = models.CharField(max_length=100, choices=ATTRIBUTES_REQUIREMENT, null=True, blank=True)
    attribute_requirement_value = models.IntegerField(null=True, blank=True)
    skill_requirement = models.CharField(max_length=100, null=True, blank=True)
    skill_requirement_level = models.CharField(max_length=1, null=True, blank=True)
    abilit_requirement = models.ForeignKey('self', on_delete=models.CASCADE, related_name='ability_requirement', null=True, blank=True)
    execution = models.CharField(max_length=100, null=True, blank=True)
    range = models.CharField(max_length=100, null=True, blank=True)
    target = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    pe_cost = models.IntegerField(blank=True, null=True)
    resistence_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Rituals(models.Model):
    name = models.CharField(max_length=100, unique=True)
    affinity = models.BooleanField(default=False, blank=False, null=False)
    ritual_type = models.CharField(max_length=100)
    ritual_level = models.IntegerField()
    description = models.TextField()
    execution = models.CharField(max_length=100, null=True, blank=True)
    range = models.CharField(max_length=100, null=True, blank=True)
    target = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    pe_cost = models.IntegerField()
    buff = models.IntegerField(null=True, blank=True)
    buff_type = models.CharField(max_length=100, null=True, blank=True)
    damage_dice = models.IntegerField(null=True, blank=True)
    damage_multiplier = models.IntegerField(null=True, blank=True)
    damage_type = models.CharField(max_length=100, null=True, blank=True)
    resistence_type = models.CharField(max_length=100, null=True, blank=True)
    student_level = models.IntegerField(null=True, blank=True)
    student_affinity = models.BooleanField(default=False, blank=False, null=False)
    student_description = models.TextField(null=True, blank=True)
    student_execution = models.CharField(max_length=100, null=True, blank=True)
    student_range = models.CharField(max_length=100, null=True, blank=True)
    student_target = models.CharField(max_length=100, null=True, blank=True)
    student_duration = models.CharField(max_length=100, null=True, blank=True)
    student_pe_cost = models.IntegerField(null=True, blank=True)
    student_buff = models.IntegerField(null=True, blank=True)
    student_buff_type = models.CharField(max_length=100, null=True, blank=True)
    student_damage_dice = models.IntegerField(null=True, blank=True)
    student_damage_multiplier = models.IntegerField(null=True, blank=True)
    student_damage_type = models.CharField(max_length=100, null=True, blank=True)
    student_resistence_type = models.CharField(max_length=100, null=True, blank=True)
    true_level = models.IntegerField(null=True, blank=True)
    true_affinity = models.BooleanField(default=False, blank=False, null=False)
    true_description = models.TextField(null=True, blank=True)
    true_execution = models.CharField(max_length=100, null=True, blank=True)
    true_range = models.CharField(max_length=100, null=True, blank=True)
    true_target = models.CharField(max_length=100, null=True, blank=True)
    true_duration = models.CharField(max_length=100, null=True, blank=True)
    true_pe_cost = models.IntegerField(null=True, blank=True)
    true_buff = models.IntegerField(null=True, blank=True)
    true_buff_type = models.CharField(max_length=100, null=True, blank=True)
    true_damage_dice = models.IntegerField(null=True, blank=True)
    true_damage_multiplier = models.IntegerField(null=True, blank=True)
    true_damage_type = models.CharField(max_length=100, null=True, blank=True)
    true_resistence_type = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class ParanormalPowers(models.Model):
    ATTRIBUTES_REQUIREMENT = (
        ('strength', 'str'),
        ('dexterity', 'dex'),
        ('intelligence', 'int'),
        ('presence', 'pre'),
        ('vigor', 'vig'),
    )
    
    name = models.CharField(max_length=100, unique=True)
    power_type = models.CharField(max_length=100)
    passive = models.BooleanField(default=False, blank=False, null=False)
    description = models.TextField()
    number_of_pre_powers = models.IntegerField(default=1, blank=True, null=True)
    number_of_pre_powers_type = models.CharField(max_length=100, null=True, blank=True)
    attribute_requirement = models.CharField(max_length=100, choices=ATTRIBUTES_REQUIREMENT, null=True, blank=True)
    attribute_requirement_value = models.IntegerField(null=True, blank=True)
    skill_requirement = models.CharField(max_length=100, null=True, blank=True)
    skill_requirement_level = models.CharField(max_length=1, null=True, blank=True)
    execution = models.CharField(max_length=100, null=True, blank=True)
    range = models.CharField(max_length=100, null=True, blank=True)
    target = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    pe_cost = models.IntegerField(null=True, blank=True)
    buff = models.IntegerField(null=True, blank=True)
    buff_type = models.CharField(max_length=100, null=True, blank=True)
    damage_dice = models.IntegerField(null=True, blank=True)
    damage_multiplier = models.IntegerField(null=True, blank=True)
    damage_type = models.CharField(max_length=100, null=True, blank=True)
    resistence_type = models.CharField(max_length=100, null=True, blank=True)
    affinity_description = models.TextField(null=True, blank=True)
    affinity_buff = models.IntegerField(null=True, blank=True)
    affinity_buff_type = models.CharField(max_length=100, null=True, blank=True)
    affinity_damage_dice = models.IntegerField(null=True, blank=True)
    affinity_damage_multiplier = models.IntegerField(null=True, blank=True)
    affinity_damage_type = models.CharField(max_length=100, null=True, blank=True)
    affinity_resistence_type = models.CharField(max_length=100, null=True, blank=True)
    