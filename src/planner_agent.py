# planner_agent.py

from pydantic import BaseModel, Field
from agents import Agent
from src.config import get_env_variable
from src.instructions import PLANNER_AGENT_INSTRUCTIONS

MODEL = get_env_variable("MODEL")

class WebSearchItem(BaseModel):
    reason: str = Field(description="You reasoning for why this search is important to the query.")
    query: str = Field(description="the search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web search terms to perform to best answer the query.")

planner_agent = Agent(
    name="Planner Agent",
    instructions=PLANNER_AGENT_INSTRUCTIONS,
    model=MODEL,
    output_type=WebSearchPlan,
)