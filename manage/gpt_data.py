from openai import OpenAI
import sys

def get(state):
    client = OpenAI(
        api_key="211fa21c08be45e86847eff9d61cb4e6bc7374995f3b7ac894d34f2395a415dd",
        base_url='https://llm.mdb.ai/')
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'user', 'content': state}
        ],
        stream=False
    )

    return completion.choices[0].message.content
