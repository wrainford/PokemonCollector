# Generated by Django 4.0.3 on 2022-04-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_pokemon_pokemonfood'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonfood',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
