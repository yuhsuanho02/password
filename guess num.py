import random
start = input("請輸入範圍起始值:")
end = input("請輸入範圍終止值:")
start = int(start)
end = int(end)
a = random.randint(start, end)
count = 0
while True:
    count += 1 #count = count = 1
    num = input('你覺得是哪一個數字呢?')
    num = int(num)
    if num == a:
        print("答對了!")
        print("這是你猜的第", count, "次")
        break
    elif num > a:
        print("再小一點")
    elif num < a:
        print("再大一點")
    print("這是你猜的第", count, "次")