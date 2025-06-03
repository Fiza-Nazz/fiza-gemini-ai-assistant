import chainlit as cl
import google.generativeai as genai

genai.configure(api_key="AIzaSyASgosNDGxctD1WdaTp1FC107fETsFz2l4")
model = genai.GenerativeModel("gemini-1.5-flash")

@cl.on_chat_start
async def start():
    await cl.Message(content="""
# 👋 Welcome to **Fiza's AI Assistant** ♥ 
I'm here to help you with:

- 🧠 AI blog topic suggestions  
- ✍️ Writing blog content  
- ✅ Grammar and clarity checks  
- 🤖 General AI queries  

_Just type your request below!_
""").send()

@cl.on_message
async def main(message: cl.Message):
    content = message.content.lower()

    if "topic" in content:
        prompt = "Suggest an AI blog topic for LinkedIn audience"
    elif "write" in content:
        prompt = "Write a blog on 'How AI is helping students in 2025'"
    elif "grammar" in content:
        prompt = f"Check grammar and improve clarity: {message.content}"
    else:
        prompt = message.content

    response = model.generate_content(prompt)
    await cl.Message(content=response.text).send()
