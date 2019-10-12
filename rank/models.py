from django.db import models

# Create your models here.
class Rank(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('publish_date')
    submission = models.IntegerField(default=0)
    state = models.CharField(max_length=20,default='open')
    def __str__(self):
        return self.title
    def update(self):
        self.submission = len(Record.objects.filter(rank = self))

class Record(models.Model):
    publisher = models.CharField(max_length=100)
    score = models.FloatField()
    pub_date = models.DateTimeField('publish_date')
    rank = models.ForeignKey(to=Rank, on_delete=models.CASCADE)
