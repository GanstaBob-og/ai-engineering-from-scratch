from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")

response = client.chat.completions.create(
    model=MODEL,
    max_tokens=256,
    messages=[{"role": "user", "content": "Что такое нейросеть в одном предложении?"}]
)

print(response.choices[0].message.content)
