import chainlit as cl 

@cl.on_message
async def main(message: cl.Message):
    response = f"your last message was : {message.content}"

    await cl.Message(content=response).send()


    


if __name__ == "__main__":
    main()
