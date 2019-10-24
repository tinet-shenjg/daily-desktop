import cv2
import time
from PIL import ImageFont, ImageDraw, Image
import numpy as np

bk_img = cv2.imread("work.png")
#设置需要显示的字体
fontpath = "/System/Library/Fonts/PingFang.ttc"
font = ImageFont.truetype(fontpath, 40)
img_pil = Image.fromarray(bk_img)
draw = ImageDraw.Draw(img_pil)
#绘制文字信息
date = time.strftime('%Y年%m月%d日',time.localtime(time.time()))
draw.text((2000, 300),  date + " 计划", font = font, fill = (255, 255, 255))
count = int(input("请输入今日计划条数："))
print(count)
row = 300
var = 0
while var < count:
    var+=1
    row = row + 90
    title = input("请输入计划：")
    draw.text((2000, row),  str(var) + "." + title, font = font, fill = (255, 255, 255))
bk_img = np.array(img_pil)

## cv2.imshow("add_text",bk_img)
cv2.waitKey()
cv2.imwrite("add_text.jpg",bk_img)

