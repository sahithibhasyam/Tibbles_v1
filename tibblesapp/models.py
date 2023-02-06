from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#---------------------------------------------------------------------------------------
    
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

#---------------------------------------------------------------------------------------

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

#---------------------------------------------------------------------------------------

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

#---------------------------------------------------------------------------------------

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

#---------------------------------------------------------------------------------------

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

#---------------------------------------------------------------------------------------

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

#---------------------------------------------------------------------------------------

class Department(models.Model):
    d_no = models.IntegerField(db_column='D_NO', primary_key=True)  # Field name made lowercase.
    d_name = models.CharField(db_column='D_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    d_hod = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='D_HOD_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'

#---------------------------------------------------------------------------------------

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

#---------------------------------------------------------------------------------------

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

#---------------------------------------------------------------------------------------

class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

#---------------------------------------------------------------------------------------

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

#---------------------------------------------------------------------------------------

class Faculty(models.Model):
    faculty_id = models.IntegerField(db_column='FACULTY_ID', primary_key=True)  # Field name made lowercase.
    faculty_name = models.CharField(db_column='FACULTY_NAME', max_length=50)  # Field name made lowercase.
    d_no = models.ForeignKey(Department, models.DO_NOTHING, db_column='D_NO', blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'faculty'

#---------------------------------------------------------------------------------------

class PrefSlot(models.Model):
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='FACULTY_ID')  # Field name made lowercase.
    day = models.CharField(db_column='DAY', primary_key=True, max_length=9)  # Field name made lowercase.
    slot_no = models.ForeignKey('Slot', models.DO_NOTHING, db_column='SLOT_NO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pref_slot'
        unique_together = (('day', 'slot_no', 'faculty'),)

#---------------------------------------------------------------------------------------

class PrefSub(models.Model):
    faculty = models.OneToOneField(Faculty, models.DO_NOTHING, db_column='FACULTY_ID', primary_key=True)  # Field name made lowercase.
    pref_1 = models.ForeignKey('Subject', models.DO_NOTHING, db_column='PREF_1', related_name='pref_1_subjects')  # Field name made lowercase.
    pref_2 = models.ForeignKey('Subject', models.DO_NOTHING, db_column='PREF_2', related_name='pref_2_subjects')  # Field name made lowercase.
    pref_3 = models.ForeignKey('Subject', models.DO_NOTHING, db_column='PREF_3', related_name='pref_3_subjects')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pref_sub'

#---------------------------------------------------------------------------------------

class Slot(models.Model):
    day = models.CharField(db_column='DAY', max_length=9)  # Field name made lowercase.
    slot_no = models.IntegerField(db_column='SLOT_NO', primary_key=True)  # Field name made lowercase.
    hours = models.IntegerField(db_column='HOURS')  # Field name made lowercase.
    slot_starttime = models.TimeField(db_column='SLOT_STARTTIME')  # Field name made lowercase.
    slot_endtime = models.TimeField(db_column='SLOT_ENDTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slot'
        unique_together = (('slot_no', 'day'),)

#---------------------------------------------------------------------------------------

class SlotAllocationSem3(models.Model):
    faculty_id = models.IntegerField(db_column='FACULTY_ID', blank=True, null=True)  # Field name made lowercase.
    subject_code = models.CharField(db_column='SUBJECT_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(db_column='DAY', primary_key=True, max_length=9)  # Field name made lowercase.
    slot_no = models.ForeignKey(Slot, models.DO_NOTHING, db_column='SLOT_NO')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'slot_allocation_sem3'
        unique_together = (('day', 'slot_no'),)

#---------------------------------------------------------------------------------------

class Subject(models.Model):
    subject_code = models.CharField(db_column='SUBJECT_CODE', primary_key=True, max_length=50)  # Field name made lowercase.
    d_no = models.ForeignKey(Department, models.DO_NOTHING, db_column='D_NO')  # Field name made lowercase.
    subject_name = models.CharField(db_column='SUBJECT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    semester = models.IntegerField(db_column='SEMESTER', blank=True, null=True)  # Field name made lowercase.
    hours_per_week = models.IntegerField(db_column='HOURS_PER_WEEK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subject'
        unique_together = (('subject_code', 'd_no'),)

#---------------------------------------------------------------------------------------

class SubjectAllocations(models.Model):
    faculty_id = models.IntegerField(db_column='Faculty_ID', primary_key=True)  # Field name made lowercase.
    subject_code = models.CharField(db_column='Subject_code', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subject_allocations'
        unique_together = (('faculty_id', 'subject_code'),)


#---------------------------------------------------------------------------------------

class Timetable(models.Model):
    subject_code = models.CharField(db_column='SUBJECT_CODE', primary_key=True, max_length=50)  # Field name made lowercase.
    slot_no = models.IntegerField(db_column='SLOT_NO')  # Field name made lowercase.
    faculty_id = models.IntegerField(db_column='FACULTY_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'timetable'
        unique_together = (('subject_code', 'slot_no'),)

#---------------------------------------------------------------------------------------

class Users(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    d_no = models.IntegerField(db_column='D_NO')  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

#---------------------------------------------------------------------------------------

class displaydata(models.Model):
    day = models.CharField(max_length=10)
    timings = models.CharField(max_length=50)
    subject_code = models.CharField(max_length=10)
    faculty_name = models.CharField(max_length=50)
    