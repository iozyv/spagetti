print("--------------------\n")
print("1. 달력\n2. 요일 계산기\n3. 디데이 계산기\n4. 종료\n")
print("--------------------\n")
num = int(input("▶ 숫자를 입력하세요: "))
print("")

while(num==1 or num==2 or num==3 or num==4):
    if num==1 or num==2:
        yy = int(input("연도(YYYY): "))
        mm = int(input("월(MM): "))
        if num==2:
            dd = int(input("일(DD): "))

        # 각 달의 마지막 날짜
        lastDate = [31,28,31,30,31,30,31,31,30,31,30,31]

        # 입력한 년도의 전년도 12월 31일까지 날짜 수
        dateCount = 0
        for i in range(1,yy):
            if i%4==0 and i%100!=0 or i%400==0: # 윤년일 경우 1을 더 더함
                dateCount = dateCount+1
        dateCount = (yy-1)*365+dateCount

        # 입력한 달의 전 월 마지막 날까지
        if yy%4==0 and yy%100!=0 or yy%400==0: 
            lastDate[1] = 29
        for i in range(mm-1):
            dateCount += lastDate[i]

        # 입력한 달의 1일 요일 
        if num==1:
            firstDay = (dateCount+1)%7 # 0:일 1:월 2:화 3:수 4:목 5:금 6:토
            
        # 1번 출력
            days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

            print("\n         "+str(yy)+"년"+" "+str(mm)+"월"+"\n\n")
            for i in days:
                print(i,end=' ')
            print("\n")

            for i in range(4*firstDay):
                print(" ",end='')
            print("",end='')
            
            for i in range(1,lastDate[mm-1]+1):
                if len(str(i))==1:
                    print(" "+str(i),end='  ')
                elif len(str(i))==2:
                    print(str(i),end='  ')
                for j in range(1,7):
                    if i==7*j-firstDay:
                        print("\n")
            print("")

        # 입력한 날짜의 요일
        if num==2: 
            totalDay = (dateCount+dd)%7

         # 2번 출력
            daysKor = ["일","월","화","수","목","금","토"]
            print("\n"+str(yy)+"년 "+str(mm)+"월 "+str(dd)+"일은 "+daysKor[totalDay]+"요일입니다")

    if num==3:
        yearStart,monthStart,dayStart = input("기준 날짜(YYYY/MM/DD): ").split("/")
        yearToday,monthToday,dayToday = input("오늘 날짜(YYYY/MM/DD): ").split("/")
        yearStart = int(yearStart)
        monthStart = int(monthStart)
        dayStart = int(dayStart)
        yearToday = int(yearToday)
        monthToday = int(monthToday)
        dayToday = int(dayToday)

        lastDate = [31,28,31,30,31,30,31,31,30,31,30,31]

        # 기준 날짜
        dateCount = 0
        for i in range(1,yearStart):
            if i%4==0 and i%100!=0 or i%400==0:
                dateCount = dateCount+1
        dateCountStart = (yearStart-1)*365+dateCount

        if yearStart%4==0 and yearStart%100!=0 or yearStart%400==0: 
            lastDate[1] = 29
        for i in range(monthStart-1):
            dateCountStart += lastDate[i]
         
        totalDayStart = dateCountStart+dayStart

        # 오늘 날짜
        dateCount = 0
        for i in range(1,yearToday):
            if i%4==0 and i%100!=0 or i%400==0:
                dateCount = dateCount+1
        dateCountToday = (yearToday-1)*365+dateCount

        if yearToday%4==0 and yearToday%100!=0 or yearToday%400==0: 
            lastDate[1] = 29
        for i in range(monthToday-1):
            dateCountToday += lastDate[i]
         
        totalDayToday = dateCountToday+dayToday

        if totalDayStart >= totalDayToday: # D-Day
            decimalDay = totalDayStart-totalDayToday
            if decimalDay==0:
                print("\n"+str(yearStart)+"년 "+str(monthStart)+"월 "+str(dayStart)+"일은 D-DAY 입니다")
            else:
                print("\n"+str(yearStart)+"년 "+str(monthStart)+"월 "+str(dayStart)+"일은 D-"+str(decimalDay)+" 입니다")

        elif totalDayToday > totalDayStart: # D+Day
            print("\n  0. 0일부터 시작\n  1. 1일부터 시작\n")
            number = int(input("숫자를 선택하세요: "))
            decimalDay = totalDayToday-totalDayStart
            if number==1:
                decimalDay = decimalDay+1
            print("\n"+str(yearStart)+"년 "+str(monthStart)+"월 "+str(dayStart)+"일은 D+"+str(decimalDay)+" 입니다")

    print("\n--------------------\n")
    num = int(input("▶ 숫자를 입력하세요: "))
    print("")

    if num==4:
        break 
