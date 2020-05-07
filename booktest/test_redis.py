from redis import *

if __name__ == '__main__':
    # 创建一个StrictRedis对象，连接redis数据库
    try:
        sr = StrictRedis(host='192.168.6.160', port=6379, db=0)
        # 添加一个键为name，值为itheima的数据
        # res = sr.set('name', 'itheima')
        # print(res)
        # 修改name的值为itcast
        # res = sr.set('name', 'itcast')
        # print(res)
        # 获取name的值
        # res = sr.get('name')
        # print(res)
        # 删除Name
        # res = sr.delete('name')
        # print(res)
        # 获取数据库中所有的键
        res = sr.keys()
        print(res)
    except Exception as e:
        print(e)