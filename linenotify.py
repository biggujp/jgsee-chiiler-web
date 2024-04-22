############################################################
############################################################
######################DEVELOPER BY PORNCHAI#################
############################################################
############################################################
import urequests

url = 'https://notify-api.line.me/api/notify'

class  Linenotify_API():
	def __init__(self,token):
		self.token = token
		
	def lineNotify(self,msg):
		headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+self.token}
		msg = 'message={}'.format(msg).encode('utf-8')
		res = urequests.post(url, headers=headers , data = msg)
		return res
