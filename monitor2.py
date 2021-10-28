import json
import requests
import time
from datetime import datetime
# from time import time

#url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','https://mchat.mbest.co.kr:8060/api/AppCallHis','http://www5.megastudy.net','http://www.megastudy.net') # tuple
# url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','http://www4.megastudy.net','http://www5.megastudy.net','http://m1.megastudy.net','http://m2.megastudy.net','http://m.megastudy.net') # tuple
#url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','http://www4.megastudy.net','http://www5.megastudy.net','http://m.megastudy.net','http://file1.megastudy.net/fileserver/site_check.asp','http://www.megagong.net') # tuple

# VPN이 켜져 있을 경우 
# url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','http://www4.megastudy.net','http://www5.megastudy.net','http://www6.megastudy.net','http://www7.megastudy.net','http://www8.megastudy.net','http://www9.megastudy.net','http://www10.megastudy.net','http://www11.megastudy.net','http://www.megagong.net') # tuple

# 일반적일 경우 
# url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','http://www4.megastudy.net','http://www5.megastudy.net','http://m.megastudy.net','http://file1.megastudy.net/fileserver/site_check.asp','http://www.megagong.net') # tuple
url = ('http://www1.megastudy.net','http://www2.megastudy.net','http://www3.megastudy.net','http://www4.megastudy.net','http://www5.megastudy.net','http://220.73.215.234','http://220.73.215.235','http://220.73.215.171','http://220.73.215.172','http://220.73.215.233','http://m.megastudy.net','http://file1.megastudy.net/fileserver/site_check.asp','http://tzone.megastudy.net/voc/_check_bbs.asp','http://www.megagong.net') # tuple

sleep_tm = 120	# sleep time (sec)

def fncMonit():
	while True:
		for site in url:
			fnm_log = "log_" + str(datetime.today())[:10]+".txt"
			f = open("./log/"+fnm_log, 'a')
			f.write(str(datetime.today())[:19]+" : ")
			
			# Tzone용 별도
			fnm_log_tz = "log_tz" + str(datetime.today())[:10]+".txt"
			f_tz = open("./log_tz/"+fnm_log_tz, 'a')

			with requests.Session() as s:
				try : 
					start_time = time.time_ns()/(1000000*1000);
					r = s.get(site)
					res_time = time.time_ns()/(1000000*1000) - start_time;

					if site.find("tzone.megastudy.net") > -1:
						if (res_time > 2.5) :
							fncSendToSlackTm(site,str(round(res_time,3)))
					else:
						if (res_time > 1.5) :
							fncSendToSlackTm(site,str(round(res_time,3)))
							

					if r.status_code == 200: # r.status_code : response status
						print('%s is ok / Response Status : %d / Time : %.3f ' %(site, r.status_code, round(res_time,3)))
						f.write('%s is ok / Response Status : %d / Time : %.3f \n' %(site, r.status_code, round(res_time,3)))
						if site.find("tzone.megastudy.net") > -1:
							f_tz.write(str(datetime.today())[:19]+" : ")
							f_tz.write('%s is ok / Response Status : %d / Time : %.3f \n' %("TZONE", r.status_code, round(res_time,3)))
					else:
						print('%s is Check : Response Status : %d / Time : %.10f ' % (site, r.status_code, round(res_time,3)))
						f.write('%s is ok / Response Status : %d / Time : %.3f \n' %(site, r.status_code, round(res_time,3)))
						if site.find("tzone.megastudy.net") > -1:
							f_tz.write(str(datetime.today())[:19]+" : ")
							f_tz.write('%s is ok / Response Status : %d / Time : %.3f \n' %("TZONE", r.status_code, round(res_time,3)))
						fncSendToSlack(site, 'Check')
				except Exception as e:
					print('Exception:', e)
					fncSendToSlack(site,'Error')
			f.close()
			f_tz.close()

		print(str(datetime.today())[:19])

		time.sleep(sleep_tm) # (sec) loop

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
    fncMonit()

