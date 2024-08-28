import socket
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

def start_server(host='0.0.0.0', port=6969):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(4096).decode('utf-8')
        if data:
            data = json.loads(data)
            client_id = data.get('client_id')
            prompts = data.get('prompts')
            results = []
            for prompt in prompts:
                response = getResponse(prompt)
                result = {"client_id": client_id}
                result.update(response) 
                results.append(result)
            client_socket.sendall(json.dumps(results).encode('utf-8'))
            client_socket.close()

start_server()