import os
import warnings
from dotenv import load_dotenv, find_dotenv
from langchain_openai import OpenAI
from langchain.agents.react.base import DocstoreExplorer
from langchain_community.docstore.wikipedia import Wikipedia

# Suppress deprecation warnings for cleaner output
warnings.filterwarnings('ignore')

load_dotenv(find_dotenv())

# Ensure API keys are set
if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in environment.")

llm_model = "gpt-3.5-turbo"
chat_llm = OpenAI(temperature=0.7)

# Initialize Wikipedia docstore
docstore = DocstoreExplorer(Wikipedia())