# Generated by Django 4.0.4 on 2022-05-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Http',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortened', models.CharField(max_length=250)),
                ('original', models.CharField(max_length=1000)),
            ],
        ),
    ]
