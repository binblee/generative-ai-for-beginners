from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
model = "deepseek-v3"
# model = "deepseek-r1"

prompt = "Complete the following: Once upon a time, there was"
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(
    model=model,
    messages=messages,
)

print(completion.choices[0].message.content)
