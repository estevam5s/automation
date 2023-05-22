import pytest
from app import app_routes

def test_app_routes():
    # Test Home route
    assert app_routes("Home") == "Rendered Home page"

    # Test Data Consult route
    assert app_routes("Data Consult") == "Rendered Data Consult page"

    # Test Charts route
    assert app_routes("Charts") == "Rendered Charts page"

    # Test Sales Statistics route
    assert app_routes("Sales Statistics") == "Rendered Sales Statistics page"

    # Test Profit Analysis route
    assert app_routes("Profit Analysis") == "Analyzed data for Profit Analysis"

    # Test Financial Reports route
    assert app_routes("Financial Reports") == "Rendered Financial Reports page"

    # Test Trend Analysis route
    assert app_routes("Trend Analysis") == "Rendered Trend Analysis page"

    # Test Sales History route
    assert app_routes("Sales History") == "Rendered Sales History page"

    # Test Stock Management route
    assert app_routes("Stock Management") == "Rendered Stock Management page"

    # Test Exit route
    assert app_routes("Exit") == "Exited the system"
