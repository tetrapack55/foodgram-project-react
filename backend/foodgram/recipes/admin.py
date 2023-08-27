from django.contrib import admin

from recipes.models import Ingredient, Recipe, RecipeIngredient, Tag


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author',
                    'text', 'added_to_favorite')
    search_fields = ('name',)
    list_filter = ('author', 'name', 'tags')
    inlines = (RecipeIngredientInline,)
    empty_value_display = '<< пусто >>'

    @staticmethod
    def added_to_favorite(obj):
        return obj.favorites.count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'slug',)
    search_fields = ('name',)
    empty_value_display = '<< пусто >>'


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)
    empty_value_display = '<< пусто >>'
