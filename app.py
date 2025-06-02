import chainlit as cl
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyASgosNDGxctD1WdaTp1FC107fETsFz2l4")

model = genai.generativemodel("models/gemini-1.5-flash")

@cl.on_message
async def main(message: cl.Message):
    # Basic logic
    if "topic" in message.content.lower():
        prompt = "Suggest an AI blog topic for LinkedIn audience"
    elif "write" in message.content.lower():
        prompt = "Write a blog on 'How AI is helping students in 2025'"
    elif "grammar" in message.content.lower():
        prompt = f"Check grammar and improve clarity: {message.content}"
    else:
        prompt = message.content

    response = model.generate_content(prompt)
    await cl.Message(content=response.text).send()
