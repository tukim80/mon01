import time
import requests
import subprocess

normal = "정상 입니다"
errorA = "접속에 문제가 발생하였습니다"
errorB = "접속이 차단 되었습니다 "

url = "http://www.tukim.org"

myToken = "xoxb-3564005005013-3564049011349-CvuaSvRoEzRNmHUz8rTOIqeP"

def slack(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)


def myget():
    with requests.get(url, stream=True) as rsp:
        ip, port = rsp.raw._connection.sock.getpeername()
        rspT = rsp.text
        print("접속 서버 정보: ", ip, port)
        print(normal, rsp.status_code, "OK")
        rsp.raise_for_status()

def main():

    try:
        myget()
        slack(myToken,"#security01",normal)

    except requests.exceptions.HTTPError as errb:
        print("Http Code Error!!!!!!!!!!!!!!!!!!!!!! : ", errb)
        slack(myToken,"#security01",errorB)

    except requests.exceptions.ConnectionError as erra:
        print("Error Connecting : ", erra)
        slack(myToken,"#security01",errorA)

    finally:
        while True:
            print("모니터링 진행 중!!!!!!!!!!!!!!!@#")
            print("###############################")
            time.sleep(3)
            main()

main()
