from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker
import requests
from datetime import date
import json

from pyecharts.globals import ThemeType

update_date = date.today()

# 1.疫情接口
url = "https://lab.isaaclin.cn/nCoV/api/area"
# 2.向url发请求，并将获取到的数据转换成json格式
resultJson = requests.get(url).json()
# 3.定义一个列表存储最终结果
province_data = []
# 4.只取国内数据
for item in resultJson['results']:
    if item['countryName'] == "中国":
        province_data.append(
            [
                item['provinceShortName'],
                item['confirmedCount']
            ]
        )
c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        .add("全国确诊人数", province_data, "china", is_map_symbol_show=False)
        .set_global_opts(
        title_opts=opts.TitleOpts(
            title="新冠状病毒全国疫情地图",
            subtitle="更新日期:{}".format(update_date),
        ),
        # 视觉映射配置项
        visualmap_opts=opts.VisualMapOpts(
            is_show=True,  # 是否显示
            min_=0,  # 左下角刻度最小值
            max_=2000
        )
    )
        .render("全国疫情可视化.html")
)
