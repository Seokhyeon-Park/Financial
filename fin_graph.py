from matplotlib import pyplot as plt
import fin_func
from openpyxl import load_workbook

# read Excel
wb = load_workbook(filename="fin.xlsx")

# sheet??
# print(wb.sheetnames)

# data??
kospi = wb['data']['A':'E']      # 코스피 [0]
kosdaq = wb['data']['H':'L']     # 코스닥 [1]
nasdaq = wb['data']['O':'S']     # 나스닥 [2]
djia = wb['data']['V':'Z']       # 다우지수 [3]
sp = wb['data']['AC':'AG']       # 스탠다드 푸어스 [4]
ku = wb['data']['AL':'AM']       # 환률(Korea - USA) [5]

# 시장
stocks = []
stocks.append(kospi)
stocks.append(kosdaq)
stocks.append(nasdaq)
stocks.append(djia)
stocks.append(sp)

# 데이터 가공
organStock = []
organExchange = []
for stock in stocks:
    # 코스피 코스닥 코스닥 나스닥 다우지수 스탠다드
    # Date Open High Low Close
    organStock.append(fin_func.stockDataOrgan(stock))
organExchange.append(fin_func.exchangeDataOrgan(ku))

# timeline setting
timeSetData = fin_func.timelineSet(organStock, organExchange)

# dimension
# organ[stock(market)][stock column][data]

timeline = organStock[4][0]
kospiClose = timeSetData[0]
kosdaqClose = timeSetData[1]
nasdaqClose = timeSetData[2]
djiaClose = timeSetData[3]
spClose = timeSetData[4]

# 그래프
plt.figure(figsize=(12, 7))
plt.scatter(timeline, kospiClose, s=1)
plt.scatter(timeline, kosdaqClose, s=1)
plt.scatter(timeline, nasdaqClose, s=1)
plt.scatter(timeline, djiaClose, s=1)
plt.scatter(timeline, spClose, s=1)
plt.show()