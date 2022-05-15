h = float(input('請輸入身高(cm)：'))/100
w = float(input('請輸入體重(kg)：'))
# 體重 ( 公斤 ) 除以身高 ( 公尺 ) 的平方
bmi = w/(h*h)
print(f"你的BMI數值為：{bmi}")