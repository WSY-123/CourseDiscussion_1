from django.db import models


# Create your models here.
class lessons(models.Model):
    """课程的属性"""
    number = models.CharField(max_length=10)  # 课程号
    name = models.CharField(max_length=10)  # 课程名称
    teacher = models.CharField(max_length=5)  # 开课教师
    institute = models.CharField(max_length=20)  # 开课学院
    credit = models.FloatField()  # 学分
    semester = models.CharField(max_length=15)  # 开课学年
    time = models.CharField(max_length=20)  # 上课时间
    weeks = models.CharField(max_length=20)  # 开课周次
    location = models.CharField(max_length=10)  # 上课地点
    date_added = models.DateTimeField(auto_now_add=True)  # 课程添加时间

    def __str__(self):
        """返回模型地字段表示"""
        return self.name


class feedback(models.Model):
    """反馈"""
    title = models.CharField(max_length=20)  # 标题
    text = models.TextField()  # 内容
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回反馈的字段显示"""
        return self.title
