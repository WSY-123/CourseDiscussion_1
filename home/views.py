from django.shortcuts import render
from search.models import lessons
from users.models import User
from discussion.models import Question, Tag


def homepage(request):
    users = User.objects.all()
    lessonlist = lessons.objects.all()
    questions = Question.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {'users':users, 'lessons': lessonlist, 'questions': questions, 'tags': tags})
