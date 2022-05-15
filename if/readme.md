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

# if, elif, else

- 對縮排 (indent) 很要求
    - 建議統一用「tab」鍵來縮排
- == 等於、< 小於、> 大於


```py
# guess.py
x = float(input("請輸入任一不等於0的數值："))

if x == 0:
    print("不可以輸入0哦")
elif x < 0:
    print("是負值")
elif x < 100:
    print("小於100")  
else:
    print("大於等於100")
```

---

# match, case, _
- 多條件要判斷時
- 或者 or  | 
- 而且 and & 
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