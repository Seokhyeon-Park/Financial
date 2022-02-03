from matplotlib import pyplot as plt

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

# 시간 좌표 설정 (시장, 환율)
def timelineSet(organStock, organExchange):
    # 날짜 기준 배열 생성
    timeline = organStock[3][0]

    # stocks
    # 코스피 [0], 코스닥 [1], 다우존스 [2], S&P 500 [3], 나스닥	[4], 환율(Korea - USA) [5]
    # 환율(Korea - USA) : organExchange
    stocks = []
    for st in range(0, 6):
        print("st : ", st)
        stocks.append([])
        for os in range(0, len(timeline)):
            stocks[st].append(0)

    print("stocks ??", len(stocks))
    print("stocks date ??", len(stocks[0]))

    for time in timeline:
        # kospi에 기록이 있는 값만
        if time in organStock[0][0]:
            stocks[0][timeline.index(time)] = organStock[0][4][organStock[0][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[0][0].index(time), "\tvalue : ", organStock[0][4][organStock[0][0].index(time)])
        # kosdaq 기록이 있는 값만
        if time in organStock[1][0]:
            stocks[1][timeline.index(time)] = organStock[1][4][organStock[1][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[1][0].index(time), "\tvalue : ", organStock[1][4][organStock[1][0].index(time)])
        # djia 기록이 있는 값만
        if time in organStock[2][0]:
            stocks[2][timeline.index(time)] = organStock[2][4][organStock[2][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[2][0].index(time), "\tvalue : ", organStock[2][4][organStock[2][0].index(time)])
        # sp 기록이 있는 값만
        if time in organStock[3][0]:
            stocks[3][timeline.index(time)] = organStock[3][4][organStock[3][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[3][0].index(time), "\tvalue : ", organStock[3][4][organStock[3][0].index(time)])
        # nasdaq 기록이 있는 값만
        if time in organStock[4][0]:
            stocks[4][timeline.index(time)] = organStock[4][4][organStock[4][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[4][0].index(time), "\tvalue : ", organStock[4][4][organStock[4][0].index(time)])
        # 환율 기록이 있는 값만 
        if time in organExchange[0][0]:
            stocks[5][timeline.index(time)] = organExchange[0][1][organExchange[0][0].index(time)]
            # print("time : ", time, "\tindex : ", organStock[4][0].index(time), "\tvalue : ", organExchange[0][1][organExchange[0][0].index(time)])
    
    print("kospi ?? : ", stocks[0][0])
    print("kosdaq ?? : ", stocks[1][0])
    print("djia ?? : ", stocks[2][0])
    print("sp ?? : ", stocks[3][0])
    print("nasdaq ?? : ", stocks[4][0])
    print("ku ?? : ", stocks[5][0])

    # 0 값 변경
    for market in range(0, len(stocks)):
        for ind in range(0, len(stocks[market])):
            if stocks[market][ind] == 0:
                stocks[market][ind] = None

    # close 정보 리턴
    return stocks

# figure 설정 및 저장 (x축, y축[배열], label[배열], x축 값 간격, y축 값 표기 간격)
def figureSet(timeline, markets, labels, difX, difY):
    # 그래프
    plt.figure(figsize=(48, 30))

    # 그래프 그리기
    for market, label in zip(markets, labels):
        plt.plot(timeline, market, label=label)
        plt.legend()

        # difX 일 마다 지수 값 표시
        for i in range(0, len(timeline), difX):
            # x, y, 값 표기 위치, ...
            if market[i] is not None and market[i-difX] is not None:
                if i > 0:
                        plt.text(timeline[i], market[i] + difY, round(market[i], 2), horizontalalignment='center', verticalalignment='bottom', size = 12)
                        plt.plot(timeline[i], market[i], 'ro')
                        
        # 마지막 날 무조건 표기 (휴장 및 휴일)
        for i in range(1, 10, 1):
            if market[-i] is not None:
                plt.text(timeline[-i], market[-i] + difY, round(market[-i], 2), horizontalalignment='center', verticalalignment='bottom', size = 12)
                plt.plot(timeline[-i], market[-i], 'ro')
                break

    # 저장
    if len(labels)>1:
        label = ""
        for text in labels:
            label = label + "_" + text
        plt.savefig(label+'.png')
    else:    
        plt.savefig(labels[0]+'.png')
    plt.cla()