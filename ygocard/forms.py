from django import forms
from .models import Card, CardType, MonsterType, MonsterType1, MonsterType2, MonsterAbility, SpellTrapType, CardRarity

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('c_title', 'c_set', 'c_edition', 'c_image', 'c_description', 'release_date', 'procure_date',)


class CardTypeForm(forms.ModelForm):

    class Meta:
        model = CardType
        fields = ('title',)
        title = forms.ChoiceField(choices=CardType.CARDTYPE_CHOICES)
        labels = {"title": "Card Type",}


class MonsterTypeForm(forms.ModelForm):

    class Meta:
        model = MonsterType
        fields = ('title',)
        title = forms.ChoiceField(choices=MonsterType.MONSTERTYPE_CHOICES, required=False)
        labels = {"title": "Monster type",}


class MonsterType1Form(forms.ModelForm):

    class Meta:
        model = MonsterType1
        fields = ('title',)
        title = forms.ChoiceField(choices=MonsterType1.MONSTERTYPE1_CHOICES, required=False)
        labels = {"title": "Monster subtype I"}


class MonsterType2Form(forms.ModelForm):

    class Meta:
        model = MonsterType2
        fields = ('title',)
        title = forms.ChoiceField(choices=MonsterType2.MONSTERTYPE2_CHOICES, required=False)
        labels = {"title": "Monster subtype II"}



class MonsterAbilityForm(forms.ModelForm):

    class Meta:
        model = MonsterAbility
        fields = ('title',)
        title = forms.ChoiceField(choices=MonsterAbility.MONSTERABILITIES_CHOICES, required=False)
        labels = {"title": "Monster Ability"}


class SpellTrapTypeForm(forms.ModelForm):

    class Meta:
        model = SpellTrapType
        fields = ('title',)
        title = forms.ChoiceField(choices=SpellTrapType.SPELLTRAPTYPE_CHOICES, required=False)
        labels = {"title": "Spell\Trap Property"}


class CardRarityForm(forms.ModelForm):

    class Meta:
        model = CardRarity
        fields = ('title',)
        title = forms.ChoiceField(choices=CardRarity.RARITY_CHOICES)
        labels = {"title": "Card Rarity"}
