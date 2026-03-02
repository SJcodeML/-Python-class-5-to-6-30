# from google import genai
# from dotenv import load_dotenv
# import os


# load_dotenv()



# client = genai.Client()

# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='Tell me a story in 300 words.'
# )
# print(response.text)

# print(response.model_dump_json(
#     exclude_none=True, indent=4))





# ------------------------------













# import os
# from dotenv import load_dotenv
# from google import genai

# This reads your .env file and loads the key into the environment
# load_dotenv() 

# Now the client can automatically find the GEMINI_API_KEY
# client = genai.Client()
# while True :
#     user_input = input("Ask a question (or type 'exit' to quit): ")
#     if user_input.lower() == 'exit':
#         print("Goodbye!")
#         break
#     response = client.models.generate_content(
#         model='gemini-2.5-flash',
#         contents=user_input
#     )
#     print(response.text)

# print(response.model_dump_json(
#     exclude_none=True, indent=4))



# -----------------


import os
from dotenv import load_dotenv
from google import genai
import chainlit as cl

# Load environment variables from the .env file
load_dotenv() 

# Initialize the Gemini client automatically using the GEMINI_API_KEY
client = genai.Client()

@cl.on_chat_start
async def handle_chat_start():
    # Send welcome message to user
    await cl.Message(content="Hello! how can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    # This function triggers every time the user sends a message in the UI
    
    # 1. Send the user's message (message.content) to Gemini
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=message.content
    )
    
    # 2. Send Gemini's text response back to the Chainlit UI
    await cl.Message(
        content=response.text
    ).send()