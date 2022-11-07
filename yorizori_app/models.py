from django.db import models

class MemberInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'member_info'


class Recipe(models.Model):
    id = models.ForeignKey(MemberInfo, models.DO_NOTHING, db_column='id')
    source = models.CharField(max_length=100, blank=True, null=True)
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    info = models.CharField(max_length=100, blank=True, null=True)
    ex = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    c_like = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recipe'


class Review(models.Model):
    id = models.ForeignKey(MemberInfo, models.DO_NOTHING, db_column='id', blank=True, null=True)
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING)
    coment = models.CharField(max_length=100, blank=True, null=True)
    num = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'review'