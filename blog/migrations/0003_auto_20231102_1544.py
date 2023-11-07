# Generated by Django 3.2.21 on 2023-11-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20231101_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='method',
        ),
        migrations.AddField(
            model_name='recipe',
            name='content',
            field=models.TextField(default='Default Content'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='excerpt',
            field=models.TextField(default='Default Excerpt'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='Default Description'),
        ),
    ]
