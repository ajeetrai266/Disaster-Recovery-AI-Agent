from google.adk.agents import Agent
from .sub_agents.dr_plan.agent import dr_plan
from .sub_agents.dr_execution.agent import dr_execution
from .instruction import DR_INSTRUCTION

dr_agent = Agent(
    name = "dr_agent",
    model = "gemini-2.0-flash",
    description = "Disaster Recovery AI Agent",
    instruction = DR_INSTRUCTION,
    sub_agents=[dr_plan, dr_execution],
)

# Set as root agent
root_agent = dr_agent