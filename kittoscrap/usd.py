print("start@@@@@@@@@@@@@@@@@@@@@@@@@@@")

import pymysql
import urllib.request
import datetime
from datetime import datetime, timedelta


print("환율 계산기 입니다.")
#환율 정보를 불러오는 라인
page = urllib.request.urlopen("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%99%98%EC%9C%A8")
text = page.read().decode("utf8")
#시간 정보를 확인 합니다
where = text.find('class="grp_info"> <em>')
start_of_time = where + 22
end_of_time = start_of_time + 16
prin = text[start_of_time:end_of_time]
print(prin,"의 KEB하나은행 환율정보 입니다.")
#==============돈 값을 가져오고 정수형으로 바꾸는 부분=================================

#달러
usdwhere = text.find('<span>미국 <em>USD</em></span></a></th> <td><span>')
usdletter =  text[usdwhere+48] + text[usdwhere+50:usdwhere+56]


connection = pymysql.connect(
                host='117.17.189.6',
                user='root',
                password='samjung',
                port=3306,
                db='samjung_test')
try:
    with connection.cursor() as curs:
        try:
            now = datetime.now()
            Time = now.strftime('%Y-%m-%d %H:%M')

            sql = "INSERT INTO `환율` (`기준일`,`환율`) VALUES (%s,%s)"
            curs.execute(sql,(
                             Time, ##구매일자
                             usdletter))
            print("insert!!!!!",Time,usdletter)
        except:
            print("error  insert")

    connection.commit()
finally:
    connection.close()

print("USD 의 시세는 현재",usdletter,"입니다")