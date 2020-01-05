import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType


#导入数据
data1 = pd.read_csv('directory.csv')
data2 = pd.read_csv('country.csv')

#清洗数据—将国家简称替代为国家名称
data = pd.merge(data1,data2,left_on='Country',right_on='id',how = 'left')
data

#重新排序：每个国家拥有的星巴克门店数量
temp = data.groupby('value')['Brand'].count().reset_index()
temp.columns = ['country','number']
世界星巴克分布 = zip (list(temp.country),list(temp['number']))
全球星巴克分布 = list(zip(list(temp.country),list(temp['number'])))


def map_world() -> Map:
    c = (
        Map()
        .add("国家（门店数）",[list(z)for z in zip(list(temp.country),list(temp['number']))],"world",itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="#111"))
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False),is_map_symbol_show=False)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全球星巴克分布地图"),
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True,    pieces=[
        {"min": 10000, "label": "10000+","color": '#EE4000' },
        {"max": 10000, "min": 2000, "label": "2000-10000","color": '#FFA54F' },
        {"max": 2000, "min": 1000, "label": "1000-2000","color": '#FFC1C1' },
        {"max": 1000, "min": 200, "label": "200-1000","color": '	#B4EEB4' },
        {"max": 200, "min": 100, "label": "100-200","color": '	#CAE1FF ' },
        {"max": 100, "min": 0, "label": "0-100","color": '#E6E6FA	' },



    ],),
        )
    )
    return c