# Docstore Agent

This project implements a **ReAct Docstore Agent** using [LangChain](https://github.com/langchain-ai/langchain). This agent is specifically designed to interact with document stores, such as **Wikipedia**, to find precise information and answer questions.

## Purpose

Use this agent when you need to:
- **Search and Lookup**: Perform specific search and lookup operations within a knowledge base.
- **Fact Integration**: Retrieve factual snippets from Wikipedia to answer user queries.
- **ReAct Reasoning**: Leverage the ReAct framework to reason about *how* to find the answer (e.g., "Search for X", then "Lookup Y").

## Tech Stack

- **Agent Type**: `react-docstore`.
- **Tools**: `Search` and `Lookup` (backed by Wikipedia).
- **LLM**: OpenAI `gpt-3.5-turbo`.

## Project Structure

- `main.py`: Entry point to run the agent.
- `tools.py`: Defines the Wikipedia tools.
- `docstore_setup.py`: Configuration and API key management.

## Setup

1. **Environment Variables**:
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r docstore-agent/requirements.txt
   ```

## How to Run

Execute the main script:
```bash
python docstore-agent/main.py
```

## Example Output

```text
> Entering new AgentExecutor chain...
Thought: I need to search for France and find its capital.
Action: Search[France]
Observation: France is a country located in...
Thought: The observation mentions Paris is the capital.
Action: Finish[Paris]

> Finished chain.
```
# AI-Docstore-Agent
