# Generated by Django 4.0.3 on 2022-03-16 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0003_deal_wage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='branch_code',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='wage',
        ),
    ]
