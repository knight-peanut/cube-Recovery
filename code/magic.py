import time

#-----------------���в���----------
t1=time.time()
print "��ԭħ���������£�"



#-----------------��ʼ������---------------
'''
[0,1,2,3,4,5]���δ�����ɫ������̻ư�
a~f : ������ʶ�����ɫ,���δ�����������ǰ�����
magicList: ������ɫ�б�����ħ����

'''
a=[0,0,0,1,4,5,2,0,4]#��
b=[4,4,5,1,5,0,2,0,3]#��
c=[2,4,1,5,0,2,4,2,3]#��
d=[5,4,3,5,3,3,0,2,2]#ǰ
e=[1,3,5,4,1,1,0,5,1]#��
f=[3,3,4,3,2,1,5,2,1]#��
magicList = [[a],[b],[c],[d],[e],[f]]
temp=[0,0,0,0,0,0,0,0,0] #���彻������


#-------------����ħ��ת��䶯����---------

#������ת
def wholeTurnLeft():
    #�ϲ�����б任
    for i in range(9):
        temp[i] = a[i]
    a[0] = temp[6]
    a[1] = temp[3]
    a[2] = temp[0]
    a[3] = temp[7]
    a[4] = temp[4]
    a[5] = temp[1]
    a[6] = temp[8]
    a[7] = temp[5]
    a[8] = temp[2]
    #�²�����н���
    for i in range(9):
        temp [i] = b[i]
    b[0] = temp[2]
    b[1] = temp[5]
    b[2] = temp[8]
    b[3] = temp[1]
    b[4] = temp[4]
    b[5] = temp[7]
    b[6] = temp[0]
    b[7] = temp[3]
    b[8] = temp[6]
    #�м����н���
    #��ǰ�Һ���������ֻ�
    for i in range(9):
        temp [i] = c[i]
    for i in range(9):
        c[i] = d[i]
        d[i] = e[i]
        e[i] = f[i]
        f[i] = temp[i]



#������ת
def wholeTurnRight():
    for i in range(3):
        wholeTurnLeft()

#�������ת��
def leftTurnDown():
    for i in range(9):
        temp [i] = c[i]
    c[0] = temp[6]
    c[1] = temp[3]
    c[2] = temp[0]
    c[3] = temp[7]
    c[4] = temp[4]
    c[5] = temp[1]
    c[6] = temp[8]
    c[7] = temp[5]
    c[8] = temp[2]
    
    #1��4��7��
    temp[0] = d[0]
    temp[1] = d[3]
    temp[2] = d[6]

    d[0] = a[0]
    d[3] = a[3]
    d[6] = a[6]

    a[0] = f[8]
    a[3] = f[5]
    a[6] = f[2]

    f[2] = b[6]
    f[5] = b[3]
    f[8] = b[0]

    b[0] = temp[0]
    b[3] = temp[1]
    b[6] = temp[2]


#�������ת��
def leftTurnUp():
    for i in range(3):
        leftTurnDown()

#�ϲ�����ת��    
def upTurnRight():
    for i in range(9):
        temp [i] = a[i]
    a[0] = temp[2]
    a[1] = temp[5]
    a[2] = temp[8]
    a[3] = temp[1]
    a[4] = temp[4]
    a[5] = temp[7]
    a[6] = temp[0]
    a[7] = temp[3]
    a[8] = temp[6]

    #1��2��3��
    temp[0] = d[0]
    temp[1] = d[1]
    temp[2] = d[2]

    d[0] = c[0]
    d[1] = c[1]
    d[2] = c[2]
    
    c[0] = f[0]
    c[1] = f[1]
    c[2] = f[2]
    
    f[0] = e[0]
    f[1] = e[1]
    f[2] = e[2]

    e[0] = temp[0]
    e[1] = temp[1]
    e[2] = temp[2]


#�ϲ�����ת��
def upTurnLeft():
    for i in range(3):
        upTurnRight()

#ǰ��˳ʱ��
def frontClock():
    wholeTurnLeft()
    leftTurnDown()
    wholeTurnRight()


#ǰ����ʱ��
def frontOnClock():
    wholeTurnLeft()
    leftTurnUp()
    wholeTurnRight()


#�Ҳ�����
def rightTurnDown():
    for i in range(2):
        wholeTurnLeft()
    leftTurnUp()
    for i in range(2):
        wholeTurnLeft()


#�Ҳ�����
def rightTurnUp():
    for i in range(2):
        wholeTurnLeft()
    leftTurnDown()
    for i in range(2):
        wholeTurnLeft()


#-------------����ħ����ʽ--------------

