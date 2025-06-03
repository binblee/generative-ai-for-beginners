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

no_recipes = input("No of recipes (for example, 5): ")
ingredients = input("Ingredients (for example, chicken, potatoes, and carrots): ") 
filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ") 
prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, {filter}"

print(f"Prompt:\n{prompt}\n")
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(
    model=model,
    messages=messages,
)

recipes = completion.choices[0].message.content
print(f"Recipes:\n{recipes}\n")

prompt_shoppinglist = f"{recipes} Produce a shopping list for the generated recipes and please don't include ingredients that I already have."
messages = [{"role": "user", "content": prompt_shoppinglist}]
print("Creating chat completion for shopping list...")
completion = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=1200,
)
shopping_list = completion.choices[0].message.content
print(f"Shopping list:\n{shopping_list}\n")

