---
marp: true
theme: default
class: 
    - invert
    - lead
pagination: true
---

# 基礎型別 

---
# 基礎型別 
## 整數 int
123
-456

## 浮點數 float
123.0
-456.0

---

## 布林值 bool
True
False
```py
a = 1
b = 1
print(a==b)

t = False
print(t == True)

```

---

## 字串 string
"你好"
'你好'
``` py
# 跳脫字元 \ 
escapeDemo =  "你\"好\""
print(escapeDemo) #=> 你"好"
```

---

## 常見字串用法 1

```py
# 印出字串長度
strDemo =  "你好"
print(len(strDemo)) #=> 2

# 自動重複字串n遍
print(strDemo*3) #=>你好你好你好

# 串接字串
strDemo = strDemo + "，大家好"
print(strDemo) #=>你好，大家好

```
---

## 常見字串用法 2

```py
# 取出部分字串 (又叫 slicing)
# 你好，大家好
# 0 1 2 3 4 5
print(strDemo[3]) # 只有3=>大
print(strDemo[3:]) # 3開始到最後=>大家好
print(strDemo[0:2]) # 0到2，但不包含2=>你好

# 搜尋字串 (回傳位置, 沒找到的話會回傳-1)
print(strDemo.find("大家")) #=>3

# 取代字串
print(strDemo.replace("大家", "老師")) #=>你好，老師好
```
---

# 型別轉換
str()
float()
chr()
int()
```py
demo = "1234.56"
# 轉 float
demo = float(demo)
print(f"{demo} {type(demo)}")
# 轉 int
demo = int(demo)
print(f"{demo} {type(demo)}")
# 轉 string
demo = str(demo)
print(f"{demo} {type(demo)}")
```

---

# 四則運算
- 加 +
- 減 -
- 乘 *
- 除 /
    - 除法取整數 //
    - 除法取餘數 %
- 次方 **
  - x ** 3 相當於 x 的3次方
- 設定敘述
  - += 
    - x += 5 相當於 x = x + 5
    - x -= 5 相當於 x = x - 5
---

## 範例
```py
a = 10
b = 0.5
a = (a + b) * 2 # 小括號可指定運算的優先次序
print(a, end=' ') # 21 
print(type(a)) #a 已從整數自動轉為浮點數
print(a/2) # 10.5
print(a//2)# 10.0
print(a%2) # 1.0
a += 0.5
print(a) # 21.5
```

---

# 練習 - 我的BMI

---

# 練習
- 建立 my-bmi.py
    - BMI 公式是：體重(公斤)除以身高(公尺)的平方
```py
# input 會呼叫終端機，請使用者輸入數值
# float 是內建函式，將輸入值進行型別轉換
h = float(input('請輸入身高(cm)：'))/100 #轉換為公尺
w = float(input('請輸入體重(kg)：'))
# 體重 ( 公斤 ) 除以身高 ( 公尺 ) 的平方
bmi = w/(h*h)
print(f"你的BMI數值為：{bmi}")
```
