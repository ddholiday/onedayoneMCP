参考@/MCPs/tdx-mcp/tdx-examples.md 和@/mcp_codes.md 编写@/MCPs/tdx-hs300-mcp/MCP.py 
我希望大模型可以做到：
用户提问为：请为我下载最近的沪深300的60分钟级别数据。
回答：好的，数据已经保存到workspace里。文件名为xxxx.csv

而@/MCPs/tdx-hs300-mcp/MCP.py 的目标就是为大模型提供工具，让上述需求可以被响应。