from fastapi import FastAPI
import openai
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app_api = FastAPI()
openai.api_key = 'REDACTED'

app_api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

def get_gpt_output(gpt_prompt):
    message=[{'role': 'user', 'content': gpt_prompt}]
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages = message,
        temperature=0.2,
        max_tokens=700,
        frequency_penalty=0.0
    )
    return response

@app_api.get('/gpt')
def get_planting_instructions(crop: str):
    gpt_output = get_gpt_output(f'give succinct advice on how to grow {crop} in 8 steps ordered 1, 2, 3, and so on.')
    gpt_response = gpt_output['choices'][0]['message']['content']
    return {'instructions': gpt_response}

uvicorn.run(app_api, port=8000)
