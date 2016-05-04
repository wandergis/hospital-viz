# putian-hospitals
莆田系医院数据及其经纬度坐标，包括geojson和shp文件。
## 数据来源
- **数据来自网络，对数据的准确性并不完全保证，可视化结果仅供参和考学习用途。**
- [凤凰网的数据](http://news.ifeng.com/mainland/special/ptxyy/)，解密其`main2.min.js`文件，得到了hospitals的数组，使用python转成json数据。
- [BlackheartedHospital](https://github.com/langhua9527/BlackheartedHospital)仓库网友更新数据

## 在线查看

- [点击前往](https://wandergis.com/putian-hospitals/index.html)

## 更新说明

- 感谢[@kunkun12](https://github.com/kunkun12)增加查看我的附近功能(在某些PC上该功能可能会有问题)
- 根据[BlackheartedHospital](https://github.com/langhua9527/BlackheartedHospital)仓库的最新数据更新geojson，截止2016.5.4 10:40,部分数据由于名称关系可能未解析到地址。
- 目前解析了`594`条数据,以`geojson`文件为准

## todos

- ~~根据[BlackheartedHospital](https://github.com/langhua9527/BlackheartedHospital)仓库的最新数据更新geojson~~
- 交互改进

## 坐标获取

- 使用node调用高德的geocode api解析成经纬度

## 数据展示

- 使用leaflet展示

## 二维码
- ![截图](https://github.com/shihai84/putian-hospitals/blob/gh-pages/qrcode.png)

## 截图示例

![截图](https://raw.githubusercontent.com/wandergis/putian-hospitals/gh-pages/screenshot2.png)

![截图](https://raw.githubusercontent.com/wandergis/putian-hospitals/gh-pages/screenshot.png)


