#!/usr/bin/env python
# coding: utf-8

# In[76]:


import pyecharts
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

#导入数据
data1 = pd.read_csv('directory.csv')
data2 = pd.read_csv('country.csv')
#清洗、整合数据
data = pd.merge(data1,data2,left_on='Country',right_on='id',how = 'left')
data


# In[ ]:





# In[ ]:





# In[77]:


# 导入世界地图
world_map = folium.Map()

# 导入北京市区经度与纬度位置
latitude = 39.9
longitude = 116.3

# 创建地图
map = folium.Map(location=[latitude, longitude], zoom_start=5,tiles="Stamen Toner")

# 在地图上显示前2000条数据
incidents = folium.map.FeatureGroup()

for lat, lng, in zip(china.Latitude, china.Longitude):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, 
            color='yellow',
            fill=True,
            fill_color='red',
            fill_opacity=0.8
        )
    )

map = folium.Map(location=[latitude, longitude], zoom_start=4)
map.add_child(incidents)

'''为地图对象添加点击显示经纬度的子功能'''
map.add_child(folium.LatLngPopup())
map.add_child(folium.ClickForMarker())


# In[ ]:





# In[ ]:





# In[ ]:





# In[78]:


import folium
import pandas as pd


# In[79]:


states_geojson = r'../www/html/us-states.json'


# In[80]:


state_unemployment = r'../www/html/directory2.csv'


# In[81]:


cdata = pd.read_csv('directory.csv')


# In[82]:


cdata.Country
cdata.columns
data = cdata.set_index("Country")
data.head
data.index
data.columns
#读取中国的数据
china =  data.loc["CN",:]


# In[83]:


#提取国家拥有星巴克数量的数据

temp = china.groupby('City')['Brand'].count().reset_index()
temp.columns = ['city','number']


# In[90]:


# 在中国的数据中筛选前2000个数据
limit = 2000
data = china.iloc[0:limit, :]
data


# In[120]:


# 导入世界地图
world_map = folium.Map()

# 导入北京市区经度与纬度位置
latitude = 39.9
longitude = 116.3

# 创建地图
china_map = folium.Map(location=[latitude, longitude], zoom_start=12)
china_map

# 在地图上显示前2000条数据
incidents = folium.map.FeatureGroup()


# In[121]:


address = list(data['Street Address'])


# In[122]:


lat = list(data['Latitude'])
lng = list(data['Longitude'])
label = list(data['Name'])


# In[123]:


san = zip (lat,lng,label)
print(san)


# In[124]:


san = list(zip (lat,lng,label))
print(san)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


# 添加标签
latitudes = list(china.Latitude)
longitudes = list(china.Longitude)
labels = list(china.Name)
popup=san

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=popup).add_to(china_map)    

china_map.add_child(incidents)


# In[ ]:


china_map.save('chinamap2.html')


# In[48]:




for lat, lng, in zip(china.Latitude, china.Longitude):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=8, 
            color='pink',
            fill=True,
            fill_color='purple',
            fill_opacity=0.5
        )
    )

china_map = folium.Map(location=[latitude, longitude], zoom_start=4)
china_map.add_child(incidents)

'''为地图对象添加点击显示经纬度的子功能'''
china_map.add_child(folium.LatLngPopup())
china_map.add_child(folium.ClickForMarker())


# In[ ]:





# In[49]:


# 添加标签
incidents = folium.map.FeatureGroup()

latitudes = list(china.Latitude)
longitudes = list(china.Longitude)
labels = list(china.Name)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(china_map)    

china_map = folium.Map(location=[latitude, longitude], zoom_start=4)
china_map.add_child(incidents)


# In[51]:





# In[ ]:




