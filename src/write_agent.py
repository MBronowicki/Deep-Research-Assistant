# write_agent.py

from pydantic import BaseModel, Field
from agents import Agent
from src.config import get_env_variable
from src.instructions import WRITER_AGENT_INSTRUCTIONS

MODEL = get_env_variable("MODEL")

class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")
    markdown_report: str = Field(description="The final report")
    follow_up_questions: list[str] = Field(description="Suggested topics to research further")

writer_agent = Agent(
    name="Writer Agent",
    instructions=WRITER_AGENT_INSTRUCTIONS,
    model=MODEL,
    output_type=ReportData,
)