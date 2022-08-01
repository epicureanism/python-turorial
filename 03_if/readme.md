---
marp: true
theme: default
class: 
    - invert
    - lead
pagination: true
---

# 邏輯判斷

---

# 比較運算子 
  - == 等於
  - != 不等於
  - < 小於
  - > 大於
  - <= 小於等於
  - >= 大於等於

```py
100 > 10 # 得到結果 True
1 >= 2 # 得到結果 False
'python' != 'html' # 得到結果 True
```

---

# if, elif, else

- 對縮排 (indent) 很要求
    - 建議統一用「tab」鍵來縮排
```py
a = 10
b = 100
if a > b:
    print("a 大於 b")
elif a == b:
    print("a 等於 b")
else:
    print("a 小於 b")
```

---

# 邏輯運算子
- and 
  - 左右兩邊都是 True, 則回傳 True
  ```py
  1 < 2 and 3 > 2 # True
  2 < 1 and 3 > 2 # False
  ``` 
- or
  - 左右其中一邊是 True, 則回傳 True
  ```py
  1 < 2 or 3 > 2 # True
  2 < 1 or 3 > 2 # True
  2 < 1 or 2 > 3 # False
  ```
- not
  - 反轉布林值
  ```py
  not 1 < 2 #False
  not (1 < 2) #用括號在可讀性上會更容易理解
  ```

---

# 練習
```py
# guess.py
import datetime #利用 datetime 這個套件
import os 

# 取得現在時間的小時
hour = datetime.datetime.now().hour 
# 利用現在的小時來產生一個數字，公式可以自訂，在這一個小時中的答案會是一樣的
r = (hour + 1) * 4 - 2 
guess = float(input("猜數字，請輸入任一0到100的數值："))

#開始進行邏輯判斷
if guess == r:
    print("恭喜答對了！")
elif guess < r and guess < (r-50): 
    print("有點太小囉")
    os.system('python guess.py') # 重新執行一次猜數字的遊戲
elif guess < r:
    print("再大一點點") 
    os.system('python guess.py')
elif guess > r and (guess-50) > r:
    print("有點太大囉")
    os.system('python guess.py')
else:
    print("再小一點點")
    os.system('python guess.py')
```

---

# match, case, _
- 多條件要判斷時
- 或者 or  
- 而且 and 
```py
x = int(input("請輸入學期的月份："))
match x:    
    case 2:
        print("通常是寒假")
    case 7 | 8:
        print("通常是暑假")
    case 6:
        print("學期末")        
    case 9:
        print("開學囉")
    case _:
        print("要上課！")
```
---