# Generated by Django 2.2.2 on 2019-07-24 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20190724_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main.Folder'),
        ),
    ]