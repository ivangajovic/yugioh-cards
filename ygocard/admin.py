from django.contrib import admin
from .models import Card, CardType, MonsterType, MonsterType1, MonsterType2, MonsterAbility, SpellTrapType, CardRarity

# Register your models here.

admin.site.register(Card)
admin.site.register(CardType)
admin.site.register(MonsterType)
admin.site.register(MonsterType1)
admin.site.register(MonsterType2)
admin.site.register(MonsterAbility)
admin.site.register(SpellTrapType)
admin.site.register(CardRarity)