#���ֹ�ʽ
def LHand():
    upTurnRight()
    print "�ϲ���ת"
    leftTurnUp()
    print "�������ת"
    upTurnLeft()
    print "�ϲ�����ת"
    leftTurnDown()
    print "�������ת"

#���ֹ�ʽ
def RHand():
    upTurnLeft()
    print "�ϲ�����ת"
    rightTurnUp()
    print "�Ҳ�����ת"
    upTurnRight()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"

#һ�ֹ�ʽ
def One():
    rightTurnUp()
    print "�Ҳ�����ת"
    upTurnLeft()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"
    upTurnRight()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"
    frontClock()
    print "ǰ��˳ʱ��ת"
    rightTurnUp()
    print "�Ҳ�����ת"
    frontOnClock()
    print "ǰ����ʱ��ת"

#�սǹ�ʽ
def Round():
    frontClock()
    print "ǰ��˳ʱ��ת"
    rightTurnUp()
    print "�Ҳ�����ת"
    upTurnRight()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"
    upTurnRight()
    print "�ϲ�����ת"
    rightTurnUp()
    print  "�Ҳ�����ת"
    upTurnLeft()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"
    frontOnClock()
    print "ǰ����ʱ��ת"

#��С�㹫ʽ
def Lfish():
    leftTurnUp()
    print "�������ת"
    upTurnRight()
    print "�ϲ�����ת"
    leftTurnDown()
    print "�������ת"
    upTurnRight()
    print "�ϲ�����ת"
    leftTurnUp()
    print "�������ת"
    upTurnRight()
    print "�ϲ�����ת"
    upTurnRight()
    print "�ϲ�����ת"
    leftTurnDown()
    print "�������ת"

#��С�㹫ʽ
def Rfish():
    rightTurnUp()
    print "�Ҳ�����ת"
    upTurnLeft()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"
    upTurnLeft()
    print "�ϲ�����ת"
    rightTurnUp()
    print"�Ҳ�����ת"
    upTurnLeft()
    print "�ϲ�����ת"
    upTurnLeft()
    print "�ϲ�����ת"
    rightTurnDown()
    print "�Ҳ�����ת"

#----------------------�������ħ����ԭ�㷨---------------------------

#-------------ħ����ԭ�㷨��һ��:�ҵ�С�׻�
'''
С�׻����ֳƶ����ʮ�֣���ɫ�����Ŀ�������ĸ���ɫ�����������

'''
def findWhiteFlower():
    
    if(a[1]!=5) or (a[7]!=5) or (a[3]!=5) or (a[5]!=5):
        #�ȴ�ǰ���濪ʼ��������ÿ�����Ұ׿�
        flag = 0 #��ת�Ұ׿������
        while(flag!=4):
            if (d[1]!=5) and (d[7]!=5) and (d[3]!=5) and (d[5]!=5):
                wholeTurnLeft()
                print "������ת"
                flag += 1
            else:
                flag=0
                if(d[1]==5):
                    frontClock()
                    print "ǰ��˳ʱ��ת"
                    rightTurnUp()
                    print "�Ҳ�����ת"
                if(d[7]==5):
                    frontClock()
                    print "ǰ��˳ʱ��ת"
                    leftTurnUp()
                    print "�������ת"
                if(d[3]==5):
                    while(a[3]==5):
                        upTurnRight()
                        print "�ϲ���ת"
                    leftTurnUp()
                    print "�������ת"
                if(d[5]==5):
                    while(a[5]==5):
                        upTurnRight()
                        print "�ϲ���ת"
                    rightTurnUp()
                    print "�Ҳ�����ת"
    
    while(a[1]!=5) or (a[7]!=5) or (a[3]!=5) or (a[5]!=5):
        if(b[1]==5):
            while(a[7]==5):
                upTurnRight()
                print "�ϲ���ת"
            for i in range(2):
                frontClock()
                print "ǰ��˳ʱ��ת"
        wholeTurnLeft()
        print "������ת"

#--------------ħ����ԭ�㷨�ڶ���:�����λ
def Step2Position():
    for i in range(4):
        while((d[1]!=d[4]) or a[7]!=5 ):
            upTurnLeft()
            print "�ϲ���ת"
        for i in range(2):
            frontClock()
            print "ǰ��˳ʱ��ת"
        wholeTurnLeft()
        print "������ת"

