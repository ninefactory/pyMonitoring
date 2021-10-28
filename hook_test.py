import json
import requests
import time
from datetime import datetime
# from time import time


def fncTest():
	fncSendToSlackTEST('훅 테스트를 진행 합니다.~!!!', 'Check')

# push test를 진행할 경우 (1.0 기준)
def fncSendToSlackTEST(mg,ms):
	webhook_url= "https://hooks.slack.com/services/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"
	content= "["+str(datetime.today())[:19]+"] 테스트 : " + mg + " "
	payload= {"text": content}
 
	requests.post(webhook_url, data=json.dumps(payload),headers={'Content-Type':'application/json'})

# 서버응답이 없을 경우 
def fncSendToSlack(mg,ms):
	webhook_url= "https://hooks.slack.com/services/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"
	content= "["+str(datetime.today())[:19]+"] 최종 테스트 : " + mg + " / "+ms+""
	payload= {"text": content} 
	requests.post(webhook_url, data=json.dumps(payload),headers={'Content-Type':'application/json'})

# 서버 응답시간이 늦을 경우 (1.0 기준)
def fncSendToSlackTm(mg,ms):
	webhook_url= "https://hooks.slack.com/services/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"
	content= "["+str(datetime.today())[:19]+"] 시간 초과 : " + mg + " / Time:"+ms+""
	payload= {"text": content}
 
	requests.post(webhook_url, data=json.dumps(payload),headers={'Content-Type':'application/json'})


if __name__== '__main__':
    fncTest()

