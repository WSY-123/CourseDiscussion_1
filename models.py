from django.db import models
from django import forms
from captcha.fields import CaptchaField


# Create your models here.
class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    institute = (
        ('船院','船舶海洋与建筑工程学院'),
        ('电院', '电子信息与电气工程学院'),
        ('机动', '机械与动力工程学院'),
        ('材料','材料科学与工程学院'),
        ('环境','环境科学与工程学院'),
        ('生医工','生物医学工程学院'),
        ('航空','航空航天学院'),
        ('数学','数学科学学院'),
        ('物理','物理与天文学院'),
        ('化学', '化学化工学院'),
        ('致远','致远学院'),
        ('海洋','海洋学院'),
        ('生命科学','生命科学技术学院'),
        ('农学院','农业与生物学院'),
        ('药学院','药学院'),
        ('医学院', '医学院'),
        ('安泰', '安泰经济与管理学院'),
        ('法学院','凯原法学院'),
        ('外院','外国语学院'),
        ('人文','人文学院'),
        ('马院','马克思主义学院'),
        ('媒体','媒体与传播学院'),
        ('设计','设计学院'),

    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')
    institute = forms.ChoiceField(label='学院', choices=institute)

class User(models.Model):
    '''用户表'''
    gender = (
        ('male', '男'),
        ('female', '女'),
    )
    institute=(
        ('船院', '船舶海洋与建筑工程学院'),
        ('电院', '电子信息与电气工程学院'),
        ('机动', '机械与动力工程学院'),
        ('材料', '材料科学与工程学院'),
        ('环境', '环境科学与工程学院'),
        ('生医工', '生物医学工程学院'),
        ('航空', '航空航天学院'),
        ('数学', '数学科学学院'),
        ('物理', '物理与天文学院'),
        ('化学', '化学化工学院'),
        ('致远', '致远学院'),
        ('海洋', '海洋学院'),
        ('生命科学', '生命科学技术学院'),
        ('农学院', '农业与生物学院'),
        ('药学院', '药学院'),
        ('医学院', '医学院'),
        ('安泰', '安泰经济与管理学院'),
        ('法学院', '凯原法学院'),
        ('外院', '外国语学院'),
        ('人文', '人文学院'),
        ('马院', '马克思主义学院'),
        ('媒体', '媒体与传播学院'),
        ('设计', '设计学院'),
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    c_time = models.DateTimeField(auto_now_add=True)
    mylessons = models.ManyToManyField('search.lessons', related_name='myusers')
    institute = models.CharField( max_length=20,choices=institute,default='电院')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
