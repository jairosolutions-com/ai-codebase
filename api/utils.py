from groq import Groq
import os

client = Groq(
    api_key=os.getenv('API_KEY')
)

def send_code(code):
    chat_completion = client.chat.completions.create(
    messages=[
            {
                "role": "system",
                "content": "You are going to search google."
             },
            {
                "role": "user",
                "content": f"Tell me a short statement for this word? {code}"
                },

    ],
    model="gemma-7b-it",
    )
    res = (chat_completion.choices[0].message.content)
    return res