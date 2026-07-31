"""Tests for excel_quality_metrics."""

from excel_quality_metrics import ExcelQualityMetrics, ExcelQualityMetricsOptions


class TestExcelQualityMetrics:
    def test_create_instance_with_defaults(self) -> None:
        instance = ExcelQualityMetrics()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = ExcelQualityMetricsOptions(verbose=True)
        instance = ExcelQualityMetrics(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = ExcelQualityMetrics()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = ExcelQualityMetrics()
        result = instance.run()
        assert result.error is None
