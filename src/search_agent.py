# search_agent.py

from config import get_env_variable
from agents import Agent, WebSearchTool, ModelSettings

# Get MODEL and SEARCH_CONTEXT_SIZE from .env
MODEL = get_env_variable("MODEL")
SEARCH_CONTEXT_SIZE = get_env_variable("SEARCH_CONTEXT_SIZE")

INSTRUCTIONS = {
    "You are a research assistant. Given a search term, you search the web for that term and "
    "produce a concise summary of the results. The summary must 2-3 paragraphs and less than 300 "
    "words. Capture the main points. Write succintly, no need to have complete sentences or good "
    "grammar. This will be consumed by someone synthesizing a report, so its vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary itself."
}

search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size=SEARCH_CONTEXT_SIZE)],
    model=MODEL,
    model_settings=ModelSettings(tool_choice="required")
)