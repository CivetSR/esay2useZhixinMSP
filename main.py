import requests
import json
class MSP:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        url = "http://192.144.234.153:4000/user/api/login"
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "username":self.username,
            "password":self.password
        }
        res = json.loads(requests.post(url=url,headers=headers,json=data).text)
        self.token = res["data"]["token"]
    def macId(self,macId):
        self.macId = macId
    def templateId(self,templateId):
        self.templateId = templateId
    def tname(self,tname):
        self.tname = tname
    def text(self,textdata):
        data = {
            "data": textdata
        }
        headers = {
            "Authorization":self.token,
            'Content-Type': 'application/json'
        }
        url = f"http://192.144.234.153:4000/user/api/mqtt/publish/{self.macId}/template/{self.templateId}"
        res = json.loads(requests.post(headers=headers,url=url,json=data).text)
        print(res)
