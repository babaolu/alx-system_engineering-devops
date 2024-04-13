#!/usr/bin/python3
"""
Get all dashboard lists returns "OK" response
"""
import sys
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboard_lists_api import DashboardListsApi

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = sys.argv[1]
configuration.api_key["appKeyAuth"] = sys.argv[2]
configuration.api_key["site"] = "datadoghq.com"
with ApiClient(configuration) as api_client:
    api_instance = DashboardListsApi(api_client)
    response = api_instance.list_dashboard_lists()

    print(response)


