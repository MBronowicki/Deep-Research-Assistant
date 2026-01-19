# planner_agent.py

from pydantic import BaseModel, Field
from agents import Agent
from config import get_env_variable

HOW_MANY_SEARCH_TERMS = int(get_env_variable("HOW_MANY_SEARCH_TERMS"))
MODEL = get_env_variable("MODEL")

INSTRUCTIONS = f"You are a helpful researcher assistant. Given a query, come up with a set of web search terms \
to perform to best answer the query. Output {HOW_MANY_SEARCH_TERMS} terms to query for."

class WebSearchItem(BaseModel):
    reason: str = Field(description="You reasoning for why this search is important to the query.")
    query: str = Field(description="the search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web search terms to perform to best answer the query.")

planner_agent = Agent(
    name="Planner Agent",
    instructions=INSTRUCTIONS,
    model=MODEL,
    output_type=WebSearchPlan,
)