from mcp.server.fastmcp import FastMCP
import pytdx
import pandas as pd

@FastMCP.tool()
def get_stock_data(stock_code: str) -> pd.DataFrame:
    """Get stock data from TDX API"""
    api = pytdx.connect(host='124.71.163.43', port=7709)
    data = api.get_security_quotes([stock_code])
    return pd.DataFrame(data)

@FastMCP.tool()
def save_to_csv(stock_code: str, file_path: str) -> None:
    """Save stock data to CSV file"""
    data = get_stock_data(stock_code)
    data.to_csv(file_path, index=False)
