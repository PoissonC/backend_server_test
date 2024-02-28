from send_recv import receive_data_and_integer

received_data = receive_data_and_integer('0.0.0.0', 12345)

print("Received:", received_data)
