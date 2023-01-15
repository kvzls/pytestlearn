# conftest.py来实现数据，参数，方法、函数的共享,简单来说就是用于想实现数据的共享，定义一个的“全局变量”
# fixture适用于在同一个py文件中多个用例执行时的使用；而conftest.py方式适用于多个py文件之间的数据共享。比如常见的有以下场景：
# 请求接口需要共享登录接口的token/session
# 多个case共享一套测试数据
# 多个case共享配置信息
# conftest.py与运行的用例要在同一个pakage下，并且有__init__.py文件


import pytest
import requests


# scope，作用域，可以作用于class，function，modle，package，session
# autouse默认false，需要py文件中各个def中加上my_fixture,当为ture时就会自动识别添加
# params 参数化，支持列表[],元祖(),字典列表[{},{},{}],字典元祖({},{},{}),request.param固定写法，parmas主要通过request.param用于返回参数的内容
# name ，起fixture别名，当起别名后，原默认的fixture就不能用了
@pytest.fixture(scope="function", autouse=False, params=['成龙', '李连杰'], name='bieMing')
def my_fixture(request):
    print('\n前置：', request.param + '使用conftest.py的fixture')
    yield
    print("\n---------------执行后置----------------")
