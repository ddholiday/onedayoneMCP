from pytdx.hq import TdxHq_API
import os
import toml

config_path = os.path.join(os.path.dirname(__file__), '../config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)

api = TdxHq_API()
api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
# get_security_bars 参数说明：周期类型，市场，股票代码，起始位置，数量
"""
category->

K线种类
0 5分钟K线 1 15分钟K线 2 30分钟K线 3 1小时K线 4 日K线
5 周K线
6 月K线
7 1分钟
8 1分钟K线 9 日K线
10 季K线
11 年K线
market -> 市场代码 0:深圳，1:上海

stockcode -> 证券代码;

start -> 最后一条数据对应的指针; 0代表的是今天的指针;

count -> 用户要请求的 K 线数目，最大值为 800

最后两个参数可以放在一起理解。
start=0, count=800 代表的是最近800根K线。
start=800, count=800 代表的是，从后往前数第800根K线开始，往前推800根K线。
以此类推。
get_all_day_data可参考
from pytdx.hq import  TdxHq_API
api=TdxHq_API()
def get_all_day_data():
   with api.connect():
        data=[]
        for i in range(10):
              data+=api.get_security_bars(9,0,'000001',(9-i)*800,800)
    print(api.to_df(data))
"""
data = api.get_security_bars(3, 1, '510300', 0, 800)
df = api.to_df(data)
print(df)
api.disconnect()

# print(df)