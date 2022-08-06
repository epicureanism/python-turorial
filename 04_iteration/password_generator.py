import random 

characters = "0123456789abcdefghijklmnopqr!@#$%^&*"
password = ""
password_length = int(input("請輸入密碼長度："))
for i in range(password_length):
    password += random.choice(characters) #利用 random 套件來做隨機選擇
print(password)