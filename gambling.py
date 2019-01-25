import numpy as np

exitFlag=False
money = int(input('请输入你的赌资:'))
# money = 10000
yazhu = 100
count = 0
print('赌资:'+str(money))
if money > 100:
    for i in range(10000):
        count += 1
        print('当前投注金额:'+str(yazhu))
        randNum = np.random.randint(2)#随机数0和1,0代表赌博输了,1代表赌博赢了
        if randNum==0:
            money = money - yazhu
            yazhu *= 2#赌输了则下轮投注翻倍
        else:
            money = money + 2*yazhu
        print('当前剩余赌资:' + str(money))

        if money<yazhu: #赌资不够下一轮押注，则押注金额重置为100
            print('赌资剩余:' + str(money) + ',小于'+str(yazhu)+',押注重置成100。')
            yazhu = 100

        if money < 100:
            print('对不起。赌资剩余:'+str(money)+',小于100,赌博结束。')
            exitFlag = True
            break


    print('赌博了'+str(count)+'把.')

else:
    print('对不起。赌资太少，欢迎下次再来。')
