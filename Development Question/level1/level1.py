import google.generativeai as genai 
import os
import json 
import time 

genai.configure(api_key=os.getenv("API_KEY"))  ##configuring and calling the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponse(prompt): ##function to get response from gemini using api
    time_sent = int(time.time())
    response = model.generate_content(prompt + " in one line") ##helps in reducing token used and get a small answer
    message = response.text.replace('\n', ' ').strip()
    time_recieved = int(time.time())
    return {
        "Prompt": prompt,
        "Message": message,
        "TimeSent": time_sent,
        "TimeRecvd": time_recieved,
        "Source": "Gemini"
    }

def textInput(input_file, output_file): ##function to read lines from text file and create an output json file
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

    print("Output file created")


textInput('input.txt', 'output.json') ##calling the function
