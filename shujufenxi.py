import pandas as pd

#获取数据
data=pd.read_csv('全国数据.csv')

#数据清理，将无数字格换成数字0
data.loc[data['确诊']=='-','确诊']='0'
data.loc[data['死亡']=='-','死亡']='0'
data.loc[data['治愈']=='-','治愈']='0'

#查看数据类型，因为涉及计算，所以查看数据是否可运算
data.info()
#根据所需要运算的列，转换数据类型为整数型
data['确诊']=data['确诊'].astype('int64')
data['死亡']=data['死亡'].astype('int64')
data['治愈']=data['治愈'].astype('int64')
#再次查看是否成功转换
data.info()

#统计各省份总的确诊人数，死亡人数，治愈人数并保存在新的csv文件中
import csv
data_sum=data.groupby('省份')['确诊','死亡','治愈'].sum()
data_sum.to_csv('shuju.csv')
data2=pd.read_csv('shuju.csv')
#统计各省份的死亡率
data2.eval('死亡率=死亡/确诊',inplace=True)
#统计各省份的治愈率
data2.eval('治愈率=治愈/确诊',inplace=True)
#按治愈率进行降序排序
data2_s=data2.sort_values(by='治愈率',ascending=False)
data2_s.index=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',
              '21','22','23','24','25','26','27','28','29','30','31','32','33']
print(data2_s)

#将各省份的死亡率和治愈率可视化

import matplotlib.pyplot as plt
#设置字体为SimHei显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#设置正常
plt.rcParams['axes.unicode_minus'] = False

#散点图
#设置散点图大小
plt.figure(figsize=(22,8))
#获取数据
for i in range(4,6):
    plt.scatter(x= data2_s.iloc[:,0],y=data2_s.iloc[:,i])
#设置标题
plt.title('各省死亡率与治愈率对比图')
# 设置横轴标签
plt.xlabel('省份',fontsize=14)
# 设置纵轴标签
plt.ylabel('比率',fontsize=14)
#设定y轴的范围
plt.ylim((0,1))
plt.legend(data.columns[4:6])
plt.show()
#箱线图
# 创建画布并设定画布大小
p = plt.figure(figsize=(16,4))
#使用循环绘制图形
for i in range(4,6):
    ax = p.add_subplot(1,8,i-1)
    plt.boxplot(data.iloc[:,i])
    #添加x的标签
    plt.xlabel(data.columns[i])
    #设定y轴的范围
    plt.ylim((0,100))
plt.show() ## 显示图形
