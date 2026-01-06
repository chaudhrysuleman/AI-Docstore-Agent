from langchain.agents.react.base import DocstoreExplorer
from langchain_community.docstore.wikipedia import Wikipedia
from langchain.tools import Tool
from docstore_setup import docstore


tools = [
    Tool(
        name="Search",
        func=docstore.search,
        description="Search for information in wikipedia"
    ),
    Tool(
        name="Lookup",
        func=docstore.lookup,
        description="Lookup information in wikipedia"
    )
]
