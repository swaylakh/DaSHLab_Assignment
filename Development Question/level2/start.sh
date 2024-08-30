#!/bin/bash


start_server() {
    echo "Starting the server..."
    python3 server.py &
    SERVER_PID=$! 
    echo "Waiting for the server to start..."
    sleep 5  
}

start_client() {
    echo "Starting the client..."
    python3 client.py  
}

stop_server() {
    echo "Stopping the server..."
    kill $SERVER_PID
    wait $SERVER_PID 
}


export API_KEY=<enter api key>

start_server
start_client
stop_server

echo "Server and client operations completed."
