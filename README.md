# putian-hospitals
莆田系医院数据及其经纬度坐标，包括geojson和shp文件。

## 更新说明

- 可以在手机、微信查看附近的莆田系医院
- 感谢[@kunkun12](https://github.com/kunkun12)增加查看我的附近功能

## todos

- 根据[BlackheartedHospital](https://github.com/langhua9527/BlackheartedHospital)仓库的最新数据更新geojson
- 交互改进

## 在线查看

- [点击前往](http://wandergis.com/putian-hospitals/)

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


