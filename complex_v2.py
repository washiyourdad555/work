deposit = int(input("請輸入本金存款金額：")) # 本金輸入
times = 1.02 ** 6 #計算本金倍率，年利率2%，複利6年。 ##
deposit *= times # 以複合運算子計算本利和
print("6 年後存款為：" + str(deposit)) #本利和輸出
