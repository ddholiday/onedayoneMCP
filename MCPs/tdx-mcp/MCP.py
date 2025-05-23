from mcp.server.fastmcp import FastMCP
from pytdx.hq import TdxHq_API
import pandas as pd
import toml
import os

config_path = os.path.join(os.path.dirname(__file__), 'config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)

mcp = FastMCP("mcp for stock data")

def get_stock_data(stock_code: str) -> pd.DataFrame:
    """Get stock data from TDX API"""
    api = TdxHq_API()
    # 使用with语法自动管理连接
    api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
    # 获取数据并转换为DataFrame
    data = api.get_security_quote([stock_code])
    return api.to_df(data)

def get_security_quotes(stock_list: list) -> pd.DataFrame:
    """Get real-time quotes for multiple stocks from TDX API
    
    Args:
        stock_list: List of tuples containing (market_code, stock_code)
    """
    api = TdxHq_API()
    try:
        api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
        quotes = api.get_security_quote([(market, stock) for market, stock in stock_list])
        return api.to_df(quotes)
    finally:
        api.disconnect()

def get_security_quotes(stock_list: list) -> pd.DataFrame:
    """Get real-time quotes for multiple stocks from TDX API
    
    Args:
        stock_list: List of tuples containing (market_code, stock_code)
    """
    api = TdxHq_API()
    try:
        api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
        quotes = api.get_security_quotes([(market, stock) for market, stock in stock_list])
        return api.to_df(quotes)
    finally:
        api.disconnect()

def get_multiple_stock_quotes(stock_list: list) -> pd.DataFrame:
    """Get real-time quotes for multiple stocks from TDX API
    
    Args:
        stock_list: List of tuples containing (market_code, stock_code)
    """
    api = TdxHq_API()
    try:
        api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
        quotes = api.get_security_quote([(market, code) for market, code in stock_list])
        return api.to_df(quotes)
    finally:
        return "数据获取失败"
        api.disconnect()

@mcp.tool()
def save_to_csv(stock_code: str, file_path: str) -> None:
    """Save stock data to CSV file"""
    data = get_stock_data(stock_code)
    data.to_csv(file_path, index=False)

# 创建新的mcp工具。输入为股票代码，开始时间，结束时间，mcp会把对应的股票数据保存到workspace下。
@mcp.tool()
def save_to_csv_api(stock_code: str, start_date: str, end_date: str) -> None:
    """Save stock data to CSV file in workspace directory
    
    Args:
        stock_code: Stock code to fetch data for (e.g. '000001')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
    """
    data = get_stock_data(stock_code)
    # Filter data by date range
    data = data[(data['date'] >= start_date) & (data['date'] <= end_date)]
    # Save to workspace directory
    # 从config.toml中读取workspace目录
    workspace_dir = config['workspace']['directory']
    output_path = os.path.join(workspace_dir, f"{stock_code}_{start_date}_{end_date}.csv")
    data.to_csv(output_path, index=False)
    return f"数据下载成功，保存在了：{output_path}"



# 编写main函数，测试所有功能
if __name__ == '__main__':
    # 测试单只股票数据下载
    # save_to_csv_api('000300', '2023-01-01', '2023-01-31')
    
    # 测试多只股票实时行情查询
    stocks = [
        (0, '000001'),  # 深圳市场
        (1, '600000')
    ]
    quotes = get_security_quotes(stocks)
    print("多只股票实时行情:")
    print(quotes)
