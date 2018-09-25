from django.db import models

class AType(models.Model):
    """文章类型表"""
    types = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'AType'


class Article(models.Model):
    """文章表"""
    title = models.CharField(max_length=30, null=False)  # 文章标题
    is_show = models.BooleanField(default=False)  # 是否展示，False为不展示，True为展示
    is_recommend = models.BooleanField(default=False)  # 是否推荐，False为不推荐，True为推荐
    desc = models.CharField(max_length=100, null=True)  # 内容描述
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    content = models.TextField()  # 文章内容
    t = models.ForeignKey(AType, null=False, on_delete=models.CASCADE)  # 文章分类

    class Meta:
        db_table = 'article'

