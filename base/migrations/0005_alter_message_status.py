# Generated by Django 3.2.7 on 2021-10-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_message_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]