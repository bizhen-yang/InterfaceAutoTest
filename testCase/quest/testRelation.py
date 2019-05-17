from common import common
from common import configHttp as configHttp
import paramunittest
import unittest
from common.Log import MyLog

from _threading_local import local


relationInfo_xls = common.get_xls("relationCase.xlsx", "relation")
localConfigHttp = configHttp.ConfigHttp()

@paramunittest.parametrized(*relationInfo_xls)
class Relation(unittest.TestCase):
    def setParameters(self, case_name, token, device_id, invitation_code,result_code):
        self.case_name = str(case_name)
        self.url = "/u/relation/bindInvitationCode"
        self.token = str(token)
        self.device_id = str(device_id)
        self.invitation_code = str(invitation_code)
        self.result_code = str(result_code)
        
    def decscription(self):
        self.case_name
        
    def setUp(self):
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        
    def testRelation(self):
        localConfigHttp.set_url(self.url)
        header = {
            'token': self.token,
            'lang_id': "zh_CN",
            'device_id': self.device_id,
        }
        
        param = {"invitationCode":self.invitation_code}
        localConfigHttp.set_headers(header)
        localConfigHttp.set_params(param)
        self.response = localConfigHttp.post()
        
        self.checkResult()
        
    
    def tearDown(self): 
        #self.log.build_case_line(self.case_name, self.info['code'], self.info['msg'])
        self.log.build_case_line(self.case_name)
        
        
    def checkResult(self):
        self.info = self.response.json()
        common.show_return_msg(self.response)

        
        self.assertEqual(self.info['code'], self.result_code, "测试用例 "+self.case_name+"失败")
