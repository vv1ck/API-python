from flask import Flask
import json
from requests import post
app=Flask(__name__)


@app.route('/email=<email>')
def api_email(email):
	send=post(f'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={email}',headers={
		"Host": "odc.officeapps.live.com","Accept": "*/*",
		"Cache-Control": "max-age=0",
		"Accept-Encoding": "gzip, deflate",
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}).text
	if 'MSAccountNonEmail' in send:return 'This is not an email'
	elif 'MSAccount' in send:return '{"by telegram:@vv1ck" , status: True}'
	else:return '{"by telegram:@vv1ck" , status: False}'
app.run()
