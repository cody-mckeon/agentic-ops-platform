from mcp_servers.data_server.repository import AnalyticsRepository


def test_compare_weekly_kpis():
    repo = AnalyticsRepository("data/analytics/weekly_kpis.csv")
    result = repo.compare_weekly_kpis(
        current_week="2026-04-13",
        previous_week="2026-04-06",
    )

    metrics = {m.metric_name: m for m in result.metrics}

    assert metrics["sessions"].current_value == 11850.0
    assert metrics["sessions"].previous_value == 10200.0
    assert round(metrics["sessions"].percent_delta, 2) == 16.18
