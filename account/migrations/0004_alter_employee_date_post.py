# Generated by Django 4.0.4 on 2022-05-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_typeuser_remove_user_comment_remove_user_date_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_post',
            field=models.DateField(auto_now_add=True),
        ),
    ]