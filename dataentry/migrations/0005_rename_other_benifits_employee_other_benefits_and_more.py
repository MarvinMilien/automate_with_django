# Generated by Django 5.0.9 on 2024-11-07 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("dataentry", "0004_employee"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="other_benifits",
            new_name="other_benefits",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="total_benifits",
            new_name="total_benefits",
        ),
    ]
