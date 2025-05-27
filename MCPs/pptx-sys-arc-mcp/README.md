# PPTX System Architecture MCP

This MCP server provides functionality to generate system architecture diagrams in PPTX format from Markdown input.

## Features

- Convert Markdown hierarchy to PPTX architecture diagrams
- Support for custom styling of diagram elements
- Automatic layout of architecture components
- Support for multiple hierarchy levels (1-3 levels)
- Output to PPTX format for easy editing

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install python-pptx toml
   ```
3. Configure the MCP by editing `config.toml`

## Usage

### Basic Usage

```python
from mcp.server.fastmcp import FastMCP
from pptx_sys_arc_mcp import generate_architecture_diagram

# Initialize MCP
mcp = FastMCP("pptx-generator")

# Register the tool
@mcp.tool()
def generate_architecture(md_input: str, style_spec: str = "") -> bytes:
    return generate_architecture_diagram(md_input, style_spec)

# Start the MCP server
mcp.start()
```

### Input Format

The input should be a Markdown string with hierarchy represented by heading levels:

```markdown
# Level 1
## Level 2
### Level 3
## Level 2
# Level 1
```

### Output

The MCP will generate a PPTX file with the architecture diagram and return the file path.

## Configuration

Edit `config.toml` to configure:

```toml
[workspace]
path = "path/to/output/directory"
```

## API Reference

### `generate_architecture_diagram(md_input: str, style_spec: str = "") -> str`

Generate PPTX architecture diagram from Markdown input.

Parameters:
- `md_input`: Markdown string representing the architecture hierarchy
- `style_spec`: Optional JSON string specifying styling rules

Returns:
- Path to generated PPTX file

## Example

```python
input_md = """
# Application Layer
## Service 1
### Component A
### Component B
## Service 2
# Infrastructure
## Database
## Cache
"""

result = generate_architecture_diagram(input_md)
print(f"Generated PPTX: {result}")
```

## License

MIT
