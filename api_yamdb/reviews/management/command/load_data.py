import csv

from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User

TABLES_DATA = {
    User: 'users.csv',
    Category: 'category.csv',
    Genre: 'genre.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',
}


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for models, csv_f in TABLES_DATA.items():
            with open(
                f'{settings.BASE_DIR}/static/data/{csv_f}',
                'r', encoding='utf-8'
            ) as csv_file:
                reader = csv.DictReader(csv_file)
                models.objects.bulk_create(
                    models(**data) for data in reader)
        self.stdout.write(self.style.SUCCESS('Данные загружены!'))
