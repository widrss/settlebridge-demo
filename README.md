# settlebridge-demo

Demonstration of SettleBridge agent settlement capabilities.

## Setup

```bash
# Create and activate conda environment
conda env create -f environment.yml
conda activate settlebridge_demo

# Or use pip in an existing env
pip install -e ".[dev]"
```

## Configuration

```bash
cp .env.example .env
# Edit .env with your API keys and settings
```

## Development

```bash
# Run smoke test
python smoke_test.py

# Run tests
pytest

# Lint
ruff check .

# Type check
mypy src/
```

## Project Structure

```
settlebridge-demo/
├── src/
│   └── settlebridge_demo/
│       ├── __init__.py
│       └── config.py
├── tests/
├── notebooks/
├── environment.yml
├── pyproject.toml
├── requirements.txt
├── smoke_test.py
├── .env.example
└── README.md
```
