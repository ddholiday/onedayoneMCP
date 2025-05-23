from pytdx.hq import TdxHq_API
import os
import toml

config_path = os.path.join(os.path.dirname(__file__), '../config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)

api = TdxHq_API()
api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
data = api.get_security_bars(7, 60, '510300', 0, 100)
df = api.to_df(data)
print(df)
data = api.get_security_bars(7, 60, '510300', 100, 100)
df = api.to_df(data)
print(df)
api.disconnect()
# with api.connect(config['tdx']['api_host'], config['tdx']['api_port']):
#     # 参数说明：周期类型（7=分钟线），分钟数（60），股票代码，起始位置，数量
#     data = api.get_security_bars(7, 60, '000001', 0, 100)
#     df = api.to_df(data)

# print(df)