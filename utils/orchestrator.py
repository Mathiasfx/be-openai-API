from utils.openai import config_openAI

def get_answer(history):
    _prompt = open("utils/prompt_instructions_chat.prompt", "r").read()
    
    prompt = [{"role": "system", "content": _prompt}]
    history_item = [{"role": "user", "content": history}]

    prompt.extend(history_item)
    completion = config_openAI.chat_completion(self='', prompt=prompt)

    response = completion["choices"][0]["message"]["content"]
    return {"data_points": "", "answer": response, "thoughts": ""}

def get_image(history):
    prompt = open("utils/prompt_instructions_image.prompt", "r").read()

    completion = config_openAI.generate_image(self='', prompt=f'{prompt} {history}')
    response = completion["data"][0]["url"]
    return {"data_points": "", "image": response, "thoughts": ""}
