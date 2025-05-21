from mcp.server.fastmcp import FastMCP
from MCP import save_to_csv

def test_save_hs300():
    save_to_csv('000300', 'workspace/tdx/data/300.csv')
    print("HS300 data saved successfully")

if __name__ == '__main__':
    test_save_hs300()
