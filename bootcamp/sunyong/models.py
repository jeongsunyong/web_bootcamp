from django.db import models
import os
# Create your models here.

def user_upload_to(instance,filename):
    path_user='videos/{}'.format(instance.username)
    if not os.path.isdir('media/'+path_user):
        os.mkdir('media/'+path_user)
    extension=os.path.splitext(filename)[-1].lower()
    return path_user+"/{}".format(instance.title)+extension

class FileUpload(models.Model):
    username = models.CharField(max_length=150)
    title = models.CharField(max_length=100)
    vid = models.FileField(null=True, blank=True, upload_to=user_upload_to)
    uploaded_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def __who__(self):
        return self.username
    
