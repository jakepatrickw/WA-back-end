# Generated by Django 3.0.7 on 2021-01-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_logic', '0004_remove_game_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds', models.IntegerField()),
            ],
        ),
    ]
