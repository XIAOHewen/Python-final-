#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request
import pandas as pd

# 模块读进来
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
import pyecharts
import warnings
   
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.globals import ChartType, SymbolType,CurrentConfig
from jinja2 import Markup, Environment, FileSystemLoader

from country import bar_datazoom_slider
from map import map_world
# 关于 CurrentConfig，可参考 [基本使用-全局变量]
CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./templates"))
warnings.filterwarnings("ignore")

app = Flask(__name__, static_folder="templates")

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

#提取相关数据
regions_available_loaded = list(data.value.dropna().unique())

cf.set_config_file(offline=True, theme="ggplot")
py.offline.init_notebook_mode()


@app.route('/all',methods=['GET'])
def city():

    data_str = data.to_html()  
    plot_all = data_str
    regions_available = regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                           the_plot_all = plot_all,
                           the_res = data_str,
                           the_select_region=regions_available)   



@app.route('/city',methods=['POST'])
def star_select() -> 'html':
    the_region = request.form["the_region_selected"]  ## 取得用户交互输入
    print(the_region) 
    dfs = data.query("value=='{}'".format(the_region)) ## 使用df.query()方法. 按用户交互输入the_region过滤
    
    temp = dfs.groupby('City')['Brand'].count().reset_index()
    temp.columns = ['city','number']
    temp
    data_str = temp.to_html()

    fig = temp.iplot(kind="bar", x="city", y="number", theme="white",color="rgb(219,112,147)",orientation="h",asFigure=True)  # 使用iplot 做bar圖
    py.offline.plot(fig, filename="城市星巴克门店数.html",auto_open=False)                  # 備出"成果.html"檔案之交互圖
    with open("城市星巴克门店数.html", encoding="utf8", mode="r") as f:                     # 把"成果.html"當文字檔讀入成字符串
        plot_all = "".join(f.readlines())

    regions_available =  regions_available_loaded #下拉选单有内容
    return render_template('results2.html',
                            the_plot_all = plot_all,
                            the_res = data_str,
                            the_select_region=regions_available,
                           )



@app.route("/country")
def country():
    c = bar_datazoom_slider()
    return Markup(c.render_embed())

@app.route("/map")
def map():
    c = map_world()
    return Markup(c.render_embed())

@app.route('/chinamap')
def chinamap() -> 'html':
    return render_template('chinamap.html')

@app.route('/chinamap2')
def chinamap2() -> 'html':
    return render_template('chinamap2.html')

@app.route('/chinamap3')
def chinamap3() -> 'html':
    return render_template('chinamap3.html')

@app.route('/') 
@app.route('/首页')
def entry_page() -> 'html':
    return render_template('首页.html')


if __name__ == '__main__':
    app.run(port = 8002)   # debug=True, 在py使用, 在ipynb不使用
