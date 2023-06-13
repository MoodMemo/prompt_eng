# -*- coding: utf-8 -*-

import openai
import os
import datetime
#import requests
#import json


userID=1
name="이준하"
userType="22세/남자/대학생"
d = datetime.datetime.now() - datetime.timedelta(days=1) #어제 날짜로 일기 작성
date=f'{str(d.year%100):0>2}.{str(d.month):0>2}.{str(d.day):0>2}'
title=""
bodyText=""
noc=0
keyword=[]

"""
openai.api_key = os.getenv("OPENAI_API_KEY")
response2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": f"너는 {userType}의 입장에서 일기를 써주는 assistant야."},
          {"role": "user", "content": ""},
          {"role": "assistant", "content": ""}]
    )

print(response2.choices[0].message.content)
"""

temp = {
    "userId":f"{userID}",
    "name": name,
    "date": date,
    "title": title,
    "bodyText": bodyText,
    "noc": f"{noc}",
    "keyword": keyword
}


"""
url = "http://1.2.3.4"

# headers
headers = {
    "Content-Type": f"api/dailyReport/{userID}"
}

data = json.dumps(temp)

# 변환된 Data를 보내고자 하는 URL에 보내기
response = requests.post(url, headers=headers, data=data)

# 송신 결과 확인
print("response: ", response)
print("response.text: ", response.text)
"""