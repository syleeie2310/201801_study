# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class About(models.Model):
    about_me = models.CharField(max_length=255)
    home_img = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'about'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Domain(models.Model):
    title_kor = models.CharField(max_length=45, blank=True, null=True)
    title_eng = models.CharField(max_length=45)
    desc_kor = models.TextField(blank=True, null=True)
    desc_eng = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'domain'


class Experience(models.Model):
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    title_kor = models.CharField(max_length=100)
    title_eng = models.CharField(max_length=150, blank=True, null=True)
    location_kor = models.CharField(max_length=100)
    location_eng = models.CharField(max_length=150)
    desc_kor = models.TextField()
    desc_eng = models.TextField(blank=True, null=True)
    ex_type = models.ForeignKey('ExperienceType', db_column='ex_type')

    class Meta:
        managed = True
        db_table = 'experience'


class ExperienceType(models.Model):
    title = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = True
        db_table = 'experience_type'

    def __str__(self):
        return self.title

class Project(models.Model):
    title_kor = models.CharField(max_length=45)
    title_eng = models.CharField(max_length=45, blank=True, null=True)
    title_img = models.CharField(max_length=100, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    desc_kor = models.TextField()
    desc_eng = models.TextField(blank=True, null=True)
    proj_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project'


class Publication(models.Model):
    p_date = models.DateField()
    citation_kor = models.CharField(max_length=100)
    citation_eng = models.CharField(max_length=150, blank=True, null=True)
    desc_kor = models.CharField(max_length=300, blank=True, null=True)
    desc_eng = models.CharField(max_length=300, blank=True, null=True)
    p_type = models.ForeignKey('PublicationType', db_column='p_type')
    p_url = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'publication'


class PublicationType(models.Model):
    p_type = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = True
        db_table = 'publication_type'

    def __str__(self):
        return self.p_type