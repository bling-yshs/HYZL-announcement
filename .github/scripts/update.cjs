const fs = require('fs');
let message = process.argv[2];
// 读取原本的公告
let buffer = fs.readFileSync('./announcement.json');
// 转换为对象
let obj = JSON.parse(buffer.toString());
const newAnnouncement = {}
// 获取当前时间戳
let secondsTimestamp = Math.floor(new Date().getTime() / 1000);
// 更新公告
newAnnouncement.version = obj[0].version + 1;
newAnnouncement.content = message;
newAnnouncement.timestamp = secondsTimestamp;
newAnnouncement.deprecated = false;
// 添加到数组的开头
obj.unshift(newAnnouncement);
// 写入文件
fs.writeFileSync('./announcement.json', JSON.stringify(obj, null, 2));
