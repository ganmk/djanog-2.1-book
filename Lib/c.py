#!user/bin/env python3
# -*- coding: gbk -*-
import tushare as ts
import json

# ts.get_latest_news() #默认获取最近80条新闻数据，只提供新闻类型、链接和标题

# 显示最新5条新闻，并打印出新闻内容
print(ts.get_latest_news(top=1, show_content=True))
df = ts.get_latest_news(top=80, show_content=True)
df.to_csv('D:/Result.csv')

#f1 = open('a.txt','w')
#f1.write(json.dumps( df.to_json(orient='table')))
