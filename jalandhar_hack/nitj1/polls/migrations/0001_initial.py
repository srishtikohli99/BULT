# Generated by Django 2.2.1 on 2019-09-11 21:14

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('event_name', models.CharField(max_length=200)),
                ('event_date', models.DateTimeField(verbose_name='Event Date')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2019, 9, 11, 21, 14, 58, 283895, tzinfo=utc))),
                ('event_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]