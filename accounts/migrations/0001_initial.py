# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('email', models.EmailField(primary_key=True, max_length=254, serialize=False)),
                ('groups', models.ManyToManyField(related_name='user_set', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', to='auth.Group', related_query_name='user', blank=True)),
                ('user_permissions', models.ManyToManyField(related_name='user_set', verbose_name='user permissions', help_text='Specific permissions for this user.', to='auth.Permission', related_query_name='user', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=255)),
            ],
        ),
    ]
