import os
import openai
openai.api_key = "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"

messages = [
    {"role": "system", "content": "You're ChatGPT, an AI made by OpenAI"}
]

while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')