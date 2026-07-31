"""
excel_quality_metrics - Compute standard industrial quality KPIs from messy Excel exports with repeatable pipelines.
"""

__version__ = "0.1.0"

from .robust_excel_ingestion_multish import ExcelQualityMetrics
from .types import ExcelQualityMetricsOptions, ExcelQualityMetricsResult
from .exceptions import ExcelQualityMetricsError, ConfigurationError, ValidationError

__all__ = [
    "ExcelQualityMetrics",
    "ExcelQualityMetricsOptions",
    "ExcelQualityMetricsResult",
    "ExcelQualityMetricsError",
    "ConfigurationError",
    "ValidationError",
]
