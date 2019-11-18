# Generated by Django 2.2.3 on 2019-07-13 00:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest_name', models.TextField(max_length=50)),
                ('quest_type', models.TextField()),
                ('tags', models.CharField(blank=True, max_length=50)),
                ('quest_description', models.TextField()),
                ('reward', models.TextField(blank=True, max_length=50)),
                ('XP_reward', models.IntegerField()),
                ('XP_penalty', models.IntegerField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('date_of_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
