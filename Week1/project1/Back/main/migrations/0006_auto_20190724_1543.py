# Generated by Django 2.2.2 on 2019-07-24 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190724_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='folder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='main.Folder'),
        ),
    ]