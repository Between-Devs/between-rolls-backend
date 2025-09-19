from django.db import models


def get_default_skill():
    return {
        "total": 0,
        "level": "U",  # U for Untrained
        "bonus": 0
    }


def get_default_inventory():
    return []


class Character(models.Model):
    user = models.ForeignKey('login.CustomUser', on_delete=models.CASCADE,
                             related_name='characters', null=True, blank=True)
    image_link = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    level = models.IntegerField()
    origin = models.ForeignKey('Origin', on_delete=models.CASCADE, null=True, blank=True)
    clas = models.ForeignKey('Class', on_delete=models.CASCADE, null=True, blank=True)
    subclass = models.ForeignKey('Subclass', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Attributes(models.Model):
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, related_name='attributes')
    strength = models.IntegerField(default=1)
    dexterity = models.IntegerField(default=1)
    intelligence = models.IntegerField(default=1)
    presence = models.IntegerField(default=1)
    vigor = models.IntegerField(default=1)

    def __str__(self):
        return f"Attributes for {self.character.name}"


class Skill(models.Model):
    character = models.OneToOneField(
        Character, on_delete=models.CASCADE, related_name='skills')
    acrobaticts = models.JSONField(default=get_default_skill, blank=True)
    animal_handling = models.JSONField(default=get_default_skill, blank=True)
    arts = models.JSONField(default=get_default_skill, blank=True)
    athletics = models.JSONField(default=get_default_skill, blank=True)
    current_affairs = models.JSONField(default=get_default_skill, blank=True)
    science = models.JSONField(default=get_default_skill, blank=True)
    crime = models.JSONField(default=get_default_skill, blank=True)
    diplomacy = models.JSONField(default=get_default_skill, blank=True)
    deception = models.JSONField(default=get_default_skill, blank=True)
    fortitude = models.JSONField(default=get_default_skill, blank=True)
    stealth = models.JSONField(default=get_default_skill, blank=True)
    initiative = models.JSONField(default=get_default_skill, blank=True)
    intimidation = models.JSONField(default=get_default_skill, blank=True)
    insight = models.JSONField(default=get_default_skill, blank=True)
    investigation = models.JSONField(default=get_default_skill, blank=True)
    fight = models.JSONField(default=get_default_skill, blank=True)
    medicine = models.JSONField(default=get_default_skill, blank=True)
    ocultism = models.JSONField(default=get_default_skill, blank=True)
    perception = models.JSONField(default=get_default_skill, blank=True)
    piloting = models.JSONField(default=get_default_skill, blank=True)
    aim = models.JSONField(default=get_default_skill, blank=True)
    profession = models.JSONField(default=get_default_skill, blank=True)
    reflexes = models.JSONField(default=get_default_skill, blank=True)
    religion = models.JSONField(default=get_default_skill, blank=True)
    survival = models.JSONField(default=get_default_skill, blank=True)
    tatics = models.JSONField(default=get_default_skill, blank=True)
    technology = models.JSONField(default=get_default_skill, blank=True)
    will = models.JSONField(default=get_default_skill, blank=True)

    def __str__(self):
        return f"Skills of {self.character.name}"


class Origin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Class(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    initial_hp = models.IntegerField(default=0)
    hp_per_level = models.IntegerField(default=0)
    initial_pe = models.IntegerField(default=0)
    pe_per_level = models.IntegerField(default=0)
    initial_sanity = models.IntegerField(default=0)
    sanity_per_level = models.IntegerField(default=0)
    skills = models.JSONField(default=dict, blank=True, null=True)
    profociency = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class Subclass(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    clas = models.ForeignKey(
        Class, on_delete=models.CASCADE, related_name='subclasses')

    def __str__(self):
        return f"Subclass: {self.name} of {self.clas.name}"


class Inventory(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    items = models.JSONField(default=get_default_inventory, null=True, blank=True)


class AvailableAbilities(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    abilities = models.JSONField(default=dict, blank=True, null=True)


class AvailableRituals(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    rituals = models.JSONField(default=dict, blank=True, null=True)


class AvailableParanormalPowers(models.Model):
    character = models.OneToOneField(Character, on_delete=models.CASCADE)
    powers = models.JSONField(default=dict, blank=True, null=True)


class ClassProgression(models.Model):
    class_instance = models.OneToOneField(Class, on_delete=models.CASCADE, related_name='progression')
    progression = models.JSONField(default=dict, blank=True, null=True)