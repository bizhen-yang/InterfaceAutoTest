import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp

questInfo_xls = common.get_xls("quest.xlsx", "quest")
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*questInfo_xls)
class Share(unittest.TestCase):
    def setParameters(self, case_name, method,url, token, goods_id, result, code, msg):
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
        self.method = str(method)
        self.url = str(url)
        self.token = str(token)
        self.goodsId = str(goods_id)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.response = None
        self.info = None

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

    def testShare(self):
        """
        test body
        :return:
        """
        # set uel
        #self.url = common.get_url_from_xml('share')
        localConfigHttp.set_url(self.url)
        headers = {
            'token': "185b39a5460641d8962eddfcd041c6f3",
            'device_id': "05E46847-4DD3-4720-8598-CB9B21F3B6A0",
            'lang_id': "ms_MY",
            'cache-control': "no-cache",
        }
        param = {"sharingType":"incomeSharing"}
        localConfigHttp.set_headers(headers)
        localConfigHttp.set_params(param)
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

        if self.result == '0':
            self.assertEqual(self.info['code'], self.code)
            self.assertEqual(self.info['msg'], self.msg)
            goods_id = common.get_value_from_return_json(self.info, "Product", "goods_id")
            self.assertEqual(goods_id, self.goodsId)
        if self.result == '1':
            self.assertEqual(self.info['code'], self.info['code'])
            self.assertEqual(self.info['msg'], self.msg)
