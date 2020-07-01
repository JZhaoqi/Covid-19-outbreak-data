import requests
import json
#获取网页内容
def get_page(url):
    #请求头用来表示用户身份
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.9 Safari/537.36'}
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()#异常处理
        r.encoding=r.apparent_encoding#从服务器返回的网页内容猜测编码方式
        return r.json()
    except Exception as e:
        print("Error")
        return ""
        #提取信息

import pandas as pd
def parse_page(data):
    province=data['list']#找到33个省的信息
    pdata=[]#保存省的信息
    for i in range(33):#33个省
        city=province[i]['list']
        for j in city:
            temp={}
            temp["省份"]=j["province"]
            temp["城市"]=j["city"]
            temp["确诊"]=j["sure_cnt"]
            temp["疑似"]=j["like_cnt"]
            temp["死亡"]=j["die_cnt"]
            temp["治愈"]=j["cure_cnt"]
            pdata.append(temp)
    #print(pdata)
    result=pd.DataFrame(pdata)
    return result
    #数据存储
def save_file(data_df):
    data_df.to_excel("F:\\work\\全国数据.xlsx",index=False)
    print("保存成功！")
#主函数
if __name__ == '__main__':
    url='https://api.m.sm.cn/rest?format=json&method=Huoshenshan.healingCity&mapType=1'
    pdata=parse_page(hurt_json)
    save_file(pdata)
