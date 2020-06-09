# Generated by Django 3.0.3 on 2020-06-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('no_of_tickets', models.IntegerField()),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
