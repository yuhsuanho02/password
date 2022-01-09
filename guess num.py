import random
a = random.randint(1, 100)
count = 0
while True:
    count += 1 #count = count = 1
    num = input('1~100你覺得是哪一個數字呢?')
    num = int(num)
    if num == a:
        print("答對了!")
        break
    elif num > a:
        print("再小一點")
    elif num < a:
        print("再大一點")