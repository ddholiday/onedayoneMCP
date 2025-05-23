from mcp.server.fastmcp import FastMCP
import toml
import os
from pytdx.hq import TdxHq_API
import pandas as pd
from datetime import datetime

mcp = FastMCP("沪深300指数60分钟数据下载服务")

# 加载配置文件
config_path = os.path.join(os.path.dirname(__file__), 'config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)

def get_hs300_60min_data():
    """获取沪深300指数60分钟K线数据"""
    api = TdxHq_API()
    api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
    df = None
    if api:
        # 获取沪深300指数代码
        data = api.get_security_bars(3, 1, '510300', 0, 800)
        df = api.to_df(data)
        api.disconnect()
    return df
        

@mcp.tool()
def download_hs300_60min():
    """下载沪深300指数60分钟数据"""
    df = get_hs300_60min_data()
    if df is not None:
        # 生成带时间戳的文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"hs300_60min_{timestamp}.csv"
        save_path = os.path.join(config["workspace"]["path"], "tdx", "data", filename)
        
        # 确保目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 保存CSV文件
        df.to_csv(save_path, index=False)
        return "数据下载完成，文件路径：" + save_path
    else:
        return "数据获取失败，请检查网络连接或代码逻辑。"

if __name__ == '__main__':
    print(download_hs300_60min())
