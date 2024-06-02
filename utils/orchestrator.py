from utils.openai import config_openAI

def get_answer(history):
    config_openAI.set_api_credentials(self='')
    _prompt = open("utils/prompt_instructions.prompt", "r").read()
    
    prompt = [{"role": "system", "content": _prompt}]
    history_item = [{"role": "user", "content": history}]

    prompt.extend(history_item)
    completion = config_openAI.chat_completion(self='', prompt=prompt)

    response = completion["choices"][0]["message"]["content"]
    return {"data_points": "", "answer": response, "thoughts": ""}

def get_image(history):
    config_openAI.set_api_credentials(self='')
    prompt = open("utils/prompt_instructions.prompt", "r").read()

    completion = config_openAI.generate_image(self='', prompt=f'{prompt} \nDescription: {history}')
    response = completion["data"][0]["url"]
    return {"data_points": "", "image": response, "thoughts": ""}
