#!/webhook.py python
# -*- coding: utf-8 -*-

import pymsteams
import smtplib
from email.mime.text import MIMEText
import Adafruit_DHT as dht
import time

today=time.strftime('%y-%m-%d %H:%M:%S')
hum,temp=dht.read_retry(dht.DHT22,2)

def livechk_send_mail():
    from_address="servertemp@~~~~.com" #server_temp
    to_address="hq@~~~~.com" #hq-infra
    msg1="{0} 서버는 정상 동작 되고 있습니다."\
    "\n"\
    "현재 서버실 온도: {1:.1f}, 습도:  {2:.1f}".format(today, temp, hum)
    s = smtplib.SMTP('smtp.google.com', 25)
    msg = MIMEText(msg1)
    msg['Subject'] = '서버실 온도 시스템 라이브 체크 메일'
    s.sendmail(from_address,to_address,msg.as_string())
    s.quit()
    return 0

def livechk_send_msteams():
    my_message = pymsteams.connectorcard("https://~~~~.webhook.office.com/webhookb2/~~~")
    msg2="서버는 정상 동작 되고 있습니다. 현재 시간 {0}" \
    "\n" \
    "현재 서버실 온도 {1:.1f}, 습도 {2:.1f}입니다.".format(today, temp, hum)
    my_message.text(msg2)
    my_message.send()


#livechk_send_mail 함수 호출
#livechk_send_mail()
livechk_send_msteams()
