# excel_quality_metrics

Compute standard industrial quality KPIs from messy Excel exports with repeatable pipelines.

## Installation

```bash
pip install excel_quality_metrics
```

## Quick Start

```python
from excel_quality_metrics import ExcelQualityMetrics

instance = ExcelQualityMetrics()
result = instance.run()
print(result)
```

## Features

- Robust Excel ingestion (multi-sheets, merged headers, locale numbers/dates)
- Prebuilt KPI functions (FPY, scrap rate, defect PPM, Pareto by cause)
- Reproducible report outputs (cleaned dataset + KPI summary tables)

## API Reference

### `ExcelQualityMetrics`

#### Constructor

```python
ExcelQualityMetrics(options: ExcelQualityMetricsOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `ExcelQualityMetricsResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/excel_quality_metrics/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
