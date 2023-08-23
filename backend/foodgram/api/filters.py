import django_filters

from django.contrib.auth import get_user_model

from recipes.models import Recipe, Tag


User = get_user_model()


class RecipeFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        field_name="tags__slug",
        to_field_name="slug",
    )
    author = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    is_favorited = django_filters.BooleanFilter(method='get_is_favorited')
    is_in_shopping_cart = django_filters.BooleanFilter(
        method='get_is_in_shopping_cart'
    )

    def get_is_favorited(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(
                favorites__user=self.request.user,
                is_favorited=True,
            )
        return Recipe.objects.all()

    def get_is_in_shopping_cart(self, queryset, name, value):
        if value and self.request.user.is_authenticated:
            return queryset.filter(
                shopping_carts__user=self.request.user,
                is_in_shopping_cart=True,
            )
        return Recipe.objects.all()

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')
