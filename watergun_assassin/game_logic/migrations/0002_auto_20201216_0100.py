# Generated by Django 3.0.7 on 2020-12-16 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game_logic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_out', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='player',
        ),
        migrations.AddField(
            model_name='game',
            name='admin',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='game_title',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Players',
        ),
        migrations.AddField(
            model_name='rounds',
            name='game',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game_logic.Game'),
        ),
        migrations.AddField(
            model_name='rounds',
            name='target',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='target', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rounds',
            name='user_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
    ]
