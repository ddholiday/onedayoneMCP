# TDX API Programming Reference

## Configuration Setup

```python
import os
import toml

config_path = os.path.join(os.path.dirname(__file__), '../config.toml')
with open(config_path, 'r') as f:
    config = toml.load(f)
```

## API Connection

```python
from pytdx.hq import TdxHq_API

api = TdxHq_API()
api.connect(config['tdx']['api_host'], config['tdx']['api_port'])
```

## get_security_bars Parameters

| Parameter | Description |
|-----------|-------------|
| category | K-line type: <br>0: 5min <br>1: 15min <br>2: 30min <br>3: 1hr <br>4: Daily <br>5: Weekly <br>6: Monthly <br>7: 1min <br>8: 1min <br>9: Daily <br>10: Quarterly <br>11: Yearly |
| market | Market code: <br>0: Shenzhen <br>1: Shanghai |
| stockcode | Security code |
| start | Pointer to last data (0 = today) |
| count | Number of K-lines to request (max 800) |

## Example Usage

```python
# Get 1-hour K-lines for stock 510300
data = api.get_security_bars(3, 1, '510300', 0, 800)
```

## Data Conversion

```python
# Convert to pandas DataFrame
df = api.to_df(data)
```

## Notes

- `start` and `count` parameters work together:
  - `start=0, count=800`: Get latest 800 K-lines
  - `start=800, count=800`: Get next 800 K-lines from position 800
