# -*- coding: utf-8 -*-

import openai
import os
import datetime
import time
#import requests
#import json


user={'age':22,'sex':'여자','job':'대학생'}
d = datetime.datetime.now() - datetime.timedelta(days=1) #어제 날짜로 일기 작성
date=f'{str(d.year%100):0>2}.{str(d.month):0>2}.{str(d.day):0>2}'
start=time.time()
openai.api_key = os.getenv("OPENAI_API_KEY") 
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": f"너는 {user.get('age')}세 {user.get('sex')} {user.get('job')}의 입장에서 주어진 조건에 따라 일기를 쓰는 assistant야."},
        {"role": "user", "content": f"아래 [예시문]의 내용이 모두 포함되게 조건에 맞게 일기를 써줘.\n\
        일기의 제목은 하루를 한 줄로 요약해 작성하고, 일기의 키워드도 5개 뽑아줘.\n\
        조건 1 : 아래 [예시문]의 글 형식과 말투, 개조식 여부, 줄넘김, 문장부호, 말어미, 사용된 단어의 수준, ..., ㅠㅠ와 같은 이모티콘 혹은 인터넷 축약어의 사용여부 등을 분석한 후에 동일한 스타일로 일기를 쓸 것. 이때 분석 결과는 작성하지 않을 것.\n\
        조건 2 : 미사어구는 최대한 사용하지 않을 것.\n\
        조건 3 : 일기의 제목은 [제목]으로 구분해 작성하고, 키워드도 [키워드]로 구분해 작성할 것. 일기 내용은 [일기]로 구분할 것.\n\
        [예시문]\n\
        과제... 할 건 많은데 막상 과제 하러 들어가면 뭐부터 손대야 할지 감이 안 온다. 그래도 제일 어려운 부분 오늘 끝내서 내일이면 얼추 완성시킬 수 있을 것 같다\n\
        점심으로 친구들이랑 초밥 먹었다 맛은 그냥 무난! 지금 밥 다 먹고 친구들이랑 대외활동 자료 작성 잠깐 하다가 헤어져서 학사 가는 길인데... 너무 피곤하다\n\
        넘졸려서 조금만 자고 과제해야할듯... 진짜피곤하다아악\n\
        저녁먹고 산책나왔다! 기분 좋음\n\
        저녁 먹고 잔깐 산책나왔는데 메가커피 앞에서 사감쌤 마주쳤다! 사감쌤이 먹고싶은 거 사주신다고 얼른 고르래서 박웬수랑 나랑 마카롱 하나 슈크림빵 하나 골랐음... 아껴뒀다 나중에 먹어야지"}]
    )
end=time.time()
print(end-start,'sec')
print(response.choices[0].message.content)



"""
userID=1
name="이준하"
userType="22세/남자/대학생"
d = datetime.datetime.now() - datetime.timedelta(days=1) #어제 날짜로 일기 작성
date=f'{str(d.year%100):0>2}.{str(d.month):0>2}.{str(d.day):0>2}'
title=""
bodyText=""
noc=0
keyword=[]

temp = {
    "userId":f"{userID}",
    "name": name,
    "date": date,
    "title": title,
    "bodyText": bodyText,
    "noc": f"{noc}",
    "keyword": keyword
}

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