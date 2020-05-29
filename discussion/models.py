from django.db import models
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag, related_name='questions', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.title

class Answer(models.Model):
    message = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')


class Comment(models.Model):
    message = models.CharField(max_length=1000)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments')
    create_at = models.DateTimeField(auto_now_add=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')