# Generated by Django 2.1.2 on 2018-10-24 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airline_code', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('airline_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_id', models.IntegerField(primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('passenger_capacity', models.IntegerField()),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Airline')),
            ],
        ),
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Departure_date_time', models.DateTimeField()),
                ('Arrival_date_time', models.DateTimeField()),
                ('price', models.CharField(max_length=128)),
                ('journey_type', models.CharField(default='One Way', max_length=128)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_airport', to='MyApp.Airport')),
                ('flight_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.Flight')),
            ],
        ),
        migrations.AddField(
            model_name='airport',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.City'),
        ),
    ]
