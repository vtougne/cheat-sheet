from mcp.server import MCPServer

# Static weather data for demonstration
STATIC_ALERTS = {
    "NY": "No active alerts for NY.",
    "CA": "Severe Thunderstorm Warning in CA. Stay indoors.",
}

STATIC_FORECASTS = {
    "40.7128,-74.0060": "Tomorrow: Sunny, 75°F, wind NW 5 mph.",
    "34.0522,-118.2437": "Rainy, 60°F, wind SE 10 mph.",
}

# Create MCP server instance
mcp = MCPServer("weather_demo")

# Tool to get alerts for a state
@mcp.tool()
async def get_alerts(state: str) -> str:
    """Return static weather alert for a US state."""
    return STATIC_ALERTS.get(state.upper(), f"No alerts for {state}.")

# Tool to get forecast for a location
@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Return static forecast for a latitude/longitude pair."""
    key = f"{latitude},{longitude}"
    return STATIC_FORECASTS.get(key, "No forecast data for this location.")

if __name__ == "__main__":
    # Run the server over stdio transport
    mcp.run(transport="stdio")
