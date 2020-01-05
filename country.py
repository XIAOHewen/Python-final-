from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

def bar_datazoom_slider() -> Bar:
    c = (
         Bar({"theme": ThemeType.MACARONS})
        .add_xaxis(['United States', 'China', 'Canada', 'Japan', 'South Korea', 'United Kingdom', 'Mexico', 'Taiwan', 'Turkey', 'Philippines', 'Thailand', 'Indonesia', 'Malaysia', 'Germany', 'United Arab Emirates', 'France', 'Singapore', 'Russia', 'Argentina', 'Kuwait', 'Brazil', 'Saudi Arabia', 'Spain', 'Chile', 'Peru', 'India', 'Ireland', 'Switzerland', 'Netherlands', 'Poland', 'Egypt', 'Lebanon', 'Czechia', 'Greece', 'Romania', 'Vietnam', 'New Zealand', 'Puerto Rico', 'Australia', 'Bahrain', 'Denmark', 'Belgium', 'Austria', 'Qatar', 'Sweden', 'Jordan', 'Norway', 'Hungary', 'Oman', 'Colombia'])
        .add_yaxis("全球星巴克门店数量TOP50国家或地区", [13608, 2734, 1468, 1237, 993, 901, 579, 394, 326, 298,289, 268, 234, 160, 144, 132, 130, 109, 108, 106, 102, 102, 101, 96, 89, 88, 73, 61, 59, 53, 31, 29, 28, 28, 27, 25, 24, 24, 22, 21, 21, 19, 18, 18, 18, 17, 17, 16, 12, 11])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="国家或地区星巴克门店数"),
            yaxis_opts=opts.AxisOpts(name="门店数量（家）"),
            xaxis_opts=opts.AxisOpts(name="国家",axislabel_opts=opts.LabelOpts(rotate=-15)),
            datazoom_opts=opts.DataZoomOpts(),
        )
    )
    return c