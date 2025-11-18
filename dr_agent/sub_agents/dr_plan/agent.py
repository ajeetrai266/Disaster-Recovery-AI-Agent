from google.adk.agents import Agent
from .tools.get_corpus import get_corpus_info
from .tools.list_corpus import list_corpora
from .tools.create_corpus import create_corpus
from .tools.delete_corpus import delete_corpus
from .tools.add_document import add_data
from .tools.delete_document import delete_document
from .tools.query_rag import rag_query
from .instruction import DR_PLAN_RAG_INSTRUCTION

dr_plan = Agent(
    name = "dr_plan",
    model = "gemini-2.0-flash",
    description = "DR Plan ai sub agent",
    instruction=DR_PLAN_RAG_INSTRUCTION,
    tools=[
        get_corpus_info,
        list_corpora,
        create_corpus,
        delete_corpus,
        add_data,
        delete_document,
        rag_query,
    ],
)