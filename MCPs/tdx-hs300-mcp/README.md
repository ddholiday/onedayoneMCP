# 沪深300指数60分钟数据下载服务 (tdx-hs300-mcp)

## 项目简介
tdx-hs300-mcp是一个基于Model Context Protocol (MCP)的服务，提供沪深300指数(510300)的60分钟K线数据下载功能。通过简单的API调用即可获取最新的市场数据。

## 功能说明
- 下载沪深300指数最新60分钟K线数据
- 下载指定天数内的60分钟K线历史数据
- 自动保存为CSV格式文件

## 使用方法
1. 确保已安装Python 3.7+和依赖库：
   ```bash
   pip install pytdx fastapi uvicorn
   ```

2. 启动MCP服务：
   ```bash
   mcp run MCP.py
   ```

3. 使用MCP工具调用服务：
   - 下载最新60分钟数据：
     ```python
     from mcp import use_mcp_tool
     
     result = use_mcp_tool(
         server_name="pytdx_hs300_mcp",
         tool_name="download_hs300_60min"
     )
     print(result)
     ```
   
   - 下载指定天数的历史数据(默认200天)：
     ```python
     result = use_mcp_tool(
         server_name="pytdx_hs300_mcp",
         tool_name="download_hs300_60min_ndays",
         arguments={"ndays": 200}
     )
     print(result)
     ```

## 配置说明
服务使用`config.toml`配置文件，主要配置项包括：
- `tdx.api_host`: 通达信行情服务器地址
- `tdx.api_port`: 通达信行情服务器端口
- `workspace.path`: 数据保存路径

## 注意事项
1. 需要连接通达信行情服务器获取数据
2. 数据获取受服务器限制，单次最多获取800条记录
3. 历史数据按需分批次获取

GitHub地址：
[https://github.com/ddholiday/onedayoneMCP/tree/main/MCPs/tdx-hs300-mcp](https://github.com/ddholiday/onedayoneMCP/tree/main/MCPs/tdx-hs300-mcp)
