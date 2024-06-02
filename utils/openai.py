import openai
import os

class config_openAI():
    def set_api_credentials(self):
        openai.api_type = os.getenv('API_TYPE')
        openai.api_version = os.getenv('API_VERSION')
        openai.api_key = os.getenv('API_KEY')
        openai.api_base = os.getenv('API_BASE')

    def chat_completion(self, prompt):
        return openai.ChatCompletion.create(
            stop=["<|im_end|>", "<|im_start|>"],
            top_p=0.2,
            engine='openai-gpt4',
            messages=prompt,
            max_tokens=500,
            temperature=float('0.0'))
    
    def generate_image(self, prompt):
        return openai.Image.create(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
