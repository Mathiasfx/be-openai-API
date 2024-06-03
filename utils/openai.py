import os
from openai import AzureOpenAI
import json

class config_openAI():
    def chat_completion(self, prompt):
        client = AzureOpenAI(
            api_version="2024-02-01",
            azure_endpoint=os.getenv("API_BASE"),
            api_key=os.getenv("API_KEY"),
        )
        result = client.chat.completions.create(
            model='openai-gpt4',
            n=1,
            messages=prompt,
            stop=["<|im_end|>", "<|im_start|>"],
            top_p=0.2,
            max_tokens=500
        ).model_dump_json()
        return json.loads(result)
    
    def generate_image(self, prompt):
        client = AzureOpenAI(
            api_version="2024-02-01",
            azure_endpoint=os.getenv("API_BASE"),
            api_key=os.getenv("API_KEY"),
        )
        result = client.images.generate(
            model="acuello-dall-3",
            prompt=prompt,
            size="1024x1024",
            n=1
        ).model_dump_json()
        return json.loads(result)
