from flask import Flask
from requests import post
api=Flask(__name__)


@api.route('/<email>')
def api_email(email):
    send=post(f'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={email}',headers={
        "Host": "odc.officeapps.live.com","Accept": "*/*",
        "Cache-Control": "max-age=0",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"}).text
    if 'MSAccount' in send:return '{"by telegram:@vv1ck" , status: True}'
    else:return '{"by telegram:@vv1ck" , status: False}'
api.run()