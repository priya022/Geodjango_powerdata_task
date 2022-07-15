# myapp/management/commands/import_csv.py
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            for row in dataReader:
                emp = Employee()
                # etc...
                self.stdout.write(
                    'Created employee {} {}'.format(emp.first_name, emp.last_name)
                )
