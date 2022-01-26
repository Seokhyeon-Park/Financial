# [ 함수 ]
# 시장 데이터 정리
def stockDataOrgan(stockData):
    # [col][row].value
    # 실제 데이터는 row 값이 2 이상부터
    
    # 시장??
    print('Market : ', stockData[0][0].value)

    # 시장 데이터
    data = []

    # 날짜 처리
    date = []
    for d in stockData[0][2:]:
        if(d.value != None):
            # data split
            splited_data = d.value.split(' ')

            # set Date
            y = splited_data[0][:-1]
            if int(splited_data[1][:-1]) < 10:
                m = '0' + splited_data[1][:-1]
            else:
                m = splited_data[1][:-1]
            if int(splited_data[2]) < 10:
                d = '0' + splited_data[2]
            else:
                d = splited_data[2]
            
            # append Date
            date.append(y+m+d)
    # print("date : ", date)
    print("date[len] : ", len(date))
    data.append(date)
    
    # Open
    stockOpen = []
    for o in stockData[1][2:]:
        if(o.value != None):
            stockOpen.append(o.value)
    # print("open : ", stockOpen)
    print("open[len] : ", len(stockOpen))
    data.append(stockOpen)

    # High
    stockHigh = []
    for h in stockData[2][2:]:
        if(h.value != None):
            stockHigh.append(h.value)
    # print("high : ", stockHigh)
    print("high[len] : ", len(stockHigh))
    data.append(stockHigh)

    # Low
    stockLow = []
    for l in stockData[3][2:]:
        if(l.value != None):
            stockLow.append(l.value)
    # print("low : ", stockLow)
    print("low[len] : ", len(stockLow))
    data.append(stockLow)

    # Close
    stockClose = []
    for c in stockData[4][2:]:
        if(c.value != None):
            stockClose.append(c.value)
    # print("close : ", stockClose)
    print("close[len] : ", len(stockClose))
    data.append(stockClose)

    # 시장 데이터 리턴
    # Date[0] Open[1] High[2] Low[3] Close[4]
    return data

# 환율 데이터 정리
def exchangeDataOrgan(exchangeData):
    # [col][row].value
    # 실제 데이터는 row 값이 2 이상부터
    
    # 시장??
    print('Market : ', exchangeData[0][0].value)

    # 환율 데이터
    data = []

    # 날짜 처리
    date = []
    for d in exchangeData[0][2:]:
        if(d.value != None):
            # data split
            splited_data = d.value.split(' ')

            # set Date
            y = splited_data[0][:-1]
            if int(splited_data[1][:-1]) < 10:
                m = '0' + splited_data[1][:-1]
            else:
                m = splited_data[1][:-1]
            if int(splited_data[2]) < 10:
                d = '0' + splited_data[2]
            else:
                d = splited_data[2]
            
            # append Date
            date.append(y+m+d)
    # print("date : ", date)
    print("date[len] : ", len(date))
    data.append(date)

    # 환율
    exchange = []
    for e in exchangeData[1][2:]:
        if(e.value != None):
            exchange.append(e.value)
    # print("exchange data : ", exchange)
    print("exchange data[len] : ", len(exchange))
    data.append(exchange)

    # 환율 데이터 리턴
    # Date[0] Exchange Rate[1]
    return data