from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20)
    email = models.EmailField(verbose_name='邮箱', max_length=25)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.CharField(verbose_name='内容', max_length=300)

    post = models.ForeignKey('blog.Post', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.content[:20]


