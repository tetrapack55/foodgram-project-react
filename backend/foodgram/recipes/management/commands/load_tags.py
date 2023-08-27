from django.core.management.base import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'color': '#00FF00', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#FFFF00', 'slug': 'dinner'},
            {'name': 'Ужин', 'color': '#800080', 'slug': 'supper'},
            {'name': 'Десерт', 'color': '#FF0000', 'slug': 'dessert'}
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(self.style.SUCCESS('Тэги успешно загружены'))
