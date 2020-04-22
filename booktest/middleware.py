from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class BlockedIPSMiddleware(MiddlewareMixin):
    """中间件类"""
    # 定义禁止访问的用户ip
    EXCLUDE_IPS = ['127.0.0.1']

    def process_view(self, request, view_func, *args, **kwargs):
        """视图函数调用之前会调用这个函数"""
        # 获取浏览器端的ip地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>禁止访问</h1>')


class TestMiddleware(MiddlewareMixin):
    """中间件类"""
    def __init__(self, get_response):
        """服务器重启之后调用"""
        print("----init----")
        self.get_response = get_response

    def process_request(self, request):
        """产生request对象之后，url匹配之前调用"""
        print("----process_request----")

    def process_view(self, request, view_func, *args, **kwargs):
        """Url匹配之后，视图函数调用之前调用"""
        print("----process_view----")

    def process_response(self, request, response):
        """视图函数调用之后，内容返回浏览器之前"""
        print("----process_response----")
        return response


class ExceptionTestMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        """视图函数发送异常时调用"""
        print("--process_exception--")