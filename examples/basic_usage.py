#!/usr/bin/env python3
"""Basic usage example for excel_quality_metrics."""

from excel_quality_metrics import ExcelQualityMetrics, ExcelQualityMetricsOptions


def main() -> None:
    # Create with default options
    instance = ExcelQualityMetrics()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = ExcelQualityMetricsOptions(verbose=True)
    instance = ExcelQualityMetrics(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
