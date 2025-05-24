# TDX API Programming Reference

## Configuration Setup

```python
import os
import toml

config_path = os.path.join(os.path.dirname(__file__), '../config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)
```

## API Connection

```python
from pytdx.hq import TdxHq_API

api = TdxHq_API()
api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
```

## get_security_bars Parameters

| Parameter | Description |
|-----------|-------------|
| category | K-line type: <br>0: 5min <br>1: 15min <br>2: 30min <br>3: 1hr <br>4: Daily <br>5: Weekly <br>6: Monthly <br>7: 1min <br>8: 1min <br>9: Daily <br>10: Quarterly <br>11: Yearly |
| market | Market code: <br>0: Shenzhen <br>1: Shanghai |
| stockcode | Security code |
| start | Pointer to last data (0 = today) |
| count | Number of K-lines to request (max 800) |

## Example Usage

```python
# Get 1-hour K-lines for stock 510300
data = api.get_security_bars(3, 1, '510300', 0, 800)
```

## Data Conversion

```python
# Convert to pandas DataFrame
df = api.to_df(data)
```

## Notes

- `start` and `count` parameters work together:
  - `start=0, count=800`: Get latest 800 K-lines
  - `start=800, count=800`: Get next 800 K-lines from position 800


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