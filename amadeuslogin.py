import csv
import sys


def login(_id2,admin,):
    if admin == '1':
        print("최고 관리 권한 소지자 " + _id2 + "님이 로그인 하셨습니다.")
    else:
        print(_id2+ "님이 로그인하셨습니다.")

accounts=[]
columnNames=[]


def amadeus_login():
    with open("amadeus ID.csv","r") as f:
        data=csv.reader(f)
        linecount=0
        for line in data:
            # print(line)
            if linecount==0:
                columnNames = line
                linecount+=1
            else:
                account={}
                for i in range(len(columnNames)):
                    account[columnNames[i]]=line[i]
                accounts.append(account)
    #csv 데이터 읽어오기 완료!
    isValidate=False
    cnt = 0
    while True:
        _id=input("ID : ")
        _pw=input("PW : ")

        for account in accounts:
            if account["ID"] == _id and account["PW"] == _pw:
                isValidate=True
                lohin11 = 1
                login(_id, account["admin"])
                break
        if isValidate:break
        else:
            print("일치하는 계정이 없습니다.")
            cnt = cnt+1
        if cnt == 3:
            print("보안을 위해 시스템을 종료합니다.")
            sys.exit()



    

