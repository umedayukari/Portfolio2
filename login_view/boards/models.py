from django.db import models
from django.conf import settings

# Create your models here.
class ThemesManager(models.Manager):

    def fetch_all_themes(self):
        return self.order_by('id').all()


class Themes(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    objects = ThemesManager()
    
    class Meta:
        db_table = 'themes'

class Comments(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    theme = models.ForeignKey(
        'Themes', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'comments'

# Opponent情報のモデル
class Opponent(models.Model):
    date = models.DateField()
    sex = models.CharField(max_length=1)
    name = models.CharField(max_length=255)
    anniversary_details = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'opponents'

# 記念日記録のモデル
class AnniversaryRecords(models.Model):
    date = models.DateField()
    relationships = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    present = models.CharField(max_length=255)
    present_type = models.CharField(max_length=255)
    range_of_amounts = models.CharField(max_length=255)
    amount_of_money = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='photos/')
    memories = models.TextField()
    self_assessment = models.TextField()
    improvements = models.TextField()
    opponent = models.ForeignKey('Opponent', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'anniversary_records'
