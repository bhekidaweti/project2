# Generated by Django 4.2.5 on 2023-11-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_bid_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='listing',
            name='imageURL',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]