import os
import urllib.request
import json
from dotenv import load_dotenv

load_dotenv()
url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.getenv("DEEPSEEK_API_KEY")}",
}
body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "deepseek-chat"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "Что такое нейросеть в одном предложении?"}],
}).encode()
req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
    print(result["choices"][0]["message"]["content"])
