# Python创建MCP服务器指南

## 1. 基本概念
MCP (Model Control Protocol)服务器用于管理模型服务，提供统一的接口调用方式。

## 2. 创建步骤

### 2.1 导入依赖
```python
from mcp.server.fastmcp import FastMCP
import toml
import os
```

### 2.2 初始化MCP实例
```python
mcp = FastMCP("服务描述信息")
```

### 2.3 加载配置文件
```python
config_path = os.path.join(os.path.dirname(__file__), 'config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)
```

### 2.4 定义工具函数
```python
def process_data(data):
    """数据处理函数"""
    # 处理逻辑
    return processed_data
```

### 2.5 注册工具
```python
@mcp.tool()
def service_api(input_data):
    """服务接口"""
    result = process_data(input_data)
    return {"result": result}
```

## 3. 配置示例
config.toml文件示例：
```toml
[server]
host = "0.0ec2.0.0.1"
port = 8080
```

## 4. 启动服务
```python
if __name__ == '__main__':
    mcp.start()
```

## 5. 最佳实践
- 使用类型注解
- 添加日志记录
- 实现错误处理
- 编写单元测试
