---
marp: true
theme: default
class: 
    - invert
---

# Say Hello to the World 

---

# Introduce python
- Python is an interpreted, object-oriented, high-level **programming language** with dynamic semantics.
- 直譯式、進階和通用的程式語言
- 常用在
    - Data science and machine learning
    - Web 開發
    - 自動化測試、爬蟲、駭客…

---

# Install python 
- [Python](https://www.python.org/downloads/)
    - latest version
    - 安裝時選 add to path，之後才能透過指令執行 python 程式
    - 查看版本號，確認是否安裝成功
    ``` sh
    python --version
    # 預期會輸出如下的版本號，版本號不一樣沒關係，3.X以上版本即可
    # Python 3.10.4
    ```
---

# and tools
- 開發工具 [VS Code](https://code.visualstudio.com/download)
    - Extensions
        - Python (Microsoft)

---

# Variable 變數
- 存放暫時性的資訊，是程式語言中重要的概念
- 練習：qrcode of my ig, fb, or blog    
    - VS Code 中開啟 Terminal (終端機), 安裝下列 qrcode 套件 
    ```sh
    pip install qrcode[pil]    
    ```

    > 套件 (package)的目的是避免重新製造輪子，
    > 可以到這裡查詢套件的相關資訊 https://pypi.org/

---
# Variable 變數
    - 建立 hello.py，並輸入以下程式碼
```python
import qrcode

# Variable 變數存放我的SNS位置 (請改成您想要顯示的文字)
mySns = "https://www.instagram.com/epicureanism/"

# 透過QRCODE 套件產生圖形
img = qrcode.make(mySns)

# 儲存圖形
img.save("hi-world-this-is-my-sns.png")
```