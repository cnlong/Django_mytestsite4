from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,JsonResponse
from booktest.models import *
# 导入分页类
from django.core.paginator import Paginator


# Create your views here.
def static_test(request):
    """静态文件"""
    return render(request, 'booktest/static_test.html')


# 定义禁止访问的用户ip
EXCLUDE_IPS = ['127.0.0.1']
def block_ips(view_func):
    def wrapper(request, *args, **kwargs):
        # 获取浏览器端的ip地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper


# @block_ips
def index(request):
    """首页"""
    print('---index---')
    return render(request, 'booktest/index.html')


def upload_pic(request):
    """上传图片页面"""
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    """上传图片处理"""
    # 1.获取上传图片的处理对象
    pic = request.FILES['pic']
    # # 上传文件的类型
    # print(type(pic))
    # # 上传文件的名称
    # print(pic.name)
    # 2.创建一个文件
    # 创建图片保存的路径
    save_path = "{0}/booktest/{1}".format(settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容，并写入到创建的文件
        # pic.chunks()，返回一个生成器，将图片分词一块一块的小部分，可以遍历获取
        for content in pic.chunks():
            f.write(content)
    # 4.在数据库中中保存上传记录
    PicTest.objects.create(goods_pic='booktest/{0}'.format(pic.name))
    # 5.返回
    return HttpResponse('ok')


def show_area(request, pindex):
    """分页"""
    # 1.查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aParent_id=0)
    # 2.分页，一页显示10条数据,对查询集进行分页
    paginator = Paginator(areas, 10)
    # 3.获取第pindex页的内容
    if pindex == '':
        # 默认取第一页的内容
        pindex = 1
    else:
        pindex = int(pindex)
    # page是Page类的实例对象
    page = paginator.page(pindex)

    # 2.使用模板
    return render(request, 'booktest/show_area.html', {'page': page})


def areas(request):
    """省市县选择案例"""
    return render(request, 'booktest/areas.html')


def prov(request):
    """获取所有省级地区的信息"""
    # 1.获取所有省级地区的信息
    # 注意：查询得到的查询集无法进行json序列化，需要经过转换为可序列化的数据，例如列表
    areas = AreaInfo.objects.filter(aParent_id=0)
    # 2/遍历areas并拼接处json数据:atitle id
    areas_list = list()
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # 3.返回数据
    return JsonResponse({'data': areas_list})


def city(request, pid):
    """获取pid的下级市级地区的信息"""
    # 1.获取pid对应的下级信息
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent_id=pid)
    # 2/遍历areas并拼接处json数据:atitle id
    areas_list = list()
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # 3.返回数据
    return JsonResponse({'data': areas_list})


def dis(request, cid):
    """获取cid的下级县级地区的信息"""
    # 1.获取cid对应的下级信息
    areas = AreaInfo.objects.filter(aParent_id=cid)
    # 2/遍历areas并拼接处json数据:atitle id
    areas_list = list()
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # 3.返回数据
    return JsonResponse({'data': areas_list})


def set_session(request):
    """设置session"""
    request.session['username'] = 'smart'
    request.session['age'] = 18

    return HttpResponse('设置session')


def get_session(request):
    """设置session"""
    username = request.session['username']
    age = request.session['age']

    return HttpResponse(username, age)