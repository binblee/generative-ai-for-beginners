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

persona = input("Tell me the historical character I want to be: ")
question = input("Ask your question about the historical character: ")
prompt = f"""
You are going to play as a historical character {persona}. 

Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond the accurate answer only. Don't create content yourself. If you don't know something, tell that you don't remember.

Provide answer for the question: {question}
"""

messages = [{"role": "user", "content": prompt}] 
completion = client.chat.completions.create(
    model=model,
    messages=messages,
)

print(completion.choices[0].message.content)
