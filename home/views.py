from django.shortcuts import render
from search.models import lessons
from discussion.models import Question, Tag


def homepage(request):
    lessonlist = lessons.objects.all()
    questions = Question.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {'lessons': lessonlist, 'questions': questions, 'tags': tags})
