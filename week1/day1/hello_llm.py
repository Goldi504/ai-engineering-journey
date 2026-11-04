from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not found")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

role = "user"
prompt = "Do you know Goldi Kumari?"

message = {
    "role": role,
    "content": prompt
}

messages = [message]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)
