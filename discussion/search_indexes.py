from haystack import indexes
from .models import Tag, Question


class QuestionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, model_attr='tags')  # 创建一个text字段
    #title = indexes.CharField(max_length=100, model_attr='title')
    #body = indexes.CharField(max_length=1000, model_attr='body')
    #create_at = indexes.DateTimeField(auto_now_add=True, model_attr='create_at')
    #views = indexes.PositiveIntegerField(default=0, model_attr='views')
    # 对那张表进行查询
    def get_model(self):
        # 返回这个model
        return Question

    # 针对哪些数据进行查询
    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()