#--------------ħ����ԭ�㷨������:�׽ǹ�λ
def Step3Position():
    asFlag=0
    while (asFlag==0):
        #�жϵײ�������ͬɫ,�ײ�ȫΪ�׿�
        if (c[6]==c[7]==c[8])and(d[6]==d[7]==d[8])and(e[6]==e[7]==e[8])and(f[6]==f[7]==f[8])and (b[0]==b[1]==b[2]==b[3]==b[4]==b[5]==b[6]==b[7]==b[8]==5):
            asFlag=1
            break
            
        #�ϲ�ſ��ɫ�ж�
        if (a[0]==5) or (a[2]==5) or (a[6]==5) or (a[8]==5):
            while(a[6]!=5):
                upTurnRight()
                print "�ϲ�����ת"
            while(c[2]!=d[4] or c[4]!=d[0]):
                upTurnRight()
                print "�ϲ�����ת"
                wholeTurnLeft()
                print "������ת"
            for i in range(3):
                LHand()

        #�����ϲ��ɫ�ж�
        elif (c[0]==5) or (c[2]==5) or (d[0]==5) or (d[2]==5) or (e[0]==5) or (e[2]==5) or (f[0]==5) or (f[2]==5):
            while(d[0]!=5 and d[2]!=5):
                upTurnRight()
                print "�ϲ�����ת"
            if (d[0]==5):
                while(a[6]!=d[4]):
                    upTurnRight()
                    print "�ϲ�����ת"
                    wholeTurnLeft()
                    print "������ת"
                LHand()
            

            else:
                while(a[8]!=d[4]):
                    upTurnRight()
                    print "�ϲ�����ת"
                    wholeTurnLeft()
                    print "������ת"
                RHand()


        #�׿�ײ�����ж�
        elif(c[6]==5) or (c[8]==5) or (d[6]==5) or (d[8]==5) or (e[6]==5) or (e[8]==5) or (f[6]==5) or (f[8]==5):
            while(d[6]!=5 and d[8]!=5):
                wholeTurnLeft()
                print "������ת"
            if(d[6]==5):
                LHand()
            else:
                RHand()
                
        else:
            #��ɫ�ſ鳯��
            for i in range(4):
                if(d[6]==d[7]):
                    wholeTurnLeft()
                    print "������ת"
            LHand()

#---------------ħ����ԭ�㷨���Ĳ��������λ

def Step4Position():
    #�ж��ϲ��ɫ������
    yb=0 #�ƿ����
    while(c[3]!=c[4]) or (d[3]!=d[4]) or (e[3]!=e[4]) or (f[3]!=f[4]):
        yb=0
        if(a[1]==4):
            yb += 1
        if(a[3]==4):
            yb += 1
        if(a[5]==4):
            yb += 1
        if(a[7]==4):
            yb += 1
        if(c[1]==4):
            yb += 1
        if(d[1]==4):
            yb += 1
        if(e[1]==4):
            yb += 1
        if(f[1]==4):
            yb += 1

        if yb<4:
            while(a[7]==4 or d[1]==4):
                upTurnRight()
                print "�ϲ���ת"
            while(d[1]!=d[4]):
                upTurnRight()
                print "�ϲ���ת"
                wholeTurnLeft()
                print "������ת"
            if(a[7]==c[4]):
                LHand()
                wholeTurnRight()
                print "������ת"
                RHand()
            else:
                RHand()
                wholeTurnLeft()
                print "������ת"
                LHand()
        else:
           while(d[3]==d[4]):
               wholeTurnLeft()
               print "������ת"
           LHand()
           wholeTurnRight()
           print "������ת"
           RHand()

#-----------------ħ����ԭ�㷨���岽��������λ
def TopEdge():
    flag5=1
    while(flag5):
        if(a[1]==4) and (a[3]==4) and (a[5]==4) and (a[7]==4):
            flag5=0
        if(a[3]==4 and a[5]==4) or (a[1]==4 and a[7]==4):
            while(d[1]==4):
                upTurnRight()
                print "�ϲ���ת"
            One()
        while(d[1]!=4 or e[1]!=4):
            upTurnRight()
            print "�ϲ���ת"
        Round()

#-----------------ħ����ԭ�㷨��������������λ
def TopAngel():
    #�ж��Ƿ�ΪС��
    fishFlag=0 #С��ƿ���
    while(fishFlag!=4):
        fishFlag=0 
        if a[0]==4:
            fishFlag += 1
        if a[2]==4:
            fishFlag += 1
        if a[6]==4:
            fishFlag += 1
        if a[8]==4:
            fishFlag += 1
        if(fishFlag==1):
            for i in range(4):
                if(a[7]==a[8]==d[0]) or (a[6]==a[7]==d[2]):
                    break
                upTurnRight()
                print "�ϲ�����ת"
            if(a[7]==a[8]==d[0]):
                Lfish()
            else:
                Rfish()
            break
        else:
            while(d[0]!=4):
                upTurnRight()
                print "�ϲ�����ת"
            Rfish()

