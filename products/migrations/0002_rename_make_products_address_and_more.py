# Generated by Django 5.0.4 on 2024-05-19 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='make',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='model',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='price',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='products',
            name='body',
        ),
        migrations.AddField(
            model_name='products',
            name='year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
