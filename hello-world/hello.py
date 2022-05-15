import qrcode

# Variable 變數存放我的SNS位置
mySns = "https://www.instagram.com/epicureanism/"

# 透過QRCODE 套件產生圖形
img = qrcode.make(mySns)

# 儲存圖形
img.save("hi-world-this-is-me.png")