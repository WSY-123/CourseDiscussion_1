from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Tag, Question, Answer, Comment
from .forms import NewQuestionForm, NewAnswerForm, AddCommentForm


def index(request):
    questions = Question.objects.order_by('-create_at')
    return render(request, 'index.html', {'questions': questions})


def tags_page(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', {'tags': tags})


def tag_questions(request, id):
    tag = get_object_or_404(Tag, id=id)
    questions = tag.questions.order_by('-create_at')
    return render(request, 'tag_questions.html', {'tag': tag, 'questions': questions})


def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    question.views += 1
    question.save()
    if request.method == 'POST':
        if request.POST.get("which") == "answer":
            answer_form = NewAnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.save()
        elif request.POST.get("which") == "comment":
            comment_form = AddCommentForm(request.POST)
            if comment_form.is_valid():
                answer = get_object_or_404(Answer, id=int(request.POST.get("current_answer")))
                comment = comment_form.save(commit=False)
                comment.answer = answer
                comment.save()
        return redirect(reverse('discuss:question_details', kwargs={'id': question.id}))

    else:
        answer_form = NewAnswerForm()
        comment_form = AddCommentForm()
        return render(request, 'question_details.html',
                      {'question': question, 'answer_form': answer_form, 'comment_form': comment_form})


def ask_question(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.save()
        return redirect(reverse('discuss:question_details', kwargs={'id': question.id}))

    else:
        form = NewQuestionForm()

        return render(request, 'ask_question.html', {'form': form})
