# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class App(models.Model):
    id = models.IntegerField(
        primary_key=True,
        source_column='a'
    )
    school_year = models.IntegerField(
        source_column='SCHOOL_YEAR',
        max_digits=4,
    )
    district_name = models.CharField(
        source_column='DISTRICT_NAME',
        max_length=100,
    )
    enrollment_grades_k_12 = models.IntegerField(
        source_column='ENROLLMENT_GRADES_K_12',
    )
    total_susp = models.IntegerField()
    iss_b = models.IntegerField(source_column='iss_B',)
    oss_b = models.IntegerField(source_column='oss_B',)
    iss_w = models.IntegerField(source_column='iss_W',)
    oss_w = models.IntegerField(source_column='oss_W',)
    h = models.IntegerField(source_column='H', )
    a_0 = models.IntegerField(source_column='A', )
    m = models.IntegerField(soursource_column='M', )
    p = models.IntegerField(source_column='P', )
    i = models.IntegerField(source_column='I', )
    b_disp = models.DecimalField(source_column='B_disp', max_digits=5, decimal_places=1,)
    w_disp = models.DecimalField(source_column='W_disp', max_digits=5, decimal_places=1,)
    h_disp = models.DecimalField(source_column='H_disp', max_digits=5, decimal_places=1,)
    a_disp = models.DecimalField(source_column='A_disp', max_digits=5, decimal_places=1,)
    m_disp = models.DecimalField(source_column='M_disp', max_digits=5, decimal_places=1,)
    p_disp = models.DecimalField(source_column='P_disp', max_digits=5, decimal_places=1,)
    i_disp = models.DecimalField(source_column='I_disp', max_digits=5, decimal_places=1,)
