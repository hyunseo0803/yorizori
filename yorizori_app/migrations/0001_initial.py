# Generated by Django 4.1.1 on 2022-12-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInfo',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'member_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('recipe_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('info', models.TextField(blank=True, max_length=255, null=True)),
                ('ex', models.TextField(blank=True, max_length=255, null=True)),
                ('img_url', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'recipe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('coment', models.CharField(blank=True, max_length=100, null=True)),
                ('num', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
    ]
