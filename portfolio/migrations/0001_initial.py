# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(null=True, blank=True, max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(primary_key=True, serialize=False, max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(max_length=255)),
                ('home_img', models.CharField(null=True, blank=True, max_length=45)),
            ],
            options={
                'db_table': 'about',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title_kor', models.CharField(null=True, blank=True, max_length=45)),
                ('title_eng', models.CharField(max_length=45)),
                ('desc_kor', models.TextField(null=True, blank=True)),
                ('desc_eng', models.TextField(null=True, blank=True)),
                ('icon', models.CharField(null=True, blank=True, max_length=45)),
            ],
            options={
                'db_table': 'domain',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField(null=True, blank=True)),
                ('title_kor', models.CharField(max_length=100)),
                ('title_eng', models.CharField(null=True, blank=True, max_length=150)),
                ('location_kor', models.CharField(max_length=100)),
                ('location_eng', models.CharField(max_length=150)),
                ('desc_kor', models.TextField()),
                ('desc_eng', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'experience',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ExperienceType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'experience_type',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title_kor', models.CharField(max_length=45)),
                ('title_eng', models.CharField(null=True, blank=True, max_length=45)),
                ('title_img', models.CharField(null=True, blank=True, max_length=100)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField(null=True, blank=True)),
                ('desc_kor', models.TextField()),
                ('desc_eng', models.TextField(null=True, blank=True)),
                ('proj_url', models.CharField(null=True, blank=True, max_length=255)),
            ],
            options={
                'db_table': 'project',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('p_date', models.DateField()),
                ('citation_kor', models.CharField(max_length=100)),
                ('citation_eng', models.CharField(null=True, blank=True, max_length=150)),
                ('desc_kor', models.CharField(null=True, blank=True, max_length=300)),
                ('desc_eng', models.CharField(null=True, blank=True, max_length=300)),
                ('p_url', models.CharField(null=True, blank=True, max_length=300)),
            ],
            options={
                'db_table': 'publication',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('p_type', models.CharField(unique=True, max_length=45)),
            ],
            options={
                'db_table': 'publication_type',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='p_type',
            field=models.ForeignKey(db_column='p_type', to='portfolio.PublicationType'),
        ),
        migrations.AddField(
            model_name='experience',
            name='ex_type',
            field=models.ForeignKey(db_column='ex_type', to='portfolio.ExperienceType'),
        ),
    ]
