#!user/bin/env python3  
# -*- coding: gbk -*- 
import tushare as ts
import json

#ts.get_latest_news() #Ĭ�ϻ�ȡ���80���������ݣ�ֻ�ṩ�������͡����Ӻͱ���
print(ts.get_latest_news(top=1,show_content=True)) #��ʾ����5�����ţ�����ӡ����������
df =ts.get_latest_news(top=80,show_content=True)
df.to_csv('D:/Result.csv')

#f1 = open('a.txt','w')
#f1.write(json.dumps( df.to_json(orient='table')))
