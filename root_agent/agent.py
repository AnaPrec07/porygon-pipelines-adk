from google.adk.agents import Agent

from root_agent.tools.bigquery import get_bigquery_toolset

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are a helpful AI assistant designed to provide accurate "
        "and useful information."
    ),
    tools=[get_bigquery_toolset()],
)
