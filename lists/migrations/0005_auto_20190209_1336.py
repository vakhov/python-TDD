# Generated by Django 2.1.5 on 2019-02-09 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='list',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]
