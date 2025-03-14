import socket
import logging

# Define the host and port to listen on
HOST, PORT = '127.0.0.1', 8080

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow immediate reuse of address after program exit
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the host and port
    try:
        server_socket.bind((HOST, PORT))
    except Exception as e:
        logging.error(f"Error trying to bind the socket on {HOST}:{PORT} - {str(e)}")
        raise
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Serving HTTP on {HOST} port {PORT} ...")

    while True:
        try:
        # Accept a new client connection
            client_connection, client_address = server_socket.accept()
            with client_connection:
                # Receive the request data (limit to 1024 bytes for simplicity)
                request_data = client_connection.recv(1024).decode('utf-8')
                print("Received request:")
                print(request_data)

            # Extract the first line of request data (HTTP request)
            request_line = request_data.split('\r\n')[0]  # First line
            method, path, version = request_line.split(' ')
            print(f"HTTP Method: {method}")
            print(f"Requested Path: {path}")
            print(f"HTTP Version: {version}")


            # Construct a simple HTTP response
            if path == "/":
                http_response = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/html; charset=utf-8\r\n"
                    "Content-Length: 46\r\n"
                    "\r\n"
                    "<html><body><h1>Hello, HTTP!</h1></body></html>"
                )
            elif path == "/about":
                html_content ="<html><body><h1>About Us</h1></body></html>"
                content_length = len(html_content)
                http_response = (
                    "HTTP/1.1 200 OK\r\n"
                    f"Content-Type: text/html; charset=utf-8\r\n"
                    f"Content-Length: 46\r\n"
                    "\r\n"
                    f"{html_content}"
                )
            else:
                html_content = "<html><body><h1>404 Not Found</h1></body></html>"
                content_length = len(html_content)
                http_response = (
                    "HTTP/1.1 404 Not Found\r\n"
                    f"Content-Type: text/html; charset=utf-8\r\n"
                    f"Content-Length: {content_length}\r\n"
                    "\r\n"
                    f"{html_content}"
                )



            # Send the HTTP response back to the client
            client_connection.sendall(http_response.encode('utf-8'))

        
        except Exception as e:
            logging.error(f"Error processing request: {str(e)}")