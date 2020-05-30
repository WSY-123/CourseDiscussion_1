from django.db import models


# Create your models here.
class lessons(models.Model):
    """课程的属性"""
    number = models.CharField(max_length=10)  # 课程号
    name = models.CharField(max_length=10)  # 课程名称
    teacher = models.CharField(max_length=5)  # 开课教师
    institute = models.CharField(max_length=20, default="船舶海洋与建筑工程学院")  # 开课学院
    credit = models.FloatField(default=2.0)  # 学分
    semester = models.CharField(max_length=15, default="2019-2020-1")  # 开课学年
    day = models.IntegerField(default=0)  # 周几上课
    time_started = models.IntegerField(default=0)   #第几节开始
    time_ended = models.IntegerField(default=0)  #第几节结束
    week_started = models.IntegerField(default=0)  # 开始周次
    week_ended = models.IntegerField(default=0)   # 结束周次
    is_interval = models.IntegerField(default=0)   # 是否为单双周，不是为0，单周为1，双周为2
    location = models.CharField(max_length=10, default="上院102")  # 上课地点
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
