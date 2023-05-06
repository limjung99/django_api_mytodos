from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# model들은 Model을 inheritance한다.
# model마다 class 변수는 모델에서 데이터베이스 필드를 나타낸다.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1)<= self.pub_date <= now
    

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    chocie_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.chocie_text