# Generated by Django 5.0.6 on 2024-05-18 14:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partyyo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='voter',
            field=models.ManyToManyField(default=1, related_name='voter_question', to=settings.AUTH_USER_MODEL),
        ),
    ]
