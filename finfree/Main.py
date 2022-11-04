import finlab
from finlab import data

finlab.login('uMJNaAFfdbSvG3Vf1VBzJ8oSfCQpJCH0L4a7tLU6MDA76/w2XnA1mPuJZUChEa6+#free')

# 獲取歷史資料
print('=====收盤價=====')
close = data.get('price:收盤價')
print(close)

print('=====公司資料=====')
company_info = data.get('company_main_business')
print(company_info)

# todo: bug here
print('=====技術指標計算=====')
rsi = data.indicator('RSI', timeperiod=14)
print(rsi)


print('=====限定上市櫃、類股=====')
# 限定只抓取上市櫃普通股(排除ETF、ETN、特別股、存託憑證)
data.set_universe(market='TSE_OTC', category='水泥')
close = data.get('price:收盤價')
print(close)



print('=====end=====')
