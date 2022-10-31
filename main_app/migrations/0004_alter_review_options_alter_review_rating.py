# Generated by Django 4.1.1 on 2022-10-28 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_review_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=1),
        ),
    ]