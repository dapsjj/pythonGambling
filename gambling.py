import numpy as np
import math

exitFlag=False
money = int(input('请输入你的赌资:'))
if money>1:
    print('赌资:'+str(money))
    while money > 1:
        for i in range(10000):
            # yazhu = int(input('请输入押注金额:'))
            print('当前投注金额:'+str(math.pow(2,i)))
            if money<2:
                print('对不起。赌资太少，欢迎下次再来。')
                exitFlag = True
                break
            else:
                randNum = np.random.randint(2)#随机数0和1,0代表赌博输了,1代表赌博赢了
                if randNum==0:
                    money = money - math.pow(2, i)
                else:
                    money = money + 2*math.pow(2, i)
                print('当前剩余赌资:' + str(money))
                if math.pow(2, i+1)>money:
                    print('对不起。赌资剩余:'+str(money)+'小于下轮投注金额:'+str(math.pow(2, i+1))+',赌博结束。')
                    exitFlag = True
                    break
        if exitFlag:
            print('赌博了'+str(i+1)+'把.')
            break


else:
    print('对不起。赌资太少，欢迎下次再来。')
