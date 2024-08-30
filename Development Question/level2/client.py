import socket
import json

def split_prompts(prompts, num_clients):
    total_prompts = len(prompts)
    chunk_size = total_prompts // num_clients
    remainder = total_prompts % num_clients
    start_index = 0
    chunks = []
    for i in range(num_clients):
        end_index = start_index + chunk_size + (1 if i < remainder else 0)
        chunks.append(prompts[start_index:end_index])
        start_index = end_index

    return chunks

def send_prompts_to_server(client_id, prompts, server_host, server_port):
    
    payload = {
        "client_id": client_id,
        "prompts": prompts
    }

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    
    client_socket.sendall(json.dumps(payload).encode('utf-8'))

    response = client_socket.recv(4096).decode('utf-8')
    response_data = json.loads(response)
    
    with open(f'output_{client_id}.json', 'w') as file:
        json.dump(response_data, file, indent=2)

    print(f"Client {client_id}: Responses saved to output_{client_id}.json")
    client_socket.close()

def main(input_file, server_host, server_port, num_clients):
    prompts = []
    with open(input_file, 'r') as file:
        for line in file:
            stripped_line = line.strip()  
            if stripped_line:  
                prompts.append(stripped_line)

    prompt_chunks = split_prompts(prompts, num_clients)

    client_id = 1
    for prompt_chunk in prompt_chunks:
        send_prompts_to_server(client_id, prompt_chunk, server_host, server_port)
        client_id += 1


main('input.txt', '0.0.0.0', 6969, num_clients=5)
