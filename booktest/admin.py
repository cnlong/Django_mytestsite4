from django.contrib import admin
from booktest.models import AreaInfo,PicTest
# Register your models here.

class AreaInfoAdmin(admin.ModelAdmin):
    """地区模型管理"""
    list_per_page = 10  # 指定每页显示10条
    list_display = ['id', 'atitle', 'title']  # 指定显示的条目，其中'title'是在其模型类中定义的方法
    # 在后台数据显示页面下面也加载一个可删除数据的功能
    actions_on_bottom = True
    # 隐藏后台数据显示页面上面的删除功能
    actions_on_top = False
    # 列表页右侧过滤栏
    list_filter = ['atitle']
    # 列表页上方的搜索框
    search_fields = ['atitle']

admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)