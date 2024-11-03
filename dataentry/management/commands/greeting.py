from django.core.management.base import BaseCommand, CommandParser

# Propossed command = python manange.py greeting John
# Propossed output = Greetings {name}, Good morining
class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='specifies user name')

    def handle(self, *args, **kwargs):
        # write the logic
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greeting))