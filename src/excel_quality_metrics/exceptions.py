"""Custom exceptions for excel_quality_metrics."""

from __future__ import annotations


class ExcelQualityMetricsError(Exception):
    """Base exception for all ExcelQualityMetrics errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(ExcelQualityMetricsError):
    """Raised when the SDK is misconfigured."""


class ValidationError(ExcelQualityMetricsError):
    """Raised when input validation fails."""


class TimeoutError(ExcelQualityMetricsError):
    """Raised when an operation exceeds its time limit."""
