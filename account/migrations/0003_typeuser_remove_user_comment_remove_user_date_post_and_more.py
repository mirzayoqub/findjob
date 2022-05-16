# Generated by Django 4.0.4 on 2022-05-16 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_skills'),
        ('account', '0002_remove_type_job_alter_user_type_delete_job_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_post',
        ),
        migrations.RemoveField(
            model_name='user',
            name='img',
        ),
        migrations.RemoveField(
            model_name='user',
            name='price',
        ),
        migrations.RemoveField(
            model_name='user',
            name='type',
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='uploads')),
                ('comment', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('date_post', models.DateField()),
                ('price', models.IntegerField()),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.URLField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiance', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('old', models.IntegerField()),
                ('img', models.ImageField(upload_to='uploads')),
                ('comment', models.TextField()),
                ('date_post', models.DateField()),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=50)),
                ('contact', models.URLField()),
                ('type', models.ManyToManyField(to='main.type')),
                ('type_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.typeuser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]