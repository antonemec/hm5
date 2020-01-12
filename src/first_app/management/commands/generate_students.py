from django.core.management.base import BaseCommand, CommandError
from first_app.models import Student


class Command(BaseCommand):
    help = 'Generate 100 random students'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--number',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        num = int(options.get('number') or 100)
        for _ in range(num):
            Student.generate_students()
