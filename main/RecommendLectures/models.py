from django.db import models

# Create your models here.
class Generalculture(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', primary_key=True, max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'GeneralCulture'
        unique_together = (('professor', 'subjects'),)


class Mscdataprocess(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', primary_key=True, max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'MscDataProcess'
        unique_together = (('professor', 'subjects'),)


class Mscmath(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'MscMath'
        unique_together = (('subjects', 'professor'),)


class Mscscience(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'MscScience'
        unique_together = (('subjects', 'professor'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class Major21(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'major21'
        unique_together = (('subjects', 'professor'),)


class Major22(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'major22'
        unique_together = (('subjects', 'professor'),)


class Major31(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'major31'
        unique_together = (('subjects', 'professor'),)


class Major32(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'major32'
        unique_together = (('subjects', 'professor'),)


class Major41(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'major41'
        unique_together = (('subjects', 'professor'),)


class Major42(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'major42'
        unique_together = (('subjects', 'professor'),)


class MajorAll(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, db_collation='utf8_bin', blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45, db_collation='utf8_bin')  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, db_collation='utf8_bin', blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45, db_collation='utf8_bin')  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, db_collation='utf8_bin', blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, db_collation='utf8_bin', blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, db_collation='utf8_bin', blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, db_collation='utf8_bin', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    division = models.CharField(db_column='Division', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'major_all'
        unique_together = (('subjects', 'professor'),)


class Specialistculture(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', primary_key=True, max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'specialistculture'
        unique_together = (('professor', 'subjects'),)


class Specialistenglist(models.Model):
    opensemester = models.CharField(db_column='OpenSemester', max_length=45, blank=True, null=True)  # Field name made lowercase.
    subjects = models.CharField(db_column='Subjects', primary_key=True, max_length=45)  # Field name made lowercase.
    campus = models.CharField(db_column='Campus', max_length=45, blank=True, null=True)  # Field name made lowercase.
    professor = models.CharField(db_column='Professor', max_length=45)  # Field name made lowercase.
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    homework = models.CharField(db_column='Homework', max_length=45, blank=True, null=True)  # Field name made lowercase.
    groupmeeting = models.CharField(db_column='GroupMeeting', max_length=45, blank=True, null=True)  # Field name made lowercase.
    perofcredits = models.CharField(db_column='PerOfCredits', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=45, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'specialistenglist'
        unique_together = (('subjects', 'professor'),)
