#!/webhook.py python
# -*- coding: utf-8 -*-

import pymsteams
import smtplib
from email.mime.text import MIMEText
import Adafruit_DHT as dht
import time

#오늘날짜
today=time.strftime('%y-%m-%d %H:%M:%S')

#dht22을 통해 확인하는 온도(temp),습도(hum)
hum,temp=dht.read_retry(dht.DHT22,2)

#메일 보내는 함수
def send_mail():
    from_address="server_temp@~~~~~~.com"
    to_address="Server_temperature@~~~~~~.com"
    msg1="현재 시간은 {0} 입니다." \
    "\n" \
    "현재 서버실 온도 {1:.1f}, 습도 {2:.1f}입니다.".format(today, temp, hum)
    s = smtplib.SMTP('smtp.google.com', 25)
    msg = MIMEText(msg1)
    msg['Subject'] = "주의!! 서버실 온도가 상승하고 있습니다 (현재온도:{0:.1f})".format(temp)
    s.sendmail(from_address,to_address,msg.as_string())
    return 0
#팀즈 메시지 보내는 함수
def send_msteams():
    my_message = pymsteams.connectorcard("채널 URL 입력")
    msg2="현재 시간은 {0} 입니다." \
    "\n" \
    "현재 서버실 온도 {1:.1f}, 습도 {2:.1f}입니다.".format(today, temp, hum)
    my_message.text(msg2)
    my_message.send()

# 현재 온도가 25도 보다 높을 경우 send_mail,send_msteams 함수 호출
if int(temp) > 25:
#    send_mail()
    send_msteams()
    print(temp,hum)
else:
    print('fine')
    print(temp, hum)



#채널 URL : https://~~~~~~~~~~~.webhook.office.com/webhookb2/~~~~~~~~~~~~~~~~~
