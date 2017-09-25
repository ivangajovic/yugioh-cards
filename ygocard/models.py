from django.db import models
from django.utils import timezone

# Create your models here.

class Card(models.Model):
    author = models.ForeignKey('auth.User')
    c_title = models.CharField(max_length=300)
    card_type = models.ForeignKey('CardType', blank=True, null=True, on_delete=models.CASCADE, related_name='card_type')
    monster_type = models.ForeignKey('MonsterType', blank=True, null=True, on_delete=models.SET_NULL, related_name='monster_type')
    monster_type_1 = models.ForeignKey('MonsterType1', blank=True, null=True, on_delete=models.SET_NULL, related_name='monster_type_1')
    monster_type_2 = models.ForeignKey('MonsterType2', blank=True, null=True, on_delete=models.SET_NULL, related_name='monster_type_2')
    monster_ability = models.ForeignKey('MonsterAbility', blank=True, null=True, on_delete=models.SET_NULL, related_name='monster_ability')
    spell_trap_type = models.ForeignKey('SpellTrapType', blank=True, null=True, on_delete=models.SET_NULL, related_name='spell_trap_type')
    card_rarity = models.ForeignKey('CardRarity', blank=True, null=True, on_delete=models.SET_NULL, related_name='card_rarity')
    c_set = models.CharField(max_length=300)
    c_edition = models.CharField(max_length=50)
    c_image = models.FileField()
    c_description = models.TextField()
    release_date = models.DateTimeField(default=timezone.now)
    procure_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-procure_date',)

    def __str__(self):
        return self.c_title



class CardType(models.Model):
    CARDTYPE_CHOICES = (
        ('monster', 'Monster'),
        ('spell', 'Spell'),
        ('trap', 'Trap'),
        )
    title = models.CharField(max_length=20, help_text='Enter card type', choices=CARDTYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class MonsterType(models.Model):
    MONSTERTYPE_CHOICES = (
        ('aqua', 'Aqua'), ('beast', 'Beast'), ('beast-warrior', 'Beast-Warrior'),
        ('cyberse', 'Cyberse'), ('dinosaur', 'Dinosaur'), ('divine-beast', 'Divine-Beast'),
        ('dragon', 'Dragon'), ('fairy', 'Fairy'), ('fish', 'Fish'),
        ('insect', 'Insect'), ('machine', 'Machine'), ('plant', 'Plant'),
        ('psychic', 'Psychic'), ('pyro', 'Pyro'), ('reptile', 'Reptile'),
        ('rock', 'Rock'), ('sea-serpent', 'Sea-Serpent'), ('spellcaster', 'Spellcaster'),
        ('thunder', 'Thunder'), ('warrior', 'Warrior'), ('winged-beast', 'Winged-Beast'),
        ('wyrm', 'Wyrm'), ('zombie', 'Zombie'),

    )
    title = models.CharField(max_length=20, help_text='If monster card, choose monster type', choices=MONSTERTYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class MonsterType1(models.Model):
    MONSTERTYPE1_CHOICES = (
        ('normal', 'Normal'), ('effect', 'Effect'),
    )
    title = models.CharField(max_length=20, help_text='If monster card, choose card subtype', choices=MONSTERTYPE1_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class MonsterType2(models.Model):
    MONSTERTYPE2_CHOICES = (
        ('ritual', 'Ritual'), ('fusion', 'Fusion'),
        ('synchro', 'Synchro'), ('xyz', 'Xyz'),
        ('pendulum', 'Pendulum'), ('link', 'Link'), ('token', 'Token'),
    )
    title = models.CharField(max_length=20, help_text='If monster card, choose card subtype', choices=MONSTERTYPE2_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class MonsterAbility(models.Model):
    MONSTERABILITIES_CHOICES = (
        ('flip', 'Flip'), ('toon', 'Toon'),
        ('spirit', 'Spirit'), ('union', 'Union'), ('gemini', 'Gemini'),
    )
    title = models.CharField(max_length=20, help_text='If aplicable, choose monster ability', choices=MONSTERABILITIES_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class SpellTrapType(models.Model):
    SPELLTRAPTYPE_CHOICES = (
        ('normal', 'Normal'), ('continuous', 'Continuous'), ('field', 'Field'),
        ('equip', 'Equip'), ('quick-play', 'Quick-Play'), ('ritual', 'Ritual'), ('counter', 'Counter'),
    )
    title = models.CharField(max_length=20, help_text='If spell or trap card, choose card subtype', choices=SPELLTRAPTYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class CardRarity(models.Model):
    RARITY_CHOICES = (
        ('common', 'Common'), ('short print', 'Short Print'),
        ('rare', 'Rare'), ('super rare', 'Super Rare'), ('ultra rare', 'Ultra Rare'),  ('secret rare', 'Secret Rare'),
        ('ultimate rare', 'Ultimate Rare'), ('ghost rare', 'Ghost Rare'), ('platinum rare', 'Platinum Rare'),
        ('prismatic secret rare', 'Prismatic Secret Rare'), ('extra secret rare', 'Extra Secret Rare'), ('platinum secret rare', 'Platinum Secret Rare'),
        ('normal parallel rare', 'Normal Parallel Rare'), ('super parallel rare', 'Super Parallel Rare'), ('ultra parallel rare', 'Ultra Parallel Rare'),
        ('starfoil rare', 'Starfoil Rare'), ('mosaic rare', 'Mosaic Rare'), ('shatterfoil rare', 'Shatterfoil Rare'),
        ('gold rare', 'Gold Rare'), ('gold secret rare', 'gold secret Rare'), ('ghost/gold rare', 'Ghost/Gold Rare'),
    )
    title = models.CharField(max_length=30, help_text='Select rarity of the card', choices=RARITY_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title
