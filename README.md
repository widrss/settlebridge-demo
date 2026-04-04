# settlebridge-demo

Interactive Streamlit demo illustrating the difference between unverified and SettleBridge-verified agent-to-agent transactions.

## What's in the Demo

**Tab A — Without SettleBridge**
A Buyer Agent commissions a market research task. The Worker Agent returns a low-quality, hallucinated response. Payment is sent automatically the moment the response arrives — no verification, no quality check, no recourse. A running cost ticker shows the wasted spend.

**Tab B — With SettleBridge**
The same task, routed through the SettleBridge trust layer. The Worker Agent's track record is verified before assignment. Payment is held in escrow. The deliverable is scored against the acceptance criteria before funds are released. Use the **Good Agent / Bad Agent toggle** to see both outcomes:
- Good Agent → delivery verified, payment released, audit trail recorded
- Bad Agent → delivery rejected, payment returned to buyer, agent score updated

## Setup

```bash
# Create and activate the conda environment
conda env create -f environment.yml
conda activate settlebridge_demo
```

Or install into an existing Python 3.11+ environment:

```bash
pip install -e ".[dev]"
pip install streamlit>=1.35.0
```

## Run the Demo

```bash
conda activate settlebridge_demo
streamlit run streamlit_app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Configuration

```bash
cp .env.example .env
# Edit .env with your API keys (not required for the Streamlit demo)
```

## Development

```bash
# Smoke test
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
├── streamlit_app.py          # Entry point — page config and tab routing
├── app/
│   ├── demo_a.py             # Tab A: Without SettleBridge (5-step sequence)
│   ├── demo_b.py             # Tab B: With SettleBridge (7-step sequence)
│   ├── components.py         # Shared UI components, panels, badges, CSS
│   └── simulation.py         # Static demo data — task spec, agents, deliverables
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

## License

MIT
