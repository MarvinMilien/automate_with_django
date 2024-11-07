import csv
from django.core.management.base import BaseCommand, CommandParser
from django.apps import apps
import datetime

# proposed command = python manage.py exportdata model name
class Command(BaseCommand):
    help = "Export data from the database to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *arg, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        # search through all the insalled apps for the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop executing once the model is found
            except LookupError:
                pass
        
        if not model:
            self.stderr.write('Model {model_name} could not be found')
            return

        # fetch the data from the database
        data = model.objects.all()

        # generate the timestamp of current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # define the csv file name/path
        file_path = f'exported_{model_name}_data{timestamp}.csv'
        print(file_path)
        
        # open the csv file and write the data
        with open(file_path, 'w', newline="") as file:
            writer = csv.writer(file)

            # write the csv header
            # we want to print the field names of the model that we are trying to export
            writer.writerow([field.name for field in model._meta.fields])

            # write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))