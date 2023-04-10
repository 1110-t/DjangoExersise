from django.db import models

# 性別の選択肢
GENDER_CHOICES = [
    (0,'男性'),
    (1,'女性'),
    (2,'その他')
]

# 血液型の選択肢
BLOOD_CHOICES = [
    ('a','A型'),
    ('b','B型'),
    ('o','O型'),
    ('ab','AB型'),
    ('etc','不明')
]

# Create your models here.
class User(models.Model):
    name = models.CharField(blank=False,null=False,max_length=20)
    birthday = models.DateTimeField(blank=False,null=False)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    bloodtype = models.CharField(max_length=3,choices=BLOOD_CHOICES)
    profile = models.CharField(blank=False,null=False,max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title