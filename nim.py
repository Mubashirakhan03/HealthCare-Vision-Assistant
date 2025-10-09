import os
import requests
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv("var.env")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")  # Read API key from .env
if not NVIDIA_API_KEY:
    raise RuntimeError("NVIDIA_API_KEY not found in var.env!")  # Error agar key missing ho

# Stream mode
stream = True

# Read and encode image
with open("h.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode()
assert len(image_b64) < 180_000, "To upload larger images, use the assets API (see docs)"

# Headers for the request
headers = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Accept": "text/event-stream" if stream else "application/json"
}

# API URL
invoke_url = "https://ai.api.nvidia.com/v1/gr/meta/llama-3.2-11b-vision-instruct/chat/completions"

# Payload
payload = {
    "model": 'meta/llama-3.2-11b-vision-instruct',
    "messages": [
        {
            "role": "user",
            "content": f'What is in this image? <img src="data:image/png;base64,{image_b64}" />'
        }
    ],
    "max_tokens": 512,
    "temperature": 1.00,
    "top_p": 1.00,
    "stream": stream
}

# Send request
response = requests.post(invoke_url, headers=headers, json=payload)

# Handle response
if stream:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
else:
    print(response.json())
