var fs = require('fs');
var _ = require('lodash');
var async = require('async');
var request = require('request');
var data = JSON.parse(fs.readFileSync('./hospital.json'));
var hospitals = [];
for (var city in data) {
    hospitals = hospitals.concat(data[city].hospital.map(function(value, index) {
        return city + ' ' + value;
    }));
}
// url=http://restapi.amap.com/v3/geocode/geo?key=你的key&address=泉州南亚医院&city=泉州
fs.appendFileSync("hospital.csv", 'name,lng,lat\n');
async.eachLimit(hospitals, 10, function(hospital, cb) {
    var uri = 'http://restapi.amap.com/v3/geocode/geo?key=你的key&address=' + hospital.split(' ')[1] + '&city=' + hospital.split(' ')[0];
    request(encodeURI(uri), function(error, response, body) {
        if (!error && response.statusCode == 200) {
            var body = JSON.parse(response.body);
            if (body.status === '1' && body.geocodes.length > 0) {
                var location = body.geocodes[0].location.split(',');
                var str = hospital.split(' ')[1] + ',' + Number(location[0]) + ',' + Number(location[1]) + '\n';
                fs.appendFileSync("hospital.csv", str);
                console.log('完成' + hospital);
            }
        }
        cb();
    });
});
