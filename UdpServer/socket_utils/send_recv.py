import socket

def send_data_and_integer(data_str, data_int, host, port):
    """
    Send a string and an integer over the internet using sockets.
    
    Args:
        data_str (str): The string data to send.
        data_int (int): The integer data to send.
        host (str): The IP address of the receiving server.
        port (int): The port number that the server is listening on.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Concatenate the string and integer into one string with a delimiter
        data_to_send = f"{data_str},{data_int}"
        
        # Encode the string into bytes and send it
        data_to_send_bytes = data_to_send.encode('utf-8')
        s.sendall(data_to_send_bytes)
        
        print("Data sent successfully.")

def receive_data_and_integer(host, port):
    """
    Receive a string and an integer over the internet using sockets.
    
    Args:
        host (str): The IP address to listen on.
        port (int): The port number to listen on.
    
    Returns:
        A tuple containing the received string and integer.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode('utf-8')
            
            # Split the received string using the delimiter and convert the integer part to int
            received_data_str, received_data_int = data.split(',')
            received_data_int = int(received_data_int)
            
            print("Received data:", received_data_str, received_data_int)
            
            return received_data_str, received_data_int

# Example usage:
# send_data_and_integer("Hello", 42, 'your_server_ip', 12345)
# received_data = receive_data_and_integer('0.0.0.0', 12345)
# print("Received:", received_data)

