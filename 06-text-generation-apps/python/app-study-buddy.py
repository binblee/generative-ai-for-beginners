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

question = input("Ask your questions on python language to your study buddy: ")
prompt = f"""
"You're an expert on the Python language

    Whenever certain questions are asked, you need to provide response in below format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(
    model=model,
    messages=messages,
)

print(completion.choices[0].message.content)
