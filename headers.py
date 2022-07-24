
class mitmproxyHeaders:
	def __init__(self):
		pass

	def parse(self,headers_string):
		headers = {}
		cookie = {}
		if type(headers_string) != str:
			raise "you have to enter headers with the data type string:str"
		for i in headers_string.split('\n'):
			if i.split(': ')[0].lower() == 'user-agent':
				headers[i.split(': ')[0]] = i.split(': ')[1]
			elif i.split(': ')[0].lower() == 'cookie':
				cookie[i.split(': ')[1].split('=')[0]] = i.split(': ')[1].split('=')[1]
				headers[i.split(': ')[0]] = cookie
			else:
				headers[i.split(': ')[0]] = i.split(': ')[1]
		return headers