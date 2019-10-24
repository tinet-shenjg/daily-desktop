# daily-desktop

---
python生成每日工作计划桌面背景图
---

## 使用方法
1. 安装依赖

```
pip3 install opencv-python
pip3 install Pillow
```
2. 修改文件中的文字坐标
```
draw.text((2000, 300),  date + " 计划", font = font, fill = (255, 255, 255))
```

3. 找到适合自己的字体
```
fontpath = "/System/Library/Fonts/PingFang.ttc"
```

4. 执行
```
python3 desk.py
请输入今日计划条数：3
3
请输入计划：写作文
请输入计划：背单词
请输入计划：撩妹子
```
5. 预览图
![avatar](https://github.com/tinet-shenjg/daily-desktop/blob/master/background.jpg)
