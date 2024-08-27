import google.generativeai as genai ##geminiapi
import os ## for api privacy
import json ## to get output in .json format
import time ## to get time sent and recieved

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponse(prompt):
    time_sent = int(time.time())
    response = model.generate_content(prompt + " in one line")
    message = response.text.replace('\n', ' ').strip()
    time_recieved = int(time.time())
    return {
        "Prompt": prompt,
        "Message": message,
        "TimeSent": time_sent,
        "TimeRecvd": time_recieved,
        "Source": "Gemini"
    }

def textInput(input_file, output_file):
    output = []

    with open(input_file, 'r') as file:
        prompts = file.readlines()
        for prompt in prompts:
            prompt = prompt.strip() 
            if prompt: 
                response = getResponse(prompt)
                output.append(response)

    with open(output_file, 'w') as file:
        json.dump(output, file, indent=2)

textInput('input.txt', 'output.json')
