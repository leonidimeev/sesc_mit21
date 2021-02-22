import math
while True:
    print("1.Гипотенуза\n2.Площадь треугольника")
    op = input("Выбрать: ")
    if op == "1":
        katet0 = int(input("Катет 1: "))
        katet1 = int(input("Катет 2: "))
        print(math.hypot(katet0, katet1))
    storoni,h,hs,ugols = [0,0,0],0,0,[0,0]
    if op == "2":
        res = 0
        begin = True
        while res == 0:
            print("Что известно?\n1.Стороны(а) "+str(storoni)+"\n2.Высота и сторона"+str(h)+" "+str(hs)+"\n3.Углы альфа и бета "+str(ugols))
            tri = input("Выбрать: ")
            if tri == "1":
                storoni = [0,0,0]
                storona = 1
                end = True
                while end == True:
                    print("Чтобы выйти напишите 0")
                    storona = int(input("Добавить: "))
                    if storona == 0:
                        break
                    for i in range(len(storoni)):
                        if storoni[i] == 0:
                            storoni[i] = storona
                            print("Стороны: ",storoni)
                            if storoni[0] != 0 and storoni[1] != 0 and storoni[2] != 0:
                                end = False
                            break
            if tri == "2":
                h = int(input("Введите высоту: "))
                hs = input("Введите сторону, на которую опущена высота (a,b,c): ")
                if hs == "a":
                    hs = 0
                if hs == "b":
                    hs = 1
                if hs == "c":
                    hs = 2
            if tri == "3":
                end1 = False
                ugols = [0,0]
                while end1 == False:
                    ugol = int(input("Введите угол: "))
                    for i in range(len(ugols)):
                        if ugol == 0:
                            end1 = True
                            break
                        if ugols[i] == 0:
                            ugols[i] = ugol
                            print(ugols)
                            if ugols[0] != 0 and ugols[1] != 0:
                                end1 = True
                            break
            
            if h != 0 and storoni[hs] != 0:
                res = 0.5*storoni[hs]*h
                print(str(res)+"см^2")
            if storoni[0] != 0 and storoni[1] != 0 and ugols[0] != 0:
                res = (storoni[0]*storoni[1]*math.sin(math.radians(ugols[0])))/2
                print(str(res)+"см^2")
            if storoni[0] != 0 and storoni[1] != 0 and storoni[2] !=0:
                p = (storoni[0]+storoni[1]+storoni[2])/2
                res = math.sqrt(p*(p-storoni[0])*(p-storoni[1])*(p-storoni[2]))
                print(str(res)+"см^2")
            if storoni[0] != 0 and ugols[0] != 0 and ugols[1] != 0:
                res = ((storoni[0]**2*math.sin(math.radians(180-ugols[0]-ugols[1])))*math.sin(math.radians(ugols[1]))) / (2*math.sin(math.radians(ugols[0])))
                print(str(res)+"см^2")