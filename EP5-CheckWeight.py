
friend={'มาโนช':65,'โมชนา':63,'มานโช':55,'มาโชน':52,'ชาโนม':49}
def checkWeight(friend,weig):
    print("ผู้ที่มีน้ำหนักมากกว่า " + str(weig) + " คือ")
    for f in friend.items():
        if (f[1] >= weig):
            print(f[0], f[1])
checkWeight(friend, 49)   