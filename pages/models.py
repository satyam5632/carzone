from django.db import models

# Create your models here.
class Team(models.Model):
    f_name=models.CharField(max_length=10)
    l_name=models.CharField(max_length=10)
    designation=models.CharField(max_length=10)
    photo=models.ImageField(upload_to='photos/%Y/%M/%d/')
    fb_link=models.URLField(max_length=100)
    twt_link=models.URLField(max_length=100)
    g_link=models.URLField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name
