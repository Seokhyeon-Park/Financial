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

# 시간 좌표 설정
def timelineSet(organStock, organExchange):
    # 날짜 기준 배열 생성
    timeline = organStock[4][0]

    # stocks
    # 코스피 [0], 코스닥 [1], 나스닥 [2], 다우지수 [3], 스탠다드 푸어스 [4], 환율(Korea - USA) [5]
    # 환율(Korea - USA) : organExchange
    stocks = []
    for st in range(0, 6):
        print("st : ", st)
        stocks.append([])
        for os in range(0, len(organStock[4][0])):
            stocks[st].append(0)

    print("stocks ??", len(stocks))
    print("stocks date ??", len(stocks[0]))

    for time in timeline:
        # kospi에 기록이 있는 값만
        if time in organStock[0][0]:
            stocks[0][organStock[4][0].index(time)] = organStock[0][4][organStock[0][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[0][0].index(time), "\tvalue : ", organStock[0][4][organStock[0][0].index(time)])
        # kosdaq 기록이 있는 값만
        if time in organStock[1][0]:
            stocks[1][organStock[4][0].index(time)] = organStock[1][4][organStock[1][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[1][0].index(time), "\tvalue : ", organStock[1][4][organStock[1][0].index(time)])
        # nasdaq 기록이 있는 값만
        if time in organStock[2][0]:
            stocks[2][organStock[4][0].index(time)] = organStock[2][4][organStock[2][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[2][0].index(time), "\tvalue : ", organStock[2][4][organStock[2][0].index(time)])
        # djia 기록이 있는 값만
        if time in organStock[3][0]:
            stocks[3][organStock[4][0].index(time)] = organStock[3][4][organStock[3][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[3][0].index(time), "\tvalue : ", organStock[3][4][organStock[3][0].index(time)])
        # sp 기록이 있는 값만
        if time in organStock[4][0]:
            stocks[4][organStock[4][0].index(time)] = organStock[4][4][organStock[4][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[4][0].index(time), "\tvalue : ", organStock[4][4][organStock[4][0].index(time)])
        # 환율 기록이 있는 값만 
        if time in organExchange[0][0]:
            stocks[5][organStock[4][0].index(time)] = organExchange[0][1][organExchange[0][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[4][0].index(time), "\tvalue : ", organExchange[0][1][organExchange[0][0].index(time)])
    
    # print("kospi ?? : ", stocks[0])
    # print("kosdaq ?? : ", stocks[1])
    # print("nasdaq ?? : ", stocks[2])
    # print("djia ?? : ", stocks[3])
    # print("sp ?? : ", stocks[4])
    # print("ku ?? : ", stocks[5])

    # 0 값 변경
    for market in range(0, len(stocks)):
        for ind in range(0, len(stocks[market])):
            if stocks[market][ind] == 0:
                stocks[market][ind] = None

    # close 정보 리턴
    return stocks