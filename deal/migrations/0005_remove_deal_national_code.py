# Generated by Django 4.0.3 on 2022-03-16 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_remove_deal_branch_code_remove_deal_wage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='national_code',
        ),
    ]
