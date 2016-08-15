from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()
    def __repr__(self):
    # 主キーとnameを表示させて見やすくする
        return "{}: {}".format(self.pk, self.name)
    __str__ = __repr__

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts') #related_nameはリレーション先のオブジェクトから逆参照するときに使われる名前
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    # 
    # def __str__(self):
    #     return self.title
