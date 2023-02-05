    try:
        response = model_response["choices"][0]["text"]
    except KeyError:
        response = "Error: Key 'choices' not found in model_response."
        # log or print the error message for debugging purposes
        print("KeyError:", response)
    
    choices = model_response.get('choices', None)
    if choices:
        response = choices[0]['text']
    else:
        response = "No response from model"

## if "choices" in model_response:
    ## response = model_response["choices"][0]["text"]
## else:
    ## response = "The 'choices' key is not present in the dictionary."

response = requests.post("https://api.openai.com/v1/engines/text-davinci-002/jobs", data=data, timeout=60)

data = {
    "prompt": "What is the capital of France?",
    "temperature": 0.7,
    "max_tokens": 100,
    "top_p": 1,
    "n": 1,
    "stream": False,
    "presence_penalty": 0
}

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    data = {
        "prompt": text,
        "temperature": 0.7,
        "max_tokens": 100,
        "top_p": 1,
        "n": 1,
        "stream": False,
        "presence_penalty": 0
    }
    model_response = requests.post("https://api.openai.com/v1/engines/text-davinci-003/jobs",
                 headers={"Content-Type": "application/json", "Authorization": "Bearer <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>"},
                 json=data).json()
    response_text = model_response["choices"][0]["text"]
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)