# EXAMPLE ONE
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('first')
        parser.add_argument('--option')

    def handle(self, *args, **options):
        print(f'First: {options["first"]}')
        print(f'Option: {options["option"]}')

# OUTPUT
# python manage.py refresh_daily_ratings this_is_first_value --option this_is_option_value
# First: this_is_first_value
# Option: this_is_option_value

# EXAMPLE TWO
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', type=int, help='a number less than 100')
        parser.add_argument('--option', default='success!', help='the option value')

    def handle(self, *args, **options):
        if options['number'] < 100:
            print('number is less than 100')
        else:
            raise CommandError('number is more than 100')

        print(f'status is {options["option"]}')

# OUTPUT
# python manage.py refresh_daily_ratings 99
# number is less than 100
# status is success!

# python manage.py refresh_daily_ratings 101
# CommandError: number is more than 100

# EXAMPLE 3
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arguments', nargs=3, type=str, help='this has many arguments')

    def handle(self, *args, **options):
        for each in options['arguments']:
            print('Value:', each)

# python manage.py refresh_daily_ratings jan jeff jet
# Value: jan
# Value: jeff
# Value: jet

# EXAMPLE 4
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('option', action='store_true', help='always True')

    def handle(self, *args, **options):
        if options['option']:
            print('THIS IS TRUE')
        else:
            print('THIS IS FALSE')

# OUTPUT
# python manage.py refresh_daily_ratings
# THIS IS TRUE

# EXAMPLE 5
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'The help information for this command!'

    def add_arguments(self, parser):
        parser.add_argument('test')

    def handle(self, *args, **options):
        print(f'TEST: {options["test"]}')

# OUTPUT
# python manage.py refresh_daily_ratings --help
# usage: manage.py refresh_daily_ratings [-h] [--version] [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback]
#                                        [--no-color] [--force-color]
#                                        test

# The help information for this command!

# positional arguments:
#   test

# optional arguments:
#   -h, --help            show this help message and exit
#   --version             show program's version number and exit
#   -v {0,1,2,3}, --verbosity {0,1,2,3}
#                         Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output
#   --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the
#                         DJANGO_SETTINGS_MODULE environment variable will be used.
#   --pythonpath PYTHONPATH
#                         A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
#   --traceback           Raise on CommandError exceptions
#   --no-color            Don't colorize the command output.
#   --force-color         Force colorization of the command output.