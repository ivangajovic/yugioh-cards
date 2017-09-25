from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Card, CardType, MonsterType, MonsterType1, MonsterType2, MonsterAbility, SpellTrapType, CardRarity
from .forms import CardForm, CardTypeForm, MonsterTypeForm, MonsterType1Form, MonsterType2Form, MonsterAbilityForm, SpellTrapTypeForm, CardRarityForm

# Create your views here.

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'ygocard/card_list.html', {'cards': cards})


def card_detail(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'ygocard/card_detail.html', {'card': card})


@login_required
def add_new_card(request):
    # Check to see if a POST has been submitted
    if request.method == "POST":
        # Load all forms with data that user have entered
        form = CardForm(request.POST, request.FILES, prefix='crd')
        form_card_type = CardTypeForm(request.POST, prefix='ctyp')
        form_monster_type = MonsterTypeForm(request.POST, prefix='mtyp')
        form_monster_type1 = MonsterType1Form(request.POST, prefix='mtyp1')
        form_monster_type2 = MonsterType2Form(request.POST, prefix='mtyp2')
        form_monster_ability = MonsterAbilityForm(request.POST, prefix='mabt')
        form_spell_trap = SpellTrapTypeForm(request.POST, prefix='stt')
        form_card_rarity = CardRarityForm(request.POST, prefix='crrt')
        # Ensure that all forms are valid before continuing on
        if form.is_valid() and form_card_type.is_valid() and form_monster_type.is_valid() and form_monster_type1.is_valid() and form_monster_type2.is_valid() and form_monster_ability.is_valid() and form_spell_trap.is_valid() and form_card_rarity.is_valid():
            # Prepare card model, but don't commit it to the db
            card = form.save(commit=False)
            # Add all ForeignKey by saving the forms we setup
            card.author = request.user
            card.card_type = form_card_type.save()
            card.monster_type = form_monster_type.save()
            card.monster_type_1 = form_monster_type1.save()
            card.monster_type_2 = form_monster_type2.save()
            card.monster_ability = form_monster_ability.save()
            card.spell_trap_type = form_spell_trap.save()
            card.card_rarity = form_card_rarity.save()
            # Save the main object and continue
            card.save()
            return redirect('card_detail', pk=card.pk)
    else:
        # Initialize all forms with separate prefixes
        form = CardForm(prefix='crd')
        form_card_type = CardTypeForm(prefix='ctyp')
        form_monster_type = MonsterTypeForm(prefix='mtyp')
        form_monster_type1 = MonsterType1Form(prefix='mtyp1')
        form_monster_type2 = MonsterType2Form(prefix='mtyp2')
        form_monster_ability = MonsterAbilityForm(prefix='mabt')
        form_spell_trap = SpellTrapTypeForm(prefix='stt')
        form_card_rarity = CardRarityForm(prefix='crrt')

    return render(request, 'ygocard/card_edit.html', {'form': form, 'form_card_type': form_card_type, 'form_monster_type': form_monster_type, 'form_monster_type1': form_monster_type1, 'form_monster_type2': form_monster_type2, 'form_monster_ability': form_monster_ability, 'form_spell_trap': form_spell_trap, 'form_card_rarity': form_card_rarity})


@login_required
def card_edit(request, pk):
    card = get_object_or_404(Card, pk=pk)

    if request.method == "POST":
        form = CardForm(request.POST, request.FILES, instance=card, prefix='crd')
        form_card_type = CardTypeForm(request.POST, instance=card.card_type, prefix='ctyp')
        form_monster_type = MonsterTypeForm(request.POST, instance=card.monster_type, prefix='mtyp')
        form_monster_type1 = MonsterType1Form(request.POST, instance=card.monster_type_1, prefix='mtyp1')
        form_monster_type2 = MonsterType2Form(request.POST, instance=card.monster_type_2, prefix='mtyp2')
        form_monster_ability = MonsterAbilityForm(request.POST, instance=card.monster_ability, prefix='mabt')
        form_spell_trap = SpellTrapTypeForm(request.POST, instance=card.spell_trap_type, prefix='stt')
        form_card_rarity = CardRarityForm(request.POST, instance=card.card_rarity, prefix='crrt')

        if form.is_valid() and form_card_type.is_valid() and form_monster_type.is_valid() and form_monster_type1.is_valid() and form_monster_type2.is_valid() and form_monster_ability.is_valid() and form_spell_trap.is_valid() and form_card_rarity.is_valid():
            card = form.save(commit=False)
            card.author = request.user
            card.card_type = form_card_type.save()
            card.monster_type = form_monster_type.save()
            card.monster_type_1 = form_monster_type1.save()
            card.monster_type_2 = form_monster_type2.save()
            card.monster_ability = form_monster_ability.save()
            card.spell_trap_type = form_spell_trap.save()
            card.card_rarity = form_card_rarity.save()

            card.save()
            return redirect('card_detail', pk=card.pk)
    else:
        form = CardForm(instance=card, prefix='crd')
        form_card_type = CardTypeForm(instance=card.card_type, prefix='ctyp')
        form_monster_type = MonsterTypeForm(instance=card.monster_type, prefix='mtyp')
        form_monster_type1 = MonsterType1Form(instance=card.monster_type_1, prefix='mtyp1')
        form_monster_type2 = MonsterType2Form(instance=card.monster_type_2, prefix='mtyp2')
        form_monster_ability = MonsterAbilityForm(instance=card.monster_ability, prefix='mabt')
        form_spell_trap = SpellTrapTypeForm(instance=card.spell_trap_type, prefix='stt')
        form_card_rarity = CardRarityForm(instance=card.card_rarity, prefix='crrt')

    return render(request, 'ygocard/card_edit.html', {'form': form, 'form_card_type': form_card_type, 'form_monster_type': form_monster_type, 'form_monster_type1': form_monster_type1, 'form_monster_type2': form_monster_type2, 'form_monster_ability': form_monster_ability, 'form_spell_trap': form_spell_trap, 'form_card_rarity': form_card_rarity})


@login_required
def card_remove(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('card_list')
