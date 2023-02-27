# tempchk_msteams

[온습도계 세팅 가이드]

1. 아래의 패키지를 우선 설치 한다.
#python3 설치
sudo apt-get install python3-pip

#라즈베리파이 온습도 센서 라이브러리 설치
sudo pip3 install Adafruit_DHT

2. 파이썬 파일을 이동한다. (tempchk와 livechk 두가지 각각 생성)

3. 작동 테스트는 Python3 tempchk.py
                Python3 livechk.py를 사용 한다.

4. 스크립트 내에서 변경할 내용은 from_address(발신자), to_address(수신자), smtplib.SMTP(SMTP서버 및 포트)의 값만 변경 해주시면 됩니다.
                               WEBHook API 주소
(WEBHook을 사용할 경우 SMTP 발송은 주석처리하여도 무방함)

5. 크론탭을 설정 한다.
tempchk.py 파일을 크론탭을 이용하여 10분마다 또는 1분마다 실행해준다.
livechk.py 파일을 크론탭을 이용하여 1주일에 한번 월요일 9시 or 매일 9시에 실행해준다.

 

[결과물]
tempchk.py 파일은 서버실의 온도를 10분 또는 1분마다 체크하여 서버실의 온도가 기준 온도(현재 25도)보다 상승하였을 때, 메일을 보내준다.
livechk.py 파일은 해당 라즈베리파이가 전원공급, 네트워크 문제 등으로.. 정상 동작 하지 않는 상황이 발생할 것을 대비하여, 정상 동작을 확인하는 것이다.
