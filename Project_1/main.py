import requests
from dotenv import load_dotenv
import json
import os
import chainlit as cl


load_dotenv()

api_key = os.getenv("OPEN_ROUTER_API_KEY")
base_url = "https://openrouter.ai/api/v1/chat/completions"
model = "deepseek/deepseek-chat-v3-0324:free"

response = requests.post(
    url=base_url,
    headers={
        "Authorization":f"Bearer {api_key}"
    },
    data = json.dumps(
        {
            "model":model,
            "messages":[
                {
                    "role":"user",
                    "content":"Hello"
                }
            ]
        }
    )
)




@cl.on_message
async def handle_message(message:cl.Message):
    response = requests.post(
        url=base_url,
        headers={
            "Authorization":f"Bearer {api_key}"
        },
        data = json.dumps(
            {
                "model":model,
                "messages":[
                    {
                        "role":"user",
                        "content":message.content
                    }
                ]
            }
        )
    )
    result = response.json()
    data = result['choices'][0]['message']['content']

    await cl.Message(content=data).send()
