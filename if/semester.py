x = int(input("請輸入學期的月份："))

match x:    
    case 2:
        print("通常是寒假")
    case 7 | 8:
        print("通常是暑假")
    case 6:
        print("學期末")        
    case 9:
        print("開學囉")
    case _:
        print("要上課！")