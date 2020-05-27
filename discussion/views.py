from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Tag, Question, Answer, Comment
from .forms import NewQuestionForm, NewAnswerForm, AddCommentForm, AddTagForm
from users.models import User


def index(request):
    """问答主页"""
    new_questions = Question.objects.order_by('-create_at')
    hot_questions = Question.objects.order_by('-views')
    tags = Tag.objects.all()
    return render(request, 'discussion/index.html',
                  {'new_questions': new_questions, 'hot_questions': hot_questions, 'tags': tags})


def tag_questions(request, id):
    """标签下问题列表"""
    tag = get_object_or_404(Tag, id=id)
    questions = tag.questions.order_by('-create_at')
    return render(request, 'discussion/tag_questions.html', {'tag': tag, 'questions': questions})


def question_details(request, id):
    """问题详情页"""
    question = get_object_or_404(Question, id=id)
    question.views += 1
    question.save()
    if request.method == 'POST':
        if request.POST.get("which") == "answer":  # 用户所提交的是回答
            answer_form = NewAnswerForm(request.POST)
            if answer_form.is_valid():
                answer = answer_form.save(commit=False)
                answer.question = question
                answer.create_by = User.objects.get(id=request.session.get('user_id'))
                answer.save()
        elif request.POST.get("which") == "comment":  # 用户所提交的是评论
            comment_form = AddCommentForm(request.POST)
            if comment_form.is_valid():
                answer = get_object_or_404(Answer, id=int(request.POST.get("current_answer")))
                comment = comment_form.save(commit=False)
                comment.answer = answer
                comment.create_by = User.objects.get(id=request.session.get('user_id'))
                comment.save()
        return redirect(reverse('discuss:question_details', kwargs={'id': question.id}))

    else:
        answer_form = NewAnswerForm()
        comment_form = AddCommentForm()
        return render(request, 'discussion/question_details.html',
                      {'question': question, 'answer_form': answer_form, 'comment_form': comment_form})


def ask_question(request):
    """提问"""
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.asked_by = User.objects.get(id=request.session.get('user_id'))
            question.save()
        return redirect(reverse('discuss:question_details', kwargs={'id': question.id}))

    else:
        form = NewQuestionForm()

        return render(request, 'discussion/ask_question.html', {'form': form})


def add_tag(request):
    """添加新的标签"""
    if request.method == 'POST':
        form = AddTagForm(request.POST)
        if form.is_valid():
            tag = form.save()
            tag.save()
        return redirect(reverse('discuss:index'))
    else:
        form = AddTagForm()
        return render(request, 'discussion/add_tag.html', {'form': form})
