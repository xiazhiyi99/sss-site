from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
    file_name = models.CharField(max_length=30)
    pub_date = models.TimeField('publish_date')
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='repository/')

    def convert_bytes(self,num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    @property
    def size(self):
        return self.convert_bytes(self.file.size)