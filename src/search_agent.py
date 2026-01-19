# search_agent.py

from agents import Agent, WebSearchTool, ModelSettings
from src.config import get_env_variable
from src.instructions import SEARCH_AGENT_INSTRUCTIONS

# Get MODEL and SEARCH_CONTEXT_SIZE from .env
MODEL = get_env_variable("MODEL")
SEARCH_CONTEXT_SIZE = get_env_variable("SEARCH_CONTEXT_SIZE")

search_agent = Agent(
    name="Search Agent",
    instructions=SEARCH_AGENT_INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size=SEARCH_CONTEXT_SIZE)],
    model=MODEL,
    model_settings=ModelSettings(tool_choice="required")
)