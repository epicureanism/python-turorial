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