"""Type definitions for excel_quality_metrics."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ExcelQualityMetricsOptions:
    """Configuration options for ExcelQualityMetrics.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: Robust Excel ingestion (multi-sheets, merged headers, locale numbers/dates)
        feature_2: Configuration for: Prebuilt KPI functions (FPY, scrap rate, defect PPM, Pareto by cause)
        feature_3: Configuration for: Reproducible report outputs (cleaned dataset + KPI summary tables)
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None


@dataclass
class ExcelQualityMetricsResult:
    """Result returned by ExcelQualityMetrics operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
