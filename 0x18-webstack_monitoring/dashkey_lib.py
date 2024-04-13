#!/usr/bin/python3
"""
Get all dashboard lists returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = "558be1bca5a6471ec9f5ce4c4aa8845c"
configuration.api_key["appKeyAuth"] = "28c3c86bebf85fdcaae42808d31efce4f847867e"
configuration.api_key["site"] = "datadoghq.com"
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.list_dashboard_lists()

    print(response)


