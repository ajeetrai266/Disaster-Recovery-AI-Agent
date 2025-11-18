from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from .instruction import DR_EXECUTION_INSTRUCTION

dr_execution = Agent(
    name = "dr_execution",
    model = "gemini-2.0-flash",
    description = "DR Execution ai sub agent",
    instruction=DR_EXECUTION_INSTRUCTION,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@google-cloud/storage-mcp"],
            )
        ),
        MCPToolset(
            connection_params=StdioServerParameters(
                command="uvx",
                args=["mcp-kubernetes-server"],
                env={
                    "KUBECONFIG": "~/.kube/config"
                }
            )
        )
    ]
)