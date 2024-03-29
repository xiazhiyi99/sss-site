from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    # 模型类中设置:blank=True,表示代码中创建数据库记录时该字段可传空白(空串,空字符串)
    student_number = models.CharField(max_length=9, blank=False, primary_key=True)
    group_name = models.CharField(max_length=5, choices=(
        ('DS', 'DS/DL组'),
        ('YX', '游戏组'),
        ('AZ', '安卓组'),
        ('WA', '网安组'),
    ))

    class Meta:
        verbose_name = 'User'

    def __str__(self):
        # return self.user.__str__()
        return "{}".format(self.user.__str__())
