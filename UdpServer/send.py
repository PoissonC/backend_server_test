import cv2
import socket
from socket_utils.send_recv import receive_data_and_integer

def send_video_over_udp(receiver_address=('localhost', 12345), video_source=0, jpeg_quality=90):
    # Initialize camera
    cap = cv2.VideoCapture(video_source)

    # Set up UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = receiver_address

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Apply JPEG compression to the frame
            result, encoded_frame = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), jpeg_quality])

            # Ensure the frame was successfully compressed
            if not result:
                continue

            # Serialize the encoded frame
            data = encoded_frame.tobytes()

            # UDP packet size check
            if len(data) > 65507:
                print("Frame too large to send over UDP; consider reducing quality or resolution further.")
                continue

            # Send frame over UDP
            sock.sendto(data, server_address)

    finally:
        # Clean up
        cap.release()
        sock.close()

# Example usage
# send_video_over_udp(('receiver_ip_address', 12345), video_source=0, jpeg_quality=90)
# Adjust 'receiver_ip_address' to the actual IP address of the receiver and port as needed.

if __name__ == '__main__':
    received_data = receive_data_and_integer('0.0.0.0', 12345)
    send_video_over_udp(received_data, video_source=0, jpeg_quality=90)

