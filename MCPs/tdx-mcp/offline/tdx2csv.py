import os
import toml
from pytdx.reader import TdxLCMinBarReader

config_path = os.path.join(os.path.dirname(__file__), '../config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)

tdx_install_path = config['tdx']['local_path']

# 构建数据目录路径（示例股票代码：sh510300）
stock_code = "sh510300"
data_dir = os.path.join(tdx_install_path, "vipdoc", "sh", "minline")
data_file = os.path.join(data_dir, f"{stock_code}.lc1")

# 验证路径有效性
if not os.path.exists(data_file):
    raise FileNotFoundError(f"数据文件 {data_file} 不存在")

# 使用pytdx读取分钟线数据
reader = TdxLCMinBarReader()
df = reader.get_df(data_file)
print(df.tail())
