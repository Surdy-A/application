# Generated by Django 4.1.1 on 2022-09-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='appointmentdate',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='application',
            name='certificate2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='institution2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='application',
            name='noOfChildren',
            field=models.PositiveBigIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='salary',
            field=models.IntegerField(blank=True),
        ),
    ]
