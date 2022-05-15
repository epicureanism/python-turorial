x = float(input("請輸入任一不等於0的數值："))

if x == 0:
    print("不可以輸入0哦")
elif x < 0:
    print("是負值")
elif x < 100:
    print("小於100")  
else:
    print("大於等於100")