#---------------ħ����ԭ�㷨���߲������ǹ�λ        
            
def AngerlPosition():
    #�ж�һ���۾�
    fisheyes = []
    eyes = 0
    for i in range(4):
        if(c[2]==c[5]==c[8]) and (d[0]==d[3]==d[6]):
            eyes += 1
        if(d[2]==d[5]==d[8]) and (e[0]==e[3]==e[6]):
            eyes += 1
        if(e[2]==e[5]==e[8]) and (f[0]==f[3]==f[6]):
            eyes += 1
        if(f[2]==f[5]==f[8]) and (c[0]==c[3]==c[6]):
            eyes += 1
        upTurnRight()
        print "�ϲ�����ת"
        fisheyes.append(eyes)
    eyes=max(fisheyes[0],fisheyes[1],fisheyes[2],fisheyes[3])
    if(eyes==0):
        while((c[0]==d[0]==d[2])==1):
            upTurnRight()
            print "�ϲ�����ת"
        Round()
        One()
    if(eyes==1):
        while((((c[2]==c[5]==c[8]) and (d[0]==d[3]==d[6])) or ((d[2]==d[5]==d[8]) and (e[0]==e[3]==e[6])) or ((e[2]==e[5]==e[8]) and (f[0]==f[3]==f[6])) or ((f[2]==f[5]==f[8]) and (c[0]==c[3]==c[6])))==1):
            upTurnRight()
            print "�ϲ�����ת"
        while(d[2]!=d[5] or e[0]!=e[3]):
            wholeTurnLeft()
            print "��������ת"
        One()
        Round()
    else:
        #��ֻ�۾�������i��������ڣ����
        if(c[0]==c[2] or d[0]==d[2] or e[0]==e[2] or f[0]==f[2]):
            while(d[0]!=d[2]):
                upTurnRight()
                print "�ϲ�����ת"
            while(d[0]==d[3]):
                upTurnRight()
                print "�ϲ�����ת"
                wholeTurnLeft()
                print "��������ת"
            wholeTurnLeft()
            print "��������ת"
            One()
            Round()
        else:
            while(((d[2]==d[5] and e[0]==e[3]) or (f[2]==f[5] and c[0]==c[3]))==1):
                upTurnLeft()
                print "�ϲ�����ת"
            while((c[2]==c[5] and d[0]==d[3])==1):
                wholeTurnRight()
                print "��������ת"
            Round()
            One()
                
            
        

#---------------ħ����ԭ�㷨�ڰ˲�;�����λ
def PoPosition():
    #���ж�����Ƿ��λ
    while((c[0]==c[1] and d[0]==d[1] and e[0]==e[1] and f[0]==f[1])!=1):
        #�����������һ��ͬɫ����һ��ͬɫ
        if(c[0]==c[1] or d[0]==d[1] or e[0]==e[1] or f[0]==f[1]):
            while(f[0]!=f[1]):
                wholeTurnLeft()
                print "������ת"
            if(d[4]==c[1]):
                Lfish()
                upTurnRight()
                print "�ϲ���ת"
                Rfish()
            else:
                Rfish()
                upTurnLeft()
                print "�ϲ���ת"
                Lfish()
        else:
            Lfish()
            while((a[6]==a[7]==d[2])==0):
                wholeTurnLeft()
                print "������ת"
            Rfish()
    while(d[0]!=d[3]):
        upTurnLeft()
        print "�ϲ���ת"
      

#--------------��������ģ��------------
def test():
    #One()
    #Round()
    #Lfish()
    #Rfish()
    findWhiteFlower()
    print magicList
    print "---------------------����һ�ָ���----------------------"
    Step2Position()
    print magicList
    print "---------------------������ָ���----------------------"
    Step3Position()
    print magicList
    print "---------------------�������ָ���----------------------"
    Step4Position()
    print magicList
    print "---------------------�����ķָ���----------------------"
    TopEdge()
    print magicList
    print "---------------------������ָ���----------------------"
    TopAngel()
    print magicList
    print "---------------------�������ָ���----------------------"
    AngerlPosition()
    print magicList
    print "---------------------�����߷ָ���----------------------"
    PoPosition()
    print magicList
    print "---------------------����˷ָ���----------------------"

    
#����
test()
t2=time.time()
print "run step:(times)"
print 257
print "run time:(second)"
print (t2-t1)

          



























