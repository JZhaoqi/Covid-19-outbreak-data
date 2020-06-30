from urllib import request
import re
user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"

headers = {"User-Agent": user_agent}

# 爬取网站地址

req = request.Request("http://m.medsci.cn/wh.asp",headers=headers)

resp = request.urlopen(req)

# 读取页面

html = resp.read()

headline = re.findall(r'<tr style="border: 1px solid black;font-weight:bold;">.*</tr>',html.decode('utf-8'))

result = re.findall(r'<tr style="border-left:1px solid #F00;border-top:1px solid black">.*</tr>',html.decode('utf-8'))

time = re.findall(r'<p class="head-time">.*</p>',html.decode('utf-8'))

total = re.findall(r'<p class="head-title">.*</p>',html.decode('utf-8'))

# 进行数据清洗

headline = str(headline)

headline = headline.replace('''['<tr style="border: 1px solid black;font-weight:bold;"><td style="border: 1px solid black;">''',"")

headline = headline.replace('''</td><td style="border: 1px solid black;">''',"              ")

headline = headline.replace('''</td></tr>']''',"")

total = str(total)

total = total.replace('''['<p class="head-title">''','')

total = total.replace('''</p>']''','')

result = str(result)

result = result.replace('''['<tr style="border-left:1px solid #F00;border-top:1px solid black"><td style="border: 1px solid black;">''',"")

result = result.replace('''</td><td style="border: 1px solid black;">''',"              ")

result = result.replace(''''<tr style="border-left:1px solid #F00;border-top:1px solid black"><td style="border: 1px solid black;">''',"")

result = result.replace("</td></tr>'","")

result = result.replace('<td style="border: 1px solid black;"></td>',"0")

result = result.replace(', ',"\n")

result = result.replace(']',"")

time = str(time)

time = time.replace('''['<p class="head-time">''',"")

time = time.replace('''</p>']''',"")

# 输出结果

print("=================================================================")

print(total)

print(headline)

print(result)

print(time)
