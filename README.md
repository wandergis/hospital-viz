# putian-hospitals
莆田系医院数据及其经纬度坐标，包括geojson和shp文件。

## 在线查看

- [点击前往](https://wandergis.com/putian-hospitals/)

## 数据来源

- [凤凰网的数据](http://news.ifeng.com/mainland/special/ptxyy/)

- 解密其`main2.min.js`文件，得到了hospitals的数组，使用python转成json数据。

## 坐标获取

- 使用node调用高德的geocode api解析成经纬度

## 数据展示

- 使用leaflet展示

## 截图示例

![截图](https://raw.githubusercontent.com/wandergis/putian-hospitals/gh-pages/screenshot2.png)

![截图](https://raw.githubusercontent.com/wandergis/putian-hospitals/gh-pages/screenshot.png)


