from django.db import models

# Create your models here.
class AreaInfo(models.Model):
    """地址模型类"""
    # verbose_name='标题' 定义其在后台中条目显示的名称
    atitle = models.CharField(verbose_name='标题', max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle

    # 自定义后台显示的条目的方法
    def title(self):
        return self.atitle
    # 自定义的条目默认无法排序，可以设置其依赖于其他可排序的条目进行排序
    title.admin_order_field = 'atitle'
    # 自定义的条目，自定义其显示的名称
    title.short_description = '地区名称'


class PicTest(models.Model):
    """上传图片"""
    goods_pic = models.ImageField(upload_to='booktest')