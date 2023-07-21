import openai

openai.api_key = 'REDACTED'

def get_gpt_output(gpt_prompt):
  message=[{'role': 'user', 'content': gpt_prompt}]
  response = openai.ChatCompletion.create(
    model='gpt-4',
    messages = message,
    temperature=0.2,
  )
  return response

gpt_output = get_gpt_output('how would i separate a paragraph based on numbered items in html')
gpt_response = gpt_output['choices'][0]['message']['content']

print(gpt_response)
