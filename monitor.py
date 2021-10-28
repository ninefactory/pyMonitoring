import json
import requests
import time
from datetime import datetime

#url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','https://mchat.mbest.co.kr:8060/api/AppCallHis','http://www5.megastudy.net','http://www.megastudy.net') # tuple
url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','http://www4.megastudy.net','http://www5.megastudy.net','http://www.megastudy.net','http://m.megastudy.net') # tuple
sleep_tm = 300	# sleep time (sec)

def fncMonit():
	while True:
		for site in url:
			with requests.Session() as s:
				try : 
					r = s.get(site)

					if r.status_code == 200: # r.status_code : response status
						print('%s is ok : Response Status : %d' %(site, r.status_code))
					else:
						print('%s is Check : Response Status : %d' % (site, r.status_code))
						fncSendToSlack(site, 'Check')
				except Exception as e:
					print('Exception:', e)
					fncSendToSlack(site,'Error')
		
		print(str(datetime.today())[:19])

		time.sleep(sleep_tm) # (sec) loop

def fncSendToSlack(mg,ms):
	webhook_url= "https://hooks.slack.com/services/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"
	content= "["+str(datetime.today())[:19]+"] 최종 테스트 : " + mg + " / "+ms+""
	payload= {"text": content}
 
	requests.post(webhook_url, data=json.dumps(payload),headers={'Content-Type':'application/json'})


if __name__== '__main__':
    fncMonit()

