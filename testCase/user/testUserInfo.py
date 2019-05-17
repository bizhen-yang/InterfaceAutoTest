import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp

questInfo_xls = common.get_xls("quest.xlsx", "quest")
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(("testUserInfo","/u/user/info"))
class UserInfo(unittest.TestCase):
    def setParameters(self , case_name, url):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param goods_id:
        :param result:
        :param code:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)

    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def testUserInfo(self):
        """
        test body
        :return:
        """
        # set uel
        #self.url = common.get_url_from_xml('share')
        localConfigHttp.set_url(self.url)
        headers = {
            'token': localReadConfig.get_headers("token_v")
        }
        localConfigHttp.set_headers(headers)
        # get http
        self.response = localConfigHttp.get()
        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])

    def checkResult(self):
        self.info = self.response.json()
        common.show_return_msg(self.response)

        
        self.assertEqual(self.info['code'], "0000")

