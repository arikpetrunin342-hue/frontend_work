from django.core.management.base import BaseCommand
from django.apps import apps as django_apps


class Command(BaseCommand):
    help = 'Удаляет все данные из базы и добавляет несколько тестовых товаров.'

    def handle(self, *args, **options):
        Category = django_apps.get_model('catalog',
                                         'Category')
        Product = django_apps.get_model('catalog', 'Catalog', 'Product')

        self.stdout.write('Очистка базы...')

        Category.objects.all().delete()
        Product.objects.all().delete()

        self.stdout.write('Добавление новых данных...')

        cat_electronics = Category.objects.create(
            name='Электроника',
            description='Мобильные устройства'
        )

        product_poco = Product.objects.create(
            category=cat_electronics,
            name='Poco F6',
            price=18000.00
        )

        product_book = Product.objects.create(
            category=None,
            name='Python для начинающих',
            price=599.00
        )

        self.stdout.write(self.style.SUCCESS('Готово!'))