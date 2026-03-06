

import os
import re
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel

# Load environment variables from .env file
load_dotenv()

# API keys
gemini_api_key = os.getenv("GEMINI_API_KEY")
# openai_api_key = os.getenv("OPENAI_API_KEY")  # optional, for tracing or other paths

# Initialize Gemini/OpenAI provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.5-pro", openai_client=provider)

# Greeting detector
def is_greeting(text: str) -> bool:
    return bool(re.search(r'\b(hi|hello|hey|greetings|howdy|salutations)\b', text, re.IGNORECASE))

# Agent with flexible behavior
agent = Agent(
    name="Flexible Greeting Agent",
    instructions=(
           "You are a friendly assistant. Greet the user if they say hi. "
        "Otherwise, provide a helpful and concise answer to their question. "
        "If you don't know the answer, be honest and suggest that you don't have that capability."
    ),
    model=model,
)

def main():
    user_question = input("Please enter your question: ")
    if is_greeting(user_question):
        result = Runner.run_sync(agent, "Hello! How can I help you today?")
    else:
        result = Runner.run_sync(agent, user_question)
    print(result.final_output)

if __name__ == "__main__":
    main()