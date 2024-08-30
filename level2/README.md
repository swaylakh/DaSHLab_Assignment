## Level 2 Assignment

- Implemented a Client-Server Model using socket programming

- Server script hosts the server and listens for any client connections; when the client connects, it returns and outputs an output<client_id>.json file containing responses from API call made to Gemini API

- Client script partitions input.txt into several loads and assigns a client ID to each and then sends it to the server to act as multiple clients and receives the output file

- The server doesn't handle multiple requests at once and only processes one client at a time; threading can resolve this in the future. 
