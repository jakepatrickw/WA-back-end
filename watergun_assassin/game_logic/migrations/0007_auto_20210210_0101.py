# Generated by Django 3.0.7 on 2021-02-10 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_logic', '0006_round_assassinated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='rounds',
        ),
        migrations.AddField(
            model_name='round',
            name='game',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='game_logic.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='round',
            name='round_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='round',
            name='assassinated',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='game_logic.Player'),
        ),
        migrations.CreateModel(
            name='RoundPairing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assassin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='game_logic.Player')),
                ('round_number', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game_logic.Round')),
                ('target', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target', to='game_logic.Player')),
            ],
        ),
    ]
