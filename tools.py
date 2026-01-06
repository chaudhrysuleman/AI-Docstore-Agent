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
