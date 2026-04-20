from pathlib import Path

import pandas as pd

from mcp_servers.data_server.schemas import KPIComparisonResult, MetricDelta


class AnalyticsRepository:
    def __init__(self, csv_path: str) -> None:
        self.csv_path = Path(csv_path)

    def compare_weekly_kpis(
        self,
        current_week: str,
        previous_week: str,
    ) -> KPIComparisonResult:
        df = pd.read_csv(self.csv_path)

        current_row = df.loc[df["week"] == current_week]
        previous_row = df.loc[df["week"] == previous_week]

        if current_row.empty:
            raise ValueError(f"No data found for current_week={current_week}")
        if previous_row.empty:
            raise ValueError(f"No data found for previous_week={previous_week}")

        current = current_row.iloc[0]
        previous = previous_row.iloc[0]

        metric_names = ["sessions", "users", "conversions", "conversion_rate"]
        metrics: list[MetricDelta] = []

        for metric_name in metric_names:
            current_value = float(current[metric_name])
            previous_value = float(previous[metric_name])
            absolute_delta = current_value - previous_value

            if previous_value == 0:
                percent_delta = 0.0
            else:
                percent_delta = (absolute_delta / previous_value) * 100.0

            metrics.append(
                MetricDelta(
                    metric_name=metric_name,
                    current_value=current_value,
                    previous_value=previous_value,
                    absolute_delta=absolute_delta,
                    percent_delta=percent_delta,
                )
            )

        return KPIComparisonResult(
            current_week=current_week,
            previous_week=previous_week,
            metrics=metrics,
        )
