# Generated by Django 3.1.7 on 2021-03-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testField', models.CharField(max_length=50)),
                ('testField2', models.DecimalField(decimal_places=5, max_digits=20)),
            ],
        ),
    ]