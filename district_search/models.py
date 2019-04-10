# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names

from django.db import models
from postgres_copy import CopyManager

class Districts(models.Model):
    id = models.IntegerField(
        primary_key=True,
        # source_column='a'
    )
    school_year = models.IntegerField(
        # db_column='SCHOOL_YEAR',
    )
    district_name = models.CharField(
        # source_column='DISTRICT_NAME',
        max_length=100,
    )
    enrollment_grades_k_12 = models.IntegerField(
        # source_column='ENROLLMENT_GRADES_K_12',
    )
    total_susp = models.IntegerField()
    iss_b = models.IntegerField(
        # source_column='iss_B',
        null=True,
    )
    oss_b = models.IntegerField(
        # source_column='oss_B',
        null=True,
    )
    iss_w = models.IntegerField(
        # source_column='iss_W',
        null=True,
    )
    oss_w = models.IntegerField(
        # source_column='oss_W',
        null=True,
    )
    h = models.IntegerField(
        # source_column='H',
        null=True,
    )
    a = models.IntegerField(
        # source_column='A',
        null=True,
    )
    m = models.IntegerField(
        # source_column='M',
        null=True,
    )
    p = models.IntegerField(
        # source_column='P',
        null=True,
    )
    i = models.IntegerField(
        # source_column='I',
        null=True,
    )
    b_disp = models.FloatField(
        # source_column='B_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )
    w_disp = models.FloatField(
        # source_column='W_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )
    h_disp = models.FloatField(
        # source_column='H_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )
    a_disp = models.FloatField(
        # source_column='A_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )
    m_disp = models.FloatField(
        # source_column='M_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )
    p_disp = models.FloatField(
        # source_column='P_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )
    i_disp = models.FloatField(
        # source_column='I_disp',
        # max_digits=5, decimal_places=4,
        null=True,
    )

    objects = CopyManager()
