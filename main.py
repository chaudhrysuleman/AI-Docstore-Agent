from langchain.agents import initialize_agent, AgentType
from docstore_setup import chat_llm
from tools import tools

# Initialize Agent
# The 'react-docstore' agent uses the ReAct framework to interact with a docstore (Wikipedia)
print("Initializing Docstore Agent...")
docstore_agent = initialize_agent(
    tools=tools, 
    llm=chat_llm, 
    agent=AgentType.REACT_DOCSTORE, 
    verbose=True,
    max_iterations=3,
    handle_parsing_errors=True
)

def main():
    query = "What is the capital of France?"
    print(f"\nQuery: {query}\n")
    try:
        docstore_agent.run(query)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
