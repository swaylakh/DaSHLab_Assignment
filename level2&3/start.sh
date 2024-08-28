#!/bin/bash

# Function to start the server and wait until it's ready
start_server() {
    echo "Starting the server..."
    python3 server.py &  # Redirect output to server.log
    SERVER_PID=$!  # Store the PID of the server process

    echo "Waiting for the server to start..."
    sleep 5  # Increase if necessary to give the server time to initialize
}

# Function to start the client
start_client() {
    echo "Starting the client..."
    python3 client.py  # Redirect output to client.log
}

# Function to stop the server
stop_server() {
    echo "Stopping the server..."
    kill $SERVER_PID
    wait $SERVER_PID  # Wait for the server process to terminate
}


export API_KEY='AIzaSyBZXWzfBlOYJj_ZJYeeORS3y_ZVG-ZcxZA'

start_server
start_client
stop_server

echo "Server and client operations completed."
