from django.db import models

# Create your models here.

class Datas():
    file_name = models.CharField(max_length=128,null=False, blank=False)
    rows = models.IntegerField(default=0)
    #어떤 주제?
    feature1 = models.CharField(max_length=128,null=False, blank=False)
    feature2 = models.CharField(max_length=128,null=False, blank=False)
    feature3 = models.CharField(max_length=128,null=False, blank=False)
    feature4 = models.CharField(max_length=128,null=False, blank=False)
    models.DateTimeField('date published')