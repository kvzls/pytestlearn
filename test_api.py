import json
# import schedule
import pytest
import allure
from pytestlearn.requests_util import RequestsUtil
from pytestlearn.yaml_util import YamlUtil
from pytestlearn.commonlog.log_utils import logger


@allure.feature('qualityPlatform')
class Test_qualityPlatform:
    # @pytest.mark.parametrize('user,pwd', get_data['user_pwd'])
    # def test0(self, bieMing, user, pwd):
    #     url = "http://auto-web.sit.sf-express.com/tf/user/login"
    #     data = {"empNo": user,
    #             "password": pwd
    #             }
    #     print('登陆【质量管理平台】')
    #     postRequest(url, data)
    #     assert postRequest(url, data)['success'] == 'true'
    #     if user == "01422429":
    #         assert postRequest(url, data)['msg'] == '帐号不存在'

    @allure.story('case1')
    @allure.severity('normal')
    @pytest.mark.parametrize("test1case", YamlUtil().read_data_test('test1_data.yaml'))
    def test1(self, test1case):
        logger.info('常用链接主页1')
        logger.info(
            'test1case下:' + str(test1case))  # 代码里获取url返回的json，其实是字典类型，直接跟字符串用加号拼接会报错,需要将字典类型转化为字符串（str(dict)）后拼接即可：
        method = test1case['request']['method']
        url = test1case['request']['url']
        data = test1case['request']['data']
        # logger.info('test1case的数据:' + test1case)
        logger.info('url的数据:' + url)
        result = RequestsUtil().send_request(method, url, data)
        result = json.loads(result)
        logger.info('请求之后的结果:' + str(result))
        allure.attach.file(r'D:\pycharm\PycharmProjects\22年学习python基础\test01.png',
                           attachment_type=allure.attachment_type.PNG)  # allure引用图片，文件要引用file方法，访问目录记得带r
        assert result['success'] == test1case['validata']

    # @allure.story('case2')
    # @allure.severity('normal')
    # @pytest.mark.parametrize("testst1", YamlUtil().read_data_test('get_serach1.yml'))
    # def test1(self, testst1):
    #     print("test1case:", testst1)
    #     method = testst1['name']
    #     print(method)
    # url = test1case['request']['url']
    # data = test1case['request']['data']
    # print('常用链接主页1')
    # # postRequest(url, data)
    # result = RequestsUtil().send_request(method, url, data)
    # result = json.loads(result)
    # print("resu:", result)
    # allure.attach.file(r'D:\pycharm\PycharmProjects\22年学习python基础\test01.png',
    #                    attachment_type=allure.attachment_type.PNG)  # allure引用图片，文件要引用file方法，访问目录记得带r
    # assert postRequest(url, data)['success'] == test1case['validata']
    #
    # @allure.story('case2')
    # @allure.severity('normal')
    # def test2(self):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/search"
    #     data = {"pageInt": 1, "pageSize": 10, "systemID": "73", "urlTypeID": "84"}
    #     print('常用链接主页2')
    #     postRequest(url, data)
    #
    # @allure.story('case3')
    # @allure.severity('normal')
    # # @pytest.mark.parametrize('name', ["台湾", "香港"])
    # @pytest.mark.parametrize('name', get_data['name'])
    # def test3(self, name):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/search"
    #     data = {"pageInt": 1, "pageSize": 10, "systemID": "73", "urlTypeID": "84", "name": name}
    #     print('常用链接-搜索‘{}’'.format(name))
    #     postRequest(url, data)
    #
    # @allure.story('case4')
    # @allure.severity('normal')
    # def test4(self):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/update"
    #     data = {"note": "测试: 0910070924,\n0999988888,\n0956565656\n生产: 0999911111  0999966666", "systemID": "73",
    #             "urlTypeID": "84", "name": "台湾帐号", "typeID": 96, "id": 296, "created_date": "2021-12-10",
    #             "updated_date": "2022-07-20",
    #             "url": "http://twmem-right.sit.sf-express.com/index.html#/commodityManage"}
    #     print('常用链接-编辑‘台湾’')
    #     postRequest(url, data)
    #
    # @allure.story('case5')
    # @allure.severity('normal')
    # def test5(self):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/search"
    #     data = {"pageInt": 1, "pageSize": 10, "systemID": "73", "urlTypeID": "98"}
    #     print('测试工具-‘常用工具tab’')
    #     postRequest(url, data)
    #
    # @allure.story('case6')
    # @allure.severity('critical')
    # def test6(self):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/search"
    #     data = {"pageInt": 1, "pageSize": 10, "systemID": "73", "urlTypeID": "98"}
    #     print('测试工具-‘常用工具tab’')
    #     postRequest(url, data)
    #
    # @allure.story('case7')
    # @allure.severity('blocker')
    # def test7(self):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/search"
    #     data = {"pageInt": 1, "pageSize": 10, "systemID": "73", "urlTypeID": "98", "typeID": 98}
    #     print('测试工具-常用工具tab-测试常用工具')
    #     postRequest(url, data)
    #
    # @allure.story('case8')
    # @pytest.mark.parametrize('data', test_csv())
    # def test8(self, data):
    #     url = "http://auto-web.sit.sf-express.com/tf/usefulUrl/search"
    #     data = {"pageInt": 1, "pageSize": 10, "systemID": "73", "urlTypeID": "84", "name": data['name']}
    #     print('常用链接-搜索‘csv’')
    #     postRequest(url, data)


# #
#     def main(self, allure_report):
#         # 定时任务执行allure
#         pytest.main(['{}'.format(__file__), '--alluredir', allure_report])
#         # 发送邮件
#         USER = '13631222984@163.com'
#         PASSWORD = 'PXSZEEEAOQVEHBNZ'
#         # 如名字所示： Multipart就是多个部分
#         msg = MIMEMultipart()
#         HOST = 'smtp.163.com'
#         msg['subject'] = 'test email from python'
#         msg['to'] = '372855920@qq.com'
#         msg['from'] = '13631222984@163.com'
#         text = MIMEText('y用例已跑完')
#         msg.attach(text)
#         #添加附件1
#         xlsxpart = MIMEApplication(open('test_csv.csv', 'rb').read())
#         xlsxpart.add_header('Content-Disposition', 'attachment', filename='test_csv.csv')
#         msg.attach(xlsxpart)
#
#         # 开始发送邮件
#         client = smtplib.SMTP()
#         client.connect(HOST)
#         client.login(USER, PASSWORD)
#         client.sendmail('13631222984@163.com', ['372855920@qq.com'], msg.as_string())
#         client.quit()
#         print('发送成功........')
#
#
# if __name__ == '__main__':
#     # os.system('allure serve ./allure_report')
#     res = Test_qualityPlatform()
#     schedule.every(5).seconds.do(res.main, './pytestlearn/report1')  # 定时任务
#     # res.test1()
#     while True:
#         schedule.run_pending()

'''
指定测试用例
pytest --alluredir=./report1/allure --allure-severities=blocker,critical --clean-alluredir

指定features
pytest --alluredir ./result --allure-features='qualityPlatform'
生成报告：allure serve ./result   
指定story
pytest --alluredir ./report1 --allure-stories='case1' --clean-alluredir
'''
