import cv2
import socket
import pickle

# Initialize camera
cap = cv2.VideoCapture(0)

# Set up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)  # Change to receiver's IP address and port

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply JPEG compression to the frame
    # The second parameter is the format and quality of the compression
    # Here, we are specifying to compress the frame as a JPEG with 90% quality
    # You can adjust the quality to be lower to achieve higher compression (and thus lower bandwidth usage)
    result, encoded_frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

    # Ensure the frame was successfully compressed
    if not result:
        continue

    # Serialize the encoded frame
    # Since the frame is already encoded as a byte stream, you can skip pickle if desired
    # and directly send the encoded_frame.tostring() or encoded_frame.tobytes() over UDP
    data = encoded_frame.tobytes()

    # UDP packet size check
    if len(data) > 65507:
        print("Frame too large to send over UDP; consider reducing quality or resolution further.")
        continue

    # Send frame over UDP
    sock.sendto(data, server_address)

    # Display the original frame (optional, for debugging)
  #  cv2.imshow('Sending...', frame)
   # if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

# Clean up
cap.release()
cv2.destroyAllWindows()
sock.close()

