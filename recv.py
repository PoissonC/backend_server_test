import cv2
import socket
import numpy as np

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind to the same port as used in the sender
server_address = ('localhost', 12345) # Adjust IP if necessary, use '' for localhost
sock.bind(server_address)

try:
    while True:
        # Receive data
        data, address = sock.recvfrom(65507) # Buffer size; adjust if necessary
        
        if data:
            # Convert data to numpy array
            nparr = np.frombuffer(data, np.uint8)
            # Decode image
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if frame is not None:
                # Display the frame
                cv2.imshow('Received Frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'): # Press 'q' to exit
                    break
            else:
                print("Could not decode frame")
finally:
    cv2.destroyAllWindows()
    sock.close()

