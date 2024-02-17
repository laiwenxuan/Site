from pyecharts import options as opts
from pyecharts.charts import Map


# 各城市岗位数量
data = [("北京市", 1513), ("上海市", 2216), ("广州市", 2168), ("深圳市", 1585), ("杭州市", 1506), ("成都市", 2865),
        ("福州市", 29), ("厦门市", 2653), ("苏州市", 2043), ("天津市", 1787), ("武汉市", 2418), ("西安市", 1563),
        ("长沙市", 2331), ("郑州市", 2030), ("重庆市", 1853)]

c = (
    Map()
    .add(
        "城市数据",
        data,
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各大城市爬取岗位数量"),
        visualmap_opts=opts.VisualMapOpts(max_=3000),  # 设置最大值为3000
    )
    .render("othersheat.html")
)
